default taisho_1f_library_explore_01_sensitive = True
default taisho_1f_library_explore_01 = 0

default exp_taisho_1f_library_01_bookshelves = False
default exp_taisho_1f_library_01_window = False
default exp_taisho_1f_library_01_laptop = False
default exp_taisho_1f_library_01_painting = False
default exp_taisho_1f_library_01_bonsai = False

screen taisho_1f_library_explore_01():

    tag exploration

    viewport:
        draggable True
        mousewheel False
        edgescroll(75,75)
        xinitial 0.5
        scrollbars None
        arrowkeys None
        pagekeys None

        add "taisho_1f_library_base"

        imagebutton:
            sensitive "taisho_1f_library_explore_01_sensitive"
            idle "Gaspard frown"
            hover "Gaspard frown"
            xpos 111
            ypos 111
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_gaspard")
            tooltip _("Gaspard")
            at transform:
                zoom 0.14
            
        imagebutton:
            sensitive "taisho_1f_library_explore_01_sensitive"
            idle "Amina neutral"
            hover "Amina neutral"
            xpos 111
            ypos 111
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_amina")
            tooltip _("Amina")
            at transform:
                zoom 0.14
        
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_bookshelves")
            tooltip _("Bookshelves")
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_window")
            tooltip _("Window")
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_laptop")
            tooltip _("Laptop")
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_painting")
            tooltip _("Painting")
        if taisho_1f_library_explore_01 == 4:
            timer 60.0 action Play("sound2", "audio/se/fist_slam.ogg")
            timer 120.0 action Play("sound2", "audio/se/fabric_tearing.ogg")
            button:
                pos(993,454)
                xysize(128,297)
                background None
                hover_sound "audio/sfx/gui_hover.ogg"
                activate_sound "audio/sfx/gui_confirm.ogg"
                action Jump("exp_taisho_1f_library_01_bonsai")
                tooltip _("Bonsai")
    
    add "darkness_layers"

    $ tooltip = GetTooltip()

    nearrect:
        focus "tooltip"
        prefer_top True

        frame:
            xalign 0.5
            text "[tooltip]"

label exp_taisho_1f_library_01_gaspard:
    $ renpy.block_rollback()
    pause 0.5

    pause 1.0

label exp_taisho_1f_library_01_amina:
    $ renpy.block_rollback()
    pause 0.5

    pause 1.0

label exp_taisho_1f_library_01_bookshelves:
    $ renpy.block_rollback()
    pause 0.5

    if exp_taisho_1f_library_01_bookshelves == False:
        $ exp_taisho_1f_library_01_bookshelves = True
        $ taisho_1f_library_explore_01 += 1
    pause 1.0

label exp_taisho_1f_library_01_window:
    $ renpy.block_rollback()
    pause 0.5

    if exp_taisho_1f_library_01_window == False:
        $ exp_taisho_1f_library_01_window = True
        $ taisho_1f_library_explore_01 += 1
    pause 1.0

label exp_taisho_1f_library_01_laptop:
    $ renpy.block_rollback()
    pause 0.5

    if exp_taisho_1f_library_01_laptop == False:
        $ exp_taisho_1f_library_01_laptop = True
        $ taisho_1f_library_explore_01 += 1
    pause 1.0

label exp_taisho_1f_library_01_painting:
    $ renpy.block_rollback()
    pause 0.5

    if exp_taisho_1f_library_01_painting == False:
        $ exp_taisho_1f_library_01_painting = True
        $ taisho_1f_library_explore_01 += 1
    pause 1.0

label exp_taisho_1f_library_01_bonsai:
    $ renpy.block_rollback()
    pause 0.5

    if exp_taisho_1f_library_01_bonsai == False:
        $ exp_taisho_1f_library_01_bonsai = True
        $ taisho_1f_library_explore_01 += 1
    pause 1.0
    