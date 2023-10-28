screen bg_gallery():
    imagemap:
        ground "images/bg/gallery-bg.png"


default gallery_visited = False
default show_gallery = False

# Chapter 1 ART-1
label ch1_gallery:
    if gallery_visited == False:
        jump ch1_gallery_into
    else:
        jump ch1_goto_gallery

label ch1_gallery_into:

    $ start_gallery_music()
    $ renpy.music.mute_channel(False, "voice")

    scene transparent
    scene black onlayer bglayer
    show screen bg_gallery onlayer bglayer
    voice "narrator/16-art1.ogg"
    storyteller "You stumble upon an Art Gallery just near the Village Docks."

    show aliya curious8 at hover
    with dissolve
    voice "aliya/Aliya_Chapter-1_ART-1_0.ogg"
    aliya "\"Nat’s Fantastical Treasures Art Gallery.\""

    if tower_scene == True:
        jump ch1_gallery_nat
    else:
        jump ch1_gallery_interesting

# Chapter 1 ART-2
label ch1_gallery_nat:
    voice "aliya/Aliya_Chapter-1_ART-2.ogg"
    aliya "Hey Nat, is this your..."
    show riverman-neutral1 at right
    with easeinright

    voice "riverman/Riverman_Chapter1_ART-1_1.ogg"
    riverman "Never seen that place before in my life."
    voice "riverman/Riverman_Chapter1_ART-1_2.ogg"
    riverman "Though the owner has good taste if I say so myself!"

# Chapter 1 ART-3
label ch1_gallery_interesting:
    voice "aliya/Aliya_Chapter-1_ART-3.ogg"
    aliya "Looks interesting...{w=0.5} I wonder what’s in here."

    show riverman-neutral1 at right
    with easeinright

    voice "riverman/Riverman_Chapter1_ART-3_1.ogg"
    riverman "In the Gallery, the walls whisper stories.{w=1.7} They're fragments of memories.{nw}"
    voice "riverman/Riverman_Chapter1_ART-3_2.ogg"
    riverman "Some might be yours,{w=0.5} waiting to be pieced together again."


    $ gallery_visited = True

    jump ch1_goto_gallery

label ch1_goto_gallery:
    $ show_gallery = True
    scene transparent
    scene black onlayer bglayer
    jump ch1_map_menu
