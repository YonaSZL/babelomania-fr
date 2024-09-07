## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the title and navigation.
##
## This screen no longer includes a background, and it no longer transcludes
## its contents. It is intended to be easily removable from any given menu
## screen and thus you are required to do some of the heavy lifting for
## setting up containers for the contents of your menu screens.
##
screen main_nav():
    vbox:
        yalign 0.5 xpos 142 spacing 50

        button:
            xysize(120,120)
            add "gui/gm/nav_btn.png"
            add "gui/gm/save.png" at button_fade
            action ShowMenu("load")
            tooltip "Data"

        button:
            xysize(120,120)
            add "gui/gm/nav_btn.png"
            add "gui/gm/options.png" at button_fade
            action ShowMenu("preferences")
            tooltip "Options"


        button:
            xysize(120,120)
            add "gui/gm/nav_btn.png"
            add "gui/gm/history.png" at button_fade
            action ShowMenu("history")
            tooltip "History"
            if main_menu:
                sensitive False


        button:
            xysize(120,120)
            add "gui/gm/nav_btn.png"
            add "gui/gm/about.png" at button_fade
            action ShowMenu("misc")
            tooltip "About"


        ###This will bring up a second set of menu in place of this one with
        ### the gallery, music room etc.
        button:
            xysize(120,120)
            add "gui/gm/nav_btn.png"
            add "gui/gm/extra.png" at button_fade
            action NullAction()
            tooltip "Extras"


    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" font "gui/font/Sok Brubah.ttf" color u"#4b2913" size 40 xanchor .5 offset(205, 50)

screen game_menu(title):

    #style_prefix "game_menu"

    if main_menu:
        add "main_menu_background"
    add "gui/gm/bg.png"

    use main_nav

    
   

    

    button:
        xysize(66,66) pos(1754,189)
        add "gui/gm/quit.png" at button_fade
        action Quit()

    button:
        xysize(66,66) pos(1750,820)
        add "gui/gm/return.png" at button_fade
        action Return()


    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style return_button:
    xpos 60
    yalign 1.0
    yoffset -45

style game_menu_viewport:
    xsize config.screen_width-420
    ysize config.screen_height-200
    align (0.5, 0.5)
    xoffset -50
    

style game_menu_side:
    yfill True
    align (1.0, 0.5)

style game_menu_vscrollbar:
    unscrollable "hide"

style game_menu_label:
    padding (10, 10)
style game_menu_label_text:
    size 45
