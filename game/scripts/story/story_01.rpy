label story_01_awakening:
    $ renpy.block_rollback()
    $ move_time(1,6)
    $ quick_menu = True
    pause 3.0
    play LoNoise "audio/bgs/taisho_bgs.ogg" fadein 1.0
    pause 2.5
    show Shigeo cloudy with Reveal3:
        xalign 0.5 zoom 1.0 yoffset 150
    pause 3.0
    play sound "audio/em/em_impact.ogg"
    show Shigeo surprise sweat with flash
    pause 1.5
    play sound "audio/se/whoosh_heavy.ogg"
    pause 0.2
    $ dark_environ = True
    scene taisho_1f_study
    pause 1.3
    sh surprise sweat ".{w=0.3}.{w=0.3}.{w=0.5}where...?"
    pause 1.0
    $ current_location = "taisho_1f_study"
    call screen taisho_1f_study_explore_01

label story_01_there_were_three:
    $ move_time(0,12)
    $ renpy.block_rollback()
    $ flashlight_consume = False
    stop music fadeout 3.5
    scene taisho_1f_study_bare
    show dark_flashlight
    pause 1.0
    sh_i neutral "(Alright, then.{w=0.3} I should leave, now.)"
    pause 0.5
    show Shigeo frown at sh_big:
        xalign 0.5
    with dissolve
    pause 0.5
    sh_i nulla "(Nothing else of interest that I can see, in this room.{w=0.3} Seems like a small study...{w=0.5} Or meeting room.)"
    show Shigeo neutral
    sh_i nulla "(Hopefully, the rest of the building isn't as sturdily locked down as the win-)"
    play sound3 "audio/se/doorknob_rattle.ogg"
    pause 0.3
    play sound4 "audio/em/em_surprise.ogg"
    show screen emote("surprise",0.5,0.05)
    show Shigeo surprise
    pause 1.5
    sh_i nulla "(The doorknob...{w=0.5} Someone's trying to open the door!)"
    show Shigeo smile
    sh_i nulla "(Thank goodness!{w=0.3} It means that there's other people around that-)"
    pause 1.0
    show Shigeo surprise with dissolve
    pause 1.0
    sh_i nulla "(Wait...{w=0.5} {nw}"
    play sound "audio/sfx/gui_spook.ogg"
    extend "{b}trying{/b} to open the door?)"
    play sound3 "audio/se/doorknob_rattle.ogg"
    pause 0.5
    play music "audio/bgm/shadows_breathe.ogg"
    pause 1.0
    scene black
    show darkness_layer
    show Shigeo surprise at sh_big:
        xalign 0.5
    with Reveal3
    pause 1.5
    $ renpy.block_rollback()
    jump think_01_door

label story_01_door_opens:
    $ renpy.block_rollback()
    scene taisho_1f_study_bare
    show dark_flashlight
    show Shigeo surprise at sh_big:
        xalign 0.5
    with Reveal
    pause 0.5
    play sound3 "audio/se/door_slam.ogg"
    pause 0.5
    show Shigeo frown
    sh_i nulla "(That doesn't sound good at all...{w=0.5} Maybe I'm being paranoid, but I'd rather get out of here on my own terms.)"
    hide Shigeo with dissolve
    sh_i frown "(I'll hide and be silent, wait for whoever it is to go away.)"
    pause 1.0
    play sound3 "audio/se/door_slam.ogg"
    pause 1.5
    play sound3 "audio/se/door_slam.ogg"
    pause 0.5
    play sound4 "audio/se/door_fist.ogg"
    pause 0.5
    sh_i angry "(Ugh, they're persistent...!{w=0.3} But the door seems reinforced.)"
    pause 3.0
    sh_i neutral "(.{w=0.3}.{w=0.3}.{w=0.5}did they give up?)"
    pause 0.5
    play sound3 "audio/sfx/pad_input.ogg"
    pause 2.5
    play sound3 "audio/sfx/pad_success.ogg"
    pause 0.2
    play sound4 "audio/se/door_unlock.ogg"
    sh_i shock sweat "(What...?!)"
    play sound3 "audio/se/door_creak.ogg"
    pause 0.5
    play sound "audio/se/steps_wood_slow.ogg"
    pause 1.0
    sh_i frown sweat "(One...{w=0.5} Two.{w=0.3} Two sets of steps.)"
    am_x darko surprise "<...shoulder?>"
    ga_x darko angry sweat "<I'm fine!{w=0.3} Mind your own business!>"
    am_x darko angry "<Why are you being such an asshole?!{w=0.3} I was trying to help!>"
    sh_i surprise "(They're...{w=0.5} Arguing?{w=0.3} In French?{w=0.5} Wait, I think...{w=0.3} Are they...?)"
    stop music fadeout 3.5
    pause 0.5
    show Amina angry at am_med:
        xalign 0.95
    show Gaspard angry at ga_med:
        xalign 0.52
    with Reveal
    pause 0.5
    sh_i surprise "(Gaspard and Amina!)"
    ga nulla "<I didn't need your help.>"
    show Amina frown
    am nulla "<The way you're holding your shoulder begs to differ.{w=0.3} You've been acting crazy ever since we woke up!>"
    show Gaspard frown
    ga nulla "<Oh, I'm sorry if the situation we're in is getting to me...>"
    show Amina neutral
    am nulla "<It's exactly because the situation we're in is weird that we need to keep a level head...{w=0.5} Just running around ramming random doors won't do us any good.{w=0.3} We need to think.>"
    show Gaspard surprise
    ga nulla "<What is there to think about?!{w=0.3} It's clear we've been kidnapped!>"
    show Amina surprise
    am nulla "<What kind of kidnapper would leave us unrestrained in a room we can open?{w=0.3} And with a {nw}"
    play sound "audio/sfx/gui_hint.ogg"
    extend "{b}code that allows us to open another door{/b}?!>"
    sh neutral -sweat ".{w=0.3}.{w=0.3}.{w=0.5}and why would they kidnap me, too?"
    play sound "audio/em/em_shock.ogg"
    show Gaspard shock sweat
    show Amina shock sweat
    show screen emote("surprise",0.52,0.05)
    show screen emote2("surprise",0.8,0.05)
    pause 1.0
    show Shigeo neutral at sh_med:
        xalign 0.1
    with Reveal
    sh nulla "I don't come from any kind of money, old or new."
    am nulla "Shigeo Arata...!{w=0.5} <Sur le Coran de la Mecque!>"
    show Gaspard angry
    ga nulla "<What the fuck is wrong with you?!{w=0.3} You scared the shit out of me!>"
    sh nulla "Apologies.{w=0.3} I was waiting to see who came through that door...{w=0.5} And how they would choose to act."
    show Shigeo frown
    sh nulla "As you aptly put, this is a very weird situation...{w=0.5} And I agree with Amina that at this moment, it'd be better to collect our thoughts for a few minutes."
    pause 1.0
    show Amina neutral
    show Gaspard frown
    with dissolve
    play music "audio/bgm/shadows_whisper.ogg"
    am nulla "Also gives me time to get my heart-rate down."
    ga nulla "<Tsk.{w=0.3} Whatever.>"
    pause 1.0
    scene taisho_1f_study_bare
    show dark_flashlight
    with dissolve
    pause 0.5
    show Gaspard frown at ga_big:
        xalign 0.37
    show Amina neutral at am_big:
        xalign 0.97
    with dissolve
    pause 0.5
    $ move_time(0,4)
    $ renpy.block_rollback()
    call screen gaspmina_conv_01

label story_01_taisho:
    $ renpy.block_rollback()
    $ move_time(0,9)
    stop music fadeout 3.5
    pause 0.5
    sh neutral "We've stood still long enough...{w=0.5} We should move."
    pause 0.5
    scene taisho_1f_study_bare
    show dark_flashlight
    show Amina neutral at am_med:
        xalign 0.95
    show Gaspard frown at ga_med:
        xalign 0.52
    show Shigeo neutral at sh_med:
        xalign 0.1
    with dissolve
    pause 0.5
    sh nulla "Can you tell me what time is it?{w=0.3} Also, do you have anything on you to draw a map?"
    show Amina surprise
    am nulla "[dis_hours]:[dis_minutes]...{w=0.5} And I could make one with a Sketch App on my phone?"
    show Shigeo frown
    sh nulla "It's going to be inaccessible if the battery runs out...{w=0.5} But it will do until we find something to write."
    show Gaspard angry
    ga nulla "<Hey hey hey, wait a damn minute!{w=0.3} Who the hell put you in charge?!>"
    pause 1.5
    show Shigeo neutral with dissolve
    sh nulla "Nobody, I guess...{w=0.5} So, what do you suggest we should do?"
    pause 0.5
    show Gaspard frown with dissolve
    ga nulla "<We...{w=0.5} We should check the other doors in the corridor.{w=0.3} See if we can find a way out.{w=0.3} Yes.>"
    show Shigeo smile
    show Amina sad
    sh nulla "Very well.{w=0.3} Let's do that, then."
    ga nulla "<.{w=0.3}.{w=0.3}.{w=0.5}fucking...>"
    pause 0.5
    play sound "audio/se/steps_wood_slow.ogg"
    hide Gaspard with dissolve
    pause 0.5
    am nulla "Thank you for being patient with him...{w=0.5} He's usually not this bad."
    show Shigeo neutral
    sh nulla "One doesn't usually find themselves in such a situation.{w=0.3} It's alright, I'm not taking it personally.{w=0.3} He obviously needs to feel in control to be at ease...{w=0.5} I will accomodate."
    show Amina surprise
    am nulla "Could you elaborate further on what you meant?{w=0.3} About this not just being a ransom situation?"
    pause 1.0
    show Shigeo frown with dissolve
    pause 0.5
    sh nulla "We've been out for little more than an hour.{w=0.3} If it was about ransom, they would have taken us somewhere far away and isolated, instead we're still at the château...{w=0.5} And that's without adding in the detail that I'm not really worth anything, monetarily."
    show Amina neutral
    sh nulla "Also, there's matter with my phone and the doors...{w=0.5} Earlier, I thought they had placed me in such a room for protection, but now I fear that this is something much more elaborate and sinister."
    show Shigeo neutral
    sh nulla "I don't know exactly what, yet...{w=0.5} But we should take into account that {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}our captors may be observing us right now{/b}."
    play sound "audio/em/em_shock.ogg"
    show screen emote("surprise",0.83,0.05)
    show Amina surprise sweat
    pause 1.5
    am nulla "You...{w=0.5} You're serious, aren't you?{w=0.3} But more than that..."
    show Amina neutral
    am nulla "You seem to be...{w=0.5} Unbelievably calm, despite the circumstances."
    show Shigeo smile sweat
    sh nulla "Oh, I'm the right amount of nervous, believe me.{w=0.3} You should've seen before I found the flashlight...{w=0.5} But, in a weird way, such a situation is actually more calming for me."
    show Shigeo laugh -sweat
    sh nulla "I'm used to dealing with stuff like this on the job...{w=0.5} Although, never this directly."
    am nulla "Right, what you 'do for a living'...{w=0.5} And that would be?"
    pause 1.5
    show Shigeo neutral with dissolve
    sh nulla "I'm with {nw}"
    play sound4 "audio/sfx/gui_solved.ogg"
    extend "{b}Europol{/b}.{w=0.5} I'm a {b}behavioral analyst and criminal profiler{/b}."
    show Amina surprise -sweat
    pause 1.0
    play music "audio/bgm/shadows_whisper.ogg"
    pause 1.5
    scene black with dissolve
    $ flashlight_use = False
    $ flashlight_consume = False
    $ flashlight_allowed = False
    $ move_time(0,4)
    pause 1.0
    jump story_01_taisho_corridor

label story_01_taisho_corridor:
    $ renpy.block_rollback()
    scene taisho_1f_corridor with Reveal3
    pause 1.5
    show Gaspard frown:
        zoom 0.14 xpos 1000 ypos 460
    show Amina neutral at am_big:
        xpos 205
    with dissolve
    pause 1.5
    sh surprise "The light coming in from outside is strong enough...{w=0.5} Saves us some battery."
    am nulla "The window is not shuttered, unlike those in the rooms...{w=0.5} But it's still locked."
    sh frown "Also, it's made of tempered glass...{w=0.5} No chance of breaking through that bare handed."
    sh neutral "Well, let's look around and see what our options are."
    pause 1.0
    call screen taisho_1f_corridor_explore_01

label story_01_taisho_side_meet:
    $ renpy.block_rollback()
    play sound "audio/sfx/pad_input.ogg"
    pause 1.0
    play sound4 "audio/sfx/pad_success.ogg"
    pause 0.2
    play sound "audio/se/door_unlock.ogg"
    pause 1.0
    scene black with dissolve
    $ move_time(0,17)
    pause 0.5
    $ flashlight_use = True
    $ dark_environ = False
    play sound4 "audio/se/flashlight_on.ogg"
    pause 1.0
    scene taisho_1f_side_meet_base
    show darkness_layers
    with Reveal3
    pause 1.0
    sh neutral ".{w=0.3}.{w=0.3}.{w=0.5}no one's here."
    ga frown "<Also:{w=0.3} another dead end.>"
    am surprise "Or is it?{w=0.3} Look."
    pause 0.5
    show Amina surprise with dissolve:
        zoom 0.29 xpos 289 ypos 456
    am surprise "Another locked door...{w=0.5} Shigeo, what's the code you used?"
    sh neutral "19261225."
    show Amina neutral
    am neutral "Alright.{w=0.3} I'm going to try both."
    play sound "audio/sfx/pad_input.ogg"
    pause 1.0
    play sound4 "audio/sfx/pad_wrong.ogg"
    pause 1.0
    play sound "audio/sfx/pad_input.ogg"
    pause 1.0
    play sound4 "audio/sfx/pad_wrong.ogg"
    pause 0.5
    show Amina sad
    am sad "Ugh, would've been too easy, I guess...{w=0.5} Any ideas?"
    ga frown "<Ugh, this is ridiculous!{w=0.3} Why are we even in here?!{w=0.3} We should be trying to open the door to the stairwell!>"
    sh neutral "We currently lack the means to.{w=0.3} We need to-"
    play sound "audio/em/em_angry.ogg"
    show screen emote("angry",0.17,0.5)
    ga angry "<Then the window!{w=0.3} This one, or the one in the corridor!>"
    show Amina surprise
    show Gaspard angry with dissolve:
        zoom 0.32 xpos 1538 ypos 380
    ga angry "<Let's try and break open one of {i}these{/i} fucking things, already!{w=0.3} Let's do SOMETHING!>"
    am surprise "Gaspard...!"
    sh neutral "I understand your frustration, but-"
    play sound4 "audio/se/door_fist.ogg"
    ga angry "<Do you?!{w=0.3} Do you really?!{w=0.3} You seem to be taking this quite IN STRIDE!>"
    sh surprise "...!"
    show Gaspard sweat
    ga angry sweat "<All calm and collected, while I'm losing my fucking mind!{w=0.3} Locked in this REVOLTING building, made to solve FUCKING riddles?!{w=0.3} How dare!{w=0.3} HOW DARE?!>"
    show Amina:
        easein 1.0 xpos 362
    am surprise sweat "Gaspard, please calm down!{w=0.3} What's wrong with you?!"
    play sound4 "audio/se/door_fist.ogg"
    show Gaspard:
        linear 0.2 xpos 1488
    ga angry "<What's wrong?!{w=0.3} WHAT'S WRONG?!>"
    pause 1.0
    stop music fadeout 3.5
    show Gaspard surprise with dissolve
    pause 1.0
    ga surprise "<What's...{w=0.5} What's wrong.{w=0.3}.{w=0.3}.{w=0.3}?{w=0.5} I...>"
    show Amina sad sweat
    am sad sweat "I've never seen you this upset...{w=0.5} Are you feeling alright?"
    pause 0.5
    show Gaspard frown with dissolve
    pause 0.5
    ga frown "I...{w=0.5} I feel a little hot, actually, I...{w=0.5} And I'm thirsty."
    sh neutral sweat ".{w=0.3}.{w=0.3}.{w=0.5}let's take a small break.{w=0.3} Amina, please assist him.{w=0.3} I will take a look around."
    am sad -sweat "Thanks...{w=0.5} <Gaspard, why don't you lay down?>"
    pause 0.5
    hide Amina with dissolve
    hide Gaspard with dissolve
    pause 1.5
    show Shigeo neutral sweat at sh_big:
        xalign 0.5
    with dissolve
    sh_i nulla "(The stress must be getting to him...{w=0.5} Did they know that he doesn't like the building?{w=0.3} And of his temper?{w=0.3} Is that why they put him in here?)"
    show Shigeo frown
    sh_i nulla "(I wouldn't put it past whoever's doing this.{w=0.5} The fact that we are allowed to walk around this building, able to guess our way to opening the doors...{w=0.5} This isn't a kidnapping, this is {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}some kind of game or test{/b}...{w=0.5} I have no doubt that we're being observed, now.)"
    show Shigeo neutral
    sh_i nulla "(I should keep this to myself, for now.{w=0.3} Let's just hope they don't introduce any new variables before I figure out the rules or a way out of this building...)"
    pause 1.5
    stop LoNoise fadeout 3.5
    scene black with Reveal3
    $ time_menu = False
    $ stat1_show = False
    $ inventory_show = False
    pause 2.0
    scene taisho_1f_tabitha with Reveal3
    pause 3.0
    show Tabitha bow at ta_big:
        xalign 0.5
    with Reveal
    pause 2.8
    play sound "audio/se/sting.ogg"
    pause 0.2
    show Tabitha r_cold
    pause 1.5
    scene black
    pause 5.0
    $ move_time(0,10)
    pause 1.0
    play LoNoise "audio/bgs/taisho_bgs.ogg" fadein 1.0
    pause 1.5
    $ time_menu = True
    $ stat1_show = True
    $ inventory_show = True
    ga frown sweat "<That water was disgusting.>"
    am neutral "<Just be glad it wasn't stagnant.{w=0.3} It did come from a flower vase, after all.>"
    ga surprise "<With fake flowers...?{w=0.5} Why?>"
    am smile "<I don't know.{w=0.3} Authenticity?>"
    pause 1.5
    ga neutral "<Heh.{w=0.3} Of all the wasted effort on appearances...>"
    am smile "<What's that expression in English...?{w=0.5}> 'Game recognizes game'."
    pause 1.0
    scene taisho_1f_side_meet_base
    show darkness_layers
    show Amina neutral at am_big:
        xalign 0.85
    show Gaspard neutral sweat at ga_big:
        xalign 0.5 yoffset 300
    with Reveal
    pause 0.5
    am nulla "<And to be clear...{w=0.5} I'm not talking about you only.>"
    ga nulla "<Hm.{w=0.3} Finally ready to admit it out loud, then?>"
    show Amina smile
    am nulla "<Very vague...{w=0.5} There's a lot of 'it' we've been holding back on.>"
    show Gaspard laugh
    ga nulla "<Fair...{w=0.5} I was mainly talking about the fact that you've been dating me to keep daddy happy.>"
    show Amina neutral
    am nulla "<Maybe so...{w=0.5} Are you ready to admit that you've been dating me just to piss off yours?>"
    pause 1.0
    show Gaspard frown with dissolve
    ga nulla "<It's not the only reason.>"
    show Amina surprise
    am nulla "<Oh, isn't it?{w=0.5} What else is there, then?>"
    show Gaspard laugh
    ga nulla "<I'll admit that the subtle twitch of my father's brow the first time I brought you to a family function was...{w=0.5} Titillating.>"
    show Gaspard neutral
    ga nulla "<But you're much more than just a stone in the water.{w=0.3} You're crazy smart, Amina.{w=0.3} You're ambitious.{w=0.3} You'll go far and you're a connection worth having, no matter the type.>"
    pause 1.0
    show Amina sad with dissolve
    am nulla "<Gaspard, saying that you've been dating me for my potential is not exactly...{w=0.5} Nice.>"
    show Gaspard frown
    ga nulla "<Oh, come off it.{w=0.3} The benefit of making your family fit in certain circles by reflection is also potential.{w=0.3} That's what you've been seeking.>"
    show Amina frown
    am nulla "<Fine.{w=0.3} But I've been loyal throughout everything, nonetheless.{w=0.3} Don't think I didn't notice you and that bridesmaid just so happened to come back one after the other.{w=0.3} Don't think I never noticed the others.>"
    show Gaspard neutral
    ga nulla "<Really, now?{w=0.3} May I remind you that emotional affairs count, too?>"
    pause 1.5
    show Amina sad with dissolve
    am nulla "<We both went into this relationship already checked out, didn't we?>"
    show Gaspard frown -sweat
    ga nulla "<Things that happen when all you do is think about the next step in the plan...{w=0.5} That's the thing that brought us together in the first place, isn't it?>"
    show Amina neutral
    ga nulla "<A spasmodic need to finally, one day, have complete control over everything about ourselves and around ourselves...{w=0.5} That doesn't really leave a lot of space to consider someone else an equal.>"
    am nulla "<.{w=0.3}.{w=0.3}.{w=0.5}we can talk more about this when we're out of this situation.{w=0.3} For what it matters, Gaspard?{w=0.5} I don't think you're a {i}total{/i} ass.>"
    show Amina surprise
    am nulla "<Are you feeling better, now?>"
    show Gaspard neutral
    ga nulla "<Oh, such praise...{w=0.5} And yeah, I'm feeling better.{w=0.3} Just a little ringing in my ears but the water helped.>"
    show Gaspard frown
    ga nulla "<We should go see if the Italian has managed to figure a way out of here...>"
    am nulla "<I have a feeling you don't like Shigeo that much...{w=0.5} But you're the one who invited him to our table.>"
    show Gaspard neutral
    ga nulla "<Oh, that?{w=0.3} That's because he saw me and, most likely, the bridesmaid leaving the bathrooms.{w=0.3} Keep your liabilities close, know what I mean?>"
    show Amina neutral
    show Gaspard frown
    ga nulla "<And it's not that I don't like him, it's just...{w=0.5} I knew everyone at this wedding, and if I didn't, I knew {i}of{/i} them...{w=0.5} But this guy is a complete unknown.>"
    show Gaspard neutral
    ga nulla "<Not exactly a calming presence for a control freak, wouldn't you say?>"
    show Amina smile
    am nulla "<Moron.>"
    pause 1.0
    show Gaspard frown
    ga nulla "<And, Amina...{w=0.5} For what it's worth?{w=0.3} I'm sorry.{w=0.3} And thank you.>"
    show Amina neutral
    am nulla "<.{w=0.3}.{w=0.3}.{w=0.5}I'm sorry too.{w=0.3} Let me help you up.>"
    $ move_time(0,6)
    sh neutral "<How is he?>"
    show Gaspard surprise
    show Amina surprise
    pause 0.5
    play music "audio/bgm/shadows_whisper.ogg"
    show Amina neutral
    show Gaspard frown
    with dissolve
    am nulla "Better.{w=0.3} Have you made any progress?"
    sh neutral "Sort of...{w=0.5} I have a {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}plan{/b}, actually."
    pause 1.0
    scene taisho_1f_side_meet_base
    show darkness_layers
    with dissolve
    pause 0.5
    show Shigeo neutral at sh_med:
        xalign 0.24
    show Amina surprise at am_med:
        xalign 0.95
    show Gaspard frown at ga_med:
        xalign 0.6
    with dissolve
    pause 0.5
    am nulla "A plan, you say?{w=0.3} For what?"
    sh nulla "To open the door to the stairwell."
    show Gaspard surprise
    ga nulla "<Wait, really?!{w=0.3} Finally, what is it?!>"
    sh nulla "I'd like to explain my reasoning first, as the proposal involves some risk.{w=0.3} Can I?"
    show Gaspard frown
    ga nulla "<Ugh...{w=0.5} Fine, whatever.{w=0.3} Proceed.>"
    show Amina neutral
    sh nulla "Thank you.{w=0.3} So, the door in question while magnetically sealed like the ones to the rooms, doesn't have a keypad.{w=0.3} It's locked and unlocked remotely."
    show Shigeo frown
    sh nulla "Which means that to open it, we need to override that lock...{w=0.5} By creating an emergency."
    show Amina surprise
    am nulla "An emergency?"
    show Shigeo neutral
    sh nulla "Yes.{w=0.3} Building regulations state that doors to stairwells can be lockable as long as they're set to {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}unlock automatically in case of a fire{/b}."
    show Gaspard surprise
    ga nulla "<So that's how it works...{w=0.5} Wait, you mean you want to start a fire?!>"
    show Shigeo frown
    sh nulla "Just one small enough to be picked up by a smoke detector.{w=0.3} But still, with the windows being sealed...{w=0.5} It is a risk."
    show Shigeo neutral
    sh nulla "So, it's not something I can decide on my own.{w=0.3} If you think it's too dangerous, I will keep looking for a different solution."
    am nulla ".{w=0.3}.{w=0.3}.{w=0.5}do you even have something to start a fire?"
    sh nulla "Not currently.{w=0.3} But I'm pretty sure we're going to find something we can use in the next room."
    ga nulla "<And what makes you so sure?>"
    pause 1.0
    show Shigeo frown with dissolve
    sh nulla "The very specific codes, which related to the building...{w=0.5} The note in your pocket, which opened the room where I was...{w=0.5} The remotely controlled door.{w=0.3} This is not a kidnapping, this is a {i}game{/i}."
    show Gaspard surprise sweat
    show Amina surprise sweat
    ga nulla "<What are you...?!>"
    sh nulla "I mentioned this to Amina earlier.{w=0.3} I'm a profiler with Europol, my job is to...{w=0.5} Let's say make mental identikits of criminals.{w=0.3} I can see a pattern, here."
    show Shigeo neutral
    sh nulla "We've been absconded, but at the same time we've been given the tools to get out of it...{w=0.5} A half-japanese person and someone with knowledge of Japanese history in a Taishō inspired building?{w=0.3} This is not a coincidence."
    ga nulla "<You mean...{w=0.5} You're telling me that all of this...?>"
    play sound "audio/em/em_angry.ogg"
    show screen emote("angry",0.57,0.05)
    show Gaspard angry
    ga nulla "<It was {i}planned?!{/i}{w=0.3} Someone has been looking me up AND PLANNED TO DO THIS TO ME?!>"
    show Shigeo sweat
    sh nulla "To us...{w=0.5} And now I can't help but wonder what has happened to the other attendees."
    am nulla "And that led you to think there may be something to start a fire in the next room because...?"
    show Shigeo neutral -sweat
    sh nulla "Because I believe it's the solution to this particular puzzle.{w=0.3} So far we've been given a fair chance to solve them, so...{w=0.5} It seems only logical."
    show Gaspard frown
    ga nulla "<So you're trusting in the logic of a madman?{w=0.3} That's your big plan?>"
    sh nulla "It's the only one I have right now...{w=0.5} But as I said, we won't proceed unless we're all in agreement."
    pause 1.5
    show Amina neutral -sweat with dissolve
    am nulla "What about we postpone the discussion?{w=0.3} Let's get in that room and, if we can find something to start a fire, then we can discuss if to actually do it."
    sh nulla "Fine by me.{w=0.3} I still need to figure out the code, anyway.{w=0.3} I was trying other significant Taishō dates but so far, nothing's worked."
    ga nulla ".{w=0.3}.{w=0.3}.{w=0.5}which ones have you used?"
    show Shigeo surprise
    sh nulla "Hmm, the assassination of Prime Minister Hara...{w=0.5} And the appointment of the Emperor's son as regent, but I'm not sure I got the day well."
    show Gaspard neutral -sweat
    ga nulla "<Hmph, wouldn't matter anyway.{w=0.3} You're way off mark.{w=0.3} Isn't it obvious what date you're supposed to use?>"
    show Amina surprise
    play sound "audio/em/em_question.ogg"
    show screen emote("question",0.3,0.05)
    sh nulla "Uhm...{w=0.5} No, not really.{w=0.3} What do you mean?"
    show Gaspard frown
    ga nulla "<Let's say you're right and there's something to start a fire, in the next room...{w=0.5} Going off that logic, the date would need be related to fire too.>"
    show Gaspard laugh
    ga nulla "<It just so happens that, during the {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}Great Kantō earthquake{/b}, the single greatest loss of life was caused by a {i}fire whirl{/i} which incinerated more than 30.000 people.>"
    play sound "audio/em/em_shock.ogg"
    show screen emote("surprise",0.85,0.05)
    show screen emote2("surprise",0.3,0.05)
    show Shigeo shock
    show Amina shock sweat
    am nulla "<Ya Allah!>{w=0.3} Poor people!"
    sh nulla "A fire whirl...{w=0.5} Of course!"
    show Gaspard neutral
    ga nulla "<1st of September 1923.>"
    show Shigeo smile
    sh nulla "Which means the code is..."
    hide Shigeo with dissolve
    pause 0.5
    show Amina surprise -sweat with dissolve
    pause 0.5
    play sound "audio/sfx/pad_input.ogg"
    sh_i neutral "(19230901...)"
    pause 1.0
    play sound4 "audio/sfx/pad_success.ogg"
    pause 0.2
    play sound "audio/se/door_unlock.ogg"
    pause 0.3
    sh smile "It worked!{w=0.3} Great deduction, Gaspard!"
    show Gaspard laugh
    ga nulla "<Oh, I didn't do much...{w=0.5} General knowledge, really.>"
    show Amina smile
    am nulla "<Heh...{w=0.5} Again, you're not a {i}total{/i} ass.{w=0.3} Good job.>"
    show Gaspard neutral
    ga nulla "<.{w=0.3}.{w=0.3}.{w=0.5}thanks.>"
    pause 1.0
    hide Amina with dissolve
    pause 1.0
    play sound "audio/se/ears_ringing.ogg"
    show Gaspard frown sweat with dissolve
    pause 1.0
    ga_i nulla "(Ugh, the ringing is getting stronger...{w=0.5} I think it's my blood pressure.{w=0.5} I need to stop getting that worked up.)"
    show Gaspard angry
    ga_i nulla "(And that water didn't do the trick at all...{w=0.5} I'm absolutely parched!{w=0.3} Let's hope there's...{w=0.5} Something...)"
    pause 1.0
    stop LoNoise fadeout 3.5
    stop music fadeout 3.5
    scene black with Reveal3
    pause 0.5
    ga_i angry sweat "(Something to {b}sate my thirst...!{/b})"
    pause 2.0
    $ flashlight_use = False
    $ flashlight_allowed = True
    $ dark_environ = True
    jump story_01_library

label story_01_library:
    play LoNoise "audio/bgs/taisho_bgs.ogg" fadein 1.0
    scene black
    show taisho_1f_library_base:
        xalign 0.0
    show darkness_layers
    with Reveal3
    pause 1.5
    sh neutral "A big library...{w=0.5} With a twin door on the other side."
    am surprise "Must lead to the other room we couldn't open."
    ga frown "<Hmm...{w=0.5} Makes sense...>"
    sh neutral "Let's look around, then.{w=0.3} Gaspard, Amina, you can search the left side.{w=0.3} I will take the other half of the room."
    am neutral "Understood.{w=0.3} Gaspard, mind taking the corner library?{w=0.3} Your smartphone has a stronger flash than mine."
    ga frown sweat "<Corner...{w=0.5} Sure.{w=0.3} Sure.>"
    pause 1.0
    $ renpy.block_rollback()
    scene black
    show screen taisho_1f_library_explore_01_base
    call screen taisho_1f_library_explore_01 with Reveal

label story_01_gaspard_gone:
    $ renpy.block_rollback()
    pause 1.0
    play sound4 "audio/sfx/gui_spook.ogg"
    pause 0.5
    play music "audio/bgm/shadows_breathe.ogg"
    am surprise sweat "Ga...{w=0.5} Gaspard?!"
    sh surprise sweat "Where...?!{w=0.3} Gaspard!"
    pause 1.0
    scene black
    hide screen taisho_1f_library_explore_01_base
    hide screen taisho_1f_library_explore_01
    show taisho_1f_library_base:
        xalign 0.0
    show darkness_layers
    show Amina surprise sweat at am_big:
        xalign 0.3
    show Shigeo surprise sweat at sh_big:
        xalign 0.7
    with dissolve
    am nulla "He's...{w=0.5} He's {i}gone{/i}?!{w=0.3} How can he be gone?!"
    sh nulla "I...{w=0.5} I didn't notice...{w=0.5} Did you-?!"
    am nulla "No!{w=0.3} I was looking around the room and...?!{w=0.3} Where is he?!"
    show Amina sad
    show Shigeo frown
    am nulla "GASPARD!{w=0.3} GAS-{nw}"
    play sound3 "audio/se/door_slam.ogg"
    pause 0.2
    show Amina shock
    show Shigeo shock
    show screen emote("surprise",0.61,0.05)
    show screen emote2("surprise",0.33,0.05)
    $ taisho_1f_library_explore_01 += 1
    pause 1.5
    scene black
    show screen taisho_1f_library_explore_01_base
    hide Amina
    hide Shigeo
    with dissolve
    pause 1.5
    am sad sweat "{cps=10}Ga...{w=0.5} Gaspard...?"
    pause 1.0
    $ renpy.block_rollback()
    call screen taisho_1f_library_explore_01

label story_01_gaspard_found:
    pause 1.0
    scene black
    hide screen taisho_1f_library_explore_01_base
    hide screen taisho_1f_library_explore_01
    with Reveal3
    pause 1.0
    scene gaspard_turn_00
    show dark_flashlight
    with Reveal3
    pause 1.5
    am surprise sweat "Gaspard?!{w=0.3} <Ya Allah, are you hurt?!>"
    sh_i surprise sweat "(.{w=0.3}.{w=0.3}.{w=0.5}what...?)"
    am sad sweat "<Gaspard, answer me!{w=0.3} Are you->{nw}"
    play sound "audio/se/whoosh_fast.ogg"
    show screen emote("surprise",0.17,0.5)
    sh shock sweat "Stop!{w=0.3} Don't get close to him!"
    play sound4 "audio/em/em_shock.ogg"
    show screen emote("surprise",0.17,0.5)
    am shock sweat "...!{w=0.3} But Gaspard...?!"
    play sound4 "audio/em/em_impact.ogg"
    sh angry sweat "STAY BACK, I SAID!"
    am shock sweat "But...{w=0.5} But why?!"
    stop music fadeout 3.5
    pause 1.5
    sh frown sweat ".{w=0.3}.{w=0.3}.{w=0.5}something's wrong."
    pause 1.5
    call screen taisho_1f_library_gaspard_scare