init python:
    import pygame_sdl2 as pygame

    config.keymap['dismiss'].remove('mouseup_1')
    config.keymap['dismiss'].remove('K_RETURN')
    config.keymap['dismiss'].remove('K_KP_ENTER')
    config.keymap['dismiss_unfocused'].append('K_SPACE')
    config.keymap['dismiss_hard_pause'].append('K_SPACE')
    config.keymap['focus_left'] = []
    config.keymap['focus_right'] = []
    config.keymap['focus_up'] = []
    config.keymap['focus_down'] = []
    config.keymap['viewport_leftarrow'] = []
    config.keymap['viewport_rightarrow'] = []
    config.keymap['viewport_uparrow'] = []
    config.keymap['viewport_downarrow'] = []

    nav_remider_timer = 0.0
    nav_remider_threshold_default = 60.0
    nav_remider_threshold = nav_remider_threshold_default
    nav_reminder_force = False

    def detect_interaction():
        keys = pygame.key.get_pressed()
        (m_1, m_2, m_3) = pygame.mouse.get_pressed()
        if keys[pygame.K_SPACE] or m_1 or m_2 or m_3:
            # print("Interaction detected", keys[pygame.K_SPACE], m_1, m_2, m_3)
            SetVariable("nav_remider_timer", 0.0)()

    def set_show_nav_reminder(delay=nav_remider_threshold_default, force=True):
        # print("Setting nav reminder", delay, force)
        SetVariable("nav_remider_timer", 0.0)()
        SetVariable("nav_remider_threshold", delay)()
        SetVariable("nav_remider_force", force)()

    def show_nav_reminder():
        # print("Showing nav reminder", nav_remider_timer, nav_remider_threshold, nav_remider_force)
        SetVariable("nav_remider_timer", 0.0)()
        SetVariable("nav_remider_threshold", nav_remider_threshold_default)()
        SetVariable("nav_remider_force", False)()

        if not nav_remider_force and renpy.get_screen("notify"):
            return

        if not nav_remider_force and renpy.get_screen("choice"):
            return

        if not nav_remider_force and renpy.get_screen("map_menu_screen"):
            return

        if not nav_remider_force and renpy.get_screen("end_credits_screen"):
            return

        if not nav_remider_force and renpy.get_screen("gallery"):
            return

        renpy.notify("Press {b}SPACE{/b} to advance the game")

screen nav_reminder():
    frame:
        timer 0.1 action Function(detect_interaction) repeat True
        timer 1.0 action If(nav_remider_timer >= nav_remider_threshold, false = SetVariable("nav_remider_timer", nav_remider_timer + 1.0), true = [SetVariable("nav_remider_timer", 0.0), Function(show_nav_reminder)]) repeat True
