default taisho_1f_study_examine_01 = 0
default exm_taisho_1f_study_01_couch = False
default exm_taisho_1f_study_01_phone = False
default exm_taisho_1f_study_01_lamp = False
default exm_taisho_1f_study_01_floor = False
default exm_taisho_1f_study_01_flashlight = False

screen taisho_1f_study_examine_01():
    imagemap:
        ground "taisho_1f_study"
        hover "taisho_1f_study"
        
        hotspot (460, 0, 1460, 825) action Jump("exm_taisho_1f_study_01_couch") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Darkness")#COUCH/PHONE
        if exm_taisho_1f_study_01_couch:
            hotspot (533, 980, 856, 100) action Jump("exm_taisho_1f_study_01_lamp") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Darkness")#LAMP
            hotspot (0, 0, 300, 130) action Jump("exm_taisho_1f_study_01_floor") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Darkness")#FLOOR
            if taisho_1f_study_examine_01 == 3:
                hotspot (1645, 922, 275, 158) action Jump("exm_taisho_1f_study_01_flashlight") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Darkness")#FLASHLIGHT
    
    $ tooltip = GetTooltip()

    nearrect:
        focus "tooltip"
        prefer_top True

        frame:
            xalign 0.5
            text "[tooltip]"

label exm_taisho_1f_study_01_couch:
    $ renpy.block_rollback()
    pause 0.5
    if exm_taisho_1f_study_01_couch == False:
        sh_i surprise sweat "(It's so dark...{w=0.5} I can barely see anything.)"
        sh_i neutral "(This...{w=0.5} Is a couch, and a table in front of it...{w=0.5} This isn't the reception or any other room I've seen.{w=0.3} What...?)"
        sh_i surprise "(What happened?{w=0.3} Last thing I remember was Francesco talking about a wedding video and...{w=0.5} And then...?)"
        pause 1.5
        play sound "audio/se/clothes_rustle.ogg"
        sh_i frown "(What time is it...?{w=0.5} And I need some light, I need to...)"
        pause 1.5
        sh surprise "My...{w=0.5} My phone?"
        play sound "audio/em/em_shock.ogg"
        show screen emote("surprise",0.17,0.5)
        sh shock "My phone is {nw}"
        play sound "audio/sfx/gui_spook.ogg"
        extend "{b}gone?!{/b}"
        play music "audio/bgm/shadows_breathe.ogg"
        if exm_taisho_1f_study_01_couch == False:
            $ exm_taisho_1f_study_01_couch = True
    else:
        sh_i surprise "(Maybe I dropped it when...{w=0.5} When I...?)"
        pause 1.5
        sh_i frown sweat "(I did not simply fall asleep, didn't I?{w=0.3} I was brought here, I...{w=0.5} I still have my shoes on, I would never...)"
        sh_i neutral "(Even if I don't remember a lick of it, one thing is certain.{w=0.3} {nw}"
        play sound "audio/sfx/gui_spook.ogg"
        extend "{b}I did not get on that couch by myself{/b}.)"
        if exm_taisho_1f_study_01_phone == False:
            $ exm_taisho_1f_study_01_phone = True
            $ taisho_1f_study_examine_01 += 1
    pause 1.0
    call screen taisho_1f_study_examine_01

label exm_taisho_1f_study_01_lamp:
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(I can see a chandelier hanging from the ceiling...{w=0.5} Off, obviously, but that doesn't cut it, on its own.)"
    sh_i frown "(I remember the walk from the parking area to the estate proper.{w=0.3} There were plenty of lamposts, and I noticed other kinds of fixtures spread throughout what I could see of the estate.)"
    sh_i neutral "(Also, I remember checking the weather before I came...{w=0.5} Mostly clear, a few clouds and a last quarter moon.{w=0.3} There should be plenty of light to go around.)"
    sh_i frown "(Which means that either this room has no windows, or {nw}"
    play sound "audio/sfx/gui_spook.ogg"
    extend "{b}that the window has been shuttered{/b}.)"
    sh_i surprise "(But why?{w=0.5} And how?{w=0.3} I don't remember seeing any...{w=0.5} Unless?!)"
    pause 1.0
    if exm_taisho_1f_study_01_lamp == False:
        $ exm_taisho_1f_study_01_lamp = True
        $ taisho_1f_study_examine_01 += 1
    call screen taisho_1f_study_examine_01

label exm_taisho_1f_study_01_floor:
    $ renpy.block_rollback()
    pause 0.5
    sh_i frown "(I gotta find the door...{w=0.5} And the light switch.{w=0.3} Slowly, now, let's follow the floor until I hit a wall...)"
    play sound "audio/se/clothes_rustle.ogg"
    pause 1.0
    sh_i neutral "(Huh...{w=0.5} The floor is...{w=0.5} Different.)"
    sh_i surprise "(Very different...{w=0.5} This is wood, isn't it?{w=0.3} But all the floors I had seen in the Baroque building had tile...{w=0.5} Or marble.)"
    sh_i frown "(Even the glimpse I caught of the smoking room had flooring in tile...{w=0.5} Which means.)"
    sh_i surprise "(I'm no longer in the same place...{w=0.5} {nw}"
    play sound "audio/sfx/gui_spook.ogg"
    extend "{b}This isn't the Baroque Building{/b}.)"
    sh_i frown "(Granted, I could just be on the upper floor of the building but...{w=0.5} I have a hunch that's not the case.)"
    pause 1.0
    if exm_taisho_1f_study_01_floor == False:
        $ exm_taisho_1f_study_01_floor = True
        $ taisho_1f_study_examine_01 += 1
    call screen taisho_1f_study_examine_01

label exm_taisho_1f_study_01_flashlight:
    $ renpy.block_rollback()
    pause 0.5
    sh_i surprise "(Tall furniture, a library...{w=0.5} Is this a fireplace?)"
    sh_i neutral "(Alright, slowly, Shigeo...{w=0.5} Try not to knock anything over-)"
    play sound "audio/se/item_bump.ogg"
    pause 0.2
    sh surprise sweat "Ugh, last famous words...{w=0.5} Hmm...?"
    sh frown -sweat ".{w=0.3}.{w=0.3}.{w=0.5}this shape...?"
    pause 1.5
    play sound "audio/em/em_shock.ogg"
    show emote screen("surprise",0.17,0.5)
    sh shock "...!{w=0.3} Seriously?!"
    play sound "audio/sfx/gui_item_get.ogg"
    show it_flashlight with dissolve:
        xalign 0.5 yalign 0.4
    sh_i neutral "(A {b}flashlight{/b}!{w=0.3} What are even the chances?!)"
    sh_i smile "(I can finally start shedding some light on this whole situation...{w=0.5} Heh.)"
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    show screen notify("Inventory Unlocked")
    $ inventory_show = True
    sh_i frown "(It's a rechargeable model with an internal battery...{w=0.5} And an USB-C port.)"
    sh_i neutral "(Which means that as long as I {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}find a charger{/b}, no matter what it's powering, I can recharge it.)"
    sh_i neutral "(Maybe the flashlight's own charger may be around here?{w=0.3} Would make sense.)"
    pause 1.0
    if exm_taisho_1f_study_01_flashlight == False:
        $ exm_taisho_1f_study_01_flashlight = True
    call screen taisho_1f_study_examine_01