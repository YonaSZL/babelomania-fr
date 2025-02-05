default lvl3_corridor_explore_01 = 0
default exp_lvl3_corridor_01_doors = False
default exp_lvl3_corridor_01_elevators = False
default exp_lvl3_corridor_01_blood = False
default exp_lvl3_corridor_01_meeting_closed = False

#Add blood seeping under the door after going into the elevators
screen lvl3_corridor_explore_01():

    tag exploration

    button:
        pos(771,448)
        xysize(384,274)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_lvl3_corridor_01_doors")
        tooltip _("Doors")

    button:
        pos(0,258)
        xysize(340,735)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_lvl3_corridor_01_elevators")
        tooltip _("Elevators")
    
    if exp_lvl3_corridor_01_elevators:
        button:
            pos(853,706)
            xysize(139,55)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_lvl3_corridor_01_blood")
            if exp_lvl3_corridor_01_blood:
                tooltip _("Blood")
            else:
                tooltip _("?????")
    
    button:
        pos(1274,424)
        xysize(38,350)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_lvl3_corridor_01_meeting_closed")
        tooltip _("Meeting Room")

    if lvl3_corridor_explore_01 == 4:
        button:
            pos(574,424)
            xysize(38,350)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_lvl3_corridor_01_meeting_open")
            tooltip _("Meeting Room")

label exp_lvl3_corridor_01_doors:
    $ renpy.block_rollback()
    pause 0.5
    if exp_lvl3_corridor_01_blood == True:
        de_i frown sweat "(Blood...{w=0.5} How the heck do you get blood to seep through a door like that?!{w=0.3} What kind of research are they doing here?!)"
        de_i angry "(Or maybe...?{w=0.5} Oh my shit, I was only JOKING about employee revolts!)"
    else:
        de_i surprise "(Those are some...{w=0.5} Impressively heavy duty doors.{w=0.3} What the shit?)"
        pause 0.5
        show Delphine surprise at de_med:
            xalign 0.5
        with dissolve
        pause 1.0
        de_i nulla "(And the walls, too...{w=0.5} It's like the bulkheads on ships, or submarines.)"
        show Delphine smile
        de_i nulla "(Salaries must be {i}terrible{/i} around here...{w=0.5} And the corporate gym quite good.{w=0.3} But, seriously.)"
        show Delphine surprise
        de_i nulla "(Unless I was asleep for two days, I am most certainly not at sea.{w=0.3} My stomach would revolt quite violently.{w=0.3} Like that time in Tonga.)"
        show Delphine frown
        de_i nulla "(France or not, what kind of business needs this door on the {i}inside{/i}?{w=0.3} I doubt they have to worry about inundations, so if it's not water...)"
        show Delphine neutral
        play sound4 "audio/sfx/gui_spook.ogg"
        de_i nulla "({b}What exactly{/b} are these in place for?)"
        pause 1.5
        show Delphine frown with dissolve
        de nulla "<.{w=0.3}.{w=0.3}.{w=0.5}either way, it hasn't automatically opened at my presence.{w=0.3} And I bet its twin at the other end is a similar alloy boor.>"
        show Delphine neutral
        de nulla "<I don't see a keyhole or anything...{w=0.5} What am I missing?>"
        pause 1.0
        scene lvl3_corridor with dissolve
        if exp_lvl3_corridor_01_doors == False:
            $ exp_lvl3_corridor_01_doors = True
            $ lvl3_corridor_explore_01 += 1
    pause 1.0
    call screen lvl3_corridor_explore_01

label exp_lvl3_corridor_01_elevators:
    $ renpy.block_rollback()
    pause 0.5
    if exp_lvl3_corridor_01_blood == True:
        de_i angry sweat "(There's nothing I can do with this until I find a keycard or a key!)"
    else:
        de_i neutral "(A set of two standard elevators...{w=0.5} And a bigger single one on the other side of the corridor...{w=0.5} Huh.)"
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
        pause 1.0
        scene elevator_closed with Reveal
        pause 1.5
        de shock "<It cannot be...{w=0.5} It cannot be that easy!{w=0.3} None of this makes sense!>"
        pause 0.5
        show Delphine shock at de_med:
            xalign 0.5
        with dissolve
        de nulla "<I feel like I'm in a fever dream...{w=0.5} Maybe I am?{w=0.3} Am I still asleep?>"
        pause 1.0
        show Delphine disgust
        de nulla "<Ugh, get real, Delphine.{w=0.3} Not even your worst nightmare would contain {i}Berrier{/i}.>"
        show Delphine neutral
        de nulla "<There's something else going on, obviously...{w=0.5} Something weird.{w=0.3} And even though you can freely access this elevator...>"
        pause 0.5
        scene elevator_panel with Reveal
        pause 0.5
        de neutral "<You're still missing the keys to the executive toilets.{w=0.3} Maybe literally.>"
        de_i neutral "(There's a slit which I assume is for scanning {nw}"
        play sound4 "audio/sfx/gui_hint.ogg"
        extend "{b}keycards{/b}...{w=0.5} And one single floor which wants a physical key.)"
        de_i frown "('P'...{w=0.5} Parking, maybe?{w=0.3} The other floor names, though...{w=0.5} Lab, security, archive.)"
        de_i surprise "(Is this some kind of {nw}"
        play sound4 "audio/sfx/gui_spook.ogg"
        extend "{b}research facility{/b}?)"
        pause 1.5
        de_i frown sweat "(Uuuuugh, this is getting SO creepy...!{w=0.5} Anyway, that would explain the big elevator.{w=0.3} It's for cargo.)"
        play sound "audio/se/button_elevator.ogg"
        pause 2.0
        play sound4 "audio/se/button_elevator.ogg"
        pause 0.5
        play sound2 "audio/se/button_elevator.ogg"
        de_i neutral -sweat "(As I thought, without a keycard, the panel's dead.{w=0.3} I need to find one.)"
        de_i frown "(Except the immediate vicinity seems completely void of people who may be carrying some...{w=0.5} And taste.{w=0.3} Even then, do I really want to run into someone who works here?)"
        pause 1.0
        if exp_lvl3_corridor_01_elevators == False:
            $ exp_lvl3_corridor_01_elevators = True
            $ lvl3_corridor_explore_01 += 1
        play sound2 "audio/se/door_elevator.ogg"
        scene black with dissolve
    pause 1.0
    scene lvl3_corridor with dissolve
    pause 1.0
    call screen lvl3_corridor_explore_01

label exp_lvl3_corridor_01_blood:
    $ renpy.block_rollback()
    pause 0.5
    if exp_lvl3_corridor_01_blood == False:
        de_i neutral "(Hmmm...?{w=0.3} Something is seeping through the doors.)"
        de_i amused "(So much for heavy duty sealing.{w=0.3} Someone in budget has been skimming~)"
        pause 1.0
        stop music fadeout 3.5
        pause 1.5
        de surprise "<Wait.>"
        pause 1.
        show Delphine surprise at de_big:
            xalign 0.5
        with dissolve
        pause 0.5
        de nulla "<Wait...{w=0.5} Waitwaitwaitwait.>"
        show Delphine shock
        de nulla "{cps=10}Is...{w=0.5} Is that {nw}"
        play sound4 "audio/sfx/gui_spook.ogg"
        extend "{cps=10}{b}blood{/b}?!"
        play music "audio/bgm/shadows_whisper.ogg"
        pause 1.5
        show Delphine shock sweat with dissolve
        pause 0.5
        de nulla "<Blood...{w=0.5} Fresh smelling blood.{w=0.5} What...{w=0.5} What kind of research facility is this?{w=0.3} And why isn't the door dooring?!{w=0.3} This...!>"
        pause 1.5
        show Delphine frown
        de nulla "<I need to find an exit.{w=0.3} I need to find a damn keycard!{w=0.3} I need to get out of here!>"
        pause 1.0
        scene lvl3_corridor with dissolve
        if exp_lvl3_corridor_01_blood == False:
            $ exp_lvl3_corridor_01_blood = True
            $ lvl3_corridor_explore_01 += 1
    else:
        de_i shock sweat "(The more I look at it, the more gruesome images pop in my head!{w=0.5} This started out annoying, became creepy and now...)"
        de_i frown sweat "(And just when the most dangerous thing I have on me are high heels.)"
    pause 1.0
    call screen lvl3_corridor_explore_01

label exp_lvl3_corridor_01_meeting_closed:
    $ renpy.block_rollback()
    pause 0.5
    if exp_lvl3_corridor_01_blood:
        de_i frown sweat "(The elevators aren't working, the wellness room is fucking useless...!{w=0.5} Meeting room, then?!)"
        play sound3 "audio/se/doorknob_rattle.ogg"
        pause 1.0
        play sound3 "audio/se/doorknob_rattle.ogg"
        pause 0.3
        de_i angry "(Chort!{w=0.3} Of course.{w=0.3} Of course!)"
        play sound3 "audio/se/door_slam.ogg"
        show screen emote("surprise",0.15,0.5)
        de pain sweat "<UGH!{w=0.3} Shit, my hand...!>"
        play sound4 "audio/sfx/hp_down.ogg"
        $ stat3 -=5
        de_i frown sweat "(There must be something...{w=0.5} Something I can open around here...!!!)"
        if exp_lvl3_corridor_01_meeting_closed == False:
            $ exp_lvl3_corridor_01_meeting_closed = True
            $ lvl3_corridor_explore_01 += 1
    else:
        de_i neutral "(A corporate meeting room...{w=0.5} With a top-only obscuring glass wall.{w=0.3} You can't tell what's going on inside, but you can tell if people are using it.)"
        de_i frown "(This design is so effing creepy...{w=0.5} I keep thinking of one day looking down and seeing someone eyeballing people's ankles.{w=0.3} Eugh.)"
    pause 1.0
    call screen lvl3_corridor_explore_01

label exp_lvl3_corridor_01_meeting_open:
    $ renpy.block_rollback()
    pause 0.5
    de_i frown sweat "(Meeting room number two...!{w=0.3} Come on!)"
    play sound2 "audio/se/door_slide.ogg"
    pause 1.0
    de_i shock sweat "(Some luck, finally!{w=0.3} There better be a keycard in here!)"
    pause 1.0
    scene black with dissolve
    pause 1.0
    scene lvl3_meeting with Reveal
    pause 1.5
    de_i neutral sweat "(Alright...{w=0.5} Okay, there's plenty of spots to search through.{w=0.3} Let's calm down, Delphine.)"
    de_i frown sweat "(You're still in control, here.{w=0.3} If you managed to throw Gretchen a successful bridal shower, there's nothing you can't do.)"
    de_i neutral -sweat "(Do this methodically but swiftly.{w=0.3} Let's look around.)"
    pause 1.0
    call screen lvl3_meeting_examine_01
