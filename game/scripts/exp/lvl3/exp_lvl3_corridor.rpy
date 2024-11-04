default lvl3_corridor_explore_01 = 0
default exp_lvl3_corridor_01_doors = False
default exp_lvl3_corridor_01_elevators = False
default exp_lvl3_corridor_01_meeting = False

screen lvl3_corridor_explore_01():

    tag exploration

    button:
        pos(993,454)
        xysize(128,297)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_lvl3_corridor_01_doors")
        tooltip _("Doors")

    if exp_lvl3_corridor_01_bed:
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_lvl3_corridor_01_elevators")
            tooltip _("Elevators")
    
    if exp_lvl3_corridor_01_fridge:
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_lvl3_corridor_01_meeting")
            tooltip _("Meeting")

label exp_lvl3_corridor_01_doors:
    $ renpy.block_rollback()
    pause 0.5
    
    if exp_lvl3_corridor_01_doors == False:
        $ exp_lvl3_corridor_01_doors = True
        $ lvl3_corridor_explore_01 += 1
    pause 1.0
    call screen lvl3_wellness_explore_01