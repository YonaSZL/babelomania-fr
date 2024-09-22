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
    am nulla "<It's exactly because the situation we're in is weird that we need to keep a level head...{w=0.5} Just running around opening random doors won't do us any good.{w=0.3} We need to think.>"
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
    sh nulla "Oh, I'm the right amount of nervous, believe me...{w=0.5} But, in a weird way, such a situation is actually more calming for me."
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