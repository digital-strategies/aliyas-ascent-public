default visited_market = False
default vendor_angry = False

screen bg_market_screen():
    imagemap at pan_h_repeat(start=0, end=2569, duration=40.0):
        ground "images/bg/bg-village-square.png"


image bg_banana_screen = Movie(play="images/videos/banana.webm")
screen bg_banana_screen():
    imagemap:
        ground "bg_banana_screen"


label ch1_village_square:

    if vendor_angry == False:
        jump ch1_village_square_1
    else:
        jump vs_lie_low

label ch1_village_square_1:

    scene transparent
    scene black onlayer bglayer
    show screen bg_market_screen onlayer bglayer
    with dissolve

    # Chapter 1 VS-1
    show aliya curious7 at hover
    with dissolve

    # Chapter 1 VS-2


    voice "aliya/Aliya_Chapter-1_VS-1_1.ogg"
    aliya "{i}Wow! There are a lot of merchants here.{i}"

    hide aliya curious7


label ch1_market_menu:
    menu:
        "Continue looking around":
            jump ch1_market_stay
        "Proceed to market":
            jump ch1_market_proceed
        "Leave market":
            hide screen timed_achievement
            jump ch1_map_menu

label ch1_market_stay:
    pause
    jump ch1_market_menu


label ch1_market_proceed:

    $ visited_market = True

    show aliya curious7 at hover
    play sound "audio/hungry.ogg" volume 0.35
    voice "aliya/Aliya_Chapter-1_VS-1_2.ogg"
    aliya "{i}The fruits look so tasty.{/i}"


    show aliya sad2 at hover
    with dissolve

    stop sound
    voice "aliya/Aliya_Chapter-1_VS-1_3.ogg"
    aliya "{i}It looks like I don’t have any money, though.{/i}"

    # Chapter 1 VS-2
    voice "aliya/Aliya_Chapter-1_VS-2_1.ogg"
    aliya "{i}The vendor seems to be busy.{/i}"

    scene black onlayer bglayer
    scene transparent
    show screen bg_banana_screen onlayer bglayer
    with dissolve

    voice "narrator/28-vs2.ogg"
    storyteller "You see a weird looking banana beside the stall."

    scene black onlayer bglayer
    scene transparent
    show screen bg_market_screen onlayer bglayer
    with dissolve

    show aliya curious8 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_VS-2_2.ogg"
    aliya "{i}This might be from the stall...{/i}"
    voice "aliya/Aliya_Chapter-1_VS-2_3.ogg"
    aliya "{i}Should I take it?{/i}"

    scene black onlayer bglayer
    scene transparent
    show screen bg_banana_screen onlayer bglayer
    with dissolve

    hide aliya with dissolve
label vs_options1:
    menu:
        "Take banana":
            jump vs_take
        "Do not steal":
            jump vs_leave
    stop sound

# Chapter 1 VS-4
label vs_take:

    default smol_banana = False

    scene black onlayer bglayer
    scene transparent
    show screen bg_market_screen onlayer bglayer
    with dissolve

    show aliya happy3 at hover

    voice "aliya/Aliya_Chapter-1_VS-4_1.ogg"
    aliya "Hope the vendor didn’t notice!"
    voice "aliya/Aliya_Chapter-1_VS-4_2.ogg"
    aliya "This looks so delicious!"
    voice "aliya/Aliya_Chapter-1_VS-4_3.ogg"
    aliya "You’ll be a perfect snack."

    $ smol_banana = True

    jump vs_caught

# Chapter 1 VS-3
label vs_leave:

    scene black onlayer bglayer
    scene transparent
    show screen bg_market_screen onlayer bglayer
    with dissolve

    show aliya neutral19 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_VS-3.ogg"
    aliya "{i}I don’t think I should.{/i}"

    $ banana = False

    jump vs_caught

# Chapter 1 VS-5
label vs_caught:

    voice "narrator/29-vs5.ogg"
    storyteller "The vendor notices something."

    voice "vendor/vendor-1.ogg"
    vendor "Hey, what are y..."
    show aliya furious9 at hover
    play music "audio/suspense-music.ogg" volume 0.25

    show aliya jealous3 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_VS-5_1.ogg"
    aliya "Uh-oh! I need to run."

    voice "narrator/30-vs5.ogg"
    play sound "audio/running-footsteps.ogg" volume 0.9
    storyteller "You muster all your strength to run out of there as fast as you can."

    scene black onlayer bglayer
    scene docks-blurred-static
    with dissolve

    play sound "audio/catch-breath.ogg" volume 0.35
    pause 6.0

    play sound "audio/docks.ogg" volume 0.2 loop

    voice "aliya/Aliya_Chapter-1_VS-5_2.ogg"
    aliya "That was the fastest I have ever run in my life."

    $ renpy.music.clear_all_channels()
    $ start_bg_music1()

    voice "aliya/Aliya_Chapter-1_VS-5_3.ogg"
    aliya "I don’t think they saw my face, did they?"
    voice "aliya/Aliya_Chapter-1_VS-5_4.ogg"
    aliya "Better lie low for now."

    stop sound

    $ vendor_angry = True

    if smol_banana == True:
        jump ch1_eat_ban
    else:
        scene black onlayer bglayer
        jump ch1_map_menu

# Chapter 1 VS-6
label vs_lie_low:

    voice "aliya/Aliya_Chapter-1_VS-6.ogg"
    aliya "{i}Are you crazy, Aliya? Didn’t you hear what they said? We need to lie low.{/i}"

    jump ch1_map_menu







