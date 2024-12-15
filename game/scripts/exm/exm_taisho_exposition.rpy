default taisho_exposition_exam = 0

default exm_taisho_exposition_tenugui = False
default exm_taisho_exposition_scroll = False
default exm_taisho_exposition_sword = False
default exm_taisho_exposition_panel = False

screen taisho_exposition_exam():

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
        action Jump("exm_taisho_exposition_scroll")
        if flashlight_use:
            tooltip _("Item Panel #02")
        else:
            tooltip _("?????")
    
    button:
        pos(1475,717)
        xysize(132,116)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exm_taisho_exposition_sword")
        if flashlight_use:
            tooltip _("Item Panel #03")
        else:
            tooltip _("?????")
    
    button:
        pos(201,494)
        xysize(1412,158)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exm_taisho_exposition_panel")
        if flashlight_use:
            tooltip _("Wooden Panel")
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
        play sound4 "audio/sfx/gui_hint.ogg"
        sh surprise "{b}Tenugui{/b}...{w=0.5} Huh."
        am surprise "Tenugui?"
        pause 0.5
        show it_tenugui with dissolve:
            xalign 0.5 yalign 0.4
        sh neutral "Yeah.{w=0.3} See the bunch of towels over there?{w=0.3} Those are called Tenugui."
        pause 0.5
        d """{size=40}Tenugui (Set of Five)"""
        d """{size=32}Locations Obtained: Nara Prefecture, Japan, 1960"""
        d """Received as gifts from a hosting family during Abelard Du Bois's travels in Honshu, the biggest and most populous island of the Japanese arcipelago."""
        sh neutral "They're a type of traditional decorative towel.{w=0.3} They're very popular as souvenirs, among other things."
        if exm_taisho_exposition_tenugui == False:
            $ shigeo_terms.append(c_tenugui)
            play sound4 "audio/sfx/gui_slots_confirm.ogg"
            show screen notify(_("New Codex Entry: Tenugui."))
        am surprise "I see...{w=0.5} From 1960?{w=0.3} So they're almost a century old?!{w=0.3} They look amazing!"
        sh smile "They are well taken care of, I suppose, but considering the durability of the average Tenugui, I'm not surprised in the slightest."
        sh laugh "I got one when I saw a {nw}"
        play sound4 "audio/sfx/gui_hint.ogg"
        extend "{b}Rakugo{/b} show as a teen, and it's still in one piece.{w=0.3} Well, quality can vary, of course."
        am smile "Alright, now try and imagine I do not know what that is?"
        sh smile "A type of Japanese comedy theater...{w=0.5} Anyway."
        sh neutral "While they seem of good make, they seem quite devoid of hints...{w=0.5} The patterns are mostly nondescript."
        am neutral "Hmm...{w=0.5} Except the one at the very bottom, wouldn't you say?{w=0.3} The floral pattern..."
        am surprise "I think those are {nw}"
        play sound4 "audio/sfx/gui_hint.ogg"
        extend "{b}wisteria flowers{/b}."
        sh surprise "Wisteria...{w=0.5} It's been a long time since I've seen any, if ever, so I'll trust you on that."
        sh_i frown "(.{w=0.3}.{w=0.3}.{w=0.5}wisteria flowers...{w=0.5} It does ring a bell about something but I can't quite put my finger on it.)"
        if exm_taisho_exposition_tenugui == False:
            $ shigeo_terms.append(c_rakugo)
            play sound4 "audio/sfx/gui_slots_confirm.ogg"
            show screen notify(_("New Codex Entry: Rakugo."))
            $ exm_taisho_exposition_tenugui = True
            $ taisho_foyer_explore += 1
            $ stat2 -= 1
            $ move_time(0,1)
        $ flashlight_consume = True
    pause 1.0
    hide darkness_layers
    call screen taisho_exposition_exam
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
    call screen taisho_exposition_exam
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
    call screen taisho_exposition_exam
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
    call screen taisho_exposition_exam
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
    call screen taisho_exposition_exam
    with dissolve