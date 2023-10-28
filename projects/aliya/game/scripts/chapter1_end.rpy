image colosseum_life = Movie(play="images/videos/colosseum.webm")

screen colosseum_life():
    imagemap:
        ground "colosseum_life"

image village_ach = Movie(play="images/videos/village.webm")
screen village_ach():
    imagemap:
        ground "village_ach"

image stables_end = Movie(play="images/videos/stables.webm")
screen stables_end():
    imagemap:
        ground "stables_end"

image handcuffs_scene = Movie(play="images/videos/handcuffs.webm")
screen handcuffs_scene():
    imagemap:
        ground "handcuffs_scene"

image claim_badge = Movie(play="images/videos/ClaimBadge.webm")

#Chapter 1 END-0
label ch1_end:

    play sound "audio/village-ambience.ogg" volume 0.2 loop
    play music "audio/bg_music_end.ogg" volume 0.25

    scene village_ach
    scene black onlayer bglayer
    show screen village_ach onlayer bglayer

    show aliya curious7 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_END-0_1.ogg"
    aliya "{i}What’s this here in the Village?{/i}"
    voice "aliya/Aliya_Chapter-1_END-0_2.ogg"
    aliya "{i}Was that everything?{/i}"

    voice "narrator/19-end0.ogg"
    storyteller "{b}You are about to enter the point of no return. Do you want to proceed?{/b}"

    hide aliya

label ch1_end_choice:
    menu:
        "Proceed to Village":
            jump ch1_village
        "Return Later":
            jump ch1_end_later

#Chapter 1 END-10
label ch1_end_later:

    scene black onlayer bglayer
    scene transparent
    scene village_ach
    scene black onlayer bglayer
    show screen village_ach onlayer bglayer
    show aliya curious6 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_END-10_1.ogg"
    aliya "{i}I might have missed something.{/i}"
    voice "aliya/Aliya_Chapter-1_END-10_2.ogg"
    aliya "{i}I'll come back later.{/i}"
    stop sound
    jump ch1_map_menu

label ch1_village:
    play music "audio/bg_music_end.ogg" volume 0.25

    scene black onlayer bglayer
    scene transparent
    scene village_ach
    scene black onlayer bglayer
    show screen village_ach onlayer bglayer
    with dissolve

    #Chapter 1 END-1
    voice "narrator/20-end1.ogg"
    storyteller "You see the people you were with on the boat starting to walk towards the village."
    voice "narrator/21-end1.ogg"
    storyteller "You try to follow them, but then you were spotted by someone from the market."

    voice "vendor/vendor-2.ogg"
    vendor "Hey you’re the one wh..."
    

    play sound "audio/heartbeat.ogg" volume 0.2

    show aliya furious10 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_END-1.ogg"
    aliya "Crap! That’s the fruit vendor!"

    hide aliya

    menu:
        "Run South":
            jump ch1_end_south
        "Give up":
            jump ch1_end_give_up

#Chapter 1 END-2
#EXT. DOCKS
label ch1_end_south:
    stop sound

    play sound "audio/docks.ogg" volume 0.2 loop

    scene black onlayer bglayer
    scene transparent
    show screen docks_boat_pano onlayer bglayer
    with dissolve

    stop sound
    voice "narrator/22-end2.ogg"
    storyteller "You ran to the docks."

    play sound "audio/running-footsteps.ogg" volume 0.9

    show aliya fearful2 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_END-2.ogg"
    aliya "Nat’s not here! {w=0.5} What do I do?"

    play sound "audio/docks.ogg" volume 0.2 loop

    voice "vendor/vendor-3.ogg"
    vendor "Hey, stop!"
    hide aliya

    menu:
        "Run West":
            jump ch1_end_west
        "Run East":
            jump ch1_end_east
        "Give up":
            jump ch1_end_give_up

    stop sound

# Chapter 1 END-9
label ch1_end_west:

    scene black onlayer bglayer
    scene colosseum_life
    show screen colosseum_life onlayer bglayer

    play sound "audio/colloseum-crowd-cheer.ogg" volume 0.35

    voice "aliya/Aliya_Chapter-1_END-9.ogg"
    aliya "What is this place?"

    menu:
        "Run East":
            jump ch1_end_east
    jump ch1_end_east

#Chapter 1 END-3
label ch1_end_east:
    stop sound
    play music "audio/bg_music_end.ogg" volume 0.25

    scene black onlayer bglayer
    scene stables_end
    show screen stables_end onlayer bglayer
    with dissolve
    voice "narrator/23-end3.ogg"
    storyteller "You entered the stables and ran all the way through the back door."

    show aliya furious7 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_END-3_1.ogg"
    aliya "Darn it!{w=0.3} The back door’s closed!{w=0.3} It’s a dead end!"
    voice "aliya/Aliya_Chapter-1_END-3_2.ogg"
    aliya "{i}I’m trapped! What do I do?{/i}"
    play sound "audio/heartbeat.ogg" volume 0.2

    voice "vendor/vendor-4.ogg"
    vendor "Stop running!"

    hide aliya

    menu:
        "Fight back":
            jump ch1_end_fight
        "Give up":
            jump ch1_end_give_up

#Chapter 1 END-5
label ch1_end_give_up:

    show aliya sad2 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_END-5.ogg"
    aliya "I give up, I..."


    jump ch1_end_drop

#Chapter 1 END-4
label ch1_end_fight:
    play music "audio/bg_music_end.ogg" volume 0.25

    scene black onlayer bglayer
    scene transparent
    show screen bg_stables_screen onlayer bglayer
    show aliya angry10 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_END-4_1.ogg"
    aliya "STAY BACK!"


    voice "narrator/24-end4.ogg"
    storyteller "You punched the vendor."

    voice "vendor/vendor-5.ogg"
    vendor "Ow! My nose! What did you do that for?"

    show aliya hopeful1 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_END-4_2.ogg"
    aliya "I didn’t take the banana. That wasn’t me!"

    voice "vendor/vendor-6.ogg"
    vendor "What are you even talking about?!"
    jump ch1_end_drop

#Chapter 1 END-6
label ch1_end_drop:

    voice "vendor/vendor-7.ogg"
    vendor "You dropped this!"
    show aliya sad12 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_END-6_1.ogg"
    aliya "Oh! This is one of my grandmother’s trinkets!"
    voice "aliya/Aliya_Chapter-1_END-6_2.ogg"
    aliya "Thank you! It must have fallen out when I was at the market."
    voice "aliya/Aliya_Chapter-1_END-6_3.ogg"
    aliya "I’m sorry...{w=0.75} I thought it was because of the banana."

    voice "vendor/vendor-8.ogg"
    vendor "You mean the rotten banana?{w=0.5} Yeah I saw you looking at it.{w=0.2} Hope you didn’t eat it."

#Chapter 1 END-7
label ch1_end_no_eat_ban:
    play music "audio/bg_music_end.ogg" volume 0.25

    play sound "audio/soldiers-marching.ogg" volume 0.2
    voice "narrator/25-end7.ogg"
    storyteller "A group of guards marches towards you. Their captain points his finger towards your direction."

    show guard-captain at right
    voice "guard-captain/guard-captain-1.ogg"
    guard "You there, girl! You're coming with us."
    stop sound

    show aliya hopeful1 at hover
    with dissolve

    voice "aliya/Aliya_Chapter-1_END-7.ogg"
    aliya "Why? It's just a banana. This is just a misunderstanding, I swear!"

    voice "guard-captain/guard-captain-2.ogg"
    guard "Quiet! That is the least of your concerns."

    voice "vendor/vendor-9.ogg"
    vendor "There must be some kind of mistake!"

    voice "guard-captain/guard-captain-3.ogg"
    guard "Another word, and you'll be joining her in a cell."

    scene black with Dissolve(0.1)

    jump ch1_end_ending

# Chapter 1 END-8
label ch1_end_ending:
    stop sound

    scene transparent
    scene black onlayer bglayer
    scene handcuffs_scene
    show screen handcuffs_scene onlayer bglayer
    with dissolve

    voice "narrator/26-end8.ogg"
    storyteller "In the dimming light of the stable, your distressed eyes left an imprint on the stranger's heart."
    voice "narrator/27-end8.ogg"
    storyteller "Whisked away by the guards, the true gravity of your situation hung in the air."
    voice "narrator/27.1-end8.ogg"
    storyteller "As tangible and perplexing as a half-told tale."

    scene black-bg with dissolve
    scene black onlayer bglayer

    $ analytics_event("finished_chapter1", {"event_category": "chapter_finished", "event_label": "chapter1"})

    "END OF CHAPTER 1\n{w=1.0}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ TO BE CONTINUED..."

    if env.is_home_domain == True:
        congrats "Thank you for playing Aliya's Ascent! You can now claim an exclusive official Treasure Badge!"
    else:
        congrats "Thank you for playing Aliya's Ascent!"
        jump end_credits

label ch1_end_menu:
    scene claim_badge with dissolve

    menu:
        "Claim Badge":
            jump ch1_claim_badge
        "More about Treasure":
            $ renpy.run(OpenURL('https://app.treasure.lol/ '))
            jump ch1_end_menu
        "More about Treasure Badges":
            $ renpy.run(OpenURL('https://docs.treasure.lol/infrastructure/player-identity-and-progression/badges-and-achievements'))
            jump ch1_end_menu
        "Visit Gallery to see unlocked Memories":
            call screen gallery
            jump ch1_end_menu
        "Continue to End Credits":
            jump end_credits
