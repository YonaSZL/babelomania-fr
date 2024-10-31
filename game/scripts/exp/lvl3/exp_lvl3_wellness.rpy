default lvl3_wellness_explore_01 = 0
default exp_lvl3_wellness_01_shelves = False
default exp_lvl3_wellness_01_fridge = False
default exp_lvl3_wellness_01_bed = False

screen lvl3_wellness_explore_01():

    tag exploration

    button:
        pos(993,454)
        xysize(128,297)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_lvl3_wellness_01_shelves")
        tooltip _("Shelves")

label exp_lvl3_wellness_01_shelves:
    $ renpy.block_rollback()
    pause 0.5

    if exp_lvl3_wellness_01_shelves == False:
        $ exp_lvl3_wellness_01_shelves = True
        $ lvl3_wellness_explore_01 += 1
    pause 1.0
    call screen lvl3_wellness_explore_01

label exp_lvl3_wellness_01_fridge:
    $ renpy.block_rollback()
    pause 0.5

    if exp_lvl3_wellness_01_fridge == False:
        $ exp_lvl3_wellness_01_fridge = True
        $ lvl3_wellness_explore_01 += 1
    pause 1.0
    call screen lvl3_wellness_explore_01

label exp_lvl3_wellness_01_bed:
    $ renpy.block_rollback()
    pause 0.5

    if exp_lvl3_wellness_01_bed == False:
        $ exp_lvl3_wellness_01_bed = True
        $ lvl3_wellness_explore_01 += 1
    pause 1.0
    call screen lvl3_wellness_explore_01