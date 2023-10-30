# run "node calcCreditsTime.js" to calculate total time of the credits
define end_credits_time = 140.0

image end_credits = Movie(play="images/videos/end_credits.webm", loop=False)

screen end_credits():
    add "end_credits"
    imagemap:
        ground "end_credits"
        hotspot (0, 0, 1920, 1080) action OpenURL("https://github.com/digital-strategies/aliyas-ascent-public#credits")

screen space_dismiss():
    key "K_SPACE" action Jump("skip_end_credits")

label end_credits:
    scene black onlayer hidden
    scene black onlayer bglayer
    scene black
    with Dissolve(0.5)
    $ renpy.music.clear_all_channels()
    show screen space_dismiss
    show screen timed_achievement("End Credits", end_credits_time)

    show screen end_credits
    with Dissolve(1.0)

    pause 145.0
    hide screen timed_achievement
    hide screen space_dismiss
    return

label skip_end_credits:
    hide screen timed_achievement
    hide screen space_dismiss
    return
