default bathroom_painting_examine = 0
default exm_taisho_1f_study_01_subject = False
default exm_taisho_1f_study_01_title = False
default exm_taisho_1f_study_01_signature = False

screen taisho_1f_study_examine_01():
    imagemap:
        ground "images/cgs/chapter_00/bathroom_painting.jpg"
        hover "images/cgs/chapter_00/bathroom_painting.jpg"

        hotspot (460, 0, 1460, 825) action Jump("exm_taisho_1f_study_01_subject") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Painting Subject")#SUBJECT
        hotspot (533, 980, 856, 100) action Jump("exm_taisho_1f_study_01_title") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Frame")#TITLE
        hotspot (0, 0, 300, 130) action Jump("exm_taisho_1f_study_01_signature") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Handwriting")#SIGNATURE
        if taisho_1f_study_examine_01 == 3:
            hotspot (1645, 922, 275, 158) action Jump("exm_taisho_1f_study_01_return") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Return")#RETURN
    
    $ tooltip = GetTooltip()

    nearrect:
        focus "tooltip"
        prefer_top True

        frame:
            xalign 0.5
            text "[tooltip]"

label exm_taisho_1f_study_01_subject:
    $ renpy.block_rollback()
    pause 0.5
    sh_i frown "(A city tall enough to reach the sky and beyond, built in a spiral like pattern.{w=0.3} Rivers of blood rivulet off it, making a desolate landscape even more derelict...)"
    sh_i surprise "(This must be...{w=0.5} A reinterpretation of the {nw}"
    play sound "audio/sfx/gui_hint.ogg"
    extend "{b}Tower of Babel{/b}, right?{w=0.5} I've never seen one quite like this.)"
    sh_i neutral "(The ones I'm familiar with are usually...{w=0.5} Nicer.{w=0.3} They feature the tower and the community that grew up around it, or they showcase it while it's being built...)"
    sh_i frown "(This feels more like a depiction of what came after the big G went all old testament on it...{w=0.5} Although that doesn't explain the rivers of blood.)"
    sh_i surprise "(.{w=0.3}.{w=0.3}.{w=0.5}or maybe it does?)"
    pause 1.0
    if exm_taisho_1f_study_01_subject == False:
        $ exm_taisho_1f_study_01_subject = True
        $ bathroom_painting_examine += 1
    call screen bathroom_painting_examine

label exm_taisho_1f_study_01_title:
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(Doesn't feel like the original frame of the painting...{w=0.5} There's a plaque at the bottom.)"
    play sound "audio/sfx/gui_hint.ogg"
    sh_i frown "({b}'The Festering Wound'{/b}...{w=0.5} Geez, talk about resentment.)"
    sh_i amused "(Whoever made this was either {i}very{/i} religious, or not at all...{w=0.5} Or maybe both at different points in their life.)"
    sh_i surprise "(I wonder, though...{w=0.5} Was the painter resenting God himself, or is the whole thing just a metaphor?{w=0.3} Not a question you can answer without knowing the author.)"
    pause 1.0
    if exm_taisho_1f_study_01_title == False:
        $ exm_taisho_1f_study_01_title = True
        $ bathroom_painting_examine += 1
    call screen bathroom_painting_examine

label exm_taisho_1f_study_01_signature:
    $ renpy.block_rollback()
    pause 0.5
    sh_i surprise "(Huh...{w=0.5} That spot on the canvas is {nw}"
    play sound "audio/sfx/gui_hint.ogg"
    extend "{b}ruined{/b}.)"
    sh_i frown "(Is that where the signature of the author was?{w=0.5} It's all blurred and ruined, I can barely make out half of the date...)"
    sh_i neutral "(19...{w=0.5} Well, at least I know it was made in the previou century, so that's something...?)"
    pause 1.0
    if exm_taisho_1f_study_01_signature == False:
        $ exm_taisho_1f_study_01_signature = True
        $ bathroom_painting_examine += 1
    call screen bathroom_painting_examine

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
            call screen bathroom_painting_examine