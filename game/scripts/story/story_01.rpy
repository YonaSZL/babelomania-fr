label story_01_awakening:
    pause 1.0
    play LoNoise "audio/bgs/taisho_bgs.ogg" fadein 1.0
    pause 1.5
    show Shigeo cloudy with Reveal3:
        xalign 0.5 zoom 1.0 yoffset 150
    pause 2.0
    play sound "audio/em/em_impact.ogg"
    show Shigeo surprise sweat with flash
    pause 1.5
    play sound "audio/se/whoosh_heavy.ogg"
    pause 0.2
    scene taisho_1f_study
    show darkness_layer
    pause 1.3
    sh surprise sweat ".{w=0.3}.{w=0.3}.{w=0.5}where...?"
    pause 1.0
    scene black
    call screen taisho_1f_study_examine_01