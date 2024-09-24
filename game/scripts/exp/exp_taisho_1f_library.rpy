default taisho_1f_library_explore_01_sensitive = True
default taisho_1f_library_explore_01 = 0

default exp_taisho_1f_library_01_bookshelves = False
default exp_taisho_1f_library_01_window = False
default exp_taisho_1f_library_01_laptop = False
default exp_taisho_1f_library_01_painting = False
default exp_taisho_1f_library_01_bonsai = False

screen taisho_1f_library_explore_01():

    tag exploration

    viewport:
        draggable True
        mousewheel False
        edgescroll(75,75)
        xinitial 0.5
        scrollbars None
        arrowkeys None
        pagekeys None

        add "taisho_1f_library_base"

        imagebutton:
            sensitive "taisho_1f_library_explore_01_sensitive"
            idle "Gaspard frown"
            hover "Gaspard frown"
            xpos 111
            ypos 111
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_gaspard")
            tooltip _("Gaspard")
            at transform:
                zoom 0.14
            
        imagebutton:
            sensitive "taisho_1f_library_explore_01_sensitive"
            idle "Amina neutral"
            hover "Amina neutral"
            xpos 111
            ypos 111
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_amina")
            tooltip _("Amina")
            at transform:
                zoom 0.14
        
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_bookshelves")
            tooltip _("Bookshelves")
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_window")
            tooltip _("Window")
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_laptop")
            tooltip _("Laptop")
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_taisho_1f_library_01_painting")
            tooltip _("Painting")
        if taisho_1f_library_explore_01 == 4:
            timer 60.0 action Play("sound2", "audio/se/fist_slam.ogg")
            timer 120.0 action Play("sound2", "audio/se/fabric_tearing.ogg")
            button:
                pos(993,454)
                xysize(128,297)
                background None
                hover_sound "audio/sfx/gui_hover.ogg"
                activate_sound "audio/sfx/gui_confirm.ogg"
                action Jump("exp_taisho_1f_library_01_bonsai")
                tooltip _("Bonsai")
    
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

    if exp_taisho_1f_library_01_laptop == False:
        $ exp_taisho_1f_library_01_laptop = True
        $ taisho_1f_library_explore_01 += 1
    pause 1.0

label exp_taisho_1f_library_01_painting:
    $ renpy.block_rollback()
    pause 0.5

    if exp_taisho_1f_library_01_painting == False:
        $ exp_taisho_1f_library_01_painting = True
        $ taisho_1f_library_explore_01 += 1
    pause 1.0

label exp_taisho_1f_library_01_bonsai:
    $ renpy.block_rollback()
    pause 0.5

    if exp_taisho_1f_library_01_bonsai == False:
        $ exp_taisho_1f_library_01_bonsai = True
        $ taisho_1f_library_explore_01 += 1
    pause 1.0
    