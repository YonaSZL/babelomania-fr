#Conversation Screens with Habiki

default habiki_01_habiki = False
default habiki_01_tabitha = False
default habiki_01_wedding = False
default habiki_conv_01 = 0

screen habiki_conv_01:
    add "gui/talkie/bottom.png" yalign 1.0

    if habiki_conv_01 == 3:
        textbutton "Return" action Jump("story_00_meet_gaspard") align(1.0, 1.0) offset(-60,-10) text_size 60 hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"

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
                    text "Professor Habiki"
                    at btn_slide

                    ## you can put a simple variable/renpy.seen_label here to determine which bg is shown
                    ## button.png -> with the X
                    ## button_empty.png -> without X
                    if habiki_01_habiki:
                        background "gui/talkie/button.png"
                    else:
                        background "gui/talkie/button_empty.png"
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("habiki_01_habiki")


                button:
                    text "The Android"
                    at btn_slide
                    if habiki_01_tabitha:
                        background "gui/talkie/button.png"
                    else:
                        background "gui/talkie/button_empty.png"
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("habiki_01_tabitha")


                button:
                    text "The Wedding"
                    at btn_slide
                    if habiki_01_wedding:
                        background "gui/talkie/button.png"
                    else:
                        background "gui/talkie/button_empty.png"
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("habiki_01_wedding")


        ####Indicator if viewport is scrollable
        button:
            xysize(65,65) xalign 1.0 xoffset -400
            add "gui/talkie/scroll_bg.png"
            add "gui/talkie/scroll_arrow.png" at arrow_down

label habiki_01_habiki:
    $ renpy.block_rollback()
    pause 0.5
    sh neutral "Habiki...{w=0.5} So I can call you by your first name?"
    ha nulla "As long as you remember to add 'professor'."
    sh surprise "Hm...{w=0.5} Bit odd, not going to lie."
    pause 0.5
    show Habiki smile
    ha nulla "And why would you say that?"
    sh neutral "You stress the necessity of a honorific, which means you give importance to social etiquette...{w=0.5} Or at least, to your title."
    sh frown "It's a way to put some kind of distance between you and your interlocutor, and yet you give a stranger your first name instead of your family name.{w=0.3} Kind of contradictory, wouldn't you say?"
    ha nulla ".{w=0.3}.{w=0.3}.{w=0.5}indeed.{w=0.3} You're well steeped in our culture, I see."
    show Habiki neutral
    ha nulla "There's, though, a very logical explanation...{w=0.5} My Tabitha, here, is many things to me.{w=0.3} One of her primary functions is being my bodyguard."
    show Tabitha bow
    ha nulla "With that in mind, is it really odd that someone needing a two meters tall robotic bodyguard would be quite judicious, when it came to handing out his last name?"
    sh smile ".{w=0.3}.{w=0.3}.{w=0.5}fair enough.{w=0.5} But considering the century we live in, you mean to tell me I won't find that out just by looking up 'japanese professor with android' on a search engine?"
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
    if habiki_01_habiki == False:
        $ habiki_01_habiki = True
        $ habiki_conv_01 += 1
    call screen habiki_conv_01

label habiki_01_tabitha:
    $ renpy.block_rollback()
    pause 0.5
    sh frown ".{w=0.3}.{w=0.3}.{w=0.5}Tabitha...{w=0.5} Why did you give it a human name?"
    ha nulla "I feel a certain animosity, Shigeo-kun.{w=0.3} I assure you that Tabitha didn't mean you no harm."
    sh frown "Gave me quite the fright, that's for sure...{w=0.5} All I wanted to do was close the door to the smoking room properly."
    show Habiki laugh
    ha nulla "Not a fan of smoking either, I assume.{w=0.3} An awful vice to have, I agree."
    show Habiki smile
    ha nulla "But the drive to the château was quite long and tiring...{w=0.5} Hence the need to indulge.{w=0.3} But I fear that I could not persuade Tabitha to fully close the door."
    pause 1.0
    show Tabitha bow with dissolve
    pause 0.5
    sh surprise "You could not...{w=0.5} Persuade your Android?"
    show Habiki neutral
    ha_x nulla "Oh, if I really wanted I could've ordered her to...{w=0.5} But I find that going against actions dictated by her prime directives is quite disruptive."
    sh frown "Disruptive to...{w=0.5} What, exactly?"
    pause 1.0
    show Habiki smile with dissolve
    ha nulla "That, Shigeo-kun...{w=0.5} Is private."
    sh frown ".{w=0.3}.{w=0.3}.{w=0.5}fine.{w=0.3} As long as you can actually control it."
    show Habiki laugh
    ha nulla "Hahaha, why wouldn't I?!"
    sh_i frown "(I don't know, you tell me, professor 'I couldn't persuade'.)"
    pause 0.5
    show Tabitha neutral with dissolve
    pause 1.0
    if habiki_01_tabitha == False:
        $ habiki_01_tabitha = True
        $ habiki_conv_01 += 1
    call screen habiki_conv_01

label habiki_01_wedding:
    $ renpy.block_rollback()
    pause 0.5
    if not habiki_01_tabitha:
        sh surprise "Don't think I've seen you at the ceremony, nor the reception so far.{w=0.3} I would remember an elderly academic shadowed by a two meters tall android."
        show Habiki laugh
        ha nulla "Oh, you would be surprised...{w=0.5} But indeed, we've but recently arrived."
    else:
        sh surprise "If you've only recently arrived, that's why I haven't seen you at the ceremony or the reception.{w=0.3} I would remember an elderly academic shadowed by a two meters tall android."
        show Habiki laugh
        ha nulla "Oh, you would be surprised...{w=0.5} But indeed, we haven't had the opportunity to greet the bride and groom yet, truth tell."
    show Habiki neutral
    ha nulla "I was supposed to arrive earlier but bad weather delayed my flight...{w=0.5} I hope young Francesco didn't take offense with it."
    sh surprise "Francesco...{w=0.5} So you're with the groom's party."
    show Habiki smile
    ha nulla "Indeed.{w=0.3} And so do you, I believe."
    show Tabitha bow
    sh neutral "Well, yes, but...{w=0.5} How can you tell?"
    show Habiki laugh
    ha nulla "Are you kidding me?{w=0.3} Delphine's family and <coterie> wouldn't be caught dead in an outfit that cheap."
    sh surprise sweat "Ch-!{w=0.3} This suit cost me 800 Euros!{w=0.3} I had to save for it!"
    show Habiki smile
    ha nulla "And the ones I've seen them wear at similar occasions range in the tens of thousands.{w=0.3} Like many things in this world, Shigeo-kun, cheapness is a...{w=0.5} Relative concept."
    pause 1.5
    sh frown -sweat "How do you know them, anyway?"
    ha nulla "Young Francesco was my pupil.{w=0.3} One of the finest students I've ever had the honour of teaching...{w=0.5} And you?"
    sh neutral ".{w=0.3}.{w=0.3}.{w=0.5}Francesco is my childhood friend.{w=0.3} We grew up together."
    pause 1.0
    show Habiki surprise with dissolve
    pause 0.5
    ha nulla "Indeed?{w=0.5} Hmm."
    sh surprise "Huh?{w=0.5} Something wrong?"
    show Habiki frown
    ha nulla ".{w=0.3}.{w=0.3}.{w=0.5}not exactly wrong, just...{w=1.0} Nevermind."
    show Habiki neutral
    ha nulla "Nothing of importance.{w=0.3} You're just the first person I meet from Francesco's life from before college."
    sh surprise "Oh...{w=0.5} Yeah, to be honest, his invite was a surprise.{w=0.3} I didn't even know he had gotten married."
    ha nulla "I see...{w=0.5} Well, no time like the present to reconnect, don't you think?"
    show Habiki smile
    show Tabitha neutral
    ha nulla "Granted, you'll have to fight tooth and nail for some one-on-one time with him, tonight...{w=0.5} Don't know if you'll have it in you."
    sh sad "Yeah, I noticed a tendency on the bride's family's behalf to monopolize the happy couple."
    show Habiki neutral
    ha nulla "As foreseen.{w=0.3} No worries, though, Shigeo-kun.{w=0.3} I have ways to break the status quo."
    sh smile "You do?{w=0.3} Please do, then."
    pause 1.0
    if habiki_01_wedding == False:
        $ habiki_01_wedding = True
        $ habiki_conv_01 += 1
    call screen habiki_conv_01