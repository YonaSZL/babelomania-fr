
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
EasyRenPyGui is made by {a=https://github.com/shawna-p}Feniks{/a} {a=https://feniksdev.com/}@feniksdev.com{/a}
""")


default misc_page = "about"
screen misc():
    tag menu

    if misc_page == "about":
        use about
    else:
        use help
    vbox:
        align(1.0, 0.5) xoffset -425
        button:
            add "gui/button/del_bg.png"
            add "gui/gm/about.png" at button_fade align(0.5, 0.5)
            xysize(101, 101)
            action [SetVariable("misc_page", "about"), Show("misc", dissolve)]
        add "gui/button/div.png" xalign 0.5
        button:
            add "gui/button/del_bg.png"
            add "gui/gm/help.png" at button_fade align(0.5, 0.5)
            action [SetVariable("misc_page", "help"), Show("misc", dissolve)]
            xysize(101, 101)

    add "gui/button/dec_2.png"

    
screen about():

    

    #add "#21212db2" # The background; can be whatever

    
    use game_menu(_("About"))

    viewport:
        #style_prefix 'game_menu'
        xysize(930, 554) pos(390,270)
        mousewheel True pagekeys True
        scrollbars "vertical"

        has vbox
        style_prefix "about"

        label "[config.name!t]"
        text _("Version [config.version!t]\n")

        if gui.about:
            text "[gui.about!t]\n"

        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
        
    
        


style about_label_text:
    size 36

style about_text:
    color '#bfaa8f'


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.
default device = "keyboard"
screen help():

    tag menu

    

    use game_menu(_("Help"))

    viewport:
        #style_prefix 'game_menu'
        xysize(930, 554) pos(390,270)
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        style_prefix "help"
        spacing 23

        

        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        elif device == "gamepad":
            use gamepad_help
    
    add "gui/button/dec.png"

    hbox:
        align(0.5, 1.0) offset(70, -180) spacing 30
        textbutton _("Keyboard") action SetVariable("device", "keyboard")
        textbutton _("Mouse") action SetVariable("device", "mouse")

        if GamepadExists():
            textbutton _("Gamepad") action SetVariable("device", "gamepad")


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button:
    xmargin 12

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    xalign 1.0
    textalign 1.0
style help_text:
    color'#bfaa8f'
