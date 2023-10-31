init python:
    if renpy.emscripten:
        import emscripten, json

        def analytics_event(name, attributes=None):
            emscripten.run_script("try {{ gtag('event', '{}', {}); }} catch {{ /* fail silently */ }}".format(name, json.dumps(attributes or {})))

    else:
        def analytics_event(*args, **kwargs):
            pass
