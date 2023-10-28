image chapter1_mov2 movie = Movie(play="images/videos/chapter1_mov2.webm",  image="images/bg/chapter1_mov2.png", loop=False, channel="movie_voice")

screen bg_stables_screen():
    imagemap at pan_h_repeat(start=0, end=4368, duration=60.0, linear=True):
        ground "images/bg/bg-stables-1.png"

image bg_smol_screen = Movie(play="images/videos/smol.webm")
screen bg_smol_screen():
    imagemap:
        ground "bg_smol_screen"

image haystack = Movie(play="images/videos/haystack.webm")

image smol_no_controller = Movie(play="images/videos/smol-no-controller.webm")

image smol_controller = Movie(play="images/videos/smol-controller.webm")
screen smol_controller_screen():
    imagemap:
        ground "smol_controller"

screen portal_screen():
    imagemap at pan_h_repeat(start=0, end=1925, duration=40.0, reverse=False):
        ground "images/bg/bg-portal-1.png"

label ch1_stables:

    default smol_success = False

    if smol_success == True:
        jump stb_smol_2 # Chapter 1 STB-15
    elif smol_encounter == True and smol_success == False:
        jump stb_smol_1 # Chapter 1 STB-8
    elif smol_encounter == False and smol_success == False:
        jump stb_smol_0 # Chapter 1 STB-1
    else:
        jump stb_smol_2 # Chapter 1 STB-15

# Chapter 1 STB-1
label stb_smol_0:

    scene transparent
    scene black onlayer bglayer
    show screen bg_stables_screen onlayer bglayer
    with dissolve

    show aliya curious8 at hover
    with dissolve
    voice "aliya/Aliya_Chapter-1_STB-1.ogg"
    aliya "{i}Oh! There are different types of animals here.{i}"

    play sound "audio/stables.ogg" volume 0.2 loop

    hide aliya with dissolve

    menu:
        "Sneak around":
            jump stb_sneak
        "Leave stables":
            jump stb_leave

# Chapter 1 STB-3
label stb_sneak:

    show aliya curious8 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_STB-3_1.ogg"
    aliya "{i}There’s a lot of horses here.{/i}"
    voice "aliya/Aliya_Chapter-1_STB-3_2.ogg"
    aliya "{i}Seems like they’re well taken care of.{/i}"

    scene black onlayer bglayer
    scene haystack

    play sound "audio/hay-stack.ogg" volume 0.1
    voice "narrator/17.1-stb12.ogg"
    storyteller "You hear rummaging nearby."

    show aliya curious7 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_STB-3_3.ogg"
    aliya "What’s that noise?"


    # Chapter 1 STB-4
    stop sound #haystack

    play sound "audio/stables.ogg" volume 0.2 loop

    scene transparent
    scene black onlayer bglayer
    show screen bg_smol_screen onlayer bglayer
    with dissolve

    show aliya curious8 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_STB-4_1.ogg"
    aliya "Hmm, this is one weird yet adorable looking monkey."

    show aliya blush1 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_STB-4_2.ogg"
    aliya "Hi there, little buddy..."

    voice "smol-ted/smolted-2-eee.ogg"
    monkey "EEEEEEEEEE..."

    show aliya curious8 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_STB-4_3.ogg"
    aliya "{i}It’s rubbing its belly. Is it hungry?{/i}"
    voice "aliya/Aliya_Chapter-1_STB-4_4.ogg"
    aliya "Are you hungry?"

    voice "smol-ted/smolted-1-eee.ogg"
    monkey "EEEEE..."

    voice "aliya/Aliya-Chapter-1_STB-4.ogg"
    aliya "I'll take that as a yes."

    if smol_banana == True:
        jump stb_banana_true1
    else:
        jump stb_banana_false1

# Chapter 1 STB-6
label stb_banana_true1:

    voice "aliya/Aliya_Chapter-1_STB-6.ogg"
    aliya "Wait I think I do! I still have this banana from the Fruit Stall."


    jump stb_split

#Chapter 1 STB-5
label stb_banana_false1:

    default smol_encounter = False

    show aliya sad15 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_STB-5_1.ogg"
    aliya "I’m sorry little buddy. I’m hungry as well..."

    voice "smol-ted/smolted-3-eee.ogg"
    monkey "EEEEE..."

    voice "aliya/Aliya_Chapter-1_STB-5_2.ogg"
    aliya "{i}Now I feel guilty...{/i}"
    voice "aliya/Aliya_Chapter-1_STB-5_3.ogg"
    aliya "There must be something I can do."


    $ smol_encounter = True

    jump ch1_map_menu

# Chapter 1 STB-2
label stb_leave:

    show aliya curious8 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_STB-2.ogg"
    aliya "{i}I shouldn’t be sneaking around these places.{/i}"

    scene black onlayer bglayer

    jump ch1_map_menu

# Chapter 1 STB-8
label stb_smol_1:

    scene transparent
    scene black onlayer bglayer
    show screen bg_smol_screen onlayer bglayer
    with dissolve

    voice "narrator/31-stb8.ogg"
    storyteller "The adorable yet weird looking monkey keeps staring at you with its adorable cute eyes."

    if smol_banana == True:
        jump stb_banana_true2
    else:
        jump stb_banana_false2

# Chapter 1 STB-9
label stb_banana_true2:

    show aliya curious8 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_STB-9.ogg"
    aliya "I’m back! Got you a little something."


    voice "smol-ted/smolted-eee-6.ogg"
    monkey "EEEEEEEEEE..."

# Chapter 1 STB-12
label stb_split:

    voice "aliya/Aliya_Chapter-1_STB-12_1.ogg"
    aliya "Here you go, little buddy."

    scene black onlayer bglayer
    scene black with dissolve

    voice "narrator/32-stb12.ogg"
    storyteller "You gave the banana to the monkey."

    voice "narrator/33-stb12.ogg"
    storyteller "All of a sudden, the monkey jumps on top of the wooden fence and is right in front of you."

    scene smol_no_controller:
        zoom 1.15
        ease 0.5 zoom 1.0
    with dissolve


    voice "smol-ted/smolted-1.ogg"
    monkey "Pheeeeew...{w=0.5} Thanks for that! I was so hungry I couldn’t speak."
    voice "smol-ted/smolted-2.ogg"
    monkey "I’m Smol Ted by the way..."

    show aliya blush1 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_STB-12_2.ogg"
    aliya "It talks! {w=0.5} It talks!!!"
    voice "aliya/Aliya_Chapter-1_STB-12_3.ogg"
    aliya "Its head’s getting bigger too."

    hide aliya with dissolve

    voice "smol-ted/smolted-3.ogg"
    ted "Thank you, fren! I was just hungry."
    voice "smol-ted/smolted-4.ogg"
    ted "My journey ends here, I’m going back to Smolville."

    hide aliya with dissolve

    voice "narrator/34-stb12.ogg"
    storyteller "Smol Ted pulls out a remote control."

    scene transparent
    scene black onlayer bglayer
    show screen smol_controller_screen onlayer bglayer
    with dissolve

    play sound "audio/magic-controller.ogg" volume 0.2
    voice "narrator/35-stb12.ogg"
    storyteller "He presses the red button in the middle."

    scene transparent
    scene black onlayer bglayer
    show screen portal_screen onlayer bglayer
    with dissolve
    play sound "audio/portal-opening.ogg" volume 0.2

    show aliya furious2 at hover
    with dissolve

# Chapter 1 STB-13

    voice "aliya/Aliya_Chapter-1_STB-13_1.ogg"
    aliya "Woah!"

    voice "smol-ted/smolted-5.ogg"
    ted "Do you want to come with us?"

    play sound "audio/stables.ogg" volume 0.2 loop

    hide aliya furious2
    show aliya curious8 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_STB-13_2.ogg"
    aliya "I would love to! But I feel like there’s something I need to do here first."

    hide aliya with dissolve

    voice "smol-ted/smolted-6.ogg"
    ted "Understandable... Here, take it."

    voice "narrator/36-stb13.ogg"
    storyteller "Smol Ted throws the remote control to you."

    stop sound

    scene black onlayer bglayer
    scene smol_no_controller with dissolve

    voice "smol-ted/smolted-7.ogg"
    ted "Use it when you need help!"
    voice "smol-ted/smolted-8.ogg"
    ted "Goodbye for now!"

    voice "narrator/37-stb13.ogg"
    storyteller "Smol Ted waves at you then jumps into the portal."

    $ smol_success = True
    $ smol_banana = False

    # 🎥Chapter 1 MOV-2

    scene chapter1_mov2 movie with dissolve

    aliya "Smol Ted’s pretty cool...{w=0.4}{nw}"
    aliya "I like Smols.{w=1.0}{nw}"
    aliya "And you know what?{w=0.9} This world really has a Treasure Trove of interesting characters!{w=1.1}{nw}"
    aliya "I wonder if I would meet more Teds in the marketplace?{w=1.17}{nw}"
    $ set_show_nav_reminder(delay=2.0)
    aliya "I can’t go back there.{w=0.8} I’d get in trouble for stealing the banana.{w=0.2}"

    stop sound
    scene black onlayer bglayer
    jump ch1_map_menu

# Chapter 1 STB-10
label stb_banana_false2:

    show aliya curious8 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_STB-10.ogg"
    aliya "I promise I’ll get you some food, little buddy. You wait right here!"

    scene black onlayer bglayer
    jump ch1_map_menu

# Chapter 1 STB-15
label stb_smol_2:

    scene bg-stables-1 with dissolve

    voice "aliya/Aliya_Chapter-1_STB-15.ogg"
    aliya "Nothing to see here."

    scene black onlayer bglayer
    jump ch1_map_menu


