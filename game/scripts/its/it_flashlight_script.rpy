label first_flashlight_use:
    $ inventory_show = False
    scene white with dissolve
    $ dark_environ = False
    $ flashlight_use = True
    pause 1.0
    scene taisho_1f_study_bare
    show flash_circle:
        xalign 0.5 yalign 0.5
    with Reveal3
    pause 1.0
    sh smile sweat "Aaaah...{w=0.5} I feel a little better already."
    sh neutral -sweat "Now let's try and look around for more clues...{w=0.5} There's no telling when the battery is going to run out."
    play sound "audio/sfx/gui_hint.ogg"
    $ stat1_show = True
    pause 2.5
    scene black
    $ flashlight_consume = True
    $ story_progress = 1
    $ inventory_show = True
    call screen taisho_1f_study_explore_02