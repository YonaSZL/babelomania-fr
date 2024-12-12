default exp_bar_corr_01 = 0
default exp_bar_corr_window = False
default exp_bar_corr_chapel = False
default exp_bar_corr_smoke = False
default exp_bar_corr_reception = False
default exp_bar_corr_up = False

screen exp_bar_corr():
    imagemap:
        ground "images/bgs/baroque/bar_corr_recep.jpg"
        hover "images/bgs/baroque/bar_corr_recep.jpg"

        hotspot (772, 229, 371, 526) action Jump("exp_bar_corr_chapel") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Chapel Doors")#CHAPEL
        hotspot (434, 399, 118, 297) action Jump("exp_bar_corr_window") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Courtyard Window")#WINDOW
        hotspot (163, 491, 140, 452) action Jump("exp_bar_corr_smoke") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Smoking Room")#SMOKE
        hotspot (1804, 205, 116, 788) action Jump("exp_bar_corr_reception") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Reception Area")#RECEPTION
        hotspot (1361, 461, 152, 115) action Jump("exp_bar_corr_up") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Stairs Up")#STAIRS UP
        if exp_bar_corr_01 == 5:
            hotspot (1361, 577, 152, 115) action Jump("exp_bar_corr_down") hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg" tooltip _("Stairs Down")#STAIRS DOWN
    
label exp_bar_corr_window:
    $ renpy.block_rollback()
    pause 0.5
    play sound "audio/se/doorknob_rattle.ogg"
    pause 0.5
    sh_i neutral "(The window frame is quite modern...{w=0.5} I guess the original one needed replacement.{w=0.3} It's the type that needs a special key to be opened, hm?)"
    sh_i frown "(I can barely see the inner courtyard through the tempered glass...)"
    play sound "audio/sfx/gui_hint.ogg"
    sh_i surprise "(Wait, {b}tempered glass{/b}?{w=0.5} Why would they need to have tempered glass windows, here?)"
    sh_i neutral "(Are they that worried about intruders?{w=0.3} I mean, it is kind of isolated but...)"
    sh_i frown "(Then again, they have been hosting some pretty exclusive events here over the years.{w=0.3} Celebrity weddings, launch parties, even political summits.)"
    sh_i smile "(If you want to present yourself as a fitting venue for those, the level of security would be a big selling point, wouldn't it?)"
    pause 1.0
    if exp_bar_corr_window == False:
        $ exp_bar_corr_window = True
        $ exp_bar_corr_01 += 1
    call screen exp_bar_corr

label exp_bar_corr_chapel:
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(Those heavy doors lead to the chapel...{w=0.5} This château is a pretty cool location, not going to lie.)"
    sh_i smile "(I can see why Francesco and his beau chose it.{w=0.3} It reminds me of a lot of our trips, when our families would go out of town together.)"
    sh_i sad "(It's heartbreaking his parents couldn't be here today...{w=0.5} They would've loved this place.)"
    sh_i neutral "(And while I don't know much about her yet...{w=0.5} I'm sure they would've loved {nw}"
    play sound "audio/sfx/gui_hint.ogg"
    extend "{b}Delphine{/b}, too.)"
    pause 1.0
    if exp_bar_corr_chapel == False:
        $ exp_bar_corr_chapel = True
        $ exp_bar_corr_01 += 1
    call screen exp_bar_corr

label exp_bar_corr_smoke:
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(The rest of the doors on the first floor...{w=0.5} The only one currently open is the {nw}"
    play sound "audio/sfx/gui_hint.ogg"
    extend "{b}Smoking Room{/b}, correct?)"
    sh_i frown "(Ugh, what an awful habit.{w=0.3} Wish they didn't encourage it like this.{w=0.3} If you're that much of an addict that you can't go two days without one, you shouldn't attend social functions.)"
    sh_i frown "(Then again, some just plain don't care about other people, don't they?{w=0.3} Reminds me of Belgium...{w=0.5} Can't believe they still don't have an outdoor smoke ban for bus and rail stations.)"
    pause 1.0
    if exp_bar_corr_smoke == False:
        $ exp_bar_corr_smoke = True
        $ exp_bar_corr_01 += 1
    call screen exp_bar_corr

label exp_bar_corr_reception:
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(I can still hear the background music.{w=0.3} The chatter of invitees, making merry.{w=0.3} The family of the bride, happily sharing a table with the newly weds.)"
    sh_i frown "(And the constant undercurrent of snide comments.{w=0.3} From what little Francesco told me when we last talked, it was always going to be a water and oil situation but...)"
    sh_i surprise "(Makes one wonder how the heck they even ended up meeting.{w=0.3} The guy I knew wouldn't be caught dead hanging out with some of the types at this wedding.)"
    sh_i sad "(Why did he invite me too, anyway?{w=0.5} He's obviously not wanting for friends.{w=0.3} And it's not like he's made time to try and reconnect.)"
    sh_i neutral "(Not that I can blame him, it is his wedding...{w=0.5} But even in an already divided group of people, I can't fit in either way.{w=0.3} It's like high school all over again.)"
    pause 1.0
    if exp_bar_corr_reception == False:
        $ exp_bar_corr_reception = True
        $ exp_bar_corr_01 += 1
    call screen exp_bar_corr

label exp_bar_corr_up:
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(Stairs leading to the upper floors, hm?{w=0.3} Wonder what kind of rooms are up there...{w=0.5} The reception room's dome reaches high enough, so I guess there must be a walkway?)"
    sh_i surprise "(Kind of creepy, if you think about it...{w=0.5} It's totally dark from what I saw, so someone could be looking in and no one would be the wiser.)"
    sh_i neutral "(None of my business, either way.{w=0.3} The bathrooms are downstairs.)"
    pause 1.0
    if exp_bar_corr_up == False:
        $ exp_bar_corr_up = True
        $ exp_bar_corr_01 += 1
    call screen exp_bar_corr

label exp_bar_corr_down:
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(There we are.{w=0.3} The stairs going down.)"
    menu:
        sh_i neutral "(Should I go?)"

        "Let's go.":
            jump story_00_bathroom_encounters
        "Actually...":
            pause 0.5
            call screen exp_bar_corr
