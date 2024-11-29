#Conversation Screens with Tabitha

#Convo 01
default tabitha_01_scenario = False #Do you know what's going on?
default tabitha_01_gaspard = False #Why did you kill Gaspard?!
default tabitha_01_rules = False #You don't have the three rules?!
default tabitha_01_directive = False #You have the directive to protect me?!
default tabitha_conv_01 = 0

screen tabitha_conv_01:
    add "gui/talkie/bottom.png" yalign 1.0

    if tabitha_conv_01 == 3:
        textbutton _("Return") action Jump("story_03_uneasy_trio") align(1.0, 1.0) offset(-60,-10) text_size 60 hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"

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
                    text _("Professor Habiki{#}")
                    at btn_slide

                    ## you can put a simple variable/renpy.seen_label here to determine which bg is shown
                    ## button.png -> with the X
                    ## button_empty.png -> without X
                    if tabitha_01_habiki:
                        background "gui/talkie/button.png"
                    else:
                        background "gui/talkie/button_empty.png"
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("tabitha_01_habiki")


                button:
                    text _("The Android")
                    at btn_slide
                    if tabitha_01_tabitha:
                        background "gui/talkie/button.png"
                    else:
                        background "gui/talkie/button_empty.png"
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("tabitha_01_tabitha")


                button:
                    text _("The Wedding{#}")
                    at btn_slide
                    if tabitha_01_wedding:
                        background "gui/talkie/button.png"
                    else:
                        background "gui/talkie/button_empty.png"
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("tabitha_01_wedding")


        ####Indicator if viewport is scrollable
        button:
            xysize(65,65) xalign 1.0 xoffset -400
            add "gui/talkie/scroll_bg.png"
            add "gui/talkie/scroll_arrow.png" at arrow_down

label tabitha_01_habiki:
    $ renpy.block_rollback()
    pause 0.5
    sh neutral "Habiki...{w=0.5} So I can call you by your first name?"
    ha nulla "As long as you remember to add 'professor'."
    sh surprise "Hm...{w=0.5} Bit odd, not going to lie."
    pause 0.5
    show Habiki smile
    ha nulla "And why would you say that?"
    sh neutral "You stress the necessity of an honorific, which means you give importance to social etiquette...{w=0.5} Or at least, to your title."
    sh frown "It's a way to put some kind of distance between you and your interlocutor, and yet you give a stranger your first name instead of your family name.{w=0.3} Kind of contradictory, wouldn't you say?"
    ha nulla ".{w=0.3}.{w=0.3}.{w=0.5}indeed.{w=0.3} You're well steeped in our culture, I see."
    show Habiki neutral
    ha nulla "There's, though, a very logical explanation...{w=0.5} My Tabitha, here, is many things to me.{w=0.3} One of her primary functions is being my bodyguard."
    show Tabitha bow
    ha nulla "With that in mind, is it really odd that someone needing a two meters tall robotic bodyguard would be quite judicious, when it came to handing out his last name?"
    sh smile ".{w=0.3}.{w=0.3}.{w=0.5}fair enough.{w=0.5} But considering the century we live in, you mean to tell me I won't find that out just by looking up 'Japanese professor with Android' on a search engine?"
    pause 1.5
    show Habiki smile with dissolve
    ha nulla "Quite."
    sh surprise "Quite...?{w=0.5} You mean, I won't?"
    show Habiki neutral
    show Tabitha neutral
    ha nulla "You won't."
    sh surprise "Uhm...{w=0.5} Okay, then?"
    sh_i surprise "(Is he serious...?{w=0.5} Granted, it's not the first instance I hear of someone commanding a complete information blackout on surface Internet.)"
    sh_i frown "(But the kind of power and influence you need to actually {i}obtain{/i} such a thing are...)"
    pause 1.0
    if tabitha_01_habiki == False:
        $ tabitha_01_habiki = True
        $ tabitha_conv_01 += 1
    call screen tabitha_conv_01