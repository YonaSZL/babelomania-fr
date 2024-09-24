default taisho_1f_library_explore_01_sensitive = True
default taisho_1f_library_explore_01 = 0
default taisho_1f_library_explore_timer = False

default exp_taisho_1f_library_01_bookshelves = False
default exp_taisho_1f_library_01_window = False
default exp_taisho_1f_library_01_laptop = False
default exp_taisho_1f_library_01_painting = False
default exp_taisho_1f_library_01_bonsai = False

screen taisho_1f_library_explore_01():

    tag exploration

    viewport:
        draggable True
        yinitial 0.5 xinitial 0.5
        child_size (2880, 1080)
        edgescroll(150,200)
        xsize config.screen_width ysize config.screen_height

        add "taisho_1f_library_base"

        imagebutton:
            sensitive "taisho_1f_library_explore_01_sensitive"
            idle "Gaspard frown"
            hover "Gaspard frown"
            xpos 207
            ypos 577
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_gaspard")
            tooltip _("Gaspard")
            at transform:
                zoom 0.33
            
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
            pos(1724,414)
            xysize(509,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_bookshelves")
            tooltip _("Bookshelves")
        button:
            pos(2654,341)
            xysize(226,551)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_window")
            tooltip _("Window")
        button:
            pos(1898,707)
            xysize(83,45)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_laptop")
            tooltip _("Laptop")
        button:
            pos(2453,257)
            xysize(130,236)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_painting")
            tooltip _("Painting")
        if taisho_1f_library_explore_01 == 4:
            button:
                pos(2326,560)
                xysize(232,129)
                background None
                hover_sound "audio/sfx/gui_hover.ogg"
                activate_sound "audio/sfx/gui_confirm.ogg"
                action Jump("exp_taisho_1f_library_01_bonsai")
                tooltip _("Bonsai")
        if taisho_1f_library_explore_timer:
            timer 60.0 action Play("sound2", "audio/se/fist_slam.ogg")
            timer 120.0 action Play("sound2", "audio/se/fabric_tearing.ogg")
    
    add "darkness_layers"

    $ tooltip = GetTooltip()

    nearrect:
        focus "tooltip"
        prefer_top True

        frame:
            xalign 0.5
            text "[tooltip]"

label exp_taisho_1f_library_01_gaspard:
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(I'm worried about him...{w=0.5} He seems sluggish, like he used all his energy in those anger explosions from earlier.)"
    sh_i frown "(It doesn't help that the air in this building is quite stagnant.{w=0.3} It must not have been properly aired in a bit...{w=0.5} The sooner we get out of here, the better.)"
    pause 1.0

label exp_taisho_1f_library_01_amina:
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(She's been handling this better than I thought...{w=0.5} I can feel her tension but she's managed to keep a level head.)"
    sh_i smile "(She's got the psychological profile that Human Resources just loves.{w=0.3} Who knows, they may send some scouts her way after they read my report.)"
    pause 1.0

label exp_taisho_1f_library_01_bookshelves:
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(Hm...{w=0.5} It's quite sparsely stocked, for a library this big...)"
    sh_i frown "(From how the wood is worn down and warped, though, I can tell that it used to house many more tomes...{w=0.5} They've been removed, then?)"
    sh_i surprise "(I guess that they were particularly unique or antique...{w=0.5} You don't want to leave items like that in the open, when you turn a place like this into a meeting venue.)"
    sh_i smile "(Which means I can turn the leftover ones in kindle without too much remorse.)"
    if exp_taisho_1f_library_01_bookshelves == False:
        $ exp_taisho_1f_library_01_bookshelves = True
        $ taisho_1f_library_explore_01 += 1
    pause 1.0

label exp_taisho_1f_library_01_window:
    $ renpy.block_rollback()
    pause 0.5
    sh_i neutral "(Security shutters, just like all the other ones...{w=0.5} Except the one in the corridor.)"
    sh_i frown "(Which makes me wonder, why?{w=0.3} Is it because the window in there doesn't have one, or was it excluded on purpose?{w=0.3} And why?)"
    sh_i surprise "(I can see no reason why that'd be the case...{w=0.5} Except maybe...{w=0.5} Giving us a space where {nw}"
    play sound "audio/sfx/gui_hint.ogg"
    extend "{b}we wouldn't need to use the flashlight I found{/b}?"
    sh_i frown "(.{w=0.3}.{w=0.3}.{w=0.5}I had heard of the concept of gamification, but this is ridiculous.)"
    if exp_taisho_1f_library_01_window == False:
        $ exp_taisho_1f_library_01_window = True
        $ taisho_1f_library_explore_01 += 1
    pause 1.0

label exp_taisho_1f_library_01_laptop:
    $ renpy.block_rollback()
    pause 0.5
    sh_i shock "(A laptop...?!{w=0.3} Then maybe...)"
    pause 1.5
    sh_i frown "(Darn it.{w=0.3} It's an old one, the charger is not an USB-C.)"
    sh_i surprise "(Still...{w=0.5} It gives me thought.{w=0.3} I should try and see if it turns on, later.)"
    if exp_taisho_1f_library_01_laptop == False:
        $ exp_taisho_1f_library_01_laptop = True
        $ taisho_1f_library_explore_01 += 1
    pause 1.0

label exp_taisho_1f_library_01_painting:
    $ renpy.block_rollback()
    pause 0.5
    sh_i surprise "(That's a nice Ukiyo-E painting...{w=0.5} I think I've actually seen the image on a book, before.{w=0.3} Although, the way it reflects the light...?)"
    play sound4 "audio/se/steps_wood_slow.ogg"
    pause 2.0
    sh_i frown "(Yup, a plastic copy.{w=0.5} Not surprising, if Du Bois actually had the original in his possession, I doubt his descendants would just leave it hanging around.)"
    sh_i neutral "(It gives off a weird feeling, not going to lie...{w=0.5} Like the entire estate has been sanitized, in some way.{w=0.3} Deprived of its personality.)"
    sh_i frown "(.{w=0.3}.{w=0.3}.{w=0.5}maybe this is all the work of some kind of Du Bois truther who wanted to bring the 'real' château back, who knows.)"
    if exp_taisho_1f_library_01_painting == False:
        $ exp_taisho_1f_library_01_painting = True
        $ taisho_1f_library_explore_01 += 1
    pause 1.0

label exp_taisho_1f_library_01_bonsai:
    $ renpy.block_rollback()
    pause 0.5
    stop music fadeout 3.5
    sh_i surprise "(.{w=0.3}.{w=0.3}.{w=0.5}a {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}bonsai{/b}..."
    pause 1.0
    show Shigeo surprise at sh_big:
        xalign 0.5
    with dissolve
    sh_i nulla "(It's been years since I've seen one...{w=0.5} It looks well taken care of.)"
    pause 1.0
    show Shigeo sad with dissolve
    pause 0.5
    sh_i nulla "(Mom used to keep one similar to this in our living room...{w=0.5} Back in our house in Italy.{w=0.3} The display pot has the same shape and colour.)"
    show Shigeo neutral
    sh_i nulla "(Back when she and dad still loved each other...{w=0.5} Back when we were still a family.{w=0.5} Before...)"
    pause 1.0
    show Shigeo sad with dissolve
    pause 0.5
    sh_i nulla "(Francesco...{w=0.5} I hope you're alright.{w=0.3} If we)"
    $ taisho_1f_library_explore_timer = True
    if exp_taisho_1f_library_01_bonsai == False:
        $ exp_taisho_1f_library_01_bonsai = True
        $ taisho_1f_library_explore_01 += 1
    pause 1.0
    