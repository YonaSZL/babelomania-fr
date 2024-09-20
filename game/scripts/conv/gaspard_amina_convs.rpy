#Conversation Screens with Gaspard
#HEC Paris
#Sorbonne

default gaspmina_conv_01 = 0
default gaspmina_01_gaspard = False
default gaspmina_01_shigeo = False
default gaspmina_01_wedding = False

screen gaspmina_conv_01:
    add "gui/talkie/bottom.png" yalign 1.0

    if gaspmina_conv_01 == 3:
        textbutton _("Return") action Jump("story_00_meet_amina") align(1.0, 1.0) offset(-60,-10) text_size 60 hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"

    vbox:
        ypos 300 xpos -880 ##button positions

        ####Indicator if viewport is scrollable
        ####Scrollbar looked ugly
        button:
            xysize(65,65) xalign 1.0 xoffset -400
            add "gui/talkie/scroll_bg.png"
            add "gui/talkie/scroll_arrow.png" at arrow_up
            
        viewport:
            style_prefix "talkie"
            scrollbars "vertical" mousewheel True draggable True
            vbox:
                spacing 20
                button:
                    text _("Gaspard")
                    at btn_slide

                    ## you can put a simple variable/renpy.seen_label here to determine which bg is shown
                    ## button.png -> with the X
                    ## button_empty.png -> without X
                    if gaspmina_01_gaspard:
                        background "gui/talkie/button.png"
                    else:
                        background "gui/talkie/button_empty.png"
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("gaspmina_01_gaspard")

                if gaspmina_01_gaspard:
                    button:
                        text _("The Wedding")
                        at btn_slide
                        if gaspmina_01_wedding:
                            background "gui/talkie/button.png"
                        else:
                            background "gui/talkie/button_empty.png"
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                        action Jump("gaspmina_01_wedding")

                if gaspmina_01_wedding:
                    button:
                        text _("The Android")
                        at btn_slide
                        if gaspmina_01_shigeo:
                            background "gui/talkie/button.png"
                        else:
                            background "gui/talkie/button_empty.png"
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                        action Jump("gaspmina_01_shigeo")


        ####Indicator if viewport is scrollable
        button:
            xysize(65,65) xalign 1.0 xoffset -400
            add "gui/talkie/scroll_bg.png"
            add "gui/talkie/scroll_arrow.png" at arrow_down

label gaspmina_01_gaspard:
    $ renpy.block_rollback()
    pause 0.5
    ga nulla "<Since I haven't had the pleasure so far, I assume you are an invitee on the groom's side.>"
    sh neutral "<Exactly.{w=0.3} I'm an old friend of Francesco...{w=0.5} And how do you know Delphine?>"
    show Gaspard laugh
    ga nulla "<Oh, our families go way back...{w=0.5} When you deal in our kind of business, you end up always running in the same circles.>"
    show Gaspard neutral
    ga nulla "<We also went to the same business school.{w=0.3} We're not exactly close but, I wasn't about to rebuke a wedding invite.{w=0.3} Especially with Château de Bois-le-Dumont as a location.>"
    sh surprise "<It is a beautiful estate, from what I've seen...{w=0.5} You've visited here before?>"
    show Gaspard frown
    ga nulla "<A few times...{w=0.5} Although this is the first time I will have to stay the night in the Taisho building.>"
    sh neutral "<Is there a problem with that?>"
    ga nulla "<I'm not exactly a fan of the architectural style...{w=0.5} Totalitarian Japan aping the wonders of imperial Europe and producing patchworks without the strengths of either.>"
    show Gaspard neutral
    ga nulla "<They should've stuck with what they knew...{w=0.5} And not try being something they weren't.>"
    sh_i surprise "(Hmmm.{w=0.5} Is he talking about just the architecture or...?)"
    sh neutral "<South East Asia would have certainly been happier...{w=0.5} I must mention that my mother is Japanese.>"
    pause 1.0
    show Gaspard surprise
    ga nulla "<Huh...{w=0.5} I see.{w=0.3} Did you grow up in Japan?>"
    sh surprise "<Not exactly.{w=0.3} I've visited my mother's family a few times growing up, but then...{w=0.5} No, mostly in Italy, that's my father's country.>"
    ga nulla "<Half Italian, half Japanese?{w=0.3} And your French isn't half bad for a foreigner.>"
    show Gaspard neutral
    ga nulla "Although maybe you'd rather we speak English going forward?{w=0.3} I don't really mind."
    sh laugh sweatdrop "Hahaha, much obliged...{w=0.5} I've only been learning French for a couple years, I barely hit my B2."
    ga nulla "A commendable effort.{w=0.3} Keep it up."
    show Gaspard frown
    ga nulla "I would suggest speaking with more mother-tongue, though.{w=0.3} You're picking up some unbecoming phonetic habits."
    sh surprise -sweatdrop "Uhm...{w=0.5} I see.{w=0.3} I'll try my best."
    show Gaspard neutral
    sh_i surprise "(I have spent two months in Provence, though...?{w=0.3} I didn't think my pronunciation was that bad.{w=0.3} He's understanding everything I put down, anyway.)"
    pause 1.0
    if gaspmina_01_gaspard == False:
        $ gaspmina_01_gaspard = True
        $ gaspmina_conv_01 += 1
    call screen gaspmina_conv_01