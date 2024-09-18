default taisho_1f_study_examine_01 = 0
default exm_taisho_1f_study_01_couch = False
default exm_taisho_1f_study_01_title = False
default exm_taisho_1f_study_01_signature = False

screen taisho_1f_study_examine_01():
    imagemap:
        ground "taisho_1f_study"
        hover "taisho_1f_study"
        
        hotspot (460, 0, 1460, 825) action Jump("exm_taisho_1f_study_01_couch") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Darkness")#COUCH
        if exm_taisho_1f_study_01_couch:
            hotspot (533, 980, 856, 100) action Jump("exm_taisho_1f_study_01_title") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Darkness")#TITLE
            hotspot (0, 0, 300, 130) action Jump("exm_taisho_1f_study_01_signature") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Darkness")#SIGNATURE
            if taisho_1f_study_examine_01 == 3:
                hotspot (1645, 922, 275, 158) action Jump("exm_taisho_1f_study_01_return") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Darkness")#FLASHLIGHT
    
    $ tooltip = GetTooltip()

    nearrect:
        focus "tooltip"
        prefer_top True

        frame:
            xalign 0.5
            text "[tooltip]"

label exm_taisho_1f_study_01_couch:
    $ renpy.block_rollback()
    pause 0.5
    if exm_taisho_1f_study_01_couch == False:
        sh_i surprise sweat "(It's so dark...{w=0.5} I can barely see anything.)"
        sh_i neutral "(This...{w=0.5} Is a couch, and a table in front of it...{w=0.5} This isn't the reception or any other room I've seen.{w=0.3} What...?)"
        sh_i surprise "(What happened?{w=0.3} Last thing I remember was Francesco talking about a wedding video and...{w=0.5} And then...?)"
        pause 1.5
        play sound "audio/se/clothes_rustle.ogg"
        sh_i frown "(What time is it...?{w=0.5} And I need some light, I need to...)"
        pause 1.5
        sh surprise "My...{w=0.5} My phone?"
        play sound "audio/em/em_shock.ogg"
        show screen emote("surprise",0.17,0.5)
        sh shock "My phone is {nw}"
        play sound "audio/sfx/gui_spook.ogg"
        extend "{b}gone?!{/b}"
        play music "audio/bgm/shadows_breathe.ogg"
    pause 1.0
    if exm_taisho_1f_study_01_couch == False:
        $ exm_taisho_1f_study_01_couch = True
        $ taisho_1f_study_examine_01 += 1
    call screen taisho_1f_study_examine_01

label exm_taisho_1f_study_01_title:
    $ renpy.block_rollback()
    pause 0.5
    
    pause 1.0
    if exm_taisho_1f_study_01_title == False:
        $ exm_taisho_1f_study_01_title = True
        $ taisho_1f_study_examine_01 += 1
    call screen taisho_1f_study_examine_01

label exm_taisho_1f_study_01_signature:
    $ renpy.block_rollback()
    pause 0.5
    
    pause 1.0
    if exm_taisho_1f_study_01_signature == False:
        $ exm_taisho_1f_study_01_signature = True
        $ taisho_1f_study_examine_01 += 1
    call screen taisho_1f_study_examine_01

label exm_taisho_1f_study_01_return:
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(That seems to be everything I can surmise from this painting...{w=0.5} Too bad about the ruined signature of the author, I'd like to know more about them.)"
    sh_i smile "(I should take a picture.{w=0.3} I can reverse-image search it later, or show someone back home.)"
    menu:
        sh_i neutral "(Should I take that picture now?)"

        "Let's take that picture.":
            $ renpy.block_rollback()
            pause 1.0
            play sound "audio/sfx/gui_phone_unlock.ogg"
            call screen photo("bathroom_painting", True, "story_00_bathroom_return")
        
        "I want to observe it more.":
            call screen taisho_1f_study_examine_01