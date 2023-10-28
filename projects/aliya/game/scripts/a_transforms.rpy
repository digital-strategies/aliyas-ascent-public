init:
    $ hover = Position(xpos=.05, ypos=.85, xanchor='left')
    $ hover_r = Position(xpos=1.0, ypos=.85, xanchor='right')

# shake character
transform shake:
    ease .06 xoffset 24
    ease .06 xoffset -24
    ease .05 xoffset 20
    ease .05 xoffset -20
    ease .04 xoffset 0

# bounce character animation (left to right)
transform bounce_left:
    ease 0.5 xalign 1.0
    ease 0.5 xalign 0.8

# bounce character animation (right to left)
transform bounce_right:
    xalign 2.0
    linear 0.5 xalign 0.0
    ease 0.1 xalign 0.1

transform zoom:
    xalign 1.0
    linear .1 zoom 1.25
    ease .5 zoom 1.0

transform flip:
    xzoom -1.0

transform hide_after(hide_delay=3.0, transition_duration=0.5):
    alpha 1.0
    pause hide_delay
    linear transition_duration alpha 0.0

"""Panning functions

Parameters
----------
start : int, optional (default 0)
    Initial position of the image in pixels (from the left). Range between 0 and image width or height.
end : int, optional (default 1000)
    Final position of the image in pixels (from the left). Range between 0 and image width or height.
    Must always be greater than start, even if reverse is True.
duration : float, optional (default 10.0)
    Duration of the animation in seconds.
reverse : bool, optional (default False)
    If True, the image will pan from right to left instead of left to right (or top to bottom instead of bottom to top).
linear : bool, optional (default False)
    If True, the animation will be linear, otherwise it will be eased.
"""

define pan_screen_w = 1280
define pan_screen_h = 720

"pan left to right or right to left once"
transform pan_h(start=0, end=1000, duration=10.0, reverse=False, linear=False):
    subpixel True
    xoffset (-end + pan_screen_w if reverse else -start)
    choice linear == True:
        linear duration xoffset (-start if reverse else -end + pan_screen_w)
    choice linear == False:
        ease duration xoffset (-start if reverse else -end + pan_screen_w)

"pan left to right or right to left once, go back and repeat forever"
transform pan_h_repeat(start=0, end=1000, duration=10.0, reverse=False, linear=False):
    pan_h(start=start, end=end, duration=duration, reverse=reverse, linear=linear)
    pan_h(start=start, end=end, duration=duration, reverse=not reverse, linear=linear)
    repeat

"pan bottom to top or top to bottom once"
transform pan_v(start=0, end=1000, duration=10.0, reverse=False, linear=False):
    subpixel True
    yoffset (-start if reverse else -end + pan_screen_h)
    choice linear == True:
        linear duration yoffset (-end + pan_screen_h if reverse else -start)
    choice linear == False:
        ease duration yoffset (-end + pan_screen_h if reverse else -start)

"pan bottom to top or top to bottom, go back and repeat forever"
transform pan_v_repeat(start=0, end=1000, duration=10.0, reverse=False, linear=False):
    pan_v(start=start, end=end, duration=duration, reverse=reverse, linear=linear)
    pan_v(start=start, end=end, duration=duration, reverse=not reverse, linear=linear)
    repeat

