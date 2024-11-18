default lvl3_meeting_examine_01 = 0
default exm_lvl3_meeting_01_stationary = False
default exm_lvl3_meeting_01_furniture = False
default exm_lvl3_meeting_01_folder = False
default exm_lvl3_meeting_01_body = False

screen lvl3_meeting_examine_01():

    tag examination

    button:
        pos(993,454)
        xysize(128,297)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exm_lvl3_meeting_01_stationary")
        tooltip _("Stationary")
    
    if exm_lvl3_meeting_01_stationary:
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exm_lvl3_meeting_01_furniture")
            tooltip _("Furniture")

label exm_lvl3_meeting_01_stationary:
    $ renpy.block_rollback()
    pause 0.5
    de_i surprise "(That's a lot of shelves...{w=0.5} Chances of a keycard just laying around on this are pretty slim, though.)"
    de_i frown sweat "(Not like I have a lot of options, anyway...)"
    pause 1.0
    scene black with dissolve
    pause 0.5
    play sound "audio/se/box_open.ogg"
    pause 1.0
    play sound4 "audio/se/paper_shuffle.ogg"
    pause 0.5
    de_i frown "(It was a longshot...{w=0.5} Although.)"
    pause 0.5
    play sound "audio/sfx/gui_item_get.ogg"
    show it_flambas_folder with dissolve:
        xalign 0.5 yalign 0.4
    pause 1.0
    de_i surprise "(The symbol on this folder, and the others like it...{w=0.5} This is the logo of Flambas.)"
    de_i frown "(I recognize it from the objects Francesco would bring home every now and then.{w=0.3} They love their branding.)"
    de_i surprise "(So, this is not just someone else using some of their technology...{w=0.5} This place, whatever it is, belongs to them.)"
    de_i frown sweat "(What does a {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}bio-engineering{b} company need a place like this for?{w=0.3} And why was I brought here?)"
    de_i surprise "(There's some papers left in this folder...{w=0.5} Maybe?)"
    if exm_lvl3_meeting_01_stationary == False:
        play sound4 "audio/sfx/gui_slots_confirm.ogg"
        show screen notify(_("Inventory Unlocked."))
        $ inventory_show = True
        $ exm_lvl3_meeting_01_stationary = True
        $ lvl3_meeting_examine_01 += 1
    pause 1.0
    call screen lvl3_wellness_explore_01

label exm_lvl3_meeting_01_stationary:
    $ renpy.block_rollback()
    pause 0.5
    de_i frown "(More folders.{w=0.3} Pencils, pens...{w=0.5} Nothing that looks like a keycard.)"
    de_i neutral "(Let's see on the inside.{w=0.3} Nothing else for it...)"
    pause 0.5
    scene black with dissolve
    play sound3 "audio/se/paper_shuffle.ogg"
    pause 1.5
    play sound2 "audio/se/paper_shuffle.ogg"
    pause 1.0
    play sound4 "audio/se/paper_shuffle.ogg"
    de frown sweat "<Shit...{w=0.5} Shit shit shit I'm out of options, am I not?>"
    pause 0.5
    scene lvl3_meeting
    show Delphine frown sweat at de_med:
        xalign 0.5
    with dissolve
    pause 0.5
    de nulla "<Nothing...{w=0.5} Nothing, nothing, NOTHING!{w=0.3} There's nothing useful, here!{w=0.3} Just ugly stationary, empty folders and more stupid Perrier!>"
    show Delphine angry
    de nulla "<AND WHY IS THERE STILL NO CLOCKS AROUND HERE?!{w=0.3} I->"
    play sound4 "audio/se/lab_lights_off.ogg"
    pause 0.3
    play sound4 "audio/em/em_shock.ogg"
    show screen emote("surprise",0.5,0.05)
    show Delphine shock
    pause 0.5
    de nulla "<TRIASTSIA!{W=0.3} What now?!>"
    if exm_lvl3_meeting_01_furniture == False:
        $ exm_lvl3_meeting_01_furniture = True
        $ lvl3_meeting_examine_01 += 1
    pause 1.0
    call screen lvl3_wellness_explore_01