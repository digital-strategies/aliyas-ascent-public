define gallery_thumb_width = 320
define gallery_thumb_height = 180

init 1 python:
    gallery_rows = 3
    gallery_cols = 3
    gallery_items_per_page = gallery_rows * gallery_cols
    gallery_page = 0
    gallery_pages = 0

    default_thumb = im.Scale('images/gallery/thumbs/locked-1.png', gallery_thumb_width, gallery_thumb_height)

    class GalleryItem:
        counter = 0

        def __init__(self, path, thumb=None, achievement=None, blur=False):
            self.name = "gallery_item_" + str(GalleryItem.counter)
            GalleryItem.counter += 1
            self.path = path
            self.thumbPath = thumb
            self.blur = blur
            self.displayable = None
            self.thumb = None
            self.achievement = achievement
            self.processed_locked = False
            self.processed_unlocked = False

        def get_thumb_from_path(self, path):
            thumb_aspect = gallery_thumb_width / gallery_thumb_height
            cropped = crop_to_aspect(path, thumb_aspect)

            if self.blur:
                blurred = im.Blur(cropped, 12)
            else:
                blurred = cropped

            return im.Scale(blurred, gallery_thumb_width, gallery_thumb_height)

        def is_unlocked(self):
            if self.achievement == None:
                return True
            else:
                return achievement.has(self.achievement)

        def process(self):
            # print("Processing " + self.path, self.processed_locked, self.processed_unlocked)

            if self.processed_unlocked:
                return

            if self.is_unlocked():
                if ('.webm' in self.path or '.mp4' in self.path):
                    self.displayable = Movie(play=self.path)
                else:
                    self.displayable = Image(self.path)

                if (self.thumbPath == None):
                    self.thumb = self.get_thumb_from_path(self.path)
                else:
                    self.thumb = self.get_thumb_from_path(self.thumbPath)

                self.processed_unlocked = True
                return

            if self.processed_locked:
                return

            self.thumb = default_thumb
            self.processed_locked = True

    def crop_to_aspect(path, target_aspect=1280/720):
        w, h = renpy.image_size(path)
        image_aspect = w / h

        if image_aspect > target_aspect:
            new_w = h * target_aspect
            w_diff = w - new_w
            cropped = im.Crop(path, (w_diff / 2, 0, new_w, h))
        else:
            new_h = w / target_aspect
            h_diff = h - new_h
            cropped = im.Crop(path, (0, h_diff / 2, w, new_h))

        return cropped

    music_started = False

    def start_gallery_music():
        global music_started
        if music_started == True:
            return
        renpy.music.mute_all_channels(value=True)
        renpy.music.mute_channel(False, channel='gallery')
        renpy.music.play("audio/sash-music.ogg", channel='gallery', loop=True, fadeout=0.5, fadein=0.5, if_changed=True, relative_volume=0.15)
        music_started = True

    @renpy.pure
    class RestoreAudio(Action, DictEquality):
        """
        """

        def __init__(self):
            pass

        def __call__(self):
            global music_started
            renpy.music.stop(channel="gallery")
            renpy.music.mute_all_channels(value=False)
            music_started = False


init 2 python:
    gallery_items = []

    # achievements
    # page 1
    # page 2
    # page 3
    # page 4
    # page 5
    # page 6
    # page 7
    # page 8
    # page 9
    # page 10
    # page 11
    # page 12

    #free images


    def round_up(number):
        return int(number) + (number % 1 > 0)

    gallery_pages = round_up(len(gallery_items) / gallery_items_per_page)

    gallery_unlockables = len(list(filter(lambda x: x.achievement != None, gallery_items)))
    gallery_unlocked = 0

    def process_all():
        global gallery_unlocked
        gallery_unlocked = len(list(filter(lambda x: x.achievement != None and x.is_unlocked(), gallery_items)))
        for i in range(len(gallery_items)):
            gallery_items[i].process()

    def refresh_gallery():
        gal = Gallery()

        gal.hover_border = im.Scale('images/gallery/thumbs/hover.png', gallery_thumb_width, gallery_thumb_height)
        gal.locked_button = im.Scale('images/gallery/thumbs/locked-1.png', gallery_thumb_width, gallery_thumb_height)
        gal.transition = dissolve

        for i in range(len(gallery_items)):
            gal.button(gallery_items[i].name)
            if gallery_items[i].achievement != None:
                gal.condition('achievement.has("' + gallery_items[i].achievement + '")')
            gal.image(gallery_items[i].displayable)

        return gal

    process_all()

screen gallery():
    tag menu
    # Gallery background
    imagemap:
        ground "images/bg/gallery-bg.png"

    $ start_gallery_music()

    $ gallery_start = gallery_page * gallery_items_per_page
    $ gallery_end = min(gallery_start + gallery_items_per_page - 1, len(gallery_items) - 1)

    $ process_all()
    $ gal = refresh_gallery()

    # A grid of buttons.
    grid gallery_rows gallery_cols:

        xfill True
        yfill True
        spacing 20
        left_margin 120
        right_margin 100
        top_margin 40
        bottom_margin 40

        for i in range(gallery_start, gallery_end + 1):
            frame:
                xsize gallery_thumb_width
                ysize gallery_thumb_height
                add gal.make_button(gallery_items[i].name, gallery_items[i].thumb, xalign=0.5, yalign=0.5)

                if gallery_items[i].blur and gallery_items[i].is_unlocked():
                    text "Click to reveal" xalign 0.5 yalign 0.5 color '#fff'

                if gallery_items[i].achievement is not None and gallery_items[i].is_unlocked():
                    text gallery_items[i].achievement xalign 0.5 yalign 1.23 size 20 color '#ffffffb0'

    text "Page {} / {}".format(gallery_page + 1, gallery_pages):
        xpos 0.31
        ypos 0.01
        size 18
        color '#ffffff'

    text "Unlocked {} / {} Memories".format(gallery_unlocked, gallery_unlockables):
        xpos 0.54
        ypos 0.01
        size 18
        color '#ffffff'

    if gallery_page > 0:
        imagebutton:
            xalign 0.01
            yalign 0.5
            idle "gui/button/gallery_left_idle.png"
            hover "gui/button/gallery_left_hover.png"
            action SetVariable("gallery_page", gallery_page - 1)

    if (gallery_page + 1) * gallery_items_per_page < len(gallery_items):
        imagebutton:
            xalign 0.99
            yalign 0.5
            idle "gui/button/gallery_right_idle.png"
            hover "gui/button/gallery_right_hover.png"
            action SetVariable("gallery_page", gallery_page + 1)

    imagebutton:
        xalign 0.01
        yalign 0.01
        idle "gui/button/gallery_return_idle.png"
        hover "gui/button/gallery_return_hover.png"
        action [RestoreAudio(), Return()]
