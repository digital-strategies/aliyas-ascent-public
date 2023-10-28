init python:
    if renpy.emscripten:
        import emscripten, json

        def analytics_event(name, attributes=None):
            emscripten.run_script("gtag('event', '{}', {});".format(name, json.dumps(attributes or {})))

    else:
        def analytics_event(*args, **kwargs):
            pass
