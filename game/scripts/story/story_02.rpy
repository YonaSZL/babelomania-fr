label story_02_delphine:
    $ renpy.block_rollback()
    scene title_02 with Reveal
    pause 3.0
    scene black with Reveal5
    pause 1.5
    $ quick_menu = True
    pause 1.0
    play music "audio/bgm/francesco.ogg" fadein 1.5
    pause 1.5
    de_x neutral darko "<...don't understand...{w=0.5} Don't you ever miss them...?{w=0.3} I miss my mother every day.>"
    fr sad darko "<I do...{w=0.5} But more than that, I grieve for the time that was taken from us.>"
    pause 1.0
    scene francesco_flashback with Reveal2
    pause 1.5
    fr sad "<I never got the opportunity to know them...{w=0.5} Properly get to know them.{w=0.3} I was so young, and all I knew of them was what kind of parents they were.>"
    de_x surprise darko "<Were they not good parents?>"
    fr sad "<They were amazing.{w=0.3} But being a parent was only part of who they were.>"
    fr surprise "<I never got the chance to mature, become their equal.{w=0.3} To measure up against who they were, to develop my own convictions and ideals.{w=0.3} Clash against theirs.>"
    fr neutral "<The discussions about music, food, and politics.{w=0.5} Who to go out with, who to marry, names for grandchildren, furniture, clothes...{w=0.5} All those little things that most take for granted.>"
    fr sad "<I never got the chance to really know my parents as people...{w=0.5} That chance, that opportunity, was taken from us.{w=0.3} And it left a hole that shall never be filled.>"
    pause 2.0
    de_x neutral darko "<I'm still confused, Francesco...{w=0.5} Even more so, now.{w=0.3} If you grieve them and the time lost so much...>"
    de_x surprise darko "<Why have you {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    stop music fadeout 3.5
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
    play music "<from 13.74>audio/bgm/safehouse_muted.ogg" fadein 1.0
    pause 1.5
    scene lvl3_wellness_dim with Reveal2
    pause 1.0
    de_x cloudy gown "{cps=10}Hmmmmmmmmm..."
    pause 2.0
    play sound4 "audio/em/em_impact.ogg"
    show screen emote("surprise",0.17,0.5)
    de_x shock gown sweat "...!"
    play sound "audio/se/whoosh_heavy.ogg"
    pause 1.5
    show Delphine shock sweat gown with Reveal2:
        xalign 0.5
    at de_big
    pause 1.5
    de_x nulla "(.{w=0.3}.{w=0.3}.{w=0.5}where the hell is this?)"
    show Delphine surprise
    de_x nulla "(What happened to the wedding?{w=0.3} What happened to everyone?{w=0.3} I...{w=0.5} Did I pass out?)"
    show Delphine neutral
    de_x nulla "(Last thing I remember, we...{w=0.5} We were about to watch our wedding video, and then...?{w=0.5} Then what?)"
    pause 1.5
    show Delphine frown with dissolve
    pause 0.5
    de_x nulla "(Could this be...?{w=0.5} And on {nw}"
    play sound4 "audio/sfx/gui_solved.ogg"
    extend "{b}my wedding{/b}, of all days?)"
    show Delphine angry
    de nulla "<Shit.{w=0.5} Just when the most dangerous thing I have on me are high heels.>"