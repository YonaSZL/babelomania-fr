#Conversation Screens with Tabitha

#Convo 01
default tabitha_01_scenario = False #Do you know what's going on?
default tabitha_01_gaspard = False #Why did you kill Gaspard?!
default tabitha_01_rules = False #You don't have the three rules?!
default tabitha_01_directive = False #You have the directive to protect me?!
default tabitha_conv_01 = 0

screen tabitha_conv_01:
    add "gui/talkie/bottom.png" yalign 1.0

    if tabitha_conv_01 == 4:
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
                    text _("Our Situation")
                    at btn_slide
                    if tabitha_01_scenario:
                        background "gui/talkie/button.png"
                    else:
                        background "gui/talkie/button_empty.png"
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("tabitha_01_scenario")
                button:
                    text _("Gaspard...")
                    at btn_slide
                    if tabitha_01_gaspard:
                        background "gui/talkie/button.png"
                    else:
                        background "gui/talkie/button_empty.png"
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("tabitha_01_gaspard")
                if tabitha_01_gaspard:
                    button:
                        text _("Tabitha's Programming")
                        at btn_slide
                        if tabitha_01_rules:
                            background "gui/talkie/button.png"
                        else:
                            background "gui/talkie/button_empty.png"
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                        action Jump("tabitha_01_rules")
                if tabitha_01_rules:
                    button:
                        text _("Tabitha's Directives")
                        at btn_slide
                        if tabitha_01_directive:
                            background "gui/talkie/button.png"
                        else:
                            background "gui/talkie/button_empty.png"
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                        action Jump("tabitha_01_directive")


        ####Indicator if viewport is scrollable
        button:
            xysize(65,65) xalign 1.0 xoffset -400
            add "gui/talkie/scroll_bg.png"
            add "gui/talkie/scroll_arrow.png" at arrow_down

label tabitha_01_scenario:
    $ renpy.block_rollback()
    pause 0.5
    sh c_half frown "You were at the reception...{w=0.5} Or at least in the same building as we were, the Baroque building.{w=0.3} Correct?"
    ta nulla "Affirmative.{w=0.3} Afterwards, the Professor desired to observe the ceremony from the upper floors for a time."
    sh surprise "He...{w=0.5} What?{w=0.3} Why would he want to do that?"
    show Tabitha bow
    ta nulla "That information is not in my possession.{w=0.3} The Professor rarely shares his inner world with others."
    sh frown "Well...{w=0.5} If you had to guess?"
    show Tabitha surprise
    ta nulla "I do not possess sufficient data to create a predictive model with an accuracy higher than 67%, [sh_n].{w=0.3} Would it be acceptable?"
    sh surprise "I...{w=0.5} Yeah?"
    show Tabitha neutral
    ta nulla "Acknowledged.{w=0.5} Considering the data about Professor Habiki's behavioral patterns, and cross-checking it with his recent actions:{w=0.15} he is what is commonly referred to as a 'people watcher'."
    show Tabitha bow
    ta nulla "He is in the habit of trying to observe individuals of interest hidden, as to not influence their actions with his presence.{w=0.3} I posit that it was yet another occurrence of this quirk of his."
    sh neutral "Hm.{w=0.3} Sounds like a pretty solid analsys to me...{w=0.5} Why is the accuracy in the mid-ranges, then?"
    show Tabitha neutral
    ta nulla "Unfortunately, I am unable to correctly gauge who, among the attendees, was the object of his curiosity.{w=0.3} He made sure, in the days leading up to the event, to familiarize himself with the list of invitees, but he never betrayed any interest one way or the other."
    show Tabitha surprise with with dissolve
    ta nulla "With {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}one exception{/b}...{w=0.5} You, [sh_n]."
    sh surprise "Me...?"
    show Tabitha smile
    ta nulla "Affirmative.{w=0.3} He was, as the saying goes, tickled pink when interacting with you.{w=0.3} Your brief exchange left him quite amused."
    show Tabitha neutral
    ta nulla "It only amounts to correlation but there is a possibility that you may have joined the list of individuals to observe, despite his presence having been revealed to you."
    sh frown ".{w=0.3}.{w=0.3}.{w=0.5}which leaves us with nothing to go on, in the end.{w=0.5} Anyway."
    sh neutral "So you followed him to the upper floor.{w=0.3} What transpired afterwards?"
    pause 1.5
    show Tabitha surprise with dissolve
    
    pause 1.0
    if tabitha_01_scenario == False:
        $ tabitha_01_scenario = True
        $ tabitha_conv_01 += 1
    call screen tabitha_conv_01

label tabitha_01_gaspard:
    $ renpy.block_rollback()
    pause 0.5
    
    pause 1.0
    if tabitha_01_gaspard == False:
        $ tabitha_01_gaspard = True
        $ tabitha_conv_01 += 1
    call screen tabitha_conv_01

label tabitha_01_rules:
    $ renpy.block_rollback()
    pause 0.5
    
    pause 1.0
    if tabitha_01_rules == False:
        $ tabitha_01_rules = True
        $ tabitha_conv_01 += 1
    call screen tabitha_conv_01

label tabitha_01_directive:
    $ renpy.block_rollback()
    pause 0.5
    
    pause 1.0
    if tabitha_01_directive == False:
        $ tabitha_01_directive = True
        $ tabitha_conv_01 += 1
    call screen tabitha_conv_01