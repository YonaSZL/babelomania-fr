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
                hover_foreground At("gui/stats/test.png", outline_transform(2, "#876a33", 4.0))
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
                hover_foreground At("gui/stats/case.png", outline_transform(2, "#876a33", 4.0))
            else:
                idle_foreground "gui/stats/inventory.png"
                hover_foreground At("gui/stats/inventory.png", outline_transform(2, "#876a33", 4.0))
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
                hover_background At("gui/stats/time_bg.png", outline_transform(2, "#876a33", 4.0))
                xysize(395, 77)
                text "[dis_hours]:[dis_minutes]" align(0.5, 0.5) yoffset 4 textalign 0.5 color '#bfaa8f' font "gui/font/Klotee.ttf"
                add "gui/stats/signal.png" yalign 0.5 xoffset 50
                if codex_active == True:
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_codex.ogg"
                    action ShowMenu("codex_main")
                else:
                    action NullAction()

        if stat1_show:
            bar:
                xysize(353,38) xalign 0.5
                right_bar "gui/stats/empty.png"
                left_bar "gui/stats/stat_1.png"
                value AnimatedValue(value=stat1, range=100, delay=1.0)

        if stat2_show:
            bar:
                xysize(353,38) xalign 0.5
                right_bar "gui/stats/empty.png"
                left_bar "gui/stats/stat_2.png"
                value AnimatedValue(value=stat2, range=100, delay=1.0)


init python:
    config.overlay_screens.append("overlay_stats")
