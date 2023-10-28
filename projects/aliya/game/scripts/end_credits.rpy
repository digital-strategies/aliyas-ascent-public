# run "node calcCreditsTime.js" to calculate total time of the credits
define end_credits_time = 141.0
define initial_pause_time = 1.0

image end_credits_toad_vid = Movie(play="images/videos/toadstoolz-credits.webm", loop=True)
image end_credits_bfly_vid = Movie(play="images/videos/battlefly.webm", loop=True)
image end_credits_boat_vid = Movie(play="images/videos/boat_sway.webm", size=(1280, 720), loop=True)
image end_credits_aliya_vid = Movie(play="images/videos/aliya-credits.webm", loop=True)
image end_credits_smol_vid = Movie(play="images/videos/smol-controller.webm", loop=True)
image end_credits_colosseum_vid = Movie(play="images/videos/colosseum.webm", loop=True)
image end_credits_village_vid = Movie(play="images/videos/village.webm", loop=True)
image end_credits_overlay:
    "images/bg/black-bg.png"
    alpha 0.75

screen end_credits_1():
    add "end_credits_aliya_vid"
    add "end_credits_overlay"

    style_prefix "credits_lg"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "Credits"
            null height 50

            label "Dedicated to T"
            null height 50

            label "World"
            text _("{a=https://bridgeworld.treasure.lol}Bridgeworld{/a}")
            null height 40

            label "Original Story"
            text _("{a=https://docs.bridgeworld.treasure.lol/lore/bridgeworld-season-1-aliyas-ascent/}Aliya's Ascent by Andiamo{/a}")

screen end_credits_2():
    add "end_credits_smol_vid"
    add "end_credits_overlay"

    style_prefix "credits"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "Production"
            text _("{a=https://x.com/digistrats_com}Digital Strategies Guild{/a}")
            null height 30

            label "Executive Producer"
            text "DIGI"
            null height 30

            label "Senior Producer"
            text "Jovar"
            null height 30

            label "Business Development"
            text "Lee"
            null height 30

            label "VP Portfolio Strategy"
            text "Eric"

screen end_credits_3():
    add "sheet-1"
    add "end_credits_overlay"

    style_prefix "credits"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "Creative Director"
            text "Mike"
            null height 30

            label "Narrative Design"
            text "Mike"
            null height 30

            label "Script Design"
            text "Mike"
            text _("{a=https://www.youtube.com/watch?v=dQw4w9WgXcQ}Marcin{/a}")
            null height 30

            label "Additional Narrative"
            text "Elle"
            text _("{a=https://x.com/n8amis1}Spire (n8amis){/a}")
            null height 30

screen end_credits_4():
    add "sheet-3"
    add "end_credits_overlay"

    style_prefix "credits"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "Engine Programming"
            null height 10
            text _("{a=https://www.youtube.com/watch?v=dQw4w9WgXcQ}Marcin{/a}")
            null height 30

            label "Gameplay Programming"
            null height 10
            text _("{a=https://www.youtube.com/watch?v=dQw4w9WgXcQ}Marcin{/a}")
            null height 30

            label "QA Director"
            null height 10
            text _("{a=https://www.youtube.com/watch?v=dQw4w9WgXcQ}Marcin{/a}")
            null height 30

            label "Tools Programming"
            null height 10
            text _("{a=https://www.youtube.com/watch?v=dQw4w9WgXcQ}Marcin{/a}")

screen end_credits_5():
    add "menu-bg"
    add "end_credits_overlay"

    style_prefix "credits_sm"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "Gameplay Animation"
            text _("{a=https://www.youtube.com/watch?v=dQw4w9WgXcQ}Marcin{/a}")
            text "Andrey"
            null height 18

            label "Web Content & UX"
            text _("{a=https://www.youtube.com/watch?v=dQw4w9WgXcQ}Marcin{/a}")
            null height 18

            label "UI Design"
            text "Andrey"
            null height 18

            label "Background Design"
            text "Andrey"
            text "Clarence"
            null height 18

            label "Character Design"
            text "Andrey"
            text "Clarence"
            null height 18

            label "Additional Character Design"
            text _("{a=https://x.com/digistrats_com}DIGI{/a}")


screen end_credits_6():
    add "end_credits_boat_vid"
    add "end_credits_overlay"

    style_prefix "credits"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "AI Design Lead"
            null height 20
            text "Andrey"
            null height 10
            text "Clarence"
            null height 40

            label "Animations"
            null height 20
            text "Andrey"
            null height 10
            text "Clarence"
            null height 40

            label "Motion Capture"
            null height 20
            text "Ted"
            null height 10
            text "Fred"


screen end_credits_7():
    add "end_credits_bfly_vid"
    add "end_credits_overlay"

    style_prefix "credits"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "Head of Sound Design"
            null height 20
            text "Lee"
            null height 80

            label "Junior Sound Design"
            null height 20
            text "Andrey"
            null height 80

            label "Assistant Junior Sound Design"
            null height 20
            text _("{a=https://sash-alexander.com}Sash{/a}")

screen end_credits_8():
    add "end_credits_toad_vid"
    add "end_credits_overlay"

    style_prefix "credits_sm"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "Background Design"
            null height 20
            text "Andrey"
            null height 10
            text "Clarence"
            null height 40

            label "Concept Art"
            null height 20
            text "Andrey"
            null height 10
            text "Clarence"
            null height 40

            label "Practical Effects"
            null height 20
            text "Nat"
            null height 40

            label "Stunt Double"
            null height 20
            text "Ted"

screen end_credits_9():
    add "end_credits_colosseum_vid"
    add "end_credits_overlay"

    style_prefix "credits"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "Voice Acting / Smol Ted"
            null height 20
            text _("{a=https://x.com/BadgerBigger}Biggerbadger{/a}")
            null height 100

            label "Voice Acting / Guard"
            null height 20
            text "Smolinator"
            null height 100

screen end_credits_10():
    add "village-1"
    add "end_credits_overlay"

    style_prefix "credits"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "Additional Music by"
            null height 60
            text _("{a=https://sash-alexander.com}Sash{/a}")
            null height 20
            text _("{a=https://x.com/BadgerBigger}BiggerBadger{/a}")
            null height 20
            text _("{a=https://x.com/WTThemeMusic}Weary Traveller Studios{/a}")

screen end_credits_11():
    add "banana-death-scene"
    add "end_credits_overlay"

    style_prefix "credits"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "Internal Playtesting"
            null height 20
            text "Elle"
            null height 20
            text _("{a=https://sash-alexander.com}Sash{/a}")
            null height 20
            text "Aly"
            null height 20
            text "Kal"


screen end_credits_12():
    add "end_credits_village_vid"
    add "end_credits_overlay"

    style_prefix "credits_sm"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "Special Thanks"
            null height 50
            text _("{a=https://x.com/Flook_eth}Flook{/a}")
            null height 20
            text _("{a=https://x.com/0atmilkicelatt3}Brokeboy{/a}")
            null height 20
            text _("{a=https://x.com/LinkWarLord}Josh11{/a}")
            null height 20
            text _("{a=https://x.com/n8amis1}N8amis{/a}")
            null height 20
            text _("{a=https://x.com/MagicHourPod}Braiker{/a}")
            null height 20
            text _("{a=https://x.com/SkidRenz}SkidRenz{/a}")
            null height 20
            text _("{a=https://x.com/digistrats_com}Mikeee{/a}")
            null height 20
            text _("{a=https://x.com/digistrats_com}Elle{/a}")

screen end_credits_13():
    add "proto-4"
    add "end_credits_overlay"

    style_prefix "credits_sm"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "Special Thanks"
            null height 50
            text _("{a=https://sash-alexander.com}Sash{/a}")
            null height 20
            text _("{a=https://x.com/jpatten__}John Patten{/a}")
            null height 20
            text _("{a=https://x.com/karelvuong}Karel Vuong{/a}")
            null height 20
            text _("{a=https://x.com/Jpegape1}JpegApe{/a}")
            null height 20
            text _("{a=https://x.com/WTThemeMusic}Weary Traveller Studios{/a}")
            null height 20
            text _("{a=https://x.com/smolverse}Smolverse{/a}")
            null height 20
            text _("{a=https://x.com/Treasure_DAO}TreasureDAO{/a}")
            null height 20
            text _("{a=https://x.com/toadstoolzNFT}Toadstoolz{/a}")

screen end_credits_14():
    add "proto-1"
    add "end_credits_overlay"

    style_prefix "credits_sm"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "Special Thanks"
            null height 50
            text _("{a=https://x.com/KnightsOfTheEth}Knights of the Ether{/a}")
            null height 20
            text _("{a=https://x.com/LifeVerse_GG}Lifeverse{/a}")
            null height 20
            text _("{a=https://x.com/TheLostDonkeys}The Lost Donkeys{/a}")
            null height 20
            text _("{a=https://x.com/TalesofElleria}Tales of Elleria{/a}")
            null height 20
            text _("{a=https://x.com/PlayMightyHero}Mighty Action Heroes{/a}")
            null height 20
            text _("{a=https://x.com/DiegoVidaurres/}Diego (Zeelex){/a}")
            null height 20
            text _("{a=https://x.com/The_Beacon_GG}The Beacon{/a}")
            null height 20
            text _("{a=https://x.com/Spire_DAO}SpireDAO{/a}")

screen end_credits_15():
    add "proto-2"
    add "end_credits_overlay"

    style_prefix "credits_sm"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "Special Thanks"
            null height 50
            text _("{a=https://x.com/kurorobeast}Kuroro Beasts{/a}")
            null height 20
            text _("{a=https://x.com/kurorosage}Kurosage{/a}")
            null height 20
            text "MagicMan"
            null height 20
            text _("{a=https://x.com/jonEfivealive}Smolinator{/a}")
            null height 20
            text _("{a=https://x.com/0x_Astro}Astro{/a}")
            null height 20
            text _("{a=https://x.com/kkowll}Kowl{/a}")
            null height 20
            text _("{a=https://x.com/treasuretimes_}Treasure Times{/a}")
            null height 20
            text _("{a=https://x.com/officialabenger}OfficialAbenger{/a}")
            null height 20
            text _("{a=https://x.com/battleflygame}Battlefly{/a}")

screen end_credits_thanks():
    add "black-bg"

    style_prefix "credits_lg"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            label "Thanks For Playing!"

style credits_vbox:
    xalign 0.5
    text_align 0.5
    spacing 0

style credits_lg_vbox is credits_vbox
style credits_sm_vbox is credits_vbox

style credits_label:
    xalign 0.5
    justify True
    text_align 0.5
    ymargin 0

style credits_lg_label is credits_label
style credits_sm_label is credits_label

style credits_label_text:
    xalign 0.5
    justify True
    size 44
    text_align 0.5
    color "#ff0000"
    ymargin 0

style credits_lg_label_text is credits_label_text:
    size 64
style credits_sm_label_text is credits_label_text:
    size 32

style credits_text:
    xalign 0.5
    size 32
    justify True
    text_align 0.5
    color "#ffffff"
    ymargin 0

style credits_lg_text is credits_text:
    size 44
style credits_sm_text is credits_text:
    size 24


screen space_dismiss():
    key "K_SPACE" action Jump("skip_end_credits")

screen darken_overlay():
    add "end_credits_overlay"

label end_credits:
    scene black onlayer hidden
    scene black onlayer bglayer
    scene black
    with Dissolve(0.5)
    $ renpy.music.clear_all_channels()
    $ renpy.music.queue(["<silence 1.0>", "end-credits/end-credits-music.ogg", "<silence 1.0>"], channel='music', loop=False, clear_queue=True, fadein=1.0, tight=True, relative_volume=1.0)
    show screen space_dismiss
    show screen timed_achievement("End Credits", end_credits_time)

    show screen end_credits_1
    with Dissolve(1.0)
    pause 8.0

    show screen end_credits_2
    with Dissolve(1.0)
    pause 8.0

    show screen end_credits_3
    with Dissolve(1.0)
    pause 8.0

    show screen end_credits_4
    with Dissolve(1.0)
    pause 8.0

    show screen end_credits_5
    with Dissolve(1.0)
    pause 8.0

    show screen end_credits_6
    with Dissolve(1.0)
    pause 8.0

    show screen end_credits_7
    with Dissolve(1.0)
    pause 8.0

    show screen end_credits_8
    with Dissolve(1.0)
    pause 8.0

    show screen end_credits_9
    with Dissolve(1.0)
    pause 8.0

    show screen end_credits_10
    with Dissolve(1.0)
    pause 8.0

    show screen end_credits_11
    with Dissolve(1.0)
    pause 8.0

    show screen end_credits_12
    with Dissolve(1.0)
    pause 8.0

    scene
    show screen end_credits_13
    with Dissolve(1.0)
    pause 8.0

    show screen end_credits_14
    with Dissolve(1.0)
    pause 8.0

    show screen end_credits_15
    with Dissolve(1.0)
    pause 8.0

    show screen end_credits_thanks
    with Dissolve(3.0)

    hide screen space_dismiss
    pause 10.0
    hide screen timed_achievement
    return

label skip_end_credits:
    hide screen timed_achievement
    hide screen space_dismiss
    return
