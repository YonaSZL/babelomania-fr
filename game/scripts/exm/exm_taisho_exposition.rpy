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
    
    if exm_taisho_exposition_tenugui and exm_taisho_exposition_scroll and exm_taisho_exposition_sword:
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

    button:
        pos(1703,431)
        xysize(217,649)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exm_taisho_exposition_return")
        tooltip _("Return")
    
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
        pause 1.0
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
            am neutral "Someone important, I assume?"
            ta neutral "Kishi Nobusuke.{w=0.3} Japanese bureaucrat and politician, born 13 November 1896 and deceased 7 August 1987.{w=0.3} Served as Vice Minister for War Time Territory of Manchuria from 1935 to 1939.{w=0.3} Served as Prime Minister of Japan from 1957 to 1960."
            ta bow "Common Aliases:{w=0.15} {font=gui/font/ShipporiMincho-Medium.ttf}昭和の妖怪{/font}, the 'Monster of the Showa Era'."
            am surprise sweatdrop "Huff!{w=0.3} A nice guy, I take?"
            sh frown "Among other things, he was among the founders of the LDP, the Liberal Democratic Party.{w=0.3} They governed Japan almost uninterrupted from the 1950s up until a couple decades ago."
            sh surprise "And if Du Bois met him in 1960, that was literally the height of the man's power and prestige...{w=0.5} And right before his downfall."
            am neutral ".{w=0.3}.{w=0.3}.{w=0.5}sounds like the kind of company Abelard Du Bois would keep."
            sh neutral "I can't say I'm familiar with the history of France as much as I would like.{w=0.3} Was Abelard Du Bois a controversial figure?"
            am frown -sweatdrop "For now, let's just say he didn't exactly make a lot of friends in north Africa...{w=0.5} We should focus on one old-timey bastard at a time."
            sh frown "Agreed..."
            if exm_taisho_exposition_scroll == False:
                $ shigeo_people.append(c_kishi)
                play sound4 "audio/sfx/gui_slots_confirm.ogg"
                show screen notify(_("New Codex Entry: Nobusuke Kishi."))
                $ exm_taisho_exposition_scroll = True
                $ taisho_foyer_explore += 1
                $ stat2 -= 1
                $ move_time(0,1)
        else:
            play sound4 "audio/sfx/gui_phone_swipe.ogg"
            show it_scroll with dissolve:
                xalign 0.5 yalign 0.4
            pause 0.5
            nvl clear
            d """{size=40}{b}Kakekijo (Hanging Scroll)"""
            d """{size=32}{b}Location Obtained: Greater Tokyo Area, Japan, 1960"""
            d """Featuring beautiful calligraphy inscriptions and a detailed illustration, this scroll comes from the personal collection of Abelard Du Bois."""
            d """It's hypothized, but not confirmed, that this item may have been a gift from Kishi Nobusuke. The correspondence of the time places the meeting between Du Bois and the statesman in the same two days window as the acquisition of the scroll."""
        $ flashlight_consume = True
    pause 1.0
    hide it_scroll with dissolve
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
            am surprise "Huh...{w=0.5} Maybe we've found a weapon."
            sh neutral "You're talking about the {nw}"
            play sound4 "audio/sfx/gui_hint.ogg"
            extend "{b}Katana{/b}, I suppose?"
            pause 0.5
            play sound4 "audio/sfx/gui_phone_swipe.ogg"
            show it_scroll with dissolve:
                xalign 0.5 yalign 0.4
            pause 0.5
            nvl clear
            d """{size=40}{b}Uchigatana"""
            d """{size=32}{b}Location Obtained: Yamaguchi Prefecture, Japan, 1960"""
            d """One of the most unique items in Abelard Du Bois's private collection, this Uchigatana -the Japanese word to refer to a Japanese single-bladed weapon- was not gifted or bought, but found."""
            d """As detailed in his diaries, Du Bois found the weapon at an unspecified location in the Yamaguchi Prefecture during his travels in the region. Subsequent examinations date this particular weapon back to the 12th century."""
            sh neutral "Bummer.{w=0.3} I still remember some {nw}"
            play sound4 "audio/sfx/gui_hint.ogg"
            extend "{b}Kendo{/b} from high school, but that is most definitely a prop.{w=0.3} There's no way that thing is almost a thousand years old."
            ta bow "Very well observed, [shn].{w=0.3} The make of the scabbard and shape of the crossguard date it at least down to the Tokugawa period."
            am neutral "Still, prop or not, better to have it than not, wouldn't you say?"
            sh frown "Maybe...{w=0.5} It looks more heavy than it's worth carrying around, to be honest."
            sh neutral "Let's say that if we don't find anything else suitable before leaving the building, we'll smash and grab it.{w=0.3} Deal?"
            am smile "Deal."
            if exm_taisho_exposition_sword == False:
                $ exm_taisho_exposition_sword = True
                $ taisho_foyer_explore += 1
                $ stat2 -= 1
                $ move_time(0,1)
        else:
            pause 0.5
            play sound4 "audio/sfx/gui_phone_swipe.ogg"
            show it_scroll with dissolve:
                xalign 0.5 yalign 0.4
            pause 0.5
            nvl clear
            d """{size=40}{b}Uchigatana"""
            d """{size=32}{b}Location Obtained: Yamaguchi Prefecture, Japan, 1960"""
            d """One of the most unique items in Abelard Du Bois's private collection, this Uchigatana -the Japanese word to refer to a Japanese single-bladed weapon- was not gifted or bought, but found."""
            d """As detailed in his diaries, Du Bois found the weapon at an unspecified location in the Yamaguchi Prefecture during his travels in the region. Subsequent examinations date this particular weapon back to the 12th century."""
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
        pause 0.5
        play sound4 "audio/sfx/gui_phone_swipe.ogg"
        show it_scroll with dissolve:
            xalign 0.5 yalign 0.4
        pause 1.0
        am neutral "That's a big block of text.{w=0.3} And we don't have a lot of light to read."
        sh neutral "Indeed...{w=0.5} Android, are you able to memorize this text?"
        ta bow "A simple matter.{w=0.3} Engaging textual processing protocol."
        $ stat2 += 5
        pause 1.0
        ta neutral "Done.{w=0.3} Would you like me to summarize the contents for you, [shn]?"
        if exm_taisho_exposition_panel == False:
            $ shigeo_terms.append(c_airborne)
            play sound4 "audio/sfx/gui_slots_confirm.ogg"
            show screen notify(_("New Codex Entry: Airborne Transmission."))
            $ exm_taisho_exposition_panel = True
            $ taisho_foyer_explore += 1
        $ flashlight_consume = True
    pause 1.0
    hide darkness_layers
    call screen taisho_exposition_exam
    with dissolve

label exm_taisho_exposition_return:
    show darkness_layers
    $ renpy.block_rollback()
    pause 1.0
    $ tabitha_return_variable = "return_taisho_foyer_explore"
    scene taisho_foyer_base
    show Amina neutral:
        xpos 615 ypos 555 zoom 0.12
    show Tabitha neutral brief:
        xpos 1320 ypos 540 zoom 0.2
    show darkness_layers        
    with dissolve
    pause 0.5
    scene taisho_foyer_base
    show Amina neutral:
        xpos 615 ypos 555 zoom 0.12
    show Tabitha neutral brief:
        xpos 1320 ypos 540 zoom 0.2
    call screen taisho_foyer_explore