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
    de_i surprise "(These are...{w=0.5} Some impressively heavy duty doors.)"
    pause 0.5
    show Delphine surprise at de_med:
        xalign 0.5
    with dissolve
    pause 0.5
    play sound "audio/se/thud_metal.ogg"
    queue sound "audio/se/thud_metal.ogg"
    pause 0.5
    de_i nulla "(This is the kind of door I've only seen used in bulkheads on ships...{w=0.5} Or submarines.{w=0.3} Certainly not in any office building.)"
    show Delphine smile
    de_i nulla "(Goodness, the salaries must be {i}terrible{/i} around here...{w=0.5} And the workers quite the frequenters of the corporate gym.)"
    
    if exp_lvl3_corridor_01_doors == False:
        $ exp_lvl3_corridor_01_doors = True
        $ lvl3_corridor_explore_01 += 1
    pause 1.0
    call screen lvl3_wellness_explore_01