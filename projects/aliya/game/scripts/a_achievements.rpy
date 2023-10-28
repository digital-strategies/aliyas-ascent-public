init python:
    achievement.steam_position = "top left"

    achievement_volume_default = 0.4
    achievement_sound_default = "achievement.ogg"

    @renpy.pure
    class UnlockAchievement(Action, DictEquality):
        """
        :doc: other_action

        Displays `message` using :func:`renpy.notify`.
        """

        def __init__(self, achievement_name, sound=achievement_sound_default, volume=achievement_volume_default):
            self.achievement_name = achievement_name
            self.sound = sound
            self.volume = volume

        def predict(self):
            renpy.predict_screen("notify")

        def __call__(self):
            unlock_achievement(self.achievement_name, self.sound, self.volume)

    def to_achievement_code(str):
        res = ''.join(letter for letter in str if letter.isalpha())
        return res.lower()

    def unlock_achievement(achievement_name, sound=achievement_sound_default, volume=achievement_volume_default):
        renpy.play(sound, relative_volume=volume)
        if achievement.has(achievement_name):
            renpy.notify("Memory already unlocked!\n{b}" + achievement_name + "{/b}")
        else:
            achievement.grant(achievement_name)
            # convert achievement name to code for steam
            achievement.grant(to_achievement_code(achievement_name))
            renpy.notify("Memory Unlocked!\n{b}" + achievement_name + "{/b}\n{i}New gallery items available!{/i}")
            analytics_event("achievement_unlocked", {"event_category": "achievement", "event_label": achievement_name})
        achievement.sync()

screen timed_achievement(achievement_name, delay, sound=achievement_sound_default, volume=achievement_volume_default):
    timer delay action UnlockAchievement(achievement_name, sound=sound, volume=volume)
