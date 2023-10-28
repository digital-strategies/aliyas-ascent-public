init python:
    def start_bg_music1():
        renpy.music.play("audio/bg_music1.ogg", channel='music', loop=True, fadeout=0.5, fadein=0.5, if_changed=True, relative_volume=0.25)

image prelude_mov1 movie = Movie(play="images/videos/prelude_mov1.webm",  image="images/bg/prelude_mov1.png", loop=False, channel="movie_voice")
image chapter1_mov1 movie = Movie(play="images/videos/chapter1_mov1.webm",  image="images/bg/chapter1_mov1.png", loop=False, channel="movie_voice")

screen aliya_intro_video():
    imagemap:
        ground "prelude_mov1 movie"

image boat_sway = Movie(play="images/videos/boat_sway.webm", size=(1280, 720))

screen boat_screen():
    imagemap:
        ground "boat_sway"

image bg_pouch = Movie(play="images/videos/pouch.webm")

screen tutorial_img():
    imagemap:
        ground "images/bg/tutorial.png"

screen bg_pouch_screen():
    imagemap:
        ground "bg_pouch"

label start:
    $ renpy.music.clear_all_channels()
    $ start_bg_music1()
    show screen nav_reminder onlayer hidden

    scene transparent
    scene black onlayer bglayer
    show screen tutorial_img onlayer bglayer
    with Dissolve(1.0)
    pause

    $ analytics_event("started_prelude", {"event_category": "chapter_start", "event_label": "prelude"})

    # 🎥 Prelude MOV-1
    scene black with dissolve
    scene black onlayer bglayer
    # play sound "boat-wave-sound.ogg" volume 0.45
    show screen aliya_intro_video onlayer bglayer
    with dissolve
    pause 2.0

    aliya "I can’t seem to remember anything.{w=1.1}{nw}"
    aliya "I feel nauseous...{w=1.3} Where am I?{w=1.2}{nw}"
    aliya "I’m on a boat?{w=1.5} Is this just one bad dream?{w=1.5}{nw}"
    aliya "I still can’t remember anything.{w=1.4}{nw}"
    $ set_show_nav_reminder(delay=2.0)
    aliya "Even my name...{w=1.3}"

# Prelude M-1
    scene transparent
    scene black onlayer bglayer
    show screen boat_screen onlayer bglayer
    with dissolve
    show aliya think2 at hover
    with dissolve

    play sound "audio/boat-bg-music.ogg" volume 0.15 loop
    voice "narrator/1-m1.ogg"
    storyteller "There’s chattering in the background."
    $ set_show_nav_reminder(delay=2.0)
    voice "narrator/2-m1.ogg"
    storyteller "You see people sitting across as confused as you are."

    hide aliya with dissolve

    woman "Where are we?"
    man "Why am I in a boat?"

    show aliya curious8 at hover
    with dissolve

    voice "aliya/Aliya_Prelude_M-1_1.ogg"
    aliya "{i}Seems I’m not the only one who lost their memory.{/i}"

    show aliya curious6 at hover
    with dissolve

    voice "aliya/Aliya_Prelude_M-1_2.ogg"
    aliya "{i}Everyone looks comfortable enough.{w=0.3} But where's this boat taking us?{/i}"

    show aliya full neutral5 at left
    with dissolve
    show riverman-side at right
    with dissolve

# Prelude M-2
    voice "aliya/Aliya_Prelude_M-2_1.ogg"
    aliya "A Riverman..."
    voice "aliya/Aliya_Prelude_M-2_2.ogg"
    aliya "{i}My head hurts...{w=1.0} May be a good idea to ask the Riverman.{/i}"

    show aliya full suspicious1 with dissolve

    voice "aliya/Aliya_Prelude_M-2_3.ogg"
    aliya "Excuse me, sir?"

    hide riverman-side
    show riverman-neutral at right, flip
    with dissolve

    riverman "..."

    voice "aliya/Aliya_Prelude_M-2_4.ogg"
    aliya "Uhm...{w=0.5} Do you know where we’re going?"

    riverman "..."

    show aliya full sad1 with dissolve

    voice "aliya/Aliya_Prelude_M-2_5.ogg"
    aliya "{i}Great...{w=1.2} The only guy who knows what he’s doing is ignoring me.{/i}"
    hide aliya full sad1
    with dissolve
    hide riverman-neutral
    with dissolve

    scene transparent
    scene black onlayer bglayer
    show screen bg_pouch_screen onlayer bglayer
    with dissolve

    voice "aliya/Aliya_Prelude_M-2_6.ogg"
    aliya "{i}What’s this?{w=0.8} Something’s tied to my wrist.{/i}"

# Prelude M-3
    voice "aliya/Aliya_Prelude_M-3_1.ogg"
    aliya "{i}A pouch...{w=1} There’s something inscribed in it.{/i}"

    scene bg_pouch:
        subpixel True
        truecenter
        zoom 1.0
        ease 1.0 zoom 1.15

    voice "aliya/Aliya_Prelude_M-3_2.ogg"
    aliya "\"For my dearest Aliya, a safe journey to a better world.\""

    scene bg_pouch:
        subpixel True
        truecenter
        zoom 1.15
        ease 1.0 zoom 1.0

    play sound "audio/trinket.ogg" volume 0.35
    voice "aliya/Aliya_Prelude_M-3_3.ogg"
    aliya "{i}So,{w=0.7} my name’s Aliya...{w=1.6} I wonder what’s inside.{/i}"
    voice "aliya/Aliya_Prelude_M-3_4.ogg"
    aliya "{i}Trinkets...{w=1.5} Grandma loves these little trinkets.{/i}"
    voice "aliya/Aliya_Prelude_M-3_5.ogg"
    aliya "{i}These must be from her.{w=1.2} But how do I know that?{/i}"
    voice "aliya/Aliya_Prelude_M-3_6.ogg"
    aliya "{i}I’ll keep it safe for now.{/i}"

    stop sound #for pouch trinket sfx
    play sound "audio/boat-bg-music.ogg" volume 0.15 loop

    scene transparent
    scene black onlayer bglayer
    show screen boat_screen onlayer bglayer
    with dissolve
    show aliya neutral19 at hover
    with dissolve

# Prelude M-4
    voice "aliya/Aliya_Prelude_M-4_1.ogg"
    aliya "{i}What is this uneasy feeling...{/i}"
    voice "aliya/Aliya_Prelude_M-4_2.ogg"
    aliya "{i}Everyone’s surprisingly calm for a bunch of people who lost their memories...{w=1.5} Except me.{/i}"

    show riverman-side at right
    with dissolve
    show aliya full neutral5 at left
    with dissolve

    voice "riverman/Riverman_Prelude_M-4.ogg"
    riverman "All will become clear in due time."

    show aliya full confident1 at left
    with dissolve

    voice "aliya/Aliya_Prelude_M-4_3.ogg"
    aliya "That's not remotely helpful at all!"

    voice "narrator/3-m4.ogg"
    storyteller "The Riverman stares at you intensely as if he’s remembering your face."

label p_conversation2:
    menu:
        "Ask him":
            jump p_death
        "Do not ask him":
            jump p_rest

# Prelude M-5
label p_rest:

    hide riverman-side

    show aliya sad2 at hover
    with dissolve
    voice "aliya/Aliya_Prelude_M-5_1.ogg"
    aliya "Nothing I can do as well but wait.{w=0.5} My head feels like it’s going to split too."

    show aliya sad12 at hover
    with dissolve

    voice "aliya/Aliya_Prelude_M-5_2.ogg"
    aliya "Might as well try and get some sleep."


    scene black with dissolve

    voice "narrator/4-m5.ogg"
    storyteller "You slump against the boat's edge and the undulating waves lull you to sleep in the cool morning breeze."


    stop sound #for boat bg sound

# 🎥Chapter 1 MOV-1
    scene black onlayer bglayer
    scene chapter1_mov1 movie with dissolve

    aliya "{cps=10.6}On a boat, alone...{/cps}{w=0.2}{nw}"
    aliya "{cps=14.1}Riverman knows the secret.{/cps}{w=0.2}{nw}"
    $ set_show_nav_reminder(delay=2.0)
    aliya "{cps=22}Will I find the truth?{/cps}{w=0.2}"

    scene black with dissolve

    $ analytics_event("finished_prelude", {"event_category": "chapter_finished", "event_label": "prelude"})

    jump chapter1
