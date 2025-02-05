screen think(question, op_1_text, op_1_lab, op_2_text, op_2_lab, op_3_text, op_3_lab, op_4_text, op_4_lab):

    style_prefix "think"
    frame:
        
        text question size 45 color '#bfaa8f'
        at hover

    grid 2 2:
        align (0.5, 0.5) xspacing 500 yspacing 200 yoffset -100 xoffset -50
        if op_1_text != "None":
            button:
                add "gui/think/btn.png"
                hover_sound "audio/sfx/think_hover.ogg"
                activate_sound "audio/sfx/think_choice.ogg"
                text op_1_text align(0.5, 0.5) size 30 xsize 550 xoffset 50 textalign 0.5 color '#bfaa8f' at textblur

                add "gui/think/fog.png" offset(-50, -50) zoom .8 blur 4.0 at fog1
                add "gui/think/fog.png" offset(190, 50) zoom .7 blur 4.0 at fog2

                action Jump(op_1_lab)

        if op_2_text != "None":
            button:
                add "gui/think/btn.png"
                hover_sound "audio/sfx/think_hover.ogg"
                activate_sound "audio/sfx/think_choice.ogg"
                text op_2_text align(0.5, 0.5) size 30 xsize 550 xoffset 50 textalign 0.5 color '#bfaa8f' at textblur

                add "gui/think/fog.png" offset(-50, -50) zoom .8 blur 4.0 at fog1
                add "gui/think/fog.png" offset(190, 50) zoom .7 blur 4.0 at fog2

                action Jump(op_2_lab)

        if op_3_text != "None":
            button:
                add "gui/think/btn.png"
                hover_sound "audio/sfx/think_hover.ogg"
                activate_sound "audio/sfx/think_choice.ogg"
                text op_3_text align(0.5, 0.5) size 30 xsize 550 xoffset 50 textalign 0.5 color '#bfaa8f' at textblur

                add "gui/think/fog.png" offset(-50, -50) zoom .8 blur 4.0 at fog1
                add "gui/think/fog.png" offset(190, 50) zoom .7 blur 4.0 at fog2

                action Jump(op_3_lab)

        if op_4_text != "None":
            button:
                add "gui/think/btn.png"
                hover_sound "audio/sfx/think_hover.ogg"
                activate_sound "audio/sfx/think_choice.ogg"
                text op_4_text align(0.5, 0.5) size 30 xsize 550 xoffset 50 textalign 0.5 color '#bfaa8f' at textblur

                add "gui/think/fog.png" offset(-50, -50) zoom .8 blur 4.0 at fog1
                add "gui/think/fog.png" offset(190, 50) zoom .7 blur 4.0 at fog2

                action Jump(op_4_lab)




###Styles
style think_frame:
    align(0.5, 1.0) yoffset -100
    background Frame("gui/think/question.png", 60, 70, 60, 70, tile=False)
    padding (140, 40, 140, 40)

style think_button:
    xysize(613,209) align(0.5, 0.5) padding (50, 00, 50, 0)


    

    


####Transforms
transform hover():
    subpixel True
    yoffset 0
    easein 5.0 yoffset 20
    easein 5.0 yoffset 0
    repeat


transform fog1():

    parallel:
        subpixel True
        yoffset 0
        easein 4.0 yoffset 10 xoffset 5 zoom .97
        easein 4.0 yoffset 0 xoffset 0 zoom 1
        repeat

    parallel:
        subpixel True
        on idle:
            easein 1.0 xpos 0 alpha 1
        on hover:
            easein 1.0 xpos -150 alpha 0

transform fog2():

    parallel:
        subpixel True
        yoffset 0
        easein 4.0 yoffset 10 xoffset 5
        easein 4.0 yoffset 0 xoffset 0
        repeat

    parallel:
        subpixel True
        on idle:
            easein 1.0 xpos 0 alpha 1
        on hover:
            easein 1.0 xpos 150 alpha 0

transform textblur():
    blur 10 alpha .5
    on idle:
        easein 1.0 blur 2 alpha .5
    on hover:
        easein 1.0 blur 0 alpha 1

init python:

    def overlay_off():
        global time_menu
        global codex_active
        global inventory_show
        global stat1_show
        global stat2_show
        global stat3_show
        global stat4_show
        global tabitha_cmp
        #global amina_cmp
        time_menu = False
        codex_active = False
        inventory_show = False
        stat1_show = False
        stat2_show = False
        stat3_show = False
        stat4_show = False
        tabitha_cmp = False
        #amina_cmp = False
        return
    
    def overlay_on():
        global time_menu
        global codex_active
        global inventory_show
        global stat1_show
        global stat2_show
        global stat3_show
        global stat4_show
        global tabitha_cmp
        #global amina_cmp
        time_menu = True
        codex_active = True
        inventory_show = True
        stat1_show = True
        stat2_show = True
        stat3_show = True
        stat4_show = True
        tabitha_cmp = True
        #amina_cmp = True
        return