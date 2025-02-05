
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with main menu umage

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "main_menu_bg_logo"

    add "gui/main_menu/bg.png" align(0.5, 1.0) yoffset -100

    style_prefix "main"

    hbox:
        align(0.5, 1.0) yoffset -205 spacing 30 #ysize 150
        textbutton _("Continue") action ShowMenu("load") text_size 70 yoffset 15 hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg"
        add "gui/main_menu/divider.png" yoffset 15
        textbutton _("Start") action Start() text_size 100 hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"
        add "gui/main_menu/divider.png" yoffset 15
        textbutton _("Options") action ShowMenu("preferences") text_size 70 yoffset 15 hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg"

    hbox:
        style_prefix "sub"
        align(0.5, 1.0) yoffset -120 spacing 20 
        textbutton _("About") action ShowMenu("misc") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg"

        ###You can comment these out for now
        ###Here to show layout once gallery is added
        text "♦" size 20 yalign 0.5
        textbutton _("Extra") action [SetVariable("nav", "extra"), ShowMenu("gallery")] hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" sensitive persistent.vertical_clear
        ####

        text "♦" size 20 yalign 0.5
        textbutton _("Quit") action Quit() hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_return.ogg"
    


style main_button_text:
    font gui.name_text_font
    yalign 1.0

style sub_button_text:
    size 35
    kerning 5
