default taisho_exposition_explore = 0

default exm_taisho_exposition_tenugui = False
default exm_taisho_exposition_scroll = False
default exm_taisho_exposition_sword = False
default exm_taisho_exposition_panel = False

screen taisho_exposition_explore():

    tag examination

    button:
        pos(495,729)
        xysize(145,145)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exm_taisho_exposition_tenugui")
        if flashlight_use:
            tooltip _("Item Panel #01")
        else:
            tooltip _("?????")
    
    button:
        pos(698,775)
        xysize(159,134)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exm_taisho_exposition_exposition")
        if flashlight_use:
            tooltip _("Item Panel #02")
        else:
            tooltip _("?????")
    
    add "darkness_layers"

label exm_taisho_exposition_tenugui:
    show darkness_layers
    $ renpy.block_rollback()
    if flashlight_use == False:
        sh_i neutral "(It's too dark.{w=0.3} I need to use the flashlight to look around.)"
    else:
        $ flashlight_consume = False
        
        if exm_taisho_exposition_tenugui == False:
            $ shigeo_terms.append(c_airborne)
            play sound4 "audio/sfx/gui_slots_confirm.ogg"
            show screen notify(_("New Codex Entry: Airborne Transmission."))
            $ exm_taisho_exposition_tenugui = True
            $ taisho_foyer_explore += 1
            $ stat2 -= 1
            $ move_time(0,1)
        $ flashlight_consume = True
    pause 1.0
    hide darkness_layers
    call screen taisho_exposition_explore
    with dissolve

label exm_taisho_exposition_scroll:
    show darkness_layers
    $ renpy.block_rollback()
    if flashlight_use == False:
        sh_i neutral "(It's too dark.{w=0.3} I need to use the flashlight to look around.)"
    else:
        $ flashlight_consume = False
        
        if exm_taisho_exposition_scroll == False:
            $ shigeo_terms.append(c_airborne)
            play sound4 "audio/sfx/gui_slots_confirm.ogg"
            show screen notify(_("New Codex Entry: Airborne Transmission."))
            $ exm_taisho_exposition_scroll = True
            $ taisho_foyer_explore += 1
            $ stat2 -= 1
            $ move_time(0,1)
        $ flashlight_consume = True
    pause 1.0
    hide darkness_layers
    call screen taisho_exposition_explore
    with dissolve

label exm_taisho_exposition_sword:
    show darkness_layers
    $ renpy.block_rollback()
    if flashlight_use == False:
        sh_i neutral "(It's too dark.{w=0.3} I need to use the flashlight to look around.)"
    else:
        $ flashlight_consume = False
        
        if exm_taisho_exposition_sword == False:
            $ shigeo_terms.append(c_airborne)
            play sound4 "audio/sfx/gui_slots_confirm.ogg"
            show screen notify(_("New Codex Entry: Airborne Transmission."))
            $ exm_taisho_exposition_sword = True
            $ taisho_foyer_explore += 1
            $ stat2 -= 1
            $ move_time(0,1)
        $ flashlight_consume = True
    pause 1.0
    hide darkness_layers
    call screen taisho_exposition_explore
    with dissolve

label exm_taisho_exposition_panel:
    show darkness_layers
    $ renpy.block_rollback()
    if flashlight_use == False:
        sh_i neutral "(It's too dark.{w=0.3} I need to use the flashlight to look around.)"
    else:
        $ flashlight_consume = False
        
        if exm_taisho_exposition_panel == False:
            $ shigeo_terms.append(c_airborne)
            play sound4 "audio/sfx/gui_slots_confirm.ogg"
            show screen notify(_("New Codex Entry: Airborne Transmission."))
            $ exm_taisho_exposition_panel = True
            $ taisho_foyer_explore += 1
            $ stat2 -= 1
            $ move_time(0,1)
        $ flashlight_consume = True
    pause 1.0
    hide darkness_layers
    call screen taisho_exposition_explore
    with dissolve

label exm_taisho_exposition_return:
    show darkness_layers
    $ renpy.block_rollback()
    if flashlight_use == False:
        sh_i neutral "(It's too dark.{w=0.3} I need to use the flashlight to look around.)"
    else:
        $ flashlight_consume = False
        
        if exm_taisho_exposition_scroll == False:
            $ shigeo_terms.append(c_airborne)
            play sound4 "audio/sfx/gui_slots_confirm.ogg"
            show screen notify(_("New Codex Entry: Airborne Transmission."))
            $ exm_taisho_exposition_scroll = True
            $ taisho_foyer_explore += 1
            $ stat2 -= 1
            $ move_time(0,1)
        $ flashlight_consume = True
    pause 1.0
    hide darkness_layers
    call screen taisho_exposition_explore
    with dissolve