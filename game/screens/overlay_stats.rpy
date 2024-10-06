default stat1 = 50 #Flashlight Charge
default stat2 = 80


default inventory_show = True
default time_menu = True
default stat1_show = True #Flashlight Charge
default stat2_show = True
default codex_active = False
default flashlight_use = False
default flashlight_consume = False
default flashlight_allowed = True

default amina_cmp = False
default gaspard_cmp = False

screen overlay_stats():
    
    tag gui_screens

    zorder 999

    if flashlight_consume:
        if stat1 > 0:
            timer 15.0 action SetVariable("stat1", (stat1 - 1)) repeat True
        else:
            timer 0.01 action [ SetVariable("flashlight_consume", False), SetVariable("flashlight_use", False), SetVariable("dark_environ", True) ] repeat False

    vbox:
        xalign 1.0 offset(-103, 245)  spacing -10
        if amina_cmp:
            button:
                xysize(125,125)
                background "gui/stats/cm_bg.png"
                
                idle_foreground "gui/stats/test.png"##add the face image 
                hover_foreground "gui/stats/test.png"
                action NullAction()
        if gaspard_cmp:
            button:
                xysize(125,125)
                background "gui/stats/cm_bg.png"
                action NullAction()

    if inventory_show:
        button:
            add "gui/stats/avatar_bg.png"
            if briefcase_carry:
                idle_foreground "gui/stats/case.png"
                hover_foreground "gui/stats/case_hv.png"
            else:
                idle_foreground "gui/stats/inventory.png"
                hover_foreground "gui/stats/inventory_hv.png"
            xysize(230,230) xalign 1.0 offset(-50, 30)
            focus_mask True
            action Show("inventory")
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_inventory.ogg"

    vbox:
        spacing 10 offset(15,30)
        if time_menu:
            button:
                idle_background "gui/stats/time_bg.png"
                hover_background "gui/stats/time_bg.png"
                xysize(395, 77)
                text "[dis_hours]:[dis_minutes]" align(0.5, 0.5) yoffset 4 textalign 0.5 color '#bfaa8f' font gui.interface_text_font
                add "gui/stats/signal.png" yalign 0.5 xoffset 50
                if codex_active == True:
                    add "gui/stats/codex_icon.png" yalign 0.5 xalign 1.0 xoffset -50
                action NullAction()
            if codex_active == True:
                button:
                    idle_background "gui/stats/time_bg.png"
                    hover_background At("gui/stats/time_bg.png", outline_transform(2, "#876a33", 4.0))
                    xysize(395, 77)
                    text _("OPEN CODEX") align(0.5, 0.5) yoffset 4 textalign 0.5 color '#bfaa8f' font gui.interface_text_font
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_codex.ogg"
                    action ShowMenu("codex_main")

        if stat1_show:
            button:
                xysize(353,38) xalign 0.5
                bar:
                    right_bar "gui/stats/empty.png"
                    left_bar "gui/stats/stat_1.png"
                    value AnimatedValue(value=stat1, range=100, delay=1.0)
                if flashlight_consume:
                    text _("DRAINING") align(0.5, 0.5) size 22 outlines([(1, "#181112", 0, 0)]) #color u"C69C6D"
                else:
                    text _("STAND BY") align(0.5, 0.5) size 22 outlines([(1, "#181112", 0, 0)]) #color u"C69C6D"
                add "gui/stats/flash.png" xoffset -20 yalign 0.5
        if stat2_show:
            bar:
                xysize(353,38) xalign 0.5
                right_bar "gui/stats/empty.png"
                left_bar "gui/stats/stat_2.png"
                value AnimatedValue(value=stat2, range=100, delay=1.0)
                
    $ tooltip = GetTooltip()

    nearrect:
        focus "tooltip"
        prefer_top True

        frame:
            background Frame("gui/button/choice_idle_background.png", 60, 33, 60, 33, tile=False)
            padding (140, 15, 140, 15)
            xalign 0.5 yoffset 9
            text "[tooltip!t]" font gui.name_text_font color '#bfaa8f'



init python:
    config.overlay_screens.append("overlay_stats")
