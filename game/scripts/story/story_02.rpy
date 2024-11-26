label story_02_delphine:
    $ renpy.block_rollback()
    $ current_char = "delphine"
    pause 1.5
    scene title_02 with Reveal
    pause 3.0
    scene black with Reveal5
    pause 1.5
    $ quick_menu = True
    pause 1.0
    play LoNoise "audio/bgs/marina.ogg" fadein 1.5
    pause 1.5
    de_x neutral darko "<...don't understand...{w=0.5} Don't you ever miss them...?{w=0.3} I miss my mother every day.>"
    de_x frown darko "<She was far from a perfect mom, believe me...{w=0.5} But still.>"
    fr sad darko "<I do miss them...{w=0.5} But more than that, I grieve for the time that was taken from us.>"
    pause 1.5
    scene francesco_flashback with Reveal3
    pause 1.5
    fr sad "<I never got the opportunity to know them...{w=0.5} Properly get to know them.{w=0.3} I was so young, and all I knew of them was what kind of parents they were.>"
    de_x surprise darko "<Were they that bad?{w=0.3} And here I am always trauma-dumping about my mom.>"
    fr sad "<No, they were amazing...{w=0.3} But being a parent was only part of who they were.>"
    fr surprise "<I never got the chance to mature and become their equal.{w=0.3} To measure up against who they were, to develop my own convictions and ideals.{w=0.3} Clash against theirs.>"
    fr neutral "<The discussions about music, food, and politics.{w=0.5} Who to go out with, who to marry, names for grandchildren, furniture, clothes...{w=0.5} All those little things that most take for granted.>"
    fr sad "<I never got the chance to really know my parents as people...{w=0.5} That opportunity was taken from us.{w=0.3} And left a hole that shall never be filled.>"
    pause 2.0
    de_x neutral darko "<I'm still confused, Francesco...{w=0.5} Even more so, now.{w=0.3} If you grieve them like that...>"
    de_x surprise darko "<Why have you {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    stop LoNoise fadeout 3.5
    extend "{b}never visited their graves{/b}?>"
    pause 1.5
    fr sad "<.{w=0.3}.{w=0.3}.{w=0.5}because...>"
    pause 1.5
    play sound "audio/se/glitch_short.ogg"
    scene francesco_flashback_glitch
    with glitch_load
    pause 2.0
    scene black
    pause 1.5
    $ renpy.block_rollback()
    play music "<from 13.74>audio/bgm/sanctuary_muted.ogg" fadein 1.0
    pause 3.0
    scene lvl3_wellness_dim with Reveal3
    pause 1.5
    de_x cloudy gown "{cps=10}Hmmmmmmmmm..."
    pause 2.0
    play sound4 "audio/em/em_impact.ogg"
    show screen emote("surprise",0.17,0.5)
    de_x shock gown sweat "...!"
    play sound "audio/se/whoosh_heavy.ogg"
    pause 1.5
    show Delphine shock sweat gown at de_big:
        xalign 0.5
    with Reveal3
    pause 1.5
    de_xi nulla "(.{w=0.3}.{w=0.3}.{w=0.5}where the eff is this?)"
    show Delphine surprise
    de_xi nulla "(This isn't the reception room...{w=0.5} It doesn't even look like the same building!{w=0.3} I...{w=0.5} Did I pass out?)"
    show Delphine neutral
    de_xi nulla "(Last thing I remember, we were about to watch our wedding video, and then...?{w=0.5} Then what?)"
    pause 1.5
    show Delphine shock with dissolve
    pause 0.5
    de_xi nulla "(I'm drawing a complete blank...{w=0.5} How did I get here?{w=0.3} How did I pass out?!)"
    show Delphine surprise
    de_xi "(And if I'm here, what happened to dad?{w=0.3} Francesco?!{w=0.3} Everyone...!)"
    pause 1.5
    show Delphine frown with Reveal
    pause 0.5
    de_xi nulla "(Alright, {nw}"
    play sound4 "audio/sfx/gui_solved.ogg"
    extend "{b}Delphine{/b}?{w=0.3} Queen?{w=0.3} I'm gonna need you to calm down.{w=0.3} Breathe.{w=0.3} Be a bit more like mom, for a little bit.{w=0.3} You can go back to cover of World Bride in the gorgeous heels later.)"
    pause 1.0
    scene lvl3_wellness_dim with dissolve
    pause 0.5
    de_i surprise "(First thing needs doing is understanding your surroundings.{w=0.3} Otherwise known as:{w=0.15} where the heck am I?)"
    pause 1.0
    $ renpy.block_rollback()
    call screen lvl3_wellness_explore_01

label story_02_wellness_done:
    $ renpy.block_rollback()
    de_i frown "(Anyway, I see no clock...{w=0.5} No way of knowing how long I was out, then.{w=0.3} And nothing else of interest I can see.)"
    pause 1.0
    show Delphine frown at de_big:
        xalign 0.5
    with dissolve
    pause 0.5
    de_i neutral "(Time to quit this emofest.{w=0.3} But how do I open this door...?)"
    pause 1.0
    stop music fadeout 0.3
    play sound "audio/se/jingle_flambas.ogg"
    pause 0.2
    scene lvl3_wellness_bright
    play sound4 "audio/em/em_shock.ogg"
    show screen emote("surprise",0.5,0.05)
    show Delphine shock sweat at de_big:
        xalign 0.5
    pause 0.8
    inter "Thank you for deciding to rest with {b}Flambas Welness Rooms{/b}.{w=0.3} Your allotted relaxation time has expired."
    show Delphine surprise
    inter "The door will be opening up shortly.{w=0.3} We wish you a pleasant continuation of your standard work day."
    de nulla "<OT KURVA, that scared the hell out of me...!{w=0.5} Wait, Flambas?>"
    pause 1.0
    show Delphine shock with Reveal
    de nulla "<That's...{w=0.5} That's {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}Francesco's employer{/b}...>"
    play music "audio/bgm/flambas_lvl3.ogg"
    pause 1.5
    scene black with Reveal3
    pause 1.0

label story_02_lvl3:
    $ renpy.block_rollback()
    scene lvl3_corridor with Reveal3
    pause 2.5
    de surprise "<.{w=0.3}.{w=0.3}.{w=0.5}no.{w=0.5} It's not the same building.>"
    pause 1.0
    show Delphine surprise at de_med:
        xalign 0.5
    with dissolve
    de nulla "<I visited him at work, before...{w=0.5} The architecture is completely different, here.>"
    show Delphine neutral
    de nulla "<It was just their leased technology, then...{w=0.5} That confirms I'm still in France, though, considering what Francesco told me about company policy.>"
    show Delphine frown
    de nulla "<Anyway, the door just opened on its own and now...{w=0.5} No one is here?{w=0.3} He-{w=0.15}lloooo?>"
    show Delphine surprise
    de nulla "<They roipnol me or some shit, stash me in the Atlas Sharted room and then leave me to my own devices?!{w=0.3} What kind of schizo kidnapping is this?!>"
    pause 1.5
    show Delphine frown
    pause 1.0
    scene lvl3_corridor with dissolve
    de frown "<Whatever.{w=0.3} Let's find the exit.>"
    pause 1.0
    call screen lvl3_corridor_explore_01

label story_02_yokai:
    $ renpy.block_rollback()
    scene lvl3_corridor_dark with Reveal
    pause 1.5
    show Delphine fear at de_big:
        xalign 0.5
    with dissolve
    pause 0.5
    de_i nulla "(Please work...{w=0.5} Please let me get out of here-)"
    stop music fadeout 0.2
    play sound3 "audio/se/disruptor_muffled.ogg"
    pause 0.2
    show screen emote("surprise",0.5,0.15)
    show Delphine surprise
    pause 1.5
    de nulla "<.{w=0.3}.{w=0.3}.{w=0.5}a {b}gunshot{/b}?"
    pause 1.0
    play sound3 "audio/se/body_slash_muffled.ogg"
    pause 0.5
    play LoNoise "audio/bgs/heartbeat_loop.ogg" fadein 0.1
    show Delphine fear sweat with dissolve:
        linear 0.1 xalign 0.4
    pause 1.0
    play sound2 "audio/se/body_slash_muffled.ogg"
    pause 0.5
    play sound4 "audio/se/blood_splatter_muffled.ogg"
    pause 1.0
    de_i nulla "(And now what...{w=0.5} What is...?!)"
    play sound3 "audio/se/fudo_steps_muffled.ogg"
    pause 2.0
    stop LoNoise fadeout 3.5
    pause 1.5
    play sound "audio/se/door_scifi.ogg"
    pause 0.5
    scene blood with Reveal
    play music "audio/bgm/fudo_myoo.ogg"
    pause 1.5
    play sound "audio/em/em_gong.ogg"
    scene fudo_appears_01
    pause 1.5
    play sound "audio/em/em_gong.ogg"
    scene fudo_appears_02
    pause 1.5
    play sound "audio/em/em_gong.ogg"
    scene fudo_appears_03
    pause 3.0
    scene fudo_appears_04 with Reveal3
    pause 3.0
    de fear sweat "{cps=10}<Aaah...{w=0.5} Aaaaaaah...!!!>"
    pause 0.5
    play sound "audio/se/throw_heavy.ogg"
    pause 0.3
    play sound4 "audio/se/bounce_gore.ogg"
    play sound3 "audio/se/bounce_item.ogg"
    scene lvl3_corridor_dark
    show lvl3_dead_scientist
    show Fudo:
        xalign 0.5 yalign 0.25 zoom 0.25
    de scream sweat "<AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!!!>"
    show lvl3_disruptor with dissolve
    de_n scream sweat "\"<NO!{w=0.3} NONONONONONONOOOOOOO!!!>\"{i}(THIS ISN'T HAPPENING!{w=0.3} THIS CANNOT BE HAPPENING!){/i}"
    de_i fear "(DAD!{w=0.3} MOM!{w=0.3} FRANCESCO!{w=0.3} ANYONE-)"
    play sound2 "audio/se/static_short.ogg"
    mi_nst static "<.{w=0.3}.{w=0.3}.{w=0.5}e gun!>"
    play sound4 "audio/se/gui_hint.ogg"
    de surprise sweat "<...what?>"
    play sound2 "audio/se/static_short.ogg"
    mi_nst static "<Grab the {b}Disruptor{/b} and shoot it!{w=0.3} OR DO YOU WANT TO DIE?!>"
    pause 0.5
    hide Fudo with dissolve
    pause 0.5
    de angry "<SHIT!{w=0.3} SHIT SHIT SHIT SHIT SHIT!>"
    play sound3 "audio/se/item_grab.ogg"
    show it_disruptor with dissolve:
        xalign 0.5 yalign 0.4
    pause 0.5
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    show screen notify(_("Inventory Unlocked."))
    $ delphine_inventory.append(item_disruptor)
    show Fudo:
        xalign 0.5 yalign 0.5 zoom 0.5
    with dissolve
    de fear sweat "<Stay back!{w=0.3} Stay back or I'll->"
    mi_nst static "<JUST SHOOT IT!{w=0.3} You don't get it?!{w=0.3} {b}It's not human!{/b}>"
    show Fudo:
        xalign 0.5 yalign 0.7 zoom 0.65
    with dissolve
    mi_nst static "<It doesn't care for your warnings!{w=0.3} It doesn't care for your pleas!{w=0.3} It doesn't care for your fear!>"
    pause 0.5
    hide Fudo with dissolve
    pause 1.0
    show Fudo with Reveal:
        yoffset 123
    pause 0.5
    mi_nst static "<All it wants to do is {b}erase your existence{/b}!>"
    pause 1.0
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    $ stat4_show = True
    pause 1.0
    #call screen shooti_shot

label story_02_elevator_escape:
    $ renpy.block_rollback()
    play sound4 "audio/em/em_impact.ogg"
    play LoNoise2 "audio/bgs/fudo_steam.ogg"
    scene lvl3_corridor_dark
    show lvl3_dead_scientist
    show Fudo smoke:
        xalign 0.5 yalign 0.5 zoom 0.5
    with flash
    pause 1.5
    play sound4 "audio/se/fudo_collapse.ogg"
    hide Fudo with dissolve
    stop music fadeout 3.5
    pause 1.0
    de surprise sweat "<Aaah...{w=0.5} Aaaah...{w=0.5} Aaaaah, I...{w=0.5} I...?!>"
    mi_nst static "<You did not!{w=0.3} Get in the elevator before it gets back up!>"
    show screen emote("surprise",0.95,0.5)
    de shock sweat "<What?!>"
    mi_nst static "<All you did was stun it!{w=0.3} {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}Once it recovers, it will come after you again{/b}!{w=0.3} GET IN THE ELEVATOR, ALREADY!>"
    de fear sweat "<Aaah...{w=0.5} Aaaaaaaaaaaaaaah!>"
    play sound2 "audio/se/button_elevator.ogg"
    pause 0.5
    play sound "audio/se/elevator_ding.ogg"
    pause 0.5
    play sound "audio/se/elevator_door.ogg"
    scene elevator_closed_dark with dissolve
    pause 1.0
    scene elevator_panel_dark with dissolve
    de shock sweat "<I don't have a keycard...>"
    mi_nst static "<It doesn't matter, the emergency lockdown overrides it.{w=0.3} Come to me on the {nw}"
    play sound4 "audio/se/gui_hint.ogg"
    extend "{b}Archives{/b} level."
    pause 1.5
    call screen elevator_panel

label story_02_happyday:
    $ renpy.block_rollback()
    play sound4 "audio/se/button_elevator.ogg"
    pause 0.5
    play sound "audio/se/elevator_start.ogg"
    play LoNoise "audio/bgs/elevator_running.ogg" fadein 0.5
    pause 1.0
    scene elevator_closed_dark with dissolve
    pause 1.0
    mi_nst static "<Good job.{w=0.3} I'll meet you there.>"
    pause 0.5
    show Delphine surprise sweat at de_med:
        xalign 0.5
    with dissolve
    pause 0.5
    de nulla ".{w=0.3}.{w=0.3}.{w=0.5}what's your name?"
    mi_st static "<I'm {b}Mira{/b}...{w=0.5} And you?>"
    de nulla "<Delphine...{w=0.5} Thank you, Mira.>"
    mi_st static "<You're welcome...{w=0.5} Hey, was it like, your wedding or something, today?>"
    pause 1.0
    show Delphine neutral with dissolve
    pause 1.0
    de nulla "<Yes.>"
    pause 1.5
    mi_st static "<I'm sorry.>"
    play sound "audio/se/glitch_short.ogg"
    pause 2.5
    show Delphine sad with dissolve
    de_n nulla "*sniffle*{w=0.3}\"U-{w=0.15}Ugh...\"*hic*"
    pause 1.0
    play sound "audio/se/clothes_shuffle.ogg"
    hide Delphine with dissolve
    pause 1.5
    de sad "NnnnnnaaaaaaaaaaaaaAAAAAAAAAAAAAH...!!!"
    pause 2.0
    stop LoNoise fadeout 3.5
    scene black with Reveal3
    pause 2.0