#Aims for this puzzle: you need to input 'Shinzo Abe' using the wooden exposition panel. But written 'Abe Shinzo', surname first.
#Haiku Hint
##darkness returning
##from grandfather inherited
##by a son cut down
default taisho_foyer_explore = 0
default taisho_foyer_explore_timer = False
default taisho_foyer_gaspard_gone = False

default exp_taisho_foyer_amina = False
default exp_taisho_foyer_door = False
default exp_taisho_foyer_stairs = False
default exp_taisho_foyer_laptop = False
default exp_taisho_foyer_painting = False
default exp_taisho_foyer_bonsai = False

screen taisho_foyer_explore():

    tag exploration

    imagebutton:
        idle "Amina neutral"
        hover "Amina neutral"
        xpos 480
        ypos 500
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_foyer_amina")
        tooltip _("Amina{#explore_foyer}")
        at transform:
            zoom 0.18
    
    imagebutton:
        idle "Tabitha neutral brief"
        hover "Tabitha neutral brief"
        xpos 799
        ypos 480
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_foyer_tabitha")
        tooltip _("The Android{#explore_foyer}")
        at transform:
            zoom 0.2
    button:
        pos(150,375)
        xysize(200,300)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_foyer_door")
        if flashlight_use:
            tooltip _("Door to Outside{#explore_foyer}")
        else:
            tooltip _("?????")
    button:
        pos(2654,341)
        xysize(226,551)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_foyer_stairs")
        if flashlight_use:
            tooltip _("Door to Stairways{#explore_foyer}")
        else:
            tooltip _("?????")
    button:
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

label exp_taisho_foyer_door:
    $ renpy.block_rollback()
    if flashlight_use == False:
        sh_i neutral "(It's too dark.{w=0.3} I need to use the flashlight to look around.)"
    else:
        $ flashlight_consume = False
        pause 0.5

        if exp_taisho_foyer_door == False:
            $ exp_taisho_foyer_door = True
            $ taisho_foyer_explore += 1
        $ flashlight_consume = True
    pause 1.0
    call screen taisho_1f_library_explore_01