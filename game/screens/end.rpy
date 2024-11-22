screen ending():

    add "gui/ending/bg.png"
    add "gui/ending/thank you.png"


    button:
        xysize(320, 80) align(0.5, 0.5)  yoffset 275
        frame:
            background Solid(u"#ffffff") at end_bg
        label "Main Menu" text_size 70 align(0.5, 0.5) at end_text2
        label "Main Menu" text_size 70 text_color u"#ffffff" align(0.5, 0.5) at end_text1
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_codex.ogg"
        action MainMenu()


    hbox:
        align(0.5, 1.0) yoffset 50 xoffset 170 spacing 700
        button:
            xysize(358,314) anchor(0.5, 0.5)
            add "gui/ending/patreon.png"
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_codex.ogg" 
            action OpenURL("https://www.patreon.com/JPDE")
            at socfloat(0.1, 5.0)
        
        button:
            xysize(358,314) anchor(0.5, 0.5)
            add "gui/ending/itch.png"
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_codex.ogg"
            action OpenURL("https://jpde.itch.io/babelomania/rate")
            at socfloat(0.3, 4.5)

transform end_bg():

    xzoom 0.0

    on hover:
        easein 0.3 xzoom 1.0
    on idle:
        easein 0.3 xzoom 0.0
transform end_text1():
    alpha 0
    on idle:
        linear 0.3 alpha 1.0
    on hover:
        linear 0.3 alpha 0.0

transform end_text2():
    alpha 1
    on idle:
        linear 0.3 alpha 0.0
    on hover:
        linear 0.3 alpha 1.0

transform socfloat(pas, dur):
    subpixel True
    yoffset 50
    on idle:
        parallel:
            easein dur yoffset 75
            easein dur yoffset 50
            pause pas
            repeat
        parallel:
            linear 0.3 alpha 0.5

    on hover:
        linear 0.3 alpha 1.0
