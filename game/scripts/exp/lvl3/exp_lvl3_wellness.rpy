default lvl3_wellness_explore_01 = 0
default exp_lvl3_wellness_01_shelves = False

screen lvl3_wellness_explore_01():

    tag exploration

    button:
        pos(993,454)
        xysize(128,297)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_1f_corridor_01_gaspard")
        tooltip _("Gaspard")#GASPARD

label exp_lvl3_wellness_01_shelves:
    $ renpy.block_rollback()
    pause 0.5

    if exp_lvl3_wellness_01_shelves == False:
        $ exp_lvl3_wellness_01_shelves = True
    pause 1.0
    call screen lvl3_wellness_explore_01