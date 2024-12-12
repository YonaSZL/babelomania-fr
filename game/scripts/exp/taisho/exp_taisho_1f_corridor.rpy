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

label exp_taisho_1f_corridor_01_gaspard:
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(He's checking the door to the stairwell...{w=0.5} Doesn't seem like it's going well.)"
    pause 0.5
    show Shigeo neutral:
        zoom 0.14 xpos 900 ypos 450
    show Amina neutral
    with dissolve
    sh neutral "Is it also locked?"
    ga frown "<Unfortunately...{w=0.5} And I can't understand how.>"
    show Gaspard surprise
    ga surprise "<There's no keyhole and there's no numerical input pad.{w=0.3} The door doesn't seem like it was made to be locked, and yet it doesn't budge no matter how much I push.>"
    sh neutral "Which means it's locked remotely...{w=0.5} Which implies the existence of some kind of {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}control room{/b} somewhere...{w=0.5} That's probably where the estate's security usually resides."
    ga surprise "<Security...?{w=0.5} Hey, no, if that was true, then why haven't they done anything yet?!>"
    pause 1.5
    show Shigeo sad with dissolve
    sh sad "I have a feeling they might not be able to."
    ga sweat surprise "<The hell...?!{w=0.3} You mean they...>"
    show Shigeo neutral
    sh neutral "I'm not sure about anything, right now.{w=0.3} But, consider the fact we're locked inside a building of the château.{w=0.3} A large estate which is always, receptions or not, guarded in some way."
    show Shigeo frown
    sh frown "The first thing a perpetrator would need to do, to set something like this up, is neutralize the security guards..."
    pause 1.0
    show Gaspard angry with dissolve
    ga angry "<Shit...{w=0.5} Shit shit shit!{w=0.3} What the fuck IS this bullshit?!>"
    play sound4 "audio/se/door_fist.ogg"
    if taisho_note_inspected:
        show Shigeo surprise
        sh_i surprise "(He's getting increasingly frustrated...{w=0.5} I fear he might injure himself further.)"
        menu:
            sh_i neutral "(What should I do...?)"

            "Leave him alone.":
                hide Shigeo
                show Gaspard frown -sweat
                with dissolve
                call screen taisho_1f_corridor_explore_01
            "Try and change the subject.":
                $ renpy.block_rollback()
                sh_i surprise "(Let's see, let's think back...{w=0.5} Oh, he seemed to have an opinion on this building before we even came in here, didn't he?)"
                show Shigeo smile
                sh smile "<And to make it worse, they chose the worst building, didn't they?>"
                show Gaspard surprise
                ga surprise "<Hmmm?{w=0.5} Oh, yeah, don't get me {i}started{/i}.{w=0.3} The Taishō, of all things.>"
                show Gaspard frown -sweat
                ga frown -sweat "<I looked up some stuff about Abelard Du Bois, you know?{w=0.3} The guy was an absolute weirdo.{w=0.3} On one hand, great patriot, on the other he seemed to have a fascination with...{w=0.5} Other countries.>"
                show Gaspard surprise
                ga surprise "<Which is not unheard of but, the periods he decided to take inspiration from are...{w=0.5} Peculiar.{w=0.3} I mean, the Taishō era of all things?!>"
                show Shigeo surprise
                sh surprise "<You seem to not like the architecture very much.>"
                show Gaspard frown
                ga frown "<It's not just the architecture, it's just...{w=0.5} He invested I don't know how much money in replicating a weird style from an era that lasted a measly fourteen years?{w=0.3} If he was doing it for grandeur, why not choose {i}Meiji{/i}?>"
                show Gaspard neutral
                ga neutral "<Now, {i}that{/i} was an interesting period.>"
                show Shigeo neutral
                sh neutral "<I'm surprised.{w=0.3} You seem to like Japanese history very much.>"
                show Gaspard neutral
                ga neutral "<Heh...{w=0.5} I wouldn't exactly say I like it.{w=0.3} Business school, remember?{w=0.5} My firm has a lot of oversea offices, including Japan...{w=0.5} And when dealing with foreigners, it's important to understand where they're coming from.>"
                show Gaspard laugh
                ga laugh "<And that includes their history.{w=0.5} Amazing how they still to this day name their historic eras after their emperors, despite them now being ceremonial figureheads...{w=0.5} Guess they really can't quit the kowtowing habit.>"
                pause 1.5
                show Shigeo frown
                sh_i frown "(That's very {b}incorrect{/b}, but...{w=0.5} Let's not antagonize him, he seems to have calmed down.)"
                show Gaspard neutral
                ga neutral "<And of all the periods he could have chosen, Du Bois went with the shortest one named after a walking corpse of an emperor...{w=0.5} {nw}"
                play sound4 "audio/sfx/gui_hint.ogg"
                extend "{b}1912 to 1926{/b}.{w=0.3} They got all of World War I without even a little {i}Belle Époque{/i} first.>"
                sh frown "<Hmm...{w=0.5} I guess maybe he->"
                pause 0.5
                play sound "audio/em/em_surprise.ogg"
                show screen emote("surprise",0.17,0.5)
                show Shigeo surprise
                sh surprise "Wait...{w=0.5} 1912?"
                show Gaspard surprise
                ga surprise "<What...?{w=0.5} Yeah, those are the years.>"
                show Shigeo frown
                sh frown ".{w=0.3}.{w=0.3}.{w=0.5}could it be...?"
                $ shigeo_events.append(c_taisho)
                play sound4 "audio/sfx/gui_slots_confirm.ogg"
                show screen notify(_("Codex Updated"))
                ga surprise "<Could it be what?{w=0.5} Ah, whatever, I don't really care.>"
                show Gaspard neutral
                ga neutral "<I'm going to try and see if there's some way I can access the wiring, or something...{w=0.5} Mind taking this off my hands?>"
                show Shigeo surprise
                sh surprise "Taking what off your hands...?"
                play sound "audio/sfx/gui_item_get.ogg"
                show it_smartwatch with dissolve:
                    xalign 0.5 yalign 0.4
                pause 1.0
                sh surprise "A {b}smartwatch{/b}?"
                show Gaspard frown
                ga frown "<An absolutely horrid purchase.{w=0.3} It'll teach me to follow trends...{w=0.5} The wristband is itchy and plasticky and it's been bothering me all evening.>"
                show Gaspard neutral
                ga neutral "<You seemed to be quite lost without your phone...{w=0.5} With this, you can at least tell the time.>"
                if exp_taisho_1f_corridor_01_gaspard == False:
                    play sound4 "audio/sfx/gui_slots_confirm.ogg"
                    show screen notify(_("Received Smartwatch."))
                    $ shigeo_inventory.append(item_smartwatch)
                    $ exp_taisho_1f_corridor_01_gaspard = True
                    $ taisho_1f_corridor_explore_01 += 1
                    $ time_menu = True
                hide it_smartwatch with dissolve
                show Shigeo smile
                sh smile "I see...{w=0.5} Much appreciated, Gaspard."
                show Gaspard frown
                ga frown "<Think nothing of it.{w=0.3} Now, is there like a panel or something movable...?{w=0.5} Or do we need to crack the wall?>"
                pause 1.0
                hide Shigeo with dissolve
                call screen taisho_1f_corridor_explore_01        
    else:
        hide Shigeo
        show Gaspard frown -sweat
        with dissolve
    pause 1.0
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
        $ shigeo_inventory.append(item_taisho_note)
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
    am nulla "I'm usually pretty good with guessing games.{w=0.3} Maybe I'll get lucky."
    sh smile "Statistics may yet work in our favour...{w=0.5} Good luck, then."
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
    sh_i frown "(.{w=0.3}.{w=0.3}.{w=0.5}it's a longshot, but...{w=0.5} Maybe the codes for the other doors...?)"
    hide it_taisho_note with dissolve
    pause 1.0
    if taisho_note_inspected == False:
        $ taisho_note_inspected = True
        $ taisho_1f_corridor_explore_01 += 1
    call screen taisho_1f_corridor_explore_01

label exp_taisho_1f_corridor_01_side_meet:
    $ renpy.block_rollback()
    pause 0.5
    show Shigeo neutral with dissolve:
        zoom 0.11 ypos 475 xpos 795
    if exp_taisho_1f_corridor_01_side_meet:
        sh_i neutral "(This is the door I've unlocked...{w=0.5} We can go in whenever we're ready.)"
        show Shigeo frown
        menu:
            sh_i frown "(Should we go in?)"
            
            "Let's go in.":
                jump story_01_taisho_side_meet
            "Not quite yet.":
                pause 1.0
                hide Shigeo with dissolve
                call screen taisho_1f_corridor_explore_01
    else:
        sh_i neutral "(This door looks identical to the other ones, in make...{w=0.5} And just like the other ones, it requires a code.)"
        if exp_taisho_1f_corridor_01_amina == False:
            show Shigeo frown
            sh_i frown "(I should ask Amina if she's tried opening this one yet.{w=0.3} Maybe ask her for the code they found.)"
        else:
            if taisho_note_inspected == False:
                show Shigeo frown
                sh_i frown "(I should take a look at the note Amina found, try the code.)"
            else:
                if exp_taisho_1f_corridor_01_gaspard:
                    show Shigeo frown
                    sh_i frown "(Alright...{w=0.5} I think I have a good idea of what the password might be.{w=0.3} Speaking with Gaspard made me realize that the password they found was {nw}"
                    play sound4 "audio/sfx/gui_hint.ogg"
                    extend "{b}the official starting date of the Taishō era{/b}...{w=0.5} Written in the international standard format.)"
                    show Shigeo neutral
                    sh_i neutral "(Going by that logic, maybe the password for this other door would be another {i}similarly relevant date...{/i}?)"
                    pause 1.0
                    $ numeric_puzzle_input = renpy.input(prompt="What's the passcode for this door?", default='00000000', allow='0123456789', length=8, copypaste=True)
                    if numeric_puzzle_input == "19261225":
                        play sound "audio/sfx/pad_input.ogg"
                        pause 1.0
                        play sound4 "audio/sfx/pad_success.ogg"
                        pause 0.2
                        play sound "audio/se/door_unlock.ogg"
                        show Shigeo smile
                        sh smile "Yes!"
                        show Amina surprise
                        show Gaspard surprise
                        am nulla "What was that?{w=0.3} Did I hear a door unlock?"
                        sh smile "You did.{w=0.3} We can go in."
                        ga surprise "<How did you guess the code...?>"
                        show Shigeo neutral
                        sh neutral "It appears that the codes are not randomly generated but specific references to the Taisho period...{w=0.5} This door's code was the official end date of the era."
                        am nulla "For real...?{w=0.5} Oddly specific."
                        show Gaspard neutral
                        ga neutral "<Hmph.{w=0.3} You're lucky I have an interest in the subject, then.{w=0.3} You're welcome.>"
                        sh neutral ".{w=0.3}.{w=0.3}.{w=0.5}sure.{w=0.5} Thank you."
                        show Shigeo frown
                        sh frown "We can go in whenever you're ready.{w=0.3} I'll be in front."
                        show Gaspard frown
                        show Amina neutral
                        if exp_taisho_1f_corridor_01_side_meet == False:
                            $ exp_taisho_1f_corridor_01_side_meet = True
                            $ taisho_1f_corridor_explore_01 += 1
                    else:
                        play sound "audio/sfx/pad_input.ogg"
                        pause 1.0
                        play sound4 "audio/sfx/pad_wrong.ogg"
                        pause 0.5
                        show Shigeo frown
                        sh_i frown "(Darn it.{w=0.3} What did I get wrong?)"
                        show Shigeo neutral
                        sh_i neutral "(I'm pretty sure it must be the end date of the Taishō era, which was...?)"
                else:
                    show Shigeo frown
                    sh_i frown "(Let's see if the code I got off Amina's note works.)"
                    play sound2 "audio/sfx/pad_input.ogg"
                    pause 1.0
                    play sound "audio/sfx/pad_wrong.ogg"
                    pause 0.5
                    sh_i frown "(No dice...{w=0.5} Is there any way I can try and guess it?)"
                    show Shigeo neutral
                    sh_i neutral "(I should talk to Amina and Gaspard, see if they have any ideas or information.)"
        pause 1.0
        hide Shigeo with dissolve
        call screen taisho_1f_corridor_explore_01

label exp_taisho_1f_corridor_01_gamina_wake:
    $ renpy.block_rollback()
    pause 0.5
    sh neutral "Amina, is this the room where you and Gaspard woke up?"
    show Amina surprise
    am nulla "Yes.{w=0.3} As I mentioned earlier, the code which we used for your door doesn't work for that one."
    sh neutral "Fair.{w=0.3} Did you take a good look around before you left?"
    show Amina frown
    am nulla "I want to say yes, but...{w=0.5} I wouldn't call it a thorough inspection, exactly."
    sh neutral "I see..."
    sh_i neutral "(So if there's an opportunity to go back in there, we should.)"
    pause 1.0
    show Amina neutral
    if exp_taisho_1f_corridor_01_gamina_wake == False:
        $ exp_taisho_1f_corridor_01_gamina_wake = True
        $ taisho_1f_corridor_explore_01 += 1
    call screen taisho_1f_corridor_explore_01

label exp_taisho_1f_corridor_01_shigeo_wake:
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(This is the room where I woke up...)"
    sh_i frown "(No reason to go back in there, at the moment...{w=0.5} And there's nothing helpful about the door, either.)"
    pause 1.0
    if exp_taisho_1f_corridor_01_shigeo_wake == False:
        $ exp_taisho_1f_corridor_01_shigeo_wake = True
        $ taisho_1f_corridor_explore_01 += 1
    call screen taisho_1f_corridor_explore_01