init 1 python:
    map_menu_item_label = ""
    map_menu_item_label_width = 140
    map_menu_item_label_pos_x = 0
    map_menu_item_label_pos_y = 0
    map_menu_item_size = 140
    map_menu_item_border = 5

    class MapMenuItem:
        def __init__(self, path, name, target, position=(0,0), condition="True"):
            self.name = name
            self.target = target
            self.displayable = self.get_thumb_from_path(path)
            self.position = position
            self.condition = condition

        def get_thumb_from_path(self, path):
            cropped = crop_to_aspect(path, 1)
            scaled = im.Scale(cropped, map_menu_item_size, map_menu_item_size)
            circled = im.AlphaMask(scaled, im.Scale("images/bg/map_menu_mask.png", map_menu_item_size, map_menu_item_size))

            return im.Scale(circled, map_menu_item_size - 2 * map_menu_item_border, map_menu_item_size - 2 * map_menu_item_border)

init 2 python:
    map_menu_items = []

    map_menu_items.append(MapMenuItem(path="images/bg/garden.png", name="Garden", target="ch1_garden", position=(50,100)))
    map_menu_items.append(MapMenuItem(path="images/bg/docks-boat-pano.png", name="Docks", target="ch1_boat", position=(450,400)))
    map_menu_items.append(MapMenuItem(path="images/bg/bg-stables-1.png", name="Stables", target="ch1_stables", position=(1100,520)))
    map_menu_items.append(MapMenuItem(path="images/bg/very_tall_tower.png", name="Towers", target="ch1_towers", position=(1100,60)))
    map_menu_items.append(MapMenuItem(path="images/bg/bg village square.png", name="Market", target="ch1_village_square", position=(837,339)))
    map_menu_items.append(MapMenuItem(path="images/bg/village-1.png", name="Village", target="ch1_end", condition="tower_scene and visited_market", position=(400,20)))
    map_menu_items.append(MapMenuItem(path="images/bg/gallery-bg.png", name="Gallery", target="ch1_gallery", position=(774,20)))
    #map_menu_items.append(MapMenuItem(path="images/bg/bg banana.png", name="Eat Banana", target="ch1_eat_ban", condition="smol_banana", position=(700,500)))


image idle_bg = im.MatrixColor(
    im.Scale("images/bg/map_menu_mask.png", map_menu_item_size, map_menu_item_size),
    im.matrix.tint(0.7, 0.7, 0.9))
image hover_bg = im.Scale("images/bg/map_menu_mask.png", map_menu_item_size, map_menu_item_size)


screen map_menu_screen():
    imagemap:
        ground "images/bg/menu-bg.png"


    for i in range(len(map_menu_items)):
        if eval(map_menu_items[i].condition):
            imagebutton:
                xpos map_menu_items[i].position[0]
                ypos map_menu_items[i].position[1]
                idle Composite(
                    (map_menu_item_size, map_menu_item_size),
                    (0, 0), "idle_bg",
                    (map_menu_item_border, map_menu_item_border), map_menu_items[i].displayable)
                hover Composite(
                    (map_menu_item_size, map_menu_item_size),
                    (0, 0), "hover_bg",
                    (map_menu_item_border, map_menu_item_border), map_menu_items[i].displayable)
                action [
                    Hide(screen="map_menu_screen"),
                    SetVariable("map_menu_item_label", ""),
                    Jump(map_menu_items[i].target)
                    ]
                hovered [
                    SetVariable("map_menu_item_label", map_menu_items[i].name),
                    SetVariable("map_menu_item_label_pos_x", int(map_menu_items[i].position[0] - (map_menu_item_label_width - map_menu_item_size) / 2)),
                    SetVariable("map_menu_item_label_pos_y", map_menu_items[i].position[1] + map_menu_item_size + 5)
                    ]
                unhovered [SetVariable("map_menu_item_label", "")]

    if map_menu_item_label != "":
        textbutton map_menu_item_label:
            style_prefix "map_menu_item_label"
            xpos map_menu_item_label_pos_x
            ypos map_menu_item_label_pos_y
            action NullAction()

style map_menu_item_label_button:
    properties gui.button_properties("choice_button")
    xsize map_menu_item_label_width

style map_menu_item_label_button_text is default:
    properties gui.button_text_properties("choice_button")

#Chapter 1 M-/2
label ch1_map_menu:

    # some hackiness to make sure we always return here after visiting the gallery
    # (otherwise we'd return to the last visited scene, e.g. the gallery-pre one)
    if show_gallery == True:
        $ show_gallery = False
        call screen gallery
    stop sound
    $ start_bg_music1()
    window hide

    scene transparent
    scene black onlayer bglayer
    show screen map_menu_screen
    with dissolve

label ch1_map_menu_loop:
    pause
    jump ch1_map_menu_loop
