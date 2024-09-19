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
    $ renpy.block_rollback()
    stop music fadeout 3.5
    scene taisho_1f_study
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
    pause 1.0
    play music "audio/bgm/shadows_breathe.ogg"
    pause 0.5
    sh_i nulla "(The doorknob...{w=0.5} Someone's trying to open the door!)"
    show Shigeo smile
    sh_i nulla "(Thank goodness!{w=0.3} It means that there's other people around that-)"
    pause 1.0
    show Shigeo surprise with dissolve
    pause 1.0
    sh_i nulla "(Wait...{w=0.5} {nw}"
    play sound "audio/sfx/gui_spook.ogg"
    extend "{b}trying{/b} to open the door?)"
    pause 1.0
    scene black
    show darkness_layer
    show Shigeo surprise at sh_big:
        xalign 0.5
    with Reveal3
    pause 1.5
    jump think_01_door
