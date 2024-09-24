default taisho_1f_study_explore_01 = 0
default exp_taisho_1f_study_01_couch = False
default exp_taisho_1f_study_01_phone = False
default exp_taisho_1f_study_01_lamp = False
default exp_taisho_1f_study_01_floor = False
default exp_taisho_1f_study_01_flashlight = False

screen taisho_1f_study_explore_01():

    tag exploration

    imagemap:
        ground "taisho_1f_study"
        hover "taisho_1f_study"
        
        hotspot (494, 717, 571, 201) action Jump("exp_taisho_1f_study_01_couch") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Darkness")#COUCH/PHONE
        if exp_taisho_1f_study_01_phone:
            hotspot (953, 163, 336, 250) action Jump("exp_taisho_1f_study_01_lamp") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Darkness")#LAMP
            hotspot (1443, 905, 424, 133) action Jump("exp_taisho_1f_study_01_floor") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Darkness")#FLOOR
            if taisho_1f_study_explore_01 == 3 and exp_taisho_1f_study_01_flashlight == False:
                hotspot (1377, 630, 111, 76) action Jump("exp_taisho_1f_study_01_flashlight") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Darkness")#FLASHLIGHT

    $ tooltip = GetTooltip()

    nearrect:
        focus "tooltip"
        prefer_top True

        frame:
            xalign 0.5
            text "[tooltip]"

label exp_taisho_1f_study_01_couch:
    $ renpy.block_rollback()
    pause 0.5
    if exp_taisho_1f_study_01_couch == False:
        sh_i surprise sweat "(It's so dark...{w=0.5} I can barely see anything.)"
        sh_i neutral "(This...{w=0.5} Is a couch, and a table in front of it...{w=0.5} This isn't the reception or any other room I've seen.{w=0.3} What...?)"
        sh_i surprise "(What happened?{w=0.3} Last thing I remember was Francesco talking about a wedding video and...{w=0.5} And then...?)"
        pause 1.5
        sh_i frown -sweat "(What time is it...?{w=0.5} {nw}"
        play sound "audio/se/clothes_rustle.ogg"
        extend "And I need some light, I need to...)"
        pause 1.5
        play sound4 "audio/se/clothes_rustle.ogg"
        sh surprise "My...{w=0.5} My phone?"
        sh shock "My phone is {nw}"
        play sound "audio/sfx/gui_spook.ogg"
        extend "{b}gone?!{/b}"
        play music "audio/bgm/shadows_whisper.ogg"
        if exp_taisho_1f_study_01_couch == False:
            $ exp_taisho_1f_study_01_couch = True
    else:
        sh_i surprise -sweat "(Maybe I dropped it when...{w=0.5} When I...?)"
        pause 1.5
        sh_i frown sweat "(I did not simply fall asleep, didn't I?{w=0.3} I was brought here, I...{w=0.5} I still have my shoes on, I would never...)"
        sh_i neutral -sweat "(Even if I don't remember a lick of it, one thing is certain.{w=0.3} {nw}"
        play sound "audio/sfx/gui_spook.ogg"
        extend "{b}I did not get on that couch by myself{/b}.)"
        if exp_taisho_1f_study_01_phone == False:
            $ exp_taisho_1f_study_01_phone = True
            $ taisho_1f_study_explore_01 += 1
    pause 1.0
    call screen taisho_1f_study_explore_01

label exp_taisho_1f_study_01_lamp:
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(I can see a chandelier hanging from the ceiling...{w=0.5} Off, obviously, but that doesn't cut it, on its own.)"
    sh_i frown "(I remember the walk from the parking area to the estate proper.{w=0.3} There were plenty of lamposts, and I noticed other kinds of fixtures spread throughout.)"
    sh_i neutral "(Also, I checked the weather before flying in to France...{w=0.5} Mostly clear, a few clouds and a last quarter moon.{w=0.3} There should be plenty of light to go around.)"
    sh_i frown "(Which means that either this room has no windows, or {nw}"
    play sound "audio/sfx/gui_spook.ogg"
    extend "{b}that the window has been shuttered{/b}.)"
    sh_i surprise "(But why?{w=0.5} And how?{w=0.3} I don't remember seeing any...{w=0.5} Unless?!)"
    pause 1.0
    if exp_taisho_1f_study_01_lamp == False:
        $ exp_taisho_1f_study_01_lamp = True
        $ taisho_1f_study_explore_01 += 1
    call screen taisho_1f_study_explore_01

label exp_taisho_1f_study_01_floor:
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
    if exp_taisho_1f_study_01_floor == False:
        $ exp_taisho_1f_study_01_floor = True
        $ taisho_1f_study_explore_01 += 1
    call screen taisho_1f_study_explore_01

label exp_taisho_1f_study_01_flashlight:
    $ renpy.block_rollback()
    pause 0.5
    sh_i surprise "(Tall furniture, a library...{w=0.5} Is this a fireplace?)"
    sh_i neutral "(Alright, slowly, Shigeo...{w=0.5} Try not to knock anything over-)"
    play sound "audio/se/item_bump.ogg"
    pause 0.2
    show screen emote("surprise",0.17,0.5)
    sh surprise sweat "Ugh, last famous words...{w=0.5} Hmm...?"
    sh frown -sweat ".{w=0.3}.{w=0.3}.{w=0.5}this shape...?"
    pause 1.5
    play sound4 "audio/em/em_shock.ogg"
    show screen emote("surprise",0.17,0.5)
    sh shock "...!{w=0.3} Seriously?!"
    play sound "audio/sfx/gui_item_get.ogg"
    show it_flashlight with dissolve:
        xalign 0.5 yalign 0.4
    sh_i surprise "(A {b}flashlight{/b}!{w=0.3} What are even the chances?!)"
    sh_i smile "(I can finally start shedding some light on this whole situation...{w=0.5} Heh.)"
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    show screen notify(_("Inventory Unlocked"))
    $ inventory_show = True
    sh_i frown "(It's a rechargeable model with an internal battery...{w=0.5} And an USB-C port.)"
    sh_i neutral "(Which means that as long as I {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}find a charger{/b}, no matter what it's powering, I can recharge it.)"
    sh_i neutral "(Maybe the flashlight's own charger may be around here?{w=0.3} Would make sense.)"
    hide it_flashlight with dissolve
    pause 1.0
    if exp_taisho_1f_study_01_flashlight == False:
        $ exp_taisho_1f_study_01_flashlight = True
    call screen taisho_1f_study_explore_01

#After getting the flashlight

default taisho_1f_study_explore_02 = 0

default exp_taisho_1f_study_02_window = False
default exp_taisho_1f_study_02_scrolls = False
default exp_taisho_1f_study_02_door = False

screen taisho_1f_study_explore_02():

    tag exploration

    imagemap:
        ground "taisho_1f_study"
        hover "taisho_1f_study"
        
        if flashlight_use:
            hotspot (326, 352, 451, 497) action Jump("exp_taisho_1f_study_02_window") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Window")#WINDOW
            hotspot (1212, 457, 291, 227) action Jump("exp_taisho_1f_study_02_scrolls") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Hanging Scrolls")#SCROLLS
            hotspot (1762, 327, 158, 589) action Jump("exp_taisho_1f_study_02_door") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Door")#DOOR
        else:
            hotspot (326, 352, 451, 497) action Jump("exp_taisho_1f_need_flashlight") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Darkness")#WINDOW
            hotspot (1212, 457, 291, 227) action Jump("exp_taisho_1f_need_flashlight") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Darkness")#SCROLLS
            hotspot (1762, 327, 158, 589) action Jump("exp_taisho_1f_need_flashlight") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Darkness")#DOOR

    $ tooltip = GetTooltip()

    nearrect:
        focus "tooltip"
        prefer_top True

        frame:
            xalign 0.5
            text "[tooltip]"

label exp_taisho_1f_need_flashlight:
    scene taisho_1f_study
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(It's too dark to see anything properly...{w=0.5} I need to {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}use the flashlight{/b}.)"
    pause 1.0
    scene black
    call screen taisho_1f_study_explore_02

label exp_taisho_1f_study_02_window:
    scene taisho_1f_study_bare
    show dark_flashlight
    $ flashlight_consume = False
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(As I thought...{w=0.5} The window is shuttered.{w=0.3} But here's the twist.)"
    sh_i surprise "(This is not a normal shutter.{w=0.3} This is a {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}security shutter{/b}.{w=0.3} Of the type I've seen in governmental buildings.)"
    sh_i frown "(Nothing short of an explosive could damage one of these things...{w=0.5} Selling point or not, this seems excessive for a place like this.)"
    sh_i neutral "(But it also begs the question:{w=0.3} why are they down right now?)"
    pause 1.0
    scene black
    if exp_taisho_1f_study_02_window == False:
        $ exp_taisho_1f_study_02_window = True
        $ taisho_1f_study_explore_02 += 1
    if taisho_1f_study_explore_02 >= 3:
        jump story_01_there_were_three
    $ flashlight_consume = True
    call screen taisho_1f_study_explore_02

label exp_taisho_1f_study_02_scrolls:
    scene taisho_1f_study_bare
    show dark_flashlight
    $ flashlight_consume = False
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(Hanging scrolls...{w=0.5} That's a new one.{w=0.3} I haven't seen anything like this in years.)"
    sh_i frown "(The rest of the furniture seems quite western-inspired, but I can't say the same for the ceiling, the window...{w=0.5} What a strange mixture of influences.)"
    pause 1.5
    play sound "audio/em/em_surprise.ogg"
    show screen emote("surprise",0.17,0.5)
    sh_i surprise "(Wait...{w=0.5} Mixture of influences...?{w=0.3} I remember talking about this with Gaspard, earlier.)"
    sh_i neutral "(Of course.{w=0.3} This must be the {nw}"
    play sound4 "audio/sfx/gui_solved.ogg"
    extend "{b}Taishō Building{/b}.{w=0.3} We were going to be spend the night in here, weren't we?)"
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    show screen notify(_("Codex Updated."))
    $ c_chateau_dubois_taisho = True
    sh_i surprise "(This doesn't look like a bedroom, though...{w=0.3} I must be in a different wing of the building, then.)"
    sh_i neutral "(Also, no trace of a charger for the flashlight.{w=0.3} Pity.)"
    pause 1.0
    scene black
    if exp_taisho_1f_study_02_scrolls == False:
        $ exp_taisho_1f_study_02_scrolls = True
        $ taisho_1f_study_explore_02 += 1
    if taisho_1f_study_explore_02 >= 3:
        jump story_01_there_were_three
    $ flashlight_consume = True
    call screen taisho_1f_study_explore_02

label exp_taisho_1f_study_02_door:
    scene taisho_1f_study_bare
    show dark_flashlight
    $ flashlight_consume = False
    $ renpy.block_rollback()
    pause 0.5
    sh_i smile "(The door, and the light switch.{w=0.3} Let's see...)"
    play sound "audio/se/switch_01.ogg"
    pause 1.5
    play sound4 "audio/se/switch_01.ogg"
    pause 1.0
    play sound "audio/se/switch_01.ogg"
    pause 0.5
    play sound4 "audio/se/switch_01.ogg"
    sh frown "Of course not."
    sh_i frown "(So the lights are out.{w=0.3} Or maybe it's just this one room?)"
    sh_i neutral "(I can't see a plug, nor anything else I can use to try and check though...{w=0.3} I'll need to leave, then.)"
    pause 1.0
    scene black
    if exp_taisho_1f_study_02_door == False:
        $ exp_taisho_1f_study_02_door = True
        $ taisho_1f_study_explore_02 += 1
    if taisho_1f_study_explore_02 >= 3:
        jump story_01_there_were_three
    $ flashlight_consume = True
    call screen taisho_1f_study_explore_02
