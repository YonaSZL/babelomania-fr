
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
    
    add "darkness_layers"

    $ tooltip = GetTooltip()

    nearrect:
        focus "tooltip"
        prefer_top True

        frame:
            xalign 0.5
            text "[tooltip]"