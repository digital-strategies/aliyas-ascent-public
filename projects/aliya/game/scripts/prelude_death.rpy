image prelude_mov2 movie = Movie(play="images/videos/prelude_mov2.webm",  image="images/bg/prelude_mov2.png", loop=False, channel="movie_voice")
image boat sway = Movie(play="images/videos/boat_sway.webm", size=(1280, 720))
image death_scene = Movie(play="images/videos/death_scene.webm")

screen death_drowning():
    imagemap:
        ground "death_scene"

# Prelude M-6
label p_death:

    play sound "audio/boat-bg-music.ogg" volume 0.15 loop

    # scene boat sway with dissolve
    show aliya full suspicious1 at left
    with dissolve
    show riverman-side at right
    with dissolve

    voice "aliya/Aliya_Prelude_M-6_1.ogg"
    aliya "Uhm...{w=1.5} Excuse me,{w=0.8} can you tell me where we are headed?"

    voice "narrator/5-m6.ogg"
    storyteller "The riverman gazes ahead, undisturbed by your question."

label p_conversation3:
    menu:
        "Confront him":
            jump p_conversation4
        "Stop asking":
            jump p_rest

# Prelude M-7
label p_conversation4:

    show aliya angry12 at hover
    with dissolve


    voice "aliya/Aliya_Prelude_M-7_1.ogg"
    aliya "Hey!{w=1.0} Did you hear me?{w=1.1} Where are we going?"

    voice "narrator/6-m7.ogg"
    storyteller "The riverman remains unresponsive, as if you do not exist."

    hide aliya with dissolve
    hide riverman-side with dissolve

    menu:
        "Insult":
            jump p_conversation5
        "Sit":
            jump p_sit

# Prelude M-8
label p_conversation5:

    show aliya angry12 at hover
    with dissolve
    show riverman-side at right
    with dissolve


    voice "aliya/Aliya_Prelude_M-8_1.ogg"
    aliya "Talk to me!{w=0.9} Are you deaf?{w=0.9} Tell me where we're headed?"

    hide aliya with dissolve
    hide riverman-side with dissolve

    menu:
        "Threaten":
            jump p_conversation6
        "Stop":
            jump p_stop

# Prelude M-9
label p_conversation6:

    scene transparent
    scene black onlayer bglayer
    show screen boat_screen onlayer bglayer
    with dissolve
    show aliya angry3 at hover
    with dissolve
    show riverman-side at right
    with dissolve


    voice "aliya/Aliya_Prelude_M-9_1.ogg"
    aliya "You think silence will stop me?{w=1.3} I'll take control of this boat myself if I have to!"

    hide aliya with dissolve
    hide riverman-side with dissolve

    menu:
        "Attack":
            jump p_conversation7
        "Stop":
            jump p_stop

# Prelude M-12
label p_conversation7:

    show aliya angry3 at hover
    with dissolve
    show riverman-side at right
    with dissolve


    voice "aliya/Aliya_Prelude_M-12_1.ogg"
    aliya "I WARNED YOU!!!{w=2.0} You brought this on yourself, you stubborn fool."

    scene black-bg

    voice "narrator/7-m12.ogg"
    storyteller "With a fierce lunge{w=0.5}, You propel yourself towards the Riverman{w=0.5}, your intent clear and unwavering."
    voice "narrator/7.1-m12.ogg"
    storyteller "Yet{w=0.5}, in the span of a heartbeat{w=0.5}, something inexplicable happens."

    voice "narrator/8-m12.ogg"
    storyteller "The dagger{w=0.5}, once clutched in your hand{w=0.5}, now finds itself buried within your chest{w=0.5}, a cruel twist of fate."

    stop sound #for boat bg music

    play sound "audio/splash.ogg" volume 0.35

    scene transparent
    scene black onlayer bglayer
    show screen death_drowning onlayer bglayer

    with Dissolve(5.0)
    pause 1.5

    voice "narrator/9-m12.ogg"
    storyteller "As the numbing chill of the water surrounds you{w=1}, a realization dawns like the first light of dawn."
    voice "narrator/9.1-m12.ogg"
    storyteller "Your impulsive actions have awakened a force beyond your reckoning."
    voice "narrator/9.2-m12.ogg"
    storyteller "A being who peers into your thoughts as if reading an open book."
    voice "narrator/10-m12.ogg"
    storyteller "The thought is a fleeting echo as the darkness takes you{w=1}, the boat continuing on its mysterious path."


    # 🎥 Prelude MOV-2
    scene prelude_mov2 movie with dissolve

    aliya "{cps=41.5}I guess I was too impatient and paid the ultimate price.{/cps}{w=1.4}{nw}"
    $ set_show_nav_reminder(delay=2.0)
    aliya "{cps=21.7}Maybe next time I shouldn’t let my emotions get the better of me.{/cps}{w=1}"

    #BAD ENDING 1 - IMPATIENT
    $ analytics_event("death_prelude", {"event_category": "death", "event_label": "riverman"})

    menu:
        "Return to main menu":
            return
        "Reset to before you died":
            jump p_conversation6

# Prelude M-10
label p_sit:

    show aliya angry4 at hover
    with dissolve

    voice "aliya/Aliya_Prelude_M-10_1.ogg"
    aliya "He’s not responding. This sucks."

    jump p_rest

# Prelude M-11
label p_stop:

    show aliya angry4 at hover
    with dissolve

    voice "aliya/Aliya_Prelude_M-11_1.ogg"
    aliya "Better not provoke him further."

    jump p_rest

