
define config.end_splash_transition = dissolve

#label splashscreen:
#    scene black
#    call screen language with dissolve
#    scene black with dissolve
#    return

screen language():

    add "gui/language/bg.png"

    style_prefix "language"

    hbox:
        align(0.5, 0.5) spacing 200

        button:
            xysize(343,755)
            idle_background "gui/language/english.png"
            hover_background At("gui/language/english.png", outline_transform(2, "#342209", 4.0))
            label "English"
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_slots_confirm.ogg"
            action [Function(renpy.transition, dissolve), SetVariable("persistent.firstopen", True), Return()] ##+ add the language change action
        

        button:
            xysize(343,755)
            idle_background "gui/language/french.png"
            hover_background At("gui/language/french.png", outline_transform(2, "#342209", 4.0))
            label "Francais"
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_slots_confirm.ogg"
            action [Function(renpy.transition, dissolve), Return()] ##+ add the language change action


style language_label:
    align(0.5, 1.0) yoffset -110

style language_label_text:
    size 50
    color '#bfaa8f'
