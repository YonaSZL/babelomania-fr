default taisho_1f_corridor_explore_01 = 0
default exp_taisho_1f_corridor_01_gaspard = False
default exp_taisho_1f_corridor_01_amina = False
default exp_taisho_1f_corridor_01_side_meet = False
default exp_taisho_1f_corridor_01_gamina_wake = False
default exp_taisho_1f_corridor_01_shigeo_wake = False

default taisho_note_inspected = False

screen taisho_1f_corridor_explore_01():

    tag exploration

    button:
        pos(993,454)
        xysize(128,297)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_1f_corridor_01_gaspard")
        tooltip _("Gaspard")#GASPARD
    button:
        pos(328,175)
        xysize(354,597)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_1f_corridor_01_amina")
        tooltip _("Amina")#AMINA
    button:
        pos(742,420)
        xysize(56,276)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_1f_corridor_01_side_meet")
        tooltip _("Meeting Room #4")#LIBRARY SIDE MEETING ROOM
    button:
        pos(1226,339)
        xysize(100,462)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_1f_corridor_01_gamina_wake")
        tooltip _("Meeting Room #3")#LOCKED GAMING WAKE ROOM
    button:
        pos(1633,324)
        xysize(287,756)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_1f_corridor_01_shigeo_wake")
        tooltip _("Meeting Room #2")#SHIGEO WAKE ROOM

    $ tooltip = GetTooltip()

    nearrect:
        focus "tooltip"
        prefer_top True

        frame:
            xalign 0.5
            text "[tooltip]"

label exp_taisho_1f_corridor_01_gaspard:
    $ renpy.block_rollback()
    pause 0.5
    sh neutral "This is a test button."
    pause 1.0
    if exp_taisho_1f_corridor_01_gaspard == False:
        $ exp_taisho_1f_corridor_01_gaspard = True
        $ taisho_1f_corridor_explore_01 += 1
    call screen taisho_1f_corridor_explore_01

label exp_taisho_1f_corridor_01_amina:
    $ renpy.block_rollback()
    pause 0.5
    sh neutral "Two meeting rooms per side, then a door leading to the stairs...{w=0.5} All featuring a numerical input panel, exception made for the last one."
    am nulla "Yes.{w=0.3} Before you ask, I tried the code only with the doors to the rooms where we woke up."
    show Amina surprise
    am nulla "We found ourselves in the room right next to yours, by the way."
    sh smile "And I didn't even notice...{w=0.5} Completely soundproof, then."
    show Amina neutral
    am nulla "Quite...{w=0.5} Which makes me think."
    show Amina surprise
    am nulla "What if there are {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}other people in the other rooms{/b}?"
    pause 1.4
    sh frown "It is a possibility...{w=0.5} Let's try opening this one."
    show Amina neutral
    am nulla "Okay.{w=0.3} The code is..."
    play sound2 "audio/sfx/pad_input.ogg"
    pause 1.0
    play sound "audio/sfx/pad_wrong.ogg"
    pause 0.5
    show Amina sad
    am nulla "Well, worth a shot...{w=0.5} It's guesswork from now on, then."
    sh neutral "Unfortunately...{w=0.5} Speaking of, if you've memorized the code, would you mind if I held onto the note?"
    show Amina surprise
    am nulla "Not at all...{w=0.5} Here."
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    show screen notify(_("Received Door Code Note."))
    if exp_taisho_1f_corridor_01_amina == False:
        $ inventory.append(item_taisho_note)
        $ exp_taisho_1f_corridor_01_amina = True
        $ taisho_1f_corridor_explore_01 += 1
    show Amina neutral
    am nulla "Are you going to try and open the last one?"
    sh neutral "Eventually...{w=0.5} But I actually wanted to {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}inspect it{/b} for clues."
    show Amina surprise
    am nulla "Clues about what?"
    sh smile "I don't know...{w=0.5} But it's not like we have much else to go on, do we?"
    show Amina neutral
    am nulla "Hmm...{w=0.5} Guess not.{w=0.3} I'll keep trying to unlock the door here."
    show Amina smile
    am nulla "I'm usually pretty good with guessing games.{w=0.3} Maybe luck will favour me."
    sh smile "Statistics may yet work in our favour...{w=0.5} Good luck."
    pause 1.0
    call screen taisho_1f_corridor_explore_01

label exp_taisho_1f_corridor_01_taisho_note:
    $ renpy.block_rollback()
    pause 0.5
    play sound "audio/sfx/gui_item_get.ogg"
    show it_taisho_note with dissolve:
        xalign 0.5 yalign 0.4 
    sh_i neutral "(19120730...{w=0.5} An eight numbers passcode.)"
    sh_i frown "(Seems uncharacteristically long, kind of overkill.{w=0.3} Considering the amount of combinations just four numbers allow for...{w=0.5} Something shorter would certainly be easier to memorize.)"
    sh_i surprise "(Also, this format...{w=0.5} Wait, could this be a {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}date of some kind{/b}?)"
    sh_i frown "(.{w=0.3}.{w=0.3}.{w=0.5}it's a longshot, but...{w=0.5} Maybe the other doors...?)"
    hide it_taisho_note with dissolve
    pause 1.0
    if taisho_note_inspected == False:
        $ taisho_note_inspected = True
        $ taisho_1f_corridor_explore_01 += 1
    call screen taisho_1f_corridor_explore_01

label exp_taisho_1f_corridor_01_side_meet:
    $ renpy.block_rollback()
    pause 0.5
    sh neutral "This is a test button."
    pause 1.0
    if exp_taisho_1f_corridor_01_side_meet == False:
        $ exp_taisho_1f_corridor_01_side_meet = True
        $ taisho_1f_corridor_explore_01 += 1
    call screen taisho_1f_corridor_explore_01

label exp_taisho_1f_corridor_01_gamina_wake:
    $ renpy.block_rollback()
    pause 0.5
    sh neutral "This is a test button."
    pause 1.0
    if exp_taisho_1f_corridor_01_gamina_wake == False:
        $ exp_taisho_1f_corridor_01_gamina_wake = True
        $ taisho_1f_corridor_explore_01 += 1
    call screen taisho_1f_corridor_explore_01

label exp_taisho_1f_corridor_01_shigeo_wake:
    $ renpy.block_rollback()
    pause 0.5
    sh neutral "This is a test button."
    pause 1.0
    if exp_taisho_1f_corridor_01_shigeo_wake == False:
        $ exp_taisho_1f_corridor_01_shigeo_wake = True
        $ taisho_1f_corridor_explore_01 += 1
    call screen taisho_1f_corridor_explore_01