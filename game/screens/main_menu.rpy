
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with main menu umage

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "main_menu_bg"

    add "gui/main_menu/bg.png" align(0.5, 1.0) yoffset -100

    style_prefix "main"

    hbox:
        align(0.5, 1.0) yoffset -205 spacing 30 #ysize 150
        textbutton "Continue" action ShowMenu("load") text_size 70 yoffset 15
        add "gui/main_menu/divider.png" yoffset 15
        textbutton "Start" action Start() text_size 100
        add "gui/main_menu/divider.png" yoffset 15
        textbutton "Options" action ShowMenu("preferences") text_size 70 yoffset 15

    hbox:
        style_prefix "sub"
        align(0.5, 1.0) yoffset -120 spacing 20 
        textbutton "About" action ShowMenu("misc")

        ###You can comment these out for now
        ###Here to show layout once gallery is added
        text "♦" size 20 yalign 0.5
        textbutton "Gallery" action NullAction()
        ####

        text "♦" size 20 yalign 0.5
        textbutton "Quit " action Quit()
        


style main_button_text:
    font "gui/font/Sok Brubah.ttf"
    yalign 1.0

style sub_button_text:
    size 35
    kerning 5
