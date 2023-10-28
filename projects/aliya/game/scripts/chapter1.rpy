screen docks_boat_pano():
    imagemap at pan_h_repeat(start=0, end=4368, duration=40.0, linear=True):
        ground "images/bg/docks-boat-pano.png"


define tower_scene_duration = 30.0
default tower_scene = False

screen tower_screen():
    imagemap at pan_v(start=0, end=2448, duration=tower_scene_duration):
        ground "very_tall_tower"

#Chapter 1 M-0
label chapter1:
    $ analytics_event("started_chapter1", {"event_category": "chapter_start", "event_label": "chapter1"})
    $ start_bg_music1()

    scene bg-boat-blurred with dissolve

    play sound "audio/yawn.ogg" volume 0.2
    pause 1.5
    voice "aliya/Aliya_Chapter-1_M-0.ogg"

    show aliya think2 at hover
    aliya "Yawn...{w=0.3} That nap felt good."
    show riverman-side at right
    voice "riverman/Riverman_Chapter1_M-0.ogg"
    riverman "We’ve arrived."


    stop sound
    play sound "audio/docks.ogg" volume 0.2 loop
    #Chapter 1 M-1
    voice "aliya/Aliya_Chapter-1_M-1.ogg"
    aliya "I can see the village from here!"

    scene black with dissolve
    scene transparent
    scene black onlayer bglayer
    show screen docks_boat_pano onlayer bglayer
    with dissolve
    show riverman-neutral at right
    with easeinright

    voice "riverman/Riverman_Chapter1_M-1_1.ogg"
    riverman "I would like everyone’s attention."
    voice "riverman/Riverman_Chapter1_M-1_2.ogg"
    riverman "Congratulations to everyone for making it here."
    voice "riverman/Riverman_Chapter1_M-1_3.ogg"
    riverman "I have little time for questions."
    voice "riverman/Riverman_Chapter1_M-1_4.ogg"
    riverman "You’ll figure things out soon enough. Welcome to your new home."
    voice "riverman/Riverman_Chapter1_M-1_5.ogg"
    riverman "Gather your belongings and get going."

    hide riverman-neutral

#Chapter 1 M-2
    # camera:
    #     perspective True
    #     zpos 0 xpos 0

    show aliya angry4 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_M-2.ogg"
    aliya "So...{w=1} The old man’s useless and abandoned us here. {w=0.5} Where should I go?"
    hide aliya angry4

label ch1_docks_menu:
    menu:
        "Continue looking around":
            jump ch1_docks_stay
        "Leave docks":
            stop sound
            jump ch1_map_menu

label ch1_docks_stay:
    pause
    jump ch1_docks_menu

# Chapter 1 B-1
label ch1_boat:
    scene transparent
    scene black onlayer bglayer
    show screen docks_boat_pano onlayer bglayer
    with dissolve
    show aliya curious5 at hover
    with dissolve

    play sound "audio/docks.ogg" volume 0.2 loop


    voice "aliya/Aliya_Chapter-1_B-1_1.ogg"
    aliya "{i}I suppose it wouldn’t hurt to ask him where to go.{/i}"

    show aliya curious6 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_B-1_2.ogg"
    aliya "Excuse me, Mister Riverman, sir.."

    show riverman-pissed at right
    with easeinright

    voice "riverman/Riverman_Chapter1_B-1_1.ogg"
    riverman "You again... If you're looking for answers you won't find them on the boat."

    hide riverman-pissed
    show riverman-angry1 at right
    show riverman-angry1 at shake

    voice "riverman/Riverman_Chapter1_B-1_2.ogg"
    riverman "Now scram!"

    stop sound

    scene black onlayer bglayer
    jump ch1_map_menu

#Chapter 1 TOW-1
label ch1_towers:

    scene black
    scene black onlayer bglayer
    show screen tower_screen onlayer bglayer
    with dissolve
    pause tower_scene_duration

    show aliya furious2 at hover
    with dissolve

    voice "riverman/Riverman_Chapter1_TOW-1.ogg"
    riverman "You’re not the first with that look on your face."

    hide aliya

    label ch1_tower_choice:
        menu:
            "How does it do that?":
                jump ch1_how
            "Why did you bring us here?":
                jump ch1_why

#Chapter 1 TOW-2
label ch1_how:

    show aliya curious7 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_TOW-2_1.ogg"
    aliya "How does it do that? You know, the floating ball?"

    show riverman-speaking at right
    with easeinright

    voice "riverman/Riverman_Chapter1_TOW-2_0.ogg"
    riverman "What I know is that this knowledge has been lost for centuries."
    voice "riverman/Riverman_Chapter1_TOW-2_1.ogg"
    riverman "Legend has it that it was created by a powerful Legion known as Kar-El."


    show aliya curious5 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_TOW-2_2.ogg"
    aliya "Where can I find this Kar-El?"

    voice "riverman/Riverman_Chapter1_TOW-2_2.ogg"
    riverman "Well, you’re asking the wrong person. I’m just a man with a boat."

    jump ch1_why

#Chapter 1 TOW-3
label ch1_why:

    show aliya think2 at hover
    with dissolve
    voice "aliya/Aliya_Chapter-1_TOW-3_1.ogg"
    aliya "Well...{w=0.6} Now I’m curious why you brought us here."

    hide riverman-speaking
    show riverman-neutral1 at right
    with dissolve

    voice "riverman/Riverman_Chapter1_TOW-3_1.ogg"
    riverman "You're part of the migration, it's my job to bring you here."

    voice "aliya/Aliya_Chapter-1_TOW-3_2.ogg"
    aliya "But why are we migrating?{w=1.2} Where are we migrating from?{w=1.2} Why doesn’t anything make sense?{nw}"
    voice "aliya/Aliya_Chapter-1_TOW-3_3.ogg"
    aliya "WHY CAN’T I REMEMBER ANYTHING?!"

    show aliya sad2 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_TOW-3_4.ogg"
    aliya "I’m sorry...{w=0.9} I’m just a little tired from the trip I think."

    voice "riverman/Riverman_Chapter1_TOW-3_2.ogg"
    riverman "You don't need to apologize, the panic attacks will subside as you begin your new life here."
    voice "riverman/Riverman_Chapter1_TOW-3_3.ogg"
    riverman "We've all been through them..."

#Chapter 1 TOW-4
    voice "riverman/Riverman_Chapter1_TOW-4_1.ogg"
    riverman "You’ll get used to it."

    hide aliya3_stop with dissolve
    show aliya hopeful1 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_TOW-4_1.ogg"
    aliya "Thanks! I’m Aliya, by the way.{w=1} At least that’s what’s written on my little pouch here."

    riverman "..."

    hide riverman-neutral1
    show riverman-happy5 at right
    with dissolve

    voice "riverman/Riverman_Chapter1_TOW-4_2.ogg"
    nat "Nat. But most people call me the Riverman. My friends stick with Nat, though."
    voice "riverman/Riverman_Chapter1_TOW-4_3.ogg"
    nat "I’m one of the few Legions sailing on these waters but there are many others out here."
    voice "riverman/Riverman_Chapter1_TOW-4_4.ogg"
    nat "Swing by the Rivermen Hut sometime, I’ll cook you a Riverman special."


    show aliya happy3 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_TOW-4_2.ogg"
    aliya "I’ll definitely take you up on that offer!"

    hide riverman-happy5
    show riverman-happy6 at right
    with dissolve

    voice "riverman/Riverman_Chapter1_TOW-4_5.ogg"
    nat "Oh, and pay a visit to Anton in the village, even though half the people think he’s crazy..."
    voice "riverman/Riverman_Chapter1_TOW-4_6.ogg"
    nat "He was once a Quester, so he’s most likely the guy who knows what goes on in here."

    voice "aliya/Aliya_Chapter-1_TOW-4_3.ogg"
    aliya "I’ll pay him a visit.{w=0.5} Thanks, Nat!"

    $ tower_scene = True

    scene black onlayer bglayer
    jump ch1_map_menu
