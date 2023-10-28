init python:
    def get_platform():
        if renpy.windows:
            return "win"
        elif renpy.macintosh:
            return "mac"
        elif renpy.linux:
            return "linux"
        elif renpy.emscripten:
            return "web"
        else:
            raise Exception("Unknown platform")

    def is_home_domain():
        if renpy.emscripten:
            hostname = emscripten.run_script_string("window.location.hostname")
            return "ascent.lol" in hostname or "aliya.lol" in hostname or "localhost" in hostname or "127.0.0.1" in hostname
        else:
            return False

define env.platform = get_platform()
define env.is_home_domain = is_home_domain()
define env.is_web = env.platform == "web"
