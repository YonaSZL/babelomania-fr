default lvl3_corridor_explore_01 = 0
default exp_lvl3_corridor_01_shelves = False
default exp_lvl3_corridor_01_fridge = False
default exp_lvl3_corridor_01_bed = False

screen lvl3_corridor_explore_01():

    tag exploration

    button:
        pos(993,454)
        xysize(128,297)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_lvl3_corridor_01_bed")
        tooltip _("Cot")

    if exp_lvl3_corridor_01_bed:
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_lvl3_corridor_01_fridge")
            tooltip _("Fridge")
    
    if exp_lvl3_corridor_01_fridge:
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_lvl3_corridor_01_shelves")
            tooltip _("Shelves")