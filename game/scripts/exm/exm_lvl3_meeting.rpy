default lvl3_meeting_examine_01 = 0
default exm_lvl3_meeting_01_stationary = False
default exm_lvl3_meeting_01_furniture = False
default exm_lvl3_meeting_01_folder = False
default exm_lvl3_meeting_01_body = False

screen lvl3_meeting_examine_01():

    tag examination

    button:
        pos(315,367)
        xysize(255,432)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exm_lvl3_meeting_01_stationary")
        tooltip _("Stationary")
    
    if flambas_folder_inspected:
        button:
            pos(645,619)
            xysize(1259,388)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exm_lvl3_meeting_01_furniture")
            tooltip _("Furniture")

label exm_lvl3_meeting_01_stationary:
    $ renpy.block_rollback()
    pause 0.5
    if exm_lvl3_meeting_01_stationary:
        de_i neutral "(I've already searched this from top to bottom, only thing of interest was that folder...{w=0.5} Nothing else to do, here.)"
    else:
        de_i surprise "(That's a lot of shelves...{w=0.5} Chances of a keycard just laying around on this are pretty slim, though.)"
        de_i frown sweat "(Not like I have many options, anyway...)"
        pause 1.0
        scene black with dissolve
        pause 0.5
        play sound "audio/se/box_open.ogg"
        pause 3.0
        play sound4 "audio/se/paper_shuffle.ogg"
        pause 1.5
        de_i frown "(Ugh, I knew it was a longshot...{w=0.5} But.)"
        pause 0.5
        scene lvl3_meeting with Reveal
        pause 1.0
        de_i neutral "(.{w=0.3}.{w=0.3}.{w=0.5}This is...)"
        play sound "audio/sfx/gui_item_get.ogg"
        show it_flambas_folder with dissolve:
            xalign 0.5 yalign 0.4
        pause 1.0
        de_i surprise "(The symbol on this folder, and the others like it...{w=0.5} This is the logo of Flambas.)"
        de_i frown "(I recognize it from the objects Francesco would bring home every now and then.{w=0.3} They love their branding, from what I remember.{w=0.3} As much as they like aping the French Foreign ministry...)"
        play sound4 "audio/sfx/gui_slots_confirm.ogg"
        $ delphine_items.append(c_lictors)
        show screen notify(_("New Codex Entry: Fasces Lictors."))
        de_i surprise "(So, it's not just someone leasing their technology...{w=0.5} This place, whatever it is, belongs to the company.)"
        de_i frown sweat "(What the hell does a {nw}"
        play sound4 "audio/sfx/gui_spook.ogg"
        extend "{b}bio-engineering{/b} firm want with me?{w=0.3} And Francesco...)"
        de_i surprise "(He had seemed a little distant, lately.{w=0.3} I thought it was pre-nuptial jitters, but maybe...?)"
        de_i frown -sweat "(That childhood friend of his, the last minute invite...{w=0.3} I can't for the life of me recall his name, but Francesco said he was some kind of cop.)"
        de_i sad "(Francesco, are...{w=0.5} Is he in trouble?{w=0.3} Was he in trouble all this time and I...{w=0.5} {cps=15}I didn't notice?)"
        pause 1.5
        de_i neutral "(.{w=0.3}.{w=0.3}.{w=0.5}there's some papers left in this folder.)"
        if exm_lvl3_meeting_01_stationary == False:
            play sound4 "audio/sfx/gui_slots_confirm.ogg"
            $ delphine_inventory.append(item_flambas_folder)
            $ inventory_show = True
            $ exm_lvl3_meeting_01_stationary = True
            $ lvl3_meeting_examine_01 += 1
    scene lvl3_meeting with dissolve
    pause 1.0
    call screen lvl3_meeting_examine_01

label exm_lvl3_meeting_01_furniture:
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
    de frown sweat "<Shit...{w=0.5} Shit shit shit!>"
    pause 0.5
    scene lvl3_meeting
    show Delphine disgust sweat at de_med:
        xalign 0.5
    with dissolve
    pause 0.5
    stop music fadeout 1.5
    de nulla "<Nothing...{w=0.5} Nothing, nothing, NOTHING!{w=0.3} There's nothing useful, here!{w=0.3} Just ugly stationary, empty folders and more stupid Berrier!>"
    show Delphine angry
    de nulla "<AND WHY IS THERE STILL NO CLOCKS AROUND HERE?!{w=0.3} I->"
    play sound "audio/se/lights_off.ogg"
    pause 0.3
    play sound4 "audio/em/em_shock.ogg"
    scene lvl3_meeting_dark
    show screen emote("surprise",0.5,0.05)
    show Delphine shock sweat at de_med:
        xalign 0.5
    pause 0.5
    de nulla "<TRIASTSIA!{w=0.3} What now?!>"
    play sound "audio/se/jingle_flambas_distort.ogg"
    inter "Warning.{w=0.3} This facility is now in emergency evacuation mode."
    show Delphine surprise
    inter "Please proceed to the nearest elevators.{w=0.3} Flambas thanks you for entrusting us with your safety."
    de nulla "<Emergency evacuation mode...?{w=0.3} What is HAPPENING, here?!>"
    show Delphine shock
    de nulla "<But maybe that unlocked the elevators?{w=0.3} Maybe I don't need a keycard anymore...?>"
    play music "audio/bgm/shadows_breathe.ogg"
    pause 1.0
    show Delphine fear with dissolve
    de nulla "<Please let it be so...!>"
    pause 0.5
    play sound "audio/se/door_slide.ogg"
    scene black with dissolve
    if exm_lvl3_meeting_01_furniture == False:
        $ exm_lvl3_meeting_01_furniture = True
        $ lvl3_meeting_examine_01 += 1
    pause 1.0
    jump story_02_yokai