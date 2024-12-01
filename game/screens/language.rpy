
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
            hover_background "gui/language/english_gl.png"
            label _("English")
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_slots_confirm.ogg"
            action [Language(None), SetVariable("language_switcher", "English"), gui.SetPreference("name_text_font", "gui/font/Sok Brubah.ttf"), gui.SetPreference("interface_font", "gui/font/Klotee.ttf"), Function(renpy.transition, dissolve), SetVariable("persistent.firstopen", True), Return()] ##+ add the language change action
        

        button:
            xysize(343,755)
            idle_background "gui/language/french.png"
            hover_background "gui/language/french_gl.png"
            label _("Francais")
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_slots_confirm.ogg"
            action [Language("french"), SetVariable("language_switcher", "French"), gui.SetPreference("name_text_font", "gui/font/CreditValley.ttf"), gui.SetPreference("interface_font", "gui/font/ColabThi.otf"), Function(renpy.transition, dissolve), SetVariable("persistent.firstopen", True), Return()] ##+ add the language change action


style language_label:
    align(0.5, 1.0) yoffset -110

style language_label_text:
    size 50
    color '#bfaa8f'
