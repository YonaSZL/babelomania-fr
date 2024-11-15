default lvl3_meeting_examine_01 = 0
default exm_lvl3_meeting_01_stationary = False
default exm_lvl3_meeting_01_furniture = False
default exm_lvl3_meeting_01_folder = False
default exm_lvl3_meeting_01_body = False

screen lvl3_meeting_examine_01():

    tag examination

    button:
        pos(993,454)
        xysize(128,297)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exm_lvl3_meeting_01_stationary")
        tooltip _("Stationary")
    
    button:
        pos(993,454)
        xysize(128,297)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exm_lvl3_meeting_01_furniture")
        tooltip _("Furniture")
    
    button:
        pos(993,454)
        xysize(128,297)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exm_lvl3_meeting_01_folder")
        tooltip _("Folder")
    
    if lvl3_meeting_examine_01 == 3:
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exm_lvl3_meeting_01_body")
            tooltip _("Floor")