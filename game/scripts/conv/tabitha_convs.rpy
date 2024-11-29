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