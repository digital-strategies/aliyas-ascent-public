image toad_mov movie = Movie(play="images/videos/toadstoolz-easter-egg.webm", loop=False, channel="movie_voice")

screen toad_eyes():
    imagemap:
        ground "toad_mov movie"

label ch1_eat_ban:

    $ smol_banana = True

    play sound "audio/docks.ogg" volume 0.2 loop

    voice "narrator/38-eat-ban-end.ogg"
    storyteller "You examine the banana closely. It's wrinkled, and not exactly fresh."
    voice "narrator/39-eat-ban-end.ogg"
    play sound "audio/hungry.ogg" volume 0.35
    storyteller "Your stomach grumbles softly. {w=0.5}The banana might be a solution, but is it a good idea?"
    voice "narrator/40-eat-ban-end.ogg"
    storyteller "There's a faint, unusual scent to it. Eat it? Maybe, maybe not."

    play sound "audio/docks.ogg" volume 0.2 loop

label vs_options2:
    menu:
        "Take a bite":
            jump ch1_eat_ban_1
        "Maybe not":
            jump ch1_map_menu

label ch1_eat_ban_1:
# Chapter 1 BAN-1
    scene black onlayer bglayer
    scene docks-blurred-static with dissolve

    show aliya surprised1 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_BAN-1_1.ogg"
    aliya "Finally, no one to bother me. Come to Aliya!"

    voice "narrator/11-ban1.ogg"
    storyteller "You peeled the weird looking banana, and took a bite."

    show aliya sad12 at hover
    with dissolve
    voice "aliya/Aliya_Chapter-1_BAN-1_2.ogg"
    aliya "I don’t feel so good..."
    hide aliya

    stop sound

    scene white-bg with Dissolve(1.0)

# 🎥Chapter 1 MOV-3

    scene transparent
    scene black onlayer bglayer
    show screen toad_eyes onlayer bglayer
    with dissolve


    toad "Pst, hey Aliya!{w=0.5} Remember me?{w=1.0} Croaaak...{w=0.7}{nw}"
    toad "It's your friend, Fred.{w=0.8}{nw}"
    aliya "Fred?{w=1.2}{nw}"
    toad "Yeah, Croaaak...{w=1.2}{nw}"
    aliya "Where am I?{w=1.2}{nw}"
    toad "When are you coming to Croakshire?{w=1.2}{nw}"
    aliya "What?{w=1.5}{nw}"
    toad "Croakshire! Croaaaak...{w=1.6}{nw}"
    aliya "Get me out of here...{w=1} Help!{w=1}{nw}"
    $ set_show_nav_reminder(delay=2.0)
    toad "You're staying with us!{w=0.7} Right?{w=2}{nw}"

# Chapter 1 BAN-2
label ch1_eat_ban_wake_up:
    scene transparent
    scene black onlayer bglayer
    scene docks-blurred-static
    show aliya fearful2 at hover
    with dissolve

    play sound "audio/docks.ogg" volume 0.2 loop

    voice "aliya/Aliya_Chapter-1_BAN-2_1.ogg"
    aliya "Wha... What happened?"
    voice "aliya/Aliya_Chapter-1_BAN-2_2.ogg"
    aliya "All I remember was taking a bite out of the banana. Then I..."
    aliya "..."

    show aliya neutral5 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_BAN-2_3.ogg"
    aliya "That was a weird dream. Should I stop eating this?"
    voice "aliya/Aliya_Chapter-1_BAN-2_4.ogg"
    aliya "Tastes really weird too, but... I’m still so hungry!"

    hide aliya

    menu:
        "Keep Eating":
            jump ch1_eat_ban_cont
        "Stop and keep the banana":
            jump ch1_eat_ban_stop

# Chapter 1 BAN-5
label ch1_eat_ban_stop:

    scene transparent
    scene black onlayer bglayer
    scene docks-blurred-static
    show aliya neutral5 at hover

    voice "aliya/Aliya_Chapter-1_BAN-5.ogg"
    aliya "I should stop. Who knows what might happen if I eat it again."

    voice "narrator/12-ban5.ogg"
    storyteller "You put the half-eaten banana in your pocket."

    stop sound

    scene black onlayer bglayer

    jump ch1_map_menu

# Chapter 1 BAN-3
label ch1_eat_ban_cont:
    scene transparent
    scene black onlayer bglayer
    scene docks-blurred-static
    show aliya neutral5 at hover

    play sound "audio/eating-banana.ogg" volume 0.35
    voice "aliya/Aliya_Chapter-1_BAN-3.ogg"
    aliya "Hmm... Well, it’s not half bad the second time around."


    show white-bg with dissolve

# Chapter 1 MOV-4
label ch1_eat_ban_fly:
    stop sound
    scene black onlayer bglayer
    scene village-night at Pan((0, 717), (0, 0), 10, repeat=True)
    with dissolve
    play sound "audio/fly-death-scene.ogg" volume 0.3

    voice "aliya/Aliya_Chapter-1_MOV-4_1.ogg"
    aliya "Wow!"
    voice "aliya/Aliya_Chapter-1_MOV-4_2.ogg"
    aliya "I'm flying! The stars, the clouds...{w=1} This is incredible!"
    voice "aliya/Aliya_Chapter-1_MOV-4_3.ogg"
    aliya "Is this because of the banana? Did I just get a power-up?"
    voice "aliya/Aliya_Chapter-1_MOV-4_4.ogg"
    aliya "This is the best! This is..."

    # Chapter 1 BAN-4

    scene black-bg

label ch1_eat_ban_dead:
    scene banana-death-scene with Dissolve(5.0):
        zoom 1.25
        ease 15.0 zoom 1.0

    voice "narrator/13-ban4.ogg"
    storyteller "Back in reality, your joyous expressions transformed into one of distress."

    voice "narrator/13.1-ban4.ogg"
    storyteller "Your body trembled, a seizure overtaking you."

    voice "narrator/14-ban4.ogg"
    storyteller "Onlookers, noticing the sudden change, rushed to your side."

    voice "narrator/14.1-ban4.ogg"
    storyteller "Their hands reaching out in a desperate attempt to stabilize you, to bring you back from the edge."

    voice "narrator/15-ban4.ogg"
    storyteller "Voices called for help, some praying, others instructing to keep you safe."

    voice "narrator/15.1-ban4.ogg"
    storyteller "But your voice, full of wonder and fear just moments ago, now fell silent amidst the chaos."


    scene black-bg with dissolve

    "You died"

    $ analytics_event("death_chapter1", {"event_category": "death", "event_label": "banana"})

    menu:
        "Return to main menu":
            return
        "Reset to before you died":
            jump ch1_eat_ban_wake_up

