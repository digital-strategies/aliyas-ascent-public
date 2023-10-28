image battlefly_mov = Movie(play="images/videos/battlefly.webm")

screen garden_screen():
    imagemap:
        ground "battlefly_mov"

label ch1_garden:

    scene transparent
    scene black onlayer bglayer
    show screen garden_screen onlayer bglayer
    with dissolve


    play sound "audio/garden-bg-music.ogg" volume 0.5 loop

    voice "aliya/Aliya_Chapter-1_ART-1_1.ogg"
    aliya "What a beautiful garden!"
    voice "aliya/Aliya_Chapter-1_ART-1_2.ogg"
    aliya "Whoa! Look at all these beautiful and colorful butterflies!"
    voice "aliya/Aliya_Chapter-1_ART-1_3.ogg"
    aliya "Wait.{w=0.9} What are they...{w=0.7} Are they...{w=0.3} battling?"
    voice "aliya/Aliya_Chapter-1_ART-1_4.ogg"
    aliya "That’s awesome!"

    show screen timed_achievement("Battlefly Aficionado", 300.0)

label ch1_garden_menu:
    menu:
        "Continue watching":
            jump ch1_garden_stay
        "Leave garden":
            hide screen timed_achievement
            stop sound
            jump ch1_map_menu

label ch1_garden_stay:
    pause
    jump ch1_garden_menu
