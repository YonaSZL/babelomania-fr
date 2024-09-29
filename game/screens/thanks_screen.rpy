screen thank_you_screen():

    imagebutton:
        anchor(0.5,0.5)
        xpos 343
        ypos 849
        idle "gui/main_menu/rate_spook_idle.png"
        hover "gui/main_menu/rate_spook_hover.png"
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_codex.ogg"
        action OpenURL("https://itch.io/jam/spooktober-2024/rate/2938397")
    
    imagebutton:
        anchor(0.5,0.5)
        xpos 1586
        ypos 849
        idle "gui/main_menu/rate_itch_idle.png"
        hover "gui/main_menu/rate_itch_hover.png"
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_codex.ogg"
        action OpenURL("https://jpde.itch.io/babelomania/rate")
    
    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "gui/main_menu/main_return_idle.png"
        hover "gui/main_menu/main_return_hover.png"
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_codex.ogg"
        action Jump("return_from_thanks")