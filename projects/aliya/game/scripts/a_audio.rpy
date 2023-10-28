init python:
    renpy.music.register_channel("gallery", mixer="music")
    renpy.music.register_channel("main_menu", mixer="voice", movie=True)
    renpy.music.register_channel("movie_voice", mixer="voice", loop=False, stop_on_mute=True, movie=True)

