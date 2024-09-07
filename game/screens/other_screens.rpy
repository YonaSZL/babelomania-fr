
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
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
        add "gui/button/div.png" xalign 0.5
        button:
            add "gui/button/del_bg.png"
            add "gui/gm/help.png" at button_fade align(0.5, 0.5)
            action [SetVariable("misc_page", "help"), Show("misc", dissolve)]
            xysize(101, 101)
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"

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

        label "{size=35}CREDITS\n" xalign 0.5 yalign 0.5
        vbox:
            xoffset 15 yoffset -20 spacing 20
            vbox:
                label "{size=35}PRODUCER, DIRECTOR" yalign 0.5
                text "\"Meinos Kaen\"" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}PROGRAMMERS" yalign 0.5
                text "\"Meinos Kaen\", \"Skolaztika\", \"Korden\"" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}BACKGROUND ARTISTS" yalign 0.5
                text "\"kircheis5020\", \"Arsonichawt\", \"Fuura Xen\"" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}CHARACTER SPRITE ARTIST" yalign 0.5
                text "\"chocojax\", \"michumiyumi\"" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}CG ILLUSTRATORS" yalign 0.5
                text "\"SaDui\", \"Arsonichawt\", \"Halebob\"" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}ENVIRONMENT CONCEPT ARTIST" yalign 0.5
                text "\"Fuura Xen\"" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}CHARACTER CONCEPT ARTIST" yalign 0.5
                text "\"Amacoworks\"" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}ADDITIONAL CONCEPTS ARTIST" yalign 0.5
                text "\"Arsonichawt\"" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}UI ARTIST" yalign 0.5
                text "\"Skolaztika\"" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}COMPOSERS" yalign 0.5
                text "\"OddTillTheEnd\", \"Jonathan Jonhson\", \"Nailik\"" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}AUDIO EDITOR" yalign 0.5
                text "John \"Magnificent Beard\" Schmidt" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}3D MODELLER" yalign 0.5
                text "\"kircheis5020\"" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}3D ANIMATOR" yalign 0.5
                text "Danny \"DinoMan21779\" Dickson" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}PLOT, SCRIPT WRITER" yalign 0.5
                text "\"Meinos Kaen\"" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}EDITOR" yalign 0.5
                text "John \"Magnificent Beard\" Schmidt" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}IMAGE EDITING" yalign 0.5
                text "Danny \"DinoMan21779\" Dickson" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}THE REAL MVPS" yalign 0.5
                text "The Wonderful JPDE Supporters on {a=https://www.patreon.com/JPDE}Patreon{/a} and {a=https://ko-fi.com/jpde}Ko-Fi{/a}" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}ADDITIONAL SOUND EFFECTS" yalign 0.5
                text "{a=https://ellr.itch.io/}Ellr{/a}, {a=https://ateliermagicae.itch.io/}Atelier Magicae{/a}, Dev Tones, {a=https://nox-sound-design.itch.io/}Nox_Sound_Design{/a}, {a=https://www.gamedevmarket.net/member/shashirajproductions}SHASHIRAJproductions{/a}" xoffset 15 yalign 0.5
            vbox:
                label "{size=35}ADDITIONAL CODE" yalign 0.5
                text "{a=https://feniksdev.itch.io/}Feniks{/a}, {a=https://remort-studios.itch.io/}Nai @ MakeVisualNovels{/a}" xoffset 15 yalign 0.5

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
        textbutton _("Keyboard") action SetVariable("device", "keyboard") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"
        textbutton _("Mouse") action SetVariable("device", "mouse") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"

        if GamepadExists():
            textbutton _("Gamepad") action SetVariable("device", "gamepad") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"


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

    textbutton _("Calibrate") action GamepadCalibrate() hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"


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
