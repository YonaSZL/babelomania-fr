default taisho_1f_library_explore_01_sensitive = True
default taisho_1f_library_explore_01 = 0
default taisho_1f_library_explore_timer = False
default taisho_1f_library_gaspard_gone = False

default exp_taisho_1f_library_01_gaspard = False
default exp_taisho_1f_library_01_amina = False
default exp_taisho_1f_library_01_bookshelves = False
default exp_taisho_1f_library_01_window = False
default exp_taisho_1f_library_01_laptop = False
default exp_taisho_1f_library_01_painting = False
default exp_taisho_1f_library_01_bonsai = False

default exp_taisho_1f_library_01_adj = ui.adjustment()

screen taisho_1f_library_explore_01_base():

    tag base_exploration

    viewport:
        xadjustment exp_taisho_1f_library_01_adj
        child_size (2880, 1080)
        if taisho_1f_library_explore_01_sensitive:
            draggable True
            edgescroll(150,200)
        xsize config.screen_width ysize config.screen_height

        add "taisho_1f_library_base"
        if taisho_1f_library_gaspard_gone == False:
            imagebutton:
                sensitive False
                if taisho_1f_library_explore_01 < 5:
                    idle "Gaspard frown"
                    hover "Gaspard frown"
                else:
                    idle "Gaspard frown sweat"
                    hover "Gaspard frown sweat"
                xpos 207
                ypos 577
                hover_sound "audio/sfx/gui_hover.ogg"
                activate_sound "audio/sfx/gui_confirm.ogg"
                action NullAction()
                at transform:
                    zoom 0.33
        if exp_taisho_1f_library_01_bonsai == False:
            imagebutton:
                sensitive False
                idle "Amina neutral"
                hover "Amina neutral"
                xpos 1301
                ypos 520
                hover_sound "audio/sfx/gui_hover.ogg"
                activate_sound "audio/sfx/gui_confirm.ogg"
                action NullAction()
                at transform:
                    zoom 0.2
        else:
            if taisho_1f_library_explore_01 < 8:
                imagebutton:
                    sensitive False
                    idle "Amina surprise"
                    hover "Amina surprise"
                    xpos 1301
                    ypos 520
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action NullAction()
                    at transform:
                        zoom 0.2

    add "darkness_layers"

screen taisho_1f_library_explore_01():

    tag exploration

    viewport:
        xadjustment exp_taisho_1f_library_01_adj
        child_size (2880, 1080)
        if taisho_1f_library_explore_01_sensitive:
            edgescroll(150,200)
            draggable True
        xsize config.screen_width ysize config.screen_height

        add "taisho_1f_library_base"
        if taisho_1f_library_gaspard_gone == False:
            imagebutton:
                sensitive "taisho_1f_library_explore_01_sensitive"
                if taisho_1f_library_explore_01 < 5:
                    idle "Gaspard frown"
                    hover "Gaspard frown"
                else:
                    idle "Gaspard frown sweat"
                    hover "Gaspard frown sweat"
                xpos 207
                ypos 577
                hover_sound "audio/sfx/gui_hover.ogg"
                activate_sound "audio/sfx/gui_confirm.ogg"
                action Jump("exp_taisho_1f_library_01_gaspard")
                tooltip _("Gaspard")
                at transform:
                    zoom 0.33
        
        if exp_taisho_1f_library_01_bonsai == False:
            imagebutton:
                sensitive "taisho_1f_library_explore_01_sensitive"
                idle "Amina neutral"
                hover "Amina neutral"
                xpos 1301
                ypos 520
                hover_sound "audio/sfx/gui_hover.ogg"
                activate_sound "audio/sfx/gui_confirm.ogg"
                action Jump("exp_taisho_1f_library_01_amina")
                tooltip _("Amina")
                at transform:
                    zoom 0.2
            button:
                sensitive "taisho_1f_library_explore_01_sensitive"
                pos(1724,414)
                xysize(509,297)
                background None
                hover_sound "audio/sfx/gui_hover.ogg"
                activate_sound "audio/sfx/gui_confirm.ogg"
                action Jump("exp_taisho_1f_library_01_bookshelves")
                if flashlight_use:
                    tooltip _("Bookshelves")
                else:
                    tooltip _("?????")
            button:
                sensitive "taisho_1f_library_explore_01_sensitive"
                pos(2654,341)
                xysize(226,551)
                background None
                hover_sound "audio/sfx/gui_hover.ogg"
                activate_sound "audio/sfx/gui_confirm.ogg"
                action Jump("exp_taisho_1f_library_01_window")
                if flashlight_use:
                    tooltip _("Window")
                else:
                    tooltip _("?????")
            button:
                sensitive "taisho_1f_library_explore_01_sensitive"
                pos(1868,697)
                xysize(123,65)
                background None
                hover_sound "audio/sfx/gui_hover.ogg"
                activate_sound "audio/sfx/gui_confirm.ogg"
                action Jump("exp_taisho_1f_library_01_laptop")
                if flashlight_use:
                    tooltip _("Laptop")
                else:
                    tooltip _("?????")
            button:
                sensitive "taisho_1f_library_explore_01_sensitive"
                pos(2453,257)
                xysize(130,236)
                background None
                hover_sound "audio/sfx/gui_hover.ogg"
                activate_sound "audio/sfx/gui_confirm.ogg"
                action Jump("exp_taisho_1f_library_01_painting")
                if flashlight_use:
                    tooltip _("Painting")
                else:
                    tooltip _("?????")
            if taisho_1f_library_explore_01 == 6:
                button:
                    sensitive "taisho_1f_library_explore_01_sensitive"
                    pos(2326,560)
                    xysize(232,129)
                    background None
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("exp_taisho_1f_library_01_bonsai")
                    if flashlight_use:
                        tooltip _("Bonsai")
                    else:
                        tooltip _("?????")
        else:
            if taisho_1f_library_explore_01 < 8:
                imagebutton:
                    sensitive False
                    idle "Amina surprise"
                    hover "Amina surprise"
                    xpos 1301
                    ypos 520
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action NullAction()
                    at transform:
                        zoom 0.2
                mousearea:
                    area (134,602,634,404)
                    hovered Jump("story_01_gaspard_gone")
            else:
                button:
                    pos(874,461)
                    xysize(306,221)
                    background None
                    action Jump("story_01_gaspard_found")
                    tooltip _("?????")

    add "darkness_layers"

label exp_taisho_1f_library_01_gaspard:
    $ taisho_1f_library_explore_01_sensitive = False
    $ renpy.block_rollback()
    $ flashlight_consume = False
    pause 0.5
    sh_i neutral "(I'm worried about him...{w=0.5} He seems sluggish, like he used up all his energy in those outbursts from earlier.)"
    sh_i frown "(It doesn't help that the air in this building is quite stagnant.{w=0.3} It must not have been properly aired in a bit...{w=0.5} The sooner we get out of here, the better.)"
    pause 1.0
    if exp_taisho_1f_library_01_gaspard == False:
            $ exp_taisho_1f_library_01_gaspard = True
            $ taisho_1f_library_explore_01 += 1
    $ flashlight_consume = True
    $ taisho_1f_library_explore_01_sensitive = True
    call screen taisho_1f_library_explore_01

label exp_taisho_1f_library_01_amina:
    $ taisho_1f_library_explore_01_sensitive = False
    $ renpy.block_rollback()
    $ flashlight_consume = False
    pause 0.5
    sh_i neutral "(She's been handling this better than I thought...{w=0.5} I can feel her tension but she's managed to keep a level head.)"
    sh_i smile "(She's got the psychological profile Human Resources loves.{w=0.3} Who knows, they may send some scouts her way after they read my report.)"
    pause 1.0
    if exp_taisho_1f_library_01_amina == False:
            $ exp_taisho_1f_library_01_amina = True
            $ taisho_1f_library_explore_01 += 1
    $ flashlight_consume = True
    $ taisho_1f_library_explore_01_sensitive = True
    call screen taisho_1f_library_explore_01

label exp_taisho_1f_library_01_bookshelves:
    $ taisho_1f_library_explore_01_sensitive = False
    $ renpy.block_rollback()
    if flashlight_use == False:
        sh_i neutral "(It's too dark.{w=0.3} I need to use the flashlight to look around.)"
    else:
        $ flashlight_consume = False
        pause 0.5
        sh_i neutral "(Hm...{w=0.5} It's quite sparsely stocked, for a library this big.)"
        sh_i frown "(From how the wood is worn down and warped, though, I can tell that it used to house many more tomes...{w=0.5} They've been removed, then?)"
        sh_i surprise "(I guess that they were particularly unique or antique...{w=0.5} You don't want to leave items like that in the open, when you turn a place like this into a meeting venue.)"
        sh_i smile "(Which means I can turn the leftover ones in kindle without too much remorse.)"
        if exp_taisho_1f_library_01_bookshelves == False:
            $ exp_taisho_1f_library_01_bookshelves = True
            $ taisho_1f_library_explore_01 += 1
        $ flashlight_consume = True
    pause 1.0
    $ taisho_1f_library_explore_01_sensitive = True
    call screen taisho_1f_library_explore_01

label exp_taisho_1f_library_01_window:
    $ taisho_1f_library_explore_01_sensitive = False
    $ renpy.block_rollback()
    if flashlight_use == False:
        sh_i neutral "(It's too dark.{w=0.3} I need to use the flashlight to look around.)"
    else:
        $ flashlight_consume = False
        pause 0.5
        sh_i neutral "(Security shutters, just like all the other ones...{w=0.5} Except the one in the corridor.)"
        sh_i frown "(Which makes me wonder, why?{w=0.3} Is it because the window in there doesn't have one, or was it excluded on purpose?{w=0.3} And why?)"
        sh_i surprise "(I can see no reason why that'd be the case...{w=0.5} Except maybe...{w=0.5} Giving us a space where {nw}"
        play sound "audio/sfx/gui_hint.ogg"
        extend "{b}we wouldn't need to use the flashlight I found{/b}?)"
        sh_i frown "(.{w=0.3}.{w=0.3}.{w=0.5}I had heard of the concept of gamification, but this is ridiculous.)"
        if exp_taisho_1f_library_01_window == False:
            $ exp_taisho_1f_library_01_window = True
            $ taisho_1f_library_explore_01 += 1
        $ flashlight_consume = True
    pause 1.0
    $ taisho_1f_library_explore_01_sensitive = True
    call screen taisho_1f_library_explore_01

label exp_taisho_1f_library_01_laptop:
    $ taisho_1f_library_explore_01_sensitive = False
    $ renpy.block_rollback()
    if flashlight_use == False:
        sh_i neutral "(It's too dark.{w=0.3} I need to use the flashlight to look around.)"
    else:
        $ flashlight_consume = False
        pause 0.5
        sh_i shock "(A laptop...?!{w=0.3} Then maybe...)"
        pause 1.5
        sh_i frown "(Darn it.{w=0.3} It's an old one, the charger is not an USB-C.)"
        sh_i surprise "(Still...{w=0.5} It gives me thought.{w=0.3} I should try and see if it turns on, later.)"
        if exp_taisho_1f_library_01_laptop == False:
            $ exp_taisho_1f_library_01_laptop = True
            $ taisho_1f_library_explore_01 += 1
        $ flashlight_consume = True
    pause 1.0
    $ taisho_1f_library_explore_01_sensitive = True
    call screen taisho_1f_library_explore_01

label exp_taisho_1f_library_01_painting:
    $ taisho_1f_library_explore_01_sensitive = False
    $ renpy.block_rollback()
    if flashlight_use == False:
        sh_i neutral "(It's too dark.{w=0.3} I need to use the flashlight to look around.)"
    else:
        $ flashlight_consume = False
        pause 0.5
        sh_i surprise "(That's a nice Ukiyo-E painting...{w=0.5} I think I've actually seen the image on a book, before.{w=0.3} Although, the way it reflects the light...?)"
        play sound4 "audio/se/steps_wood_slow.ogg"
        pause 3.0
        sh_i frown "(Yup, a plastic copy.{w=0.5} Not surprising, if Du Bois actually had the original in his possession, I doubt his descendants would just leave it hanging around.)"
        sh_i neutral "(It gives off a weird feeling, not going to lie...{w=0.5} Like the entire estate has been sanitized, in some way.{w=0.3} Deprived of its personality.)"
        sh_i frown "(.{w=0.3}.{w=0.3}.{w=0.5}maybe this is all the work of some kind of Du Bois truther who wanted to bring the 'real' château back, who knows.)"
        if exp_taisho_1f_library_01_painting == False:
            $ exp_taisho_1f_library_01_painting = True
            $ taisho_1f_library_explore_01 += 1
        $ flashlight_consume = True
    pause 1.0
    $ taisho_1f_library_explore_01_sensitive = True
    call screen taisho_1f_library_explore_01

label exp_taisho_1f_library_01_bonsai:
    $ taisho_1f_library_explore_01_sensitive = False
    $ renpy.block_rollback()
    if flashlight_use == False:
        sh_i neutral "(It's too dark.{w=0.3} I need to use the flashlight to look around.)"
    else:
        $ flashlight_consume = False
        pause 0.5
        sh_i surprise "(.{w=0.3}.{w=0.3}.{w=0.5}a {nw}"
        play sound4 "audio/sfx/gui_hint.ogg"
        extend "{b}bonsai{/b}...)"
        pause 1.0
        $ taisho_1f_library_explore_timer = True
        sh_i surprise "(It's been years since I've seen one...{w=0.5} It looks well taken care of.)"
        sh_i sad "(Mom used to keep one similar to this in our living room...{w=0.5} Back in our house in Italy.{w=0.3} The display pot has the same shape and colour.)"
        sh_i neutral "(Back when she and dad still loved each other...{w=0.5} Back when we were still a family.{w=0.5} Before...)"
        pause 1.5
        sh_i sad "(Francesco, I hope you're alright.{w=0.3} If we were all knocked out at the reception, and we three ended up here...)"
        pause 1.5
        play sound2 "audio/se/door_slam.ogg" volume 0.5
        sh_i neutral "(Let's see what else is here.{w=0.3} It rests on a cabinet...)"
        play sound "audio/se/door_swivel.ogg"
        pause 0.5
        play sound2 "audio/se/fabric_tearing.ogg" volume 0.5
        sh_i smile "(Water bottles and some snacks...{w=0.5} Just in time, I'm starting to get peckish myself, truth tell.)"
        sh_i neutral "(And what about this wooden box...?)"
        play sound "audio/se/box_open.ogg"
        pause 1.0
        sh smile "Yes!{w=0.3} I knew it!"
        am neutral "What did you find?"
        sh smile "A box of cigars!{w=0.3} Can you guess what's inside, Gaspard?"
        pause 2.5
        sh surprise "Gaspard?"
        if exp_taisho_1f_library_01_bonsai == False:
            $ exp_taisho_1f_library_01_bonsai = True
            $ taisho_1f_library_explore_01 += 1
            $ taisho_1f_library_gaspard_gone = True
        $ flashlight_consume = True
    pause 1.0
    $ taisho_1f_library_explore_01_sensitive = True
    call screen taisho_1f_library_explore_01


default taisho_1f_library_gaspard_arm = False
default taisho_1f_library_gaspard_shoulder = False

screen taisho_1f_library_gaspard_scare():

    tag exploration

    button:
        pos(50,729)
        xysize(563,351)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("taisho_1f_library_gaspard_arm")
        tooltip _("?????")
    button:
        pos(1332,76)
        xysize(258,286)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("taisho_1f_library_gaspard_shoulder")
        tooltip _("?????")

    if taisho_1f_library_gaspard_arm and taisho_1f_library_gaspard_shoulder:
        button:
            pos(767,126)
            xysize(264,217)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("taisho_1f_library_gaspard_face")
            tooltip _("?????")

label taisho_1f_library_gaspard_arm:
    $ renpy.block_rollback()
    pause 0.5
    sh_i frown sweat "(That table is...{w=0.5} It's solid mahogany.{w=0.3} And yet, he...{w=0.5} Barehanded?{w=0.3} With his fingernails?)"
    sh_i angry sweat "(No, those cannot be called fingers anymore...{w=0.5} What are those veins?{w=0.3} Why are they...?!)"
    pause 1.0
    if taisho_1f_library_gaspard_arm == False:
        $ taisho_1f_library_gaspard_arm = True
    call screen taisho_1f_library_gaspard_scare

label taisho_1f_library_gaspard_shoulder:
    $ renpy.block_rollback()
    pause 0.5
    sh_i surprise sweat "(His clothes...{w=0.5} Was he attacked?{w=0.3} No.)"
    sh_i shock sweat "(His shoulder, it...{w=0.3} What happened to his body?!)"
    pause 1.0
    if taisho_1f_library_gaspard_shoulder == False:
        $ taisho_1f_library_gaspard_shoulder = True
    call screen taisho_1f_library_gaspard_scare