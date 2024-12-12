screen va_choice():

    add "gui/language/bg.png"

    style_prefix "language"

    hbox:
        align(0.5, 0.5) spacing 200

        button:
            xysize(343,755)
            idle_background "gui/va/none.png"
            hover_background "gui/va/none_gl.png"
            label _("No Voices")
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_slots_confirm.ogg"
            action [SetVariable("persistent.va_style", "None"), SetVariable("persistent.firstvoice", True), Return()] ##+ add the language change action
        

        button:
            xysize(343,755)
            idle_background "gui/va/beeps.png"
            hover_background "gui/va/beeps_gl.png"
            label _("Beeps")
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_slots_confirm.ogg"
            action [SetVariable("persistent.va_style", "beeps"), SetVariable("persistent.firstvoice", True), Return()] ##+ add the language change action
        
        #button:
        #    xysize(343,755)
        #    idle_background "gui/language/french.png"
        #    hover_background "gui/language/french_gl.png"
        #    label _("Francais")
        #    hover_sound "audio/sfx/gui_hover.ogg"
        #    activate_sound "audio/sfx/gui_slots_confirm.ogg"
        #    action [Language("french"), SetVariable("language_switcher", "French"), gui.SetPreference("name_text_font", "gui/font/CreditValley.ttf"), gui.SetPreference("interface_font", "gui/font/ColabThi.otf"), Function(renpy.transition, dissolve), SetVariable("persistent.firstopen", True), Return()] ##+ add the language change action