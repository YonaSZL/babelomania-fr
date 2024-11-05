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
    de_i surprise "(Those are some...{w=0.5} Impressively heavy duty doors.{w=0.3} What the shit?)"
    pause 0.5
    show Delphine surprise at de_med:
        xalign 0.5
    with dissolve
    pause 0.5
    play sound "audio/se/thud_metal.ogg"
    queue sound "audio/se/thud_metal.ogg"
    pause 0.5
    de_i nulla "(And the walls, too...{w=0.5} It's like the bulkheads on ships or submarines.)"
    show Delphine smile
    de_i nulla "(Salaries must be {i}terrible{/i} around here...{w=0.5} And the corporate gym quite good.{w=0.3} But, seriously.)"
    show Delphine surprise
    de_i nulla "(Unless I was asleep for two days, I am most certainly am not at sea.{w=0.3} Also, my stomach would violently revolt like that time in Tonga.)"
    show Delphine frown
    de_i nulla "(So what kind of business needs this kind of door?{w=0.3} They're only good for two things, keeping stuff out and keeping stuff in...{w=0.5} And if it's not water.)"
    show Delphine neutral
    play sound4 "audio/sfx/gui_spook.ogg"
    de_i nulla "({b}What exactly{/b} are these in place for?)"
    pause 1.5
    show Delphine frown
    de nulla "<.{w=0.3}.{w=0.3}.{w=0.5}either way, it hasn't automatically opened at my passage.{w=0.3} Like an alloy boor.>"
    show Delphine neutral
    de nulla "<I don't see a keyhole or anything like that...{w=0.5} What am I missing?>"
    if exp_lvl3_corridor_01_doors == False:
        $ exp_lvl3_corridor_01_doors = True
        $ lvl3_corridor_explore_01 += 1
    pause 1.0
    call screen lvl3_wellness_explore_01

label exp_lvl3_corridor_01_elevators:
    $ renpy.block_rollback()
    pause 0.5
    de_i neutral "(A set of three elevators...{w=0.5} And a bigger single one on the other side of the corridor.)"
    de_i surprise "(I figure one is for people, the other for cargo...{w=0.5} Huh.)"
    de_i frown "(No floor buttons on the outside, just up and down...)"
    pause 1.0
    play sound2 "audio/se/button_elevator.ogg"
    pause 0.5
    play sound "audio/se/elevator_ding.ogg"
    pause 0.5
    play sound4 "audio/em/em_surprise.ogg"
    show screen emote("surprise",0.17,0.5)
    de_i shock "<...!{w=0.3} SERIOUSLY?!>"
    play sound2 "audio/se/door_elevator.ogg"
    pause 0.5
    scene elevator_closed
    if exp_lvl3_corridor_01_elevators == False:
        $ exp_lvl3_corridor_01_elevators = True
        $ lvl3_corridor_explore_01 += 1
    pause 1.0
    call screen lvl3_wellness_explore_01



label exp_lvl3_corridor_01_doors:
    $ renpy.block_rollback()
    pause 0.5
    de_i surprise "(These are...{w=0.5} Some impressively heavy duty doors.)"
    pause 0.5

    if exp_lvl3_corridor_01_doors == False:
        $ exp_lvl3_corridor_01_doors = True
        $ lvl3_corridor_explore_01 += 1
    pause 1.0
    call screen lvl3_wellness_explore_01