#Conversation Screens with Gaspard
#HEC Paris
#Sorbonne

default gaspard_conv_01 = 0
default gaspard_01_gaspard = False
default gaspard_01_shigeo = False
default gaspard_01_wedding = False

screen gaspard_conv_01:
    add "gui/talkie/bottom.png" yalign 1.0

    if gaspard_conv_01 == 3:
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
                    if gaspard_01_gaspard:
                        background "gui/talkie/button.png"
                    else:
                        background "gui/talkie/button_empty.png"
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("gaspard_01_gaspard")

                if gaspard_01_gaspard:
                    button:
                        text _("The Wedding")
                        at btn_slide
                        if gaspard_01_wedding:
                            background "gui/talkie/button.png"
                        else:
                            background "gui/talkie/button_empty.png"
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                        action Jump("gaspard_01_wedding")

                if gaspard_01_wedding:
                    button:
                        text _("Shigeo")
                        at btn_slide
                        if gaspard_01_shigeo:
                            background "gui/talkie/button.png"
                        else:
                            background "gui/talkie/button_empty.png"
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                        action Jump("gaspard_01_shigeo")


        ####Indicator if viewport is scrollable
        button:
            xysize(65,65) xalign 1.0 xoffset -400
            add "gui/talkie/scroll_bg.png"
            add "gui/talkie/scroll_arrow.png" at arrow_down

label gaspard_01_gaspard:
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
    ga nulla "<A few times...{w=0.5} Although this is the first time I will have to stay the night in the Taishō building.>"
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
    if gaspard_01_gaspard == False:
        $ gaspard_01_gaspard = True
        $ gaspard_conv_01 += 1
    call screen gaspard_conv_01

label gaspard_01_wedding:
    $ renpy.block_rollback()
    pause 0.5
    sh neutral "You said that your family and Delphine's are...{w=0.5} Tight, I guess?"
    ga nulla "More or less.{w=0.3} We took a number of vacations together over the years, but our fathers are closer than me and her ever became."
    show Gaspard laugh
    ga nulla "Much to their disappointment, from what I could surmise.{w=0.3} Although, that pales in comparison to what I heard when Delphine got engaged."
    sh surprise "Oh...{w=0.5} They weren't supportive?"
    show Gaspard neutral
    ga nulla "They were once they ran out of justifications...{w=0.5} Francesco graduated top of his class, is a successful researcher and more than self-sufficient."
    show Gaspard laugh
    ga nulla "When they started talking about using his lack of living relatives and any ties to his old life before coming to France as arguments, I made them respectfully notice they were grasping at straws."
    show Gaspard neutral
    ga nulla "They could either come out and say that they didn't want Delphine to marry a non-legacy person or shut up and give them their blessing.{w=0.3} Maybe hope for a quick divorce."
    sh surprise "Huh...{w=0.5} I guess those kinds of dynamics are still a thing in certain circles, aren't they?"
    show Gaspard laugh
    ga nulla "You have no idea...{w=0.5} Not my thing, to be completely honest."
    show Gaspard neutral
    ga nulla "I find most women in my same...{w=0.5} How do you say it?{w=0.3} Bracket?{w=0.3} Most women in my same bracket of life are quite uninteresting to me."
    sh smile "I see what you mean.{w=0.3} I guess when you know nothing else your entire life, it can become quite unstimulating."
    ga nulla "Yeah, that too.{w=0.3} Glad you understand."
    sh_i surprise "(That {i}too{/i}?{w=0.3} Meaning that's not the main reason why...?{w=0.5} Hm.)"
    pause 1.0
    if gaspard_01_wedding == False:
        $ gaspard_01_wedding = True
        $ gaspard_conv_01 += 1
    call screen gaspard_conv_01

label gaspard_01_shigeo:
    $ renpy.block_rollback()
    pause 0.5
    ga nulla "So how do you exactly know Francesco, if I may?"
    sh smile "Oh, me and him go way back."
    ga nulla "Hmm...{w=0.5} From his Bachelor, then.{w=0.3} Another biochemist?"
    sh surprise "Hm?{w=0.5} No, sorry, I wasn't being clear.{w=0.3} I mean that I know Francesco from childhood."
    pause 0.5
    show Gaspard surprise
    ga nulla "Childhood...?{w=0.5} Not college?"
    sh smile "Hah, no.{w=0.3} B2 level of French, remember?{w=0.3} I've never even been to Paris, let alone studied there."
    ga nulla "So...{w=0.5} You don't know anyone from his current circle?{w=0.3} His current life?"
    sh neutral "Not really, no.{w=0.3} You're literally the person I know the most about at this reception...{w=0.5} That should tell you everything you need to know."
    pause 1.0
    show Gaspard laugh with dissolve
    pause 0.5
    ga nulla "Heh...{w=0.5} Heheheh.{w=0.5} I see."
    play sound "audio/em/em_question.ogg"
    show screen emote("question",0.17,0.5)
    sh surprise "Hmm?{w=0.5} What do you mean?"
    ga nulla "Nothing, nothing...{w=0.5} I just thought you were someone from the extended circle, that's all."
    show Gaspard neutral
    ga nulla "So you've never met Delphine, either?"
    sh neutral "No.{w=0.3} When he left Italy after high school we tried to keep in touch but we drifted apart more and more over the years...{w=0.5} I didn't even know he had gotten married, before I got the invite for the religious ceremony."
    ga nulla "Understandable...{w=0.5} Well, our meeting was quite fortuitous, then.{w=0.3} I know pretty much everyone here, and everything about everyone."
    show Gaspard laugh
    ga nulla "Stick with me, and I will have you up to date with Francesco's life by sunrise."
    sh laugh "Hah!{w=0.3} I'll hold you to that, then!"
    sh_i laugh "(Well, what do you know?{w=0.3} That weird bathroom encounter turned out fruitful, after all.)"
    pause 1.0
    if gaspard_01_shigeo == False:
        $ gaspard_01_shigeo = True
        $ gaspard_conv_01 += 1
    call screen gaspard_conv_01