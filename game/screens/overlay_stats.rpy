default stat1 = 50
default stat2 = 80


default inventory_show = True
default time_menu = True
default stat1_show = True
default stat2_show = True
screen overlay_stats():


    if inventory_show:
        button:
            add "gui/stats/avatar_bg.png"
            idle_foreground "gui/stats/placeholder.png"
            hover_foreground At("gui/stats/placeholder.png", outline_transform(2, "#876a33", 4.0))
            xysize(230,230) xalign 1.0 offset(-50, 30)
            focus_mask True
            action NullAction()


    


    vbox:
        spacing 10 offset(30,30)
        if time_menu:
            frame:
                background "gui/stats/time_bg.png"
                xysize(395, 77)
                text "19:23  |  2024.09.06" align(0.5, 0.5) textalign 0.5 color '#bfaa8f'

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
