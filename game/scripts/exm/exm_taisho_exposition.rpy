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
        if exm_taisho_exposition_tenugui == False:
            play sound "audio/sfx/gui_hint.ogg"
            sh surprise "{b}Tenugui{/b}...{w=0.5} Huh."
            am surprise "Tenugui?"
            play sound4 "audio/sfx/gui_phone_swipe.ogg"
            show it_tenugui with dissolve:
                xalign 0.5 yalign 0.4
            pause 0.5
            nvl clear
            sh neutral "Yeah.{w=0.3} See the bunch of towels over there?{w=0.3} Those are called Tenugui."
            pause 0.5
            d """{size=40}{b}Tenugui (Set of Five)"""
            d """{size=32}{b}Location Obtained: Nara Prefecture, Japan, 1960"""
            d """Received as gifts from a hosting family during Abelard Du Bois's travels in Honshu, the biggest and most populous island of the Japanese archipelago."""
            sh neutral "They're a type of traditional decorative towel.{w=0.3} They're very popular as souvenirs, among other things."
            if exm_taisho_exposition_tenugui == False:
                $ shigeo_items.append(c_tenugui)
                play sound4 "audio/sfx/gui_slots_confirm.ogg"
                show screen notify(_("New Codex Entry: Tenugui."))
            am surprise "I see...{w=0.5} From 1960?{w=0.3} So they're almost a century old?!{w=0.3} They look amazing!"
            sh smile "They are well taken care of, I suppose, but considering the durability of the average Tenugui, I'm not surprised in the slightest."
            sh laugh "I got one when I saw a {nw}"
            play sound4 "audio/sfx/gui_hint.ogg"
            extend "{b}Rakugo{/b} show as a teen, and it's still in one piece.{w=0.3} Well, quality can vary, of course."
            am smile "Alright, now try and imagine I do not know what that is?"
            sh smile "A type of Japanese comedy theater...{w=0.5} Anyway."
            sh neutral "While they appear of good make, they also seem quite devoid of hints...{w=0.5} The patterns are mostly nondescript."
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
                $ stat2 -= 2
                $ move_time(0,2)
        else:
            play sound4 "audio/sfx/gui_phone_swipe.ogg"
            show it_tenugui with dissolve:
                xalign 0.5 yalign 0.4
            pause 0.5
            nvl clear
            d """{size=40}{b}Tenugui (Set of Five)"""
            d """{size=32}{b}Location Obtained: Nara Prefecture, Japan, 1960"""
            d """Received as gifts from a hosting family during Abelard Du Bois's travels in Honshu, the biggest and most populous island of the Japanese archipelago."""
        $ flashlight_consume = True
    pause 1.0
    hide it_tenugui with dissolve
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
            play sound4 "audio/sfx/gui_phone_swipe.ogg"
            show it_scroll with dissolve:
                xalign 0.5 yalign 0.4
            pause 0.5
            nvl clear
            d """{size=40}{b}Kakekijo (Hanging Scroll)"""
            d """{size=32}{b}Location Obtained: Greater Tokyo Area, Japan, 1960"""
            d """Featuring beautiful calligraphy inscriptions and a detailed illustration, this scroll comes from the personal collection of Abelard Du Bois."""
            d """It's hypothized, but not confirmed, that this item may have been a gift from Kishi Nobusuke. The correspondence of the time places the meeting between Du Bois and the statesman in the same two days window as the acquisition of the scroll."""
            play sound4 "audio/em/em_shock.ogg"
            show screen emote("surprise",0.15,0.5)
            sh shock "{b}Kishi Nobusuke{/b}!{w=0.3} Seriously?!"
            am surprise "Who's that?{w=0.3} Someone important?"
            ta neutral "Kishi Nobusuke.{w=0.3} Japanese bureaucrat and politician, born 13 November 1896 and deceased 7 August 1987."
            
            if exm_taisho_exposition_scroll == False:
                $ shigeo_terms.append(c_airborne)
                play sound4 "audio/sfx/gui_slots_confirm.ogg"
                show screen notify(_("New Codex Entry: Airborne Transmission."))
                $ exm_taisho_exposition_scroll = True
                $ taisho_foyer_explore += 1
                $ stat2 -= 1
                $ move_time(0,1)
        else:
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