init python:
    if renpy.emscripten:
        import emscripten, json

        def call_js(script):
            emscripten.run_script(script)

        def call_js_string(script):
            return emscripten.run_script_string(script)

    else:
        def call_js(*args, **kwargs):
            pass

        def call_js_string(*args, **kwargs):
            pass

label ch1_claim_badge:
    $ analytics_event("badge_claim_started")
    $ web3_result = ""
    $ call_js("web3Sign()")
    while not renpy.in_rollback() and web3_result == "":
        $ web3_result = call_js_string("localStorage.getItem('web3Result') || ''")
        # $ print(web3_result)
        pause 0.5

    $ call_js("localStorage.removeItem('web3Result')")

    if web3_result == "success":
        $ analytics_event("badge_claimed")
        $ renpy.notify("Success!")
        jump end_credits
    else:
        jump ch1_end_menu
