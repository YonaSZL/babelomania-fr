screen elevator_panel_01():

    tag navigation

    button:
        pos(954,289)
        xysize(201,67)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/se/button_elevator.ogg"
        action Jump("story_02_happyday")
        tooltip _("Archive")