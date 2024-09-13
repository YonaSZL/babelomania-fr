##Photo-activated Variables
define bathroom_painting = False

define quicker_dissolve = Dissolve(0.1)

screen photo(var, val, lab):

    add "gui/phone/overlay.png" at phone

    button:
        xysize(185,185) align(1.0, 0.5) xoffset -110
        background "gui/phone/button.png"
        #hover_background At("gui/phone/button.png",outline_transform(6, "#876a3392",4.0))

        at phone_button

        action [Play("sound4", "audio/sfx/gui_camera.ogg"), Show("flash", quicker_dissolve), SetVariable(var, val), Jump(lab)]


screen flash():

    timer 0.2 action Hide("flash",quicker_dissolve)
    add Solid(u"#ffffff")
transform phone():

    align(0.5, 0.5)
    alpha 0.0 zoom 1.2
    easein .3 alpha 1 zoom 1

transform phone_button():
    subpixel True
    alpha 0.0 anchor (0.5, 0.5)
    pause .3
    easein .2 alpha .8

    on idle:
        easein .3 alpha .8 zoom 1
    on hover:
        easein .3 alpha 1 zoom 1.08

