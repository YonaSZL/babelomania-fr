default taisho_foyer_explore = 0
default taisho_foyer_explore_timer = False
default taisho_foyer_gaspard_gone = False

default exp_taisho_foyer_gaspard = False
default exp_taisho_foyer_amina = False
default exp_taisho_foyer_bookshelves = False
default exp_taisho_foyer_window = False
default exp_taisho_foyer_laptop = False
default exp_taisho_foyer_painting = False
default exp_taisho_foyer_bonsai = False

screen taisho_foyer_explore():

    tag exploration

    if taisho_foyer_gaspard_gone == False:
        imagebutton:
            sensitive "taisho_foyer_explore_01_sensitive"
            if taisho_foyer_explore < 5:
                idle "Gaspard frown"
                hover "Gaspard frown"
            else:
                idle "Gaspard frown sweat"
                hover "Gaspard frown sweat"
            xpos 207
            ypos 577
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_foyer_gaspard")
            tooltip _("Gaspard")
            at transform:
                zoom 0.33
    
    if exp_taisho_foyer_bonsai == False:
        imagebutton:
            sensitive "taisho_foyer_explore_01_sensitive"
            idle "Amina neutral"
            hover "Amina neutral"
            xpos 1301
            ypos 520
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_foyer_amina")
            tooltip _("Amina")
            at transform:
                zoom 0.2
        button:
            sensitive "taisho_foyer_explore_01_sensitive"
            pos(1724,414)
            xysize(509,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_foyer_bookshelves")
            if flashlight_use:
                tooltip _("Bookshelves")
            else:
                tooltip _("?????")
        button:
            sensitive "taisho_foyer_explore_01_sensitive"
            pos(2654,341)
            xysize(226,551)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_foyer_window")
            if flashlight_use:
                tooltip _("Window")
            else:
                tooltip _("?????")
        button:
            sensitive "taisho_foyer_explore_01_sensitive"
            pos(1868,697)
            xysize(123,65)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_foyer_laptop")
            if flashlight_use:
                tooltip _("Laptop")
            else:
                tooltip _("?????")
        button:
            sensitive "taisho_foyer_explore_01_sensitive"
            pos(2453,257)
            xysize(130,236)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_foyer_painting")
            if flashlight_use:
                tooltip _("Painting")
            else:
                tooltip _("?????")
        if taisho_foyer_explore == 6:
            button:
                sensitive "taisho_foyer_explore_01_sensitive"
                pos(2326,560)
                xysize(232,129)
                background None
                hover_sound "audio/sfx/gui_hover.ogg"
                activate_sound "audio/sfx/gui_confirm.ogg"
                action Jump("exp_taisho_foyer_bonsai")
                if flashlight_use:
                    tooltip _("Bonsai")
                else:
                    tooltip _("?????")
    else:
        if taisho_foyer_explore < 8:
            imagebutton:
                sensitive False
                idle "Amina surprise"
                hover "Amina surprise"
                xpos 1301
                ypos 520
                hover_sound "audio/sfx/gui_hover.ogg"
                activate_sound "audio/sfx/gui_confirm.ogg"
                action NullAction()
                at transform:
                    zoom 0.2
            mousearea:
                area (134,602,634,404)
                hovered Jump("story_01_gaspard_gone")
        else:
            button:
                pos(874,461)
                xysize(306,221)
                background None
                action Jump("story_01_gaspard_found")
                tooltip _("?????")

    add "darkness_layers"

label exp_taisho_foyer_bookshelves:
    $ renpy.block_rollback()
    if flashlight_use == False:
        sh_i neutral "(It's too dark.{w=0.3} I need to use the flashlight to look around.)"
    else:
        $ flashlight_consume = False
        pause 0.5

        if exp_taisho_foyer_bookshelves == False:
            $ exp_taisho_foyer_bookshelves = True
            $ taisho_foyer_explore += 1
        $ flashlight_consume = True
    pause 1.0
    call screen taisho_1f_library_explore_01