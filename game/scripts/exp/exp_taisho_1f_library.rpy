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
    