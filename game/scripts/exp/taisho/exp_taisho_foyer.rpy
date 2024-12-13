#Aims for this puzzle: you need to input 'Shinzo Abe' using the wooden exposition panel. But written 'Abe Shinzo', surname first.
#Haiku Hint
##darkness returning
##from grandfather inherited
##by a son cut down
default taisho_foyer_explore = 0
default taisho_foyer_explore_timer = False
default taisho_foyer_gaspard_gone = False

default exp_taisho_foyer_amina = False
default exp_taisho_foyer_tabitha = False
default exp_taisho_foyer_door = False
default exp_taisho_foyer_stairs = False
default exp_taisho_foyer_exposition = False

screen taisho_foyer_explore():

    tag exploration

    imagebutton:
        idle "Amina neutral"
        hover "Amina neutral"
        xpos 480
        ypos 500
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_foyer_amina")
        tooltip _("Amina{#explore_foyer}")
        at transform:
            zoom 0.18
    
    imagebutton:
        idle "Tabitha neutral brief"
        hover "Tabitha neutral brief"
        xpos 799
        ypos 480
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_foyer_tabitha")
        tooltip _("The Android{#explore_foyer}")
        at transform:
            zoom 0.2
    button:
        pos(150,375)
        xysize(200,300)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_foyer_door")
        if flashlight_use:
            tooltip _("Door to Outside{#explore_foyer}")
        else:
            tooltip _("?????")
    button:
        pos(2654,341)
        xysize(226,551)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_foyer_stairs")
        if flashlight_use:
            tooltip _("Door to Stairways{#explore_foyer}")
        else:
            tooltip _("?????")
    button:
        pos(1868,697)
        xysize(123,65)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_foyer_exposition")
        if flashlight_use:
            tooltip _("Exposition")
        else:
            tooltip _("?????")

    add "darkness_layers"

label exp_taisho_foyer_door:
    $ renpy.block_rollback()
    if flashlight_use == False:
        sh_i neutral "(It's too dark.{w=0.3} I need to use the flashlight to look around.)"
    else:
        $ flashlight_consume = False
        pause 0.5
        sh_i neutral "(The door to the outside.{w=0.3} Only a scant few centimeters separating us from...)"
        sh_i frown "(From what, really?)"
        pause 1.0
        show taisho_foyer_door with dissolve
        pause 0.5
        sh_i neutral "(Logically, I know that once we leave the Taisho building, we'll be in the {nw}"
        play sound4 "audio/sfx/gui_hint.ogg"
        extend "{b}Great Courtyard{/b} of the château.{w=0.3} But I wouldn't call us home-free.)"
        sh_i frown "(I doubt whoever's doing this would be done with us so soon...{w=0.5} Considering the average class and job of the people at the reception, they have maybe twentyfour hours before anyone comes looking.)"
        sh_i neutral "(Which means that, whatever their intentions, they only have so much time to squeeze us.{w=0.3} Which makes me worry.)"
        sh_i frown sweat "(A building like the Taisho is a more controlled environment for them to plan around...{w=0.5} But at the same time, it limits the things they can throw at us.)"
        sh_i neutral sweat "(Once out in the open, we'll both lose a modicum of control over our surroundings.{w=0.3} And that worries me in a completely new way, considering...)"
        pause 1.5
        sh_i frown "(We'll cross that bridge when we come to it.{w=0.3} Staying put is not an option in our current situation.)"
        pause 0.5
        if exp_taisho_foyer_door == False:
            play sound4 "audio/sfx/gui_slots_confirm.ogg"
            show screen notify(_("Codex Entry Updated - Chateau de Bois.{#Château configuration.}"))
            $ c_chateau_dubois_config = True
            $ exp_taisho_foyer_door = True
            $ taisho_foyer_explore += 1
        $ flashlight_consume = True
    hide taisho_foyer_door with dissolve
    pause 1.0
    call screen taisho_1f_library_explore_01

label exp_taisho_foyer_amina:
    $ renpy.block_rollback()
    $ flashlight_consume = False
    pause 0.5
    
    if exp_taisho_foyer_amina == False:
        $ exp_taisho_foyer_amina = True
        $ taisho_foyer_explore += 1
    $ flashlight_consume = True
    pause 1.0
    call screen taisho_1f_library_explore_01

label exp_taisho_foyer_tabitha:
    $ renpy.block_rollback()
    $ flashlight_consume = False
    pause 0.5
    
    if exp_taisho_foyer_tabitha == False:
        $ exp_taisho_foyer_tabitha = True
        $ taisho_foyer_explore += 1
    $ flashlight_consume = True
    pause 1.0
    call screen taisho_1f_library_explore_01