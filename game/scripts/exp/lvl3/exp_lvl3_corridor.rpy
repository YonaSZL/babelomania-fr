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
    pause 1.0
    scene lvl3_corridor with dissolve
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
    de shock "<...!{w=0.3} SERIOUSLY?!>"
    play sound2 "audio/se/door_elevator.ogg"
    pause 0.5
    scene elevator_closed with Reveal
    pause 1.5
    de shock "<It cannot be...{w=0.5} It cannot be that easy!{w=0.3} None of this makes sense!>"
    pause 0.5
    show Delphine shock at de_med:
        xalign 0.5
    with dissolve
    de nulla "<I feel like I'm in a fever dream...{w=0.5} Maybe I am?{w=0.3} Am I still asleep?>"
    pause 1.0
    show Delphine frown
    de nulla "<Ugh, get real, Delphine.{w=0.3} No dream or nightmare of yours would ever contain Perrier.>"
    show Delphine neutral
    de nulla "<There's something else going on, obviously...{w=0.5} Something weird.{w=0.3} And even though you can freely access this elevator...>"
    pause 0.5
    scene elevator_panel with Reveal
    pause 0.5
    de neutral "<You're still missing the keys to the executive toilets.>"
    de_i neutral "(Literally, maybe...{w=0.5} There's a panel which I assume serves for scanning {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}keycards{/b}...{w=0.5} And one single floor, instead, necessitates a physical key.)"
    de_i frown "(A signel P...{w=0.5} Parking, maybe?{w=0.3} The other floor names, though...{w=0.5} Lab, security, archive...)"
    de_i surprise "(I'm...{w=0.5} Wait, so this is some kind of {nw})"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}research facility{/b}?)"
    pause 1.5
    de_i frown sweat "(This is getting creepier and creepier...{w=0.5} Anyway.)"
    play sound "audio/se/elevator_button.ogg"
    de_i neutral "(As I thought, without a keycard, this elevator is dead.{w=0.3} I need to find one.)"
    de_i frown "(Except, the area seems completely bereft of people who may be carrying one...{w=0.5} And even then, am I really sure I want to run into one?)"
    pause 1.0
    play sound2 "audio/se/door_elevator.ogg"
    scene lvl3_corridor with dissolve
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