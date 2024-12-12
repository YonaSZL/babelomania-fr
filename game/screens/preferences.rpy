
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    #add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use game_menu(_("Preferences"))

    viewport:
        #style_prefix 'game_menu'
        xysize(1040, 554) pos(390,270 )
        mousewheel True pagekeys True draggable True
        scrollbars "vertical"
        #has vbox

        vbox:
            spacing 35
            hbox:
                #box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):
                    # Only need fullscreen/windowed on desktop and web builds

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window"):
                            # Ensures this button is selected when
                            # not in fullscreen.
                            selected not preferences.fullscreen
                            action Preference("display", "window")
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Fullscreen"):
                            action Preference("display", "fullscreen")
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text"):
                        action Preference("skip", "toggle")
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                    textbutton _("After Choices"):
                        action Preference("after choices", "toggle")
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                    textbutton _("Transitions"):
                        action InvertSelected(Preference("transitions", "toggle"))
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
            if language_switcher == "English":
                vbox:
                    style_prefix "check"
                    label _("Font")
                    textbutton _("Serif"):
                        action gui.SetPreference("font", "gui/font/LinLibertine_R.ttf")
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                    textbutton _("Sans Serif"):
                        action gui.SetPreference("font", "gui/font/Roboto-Light.ttf")
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"

            ##divider frame
            frame:
                background Solid(u"#4f331d")
                xysize(500,3)
                xoffset 200
            

            #null height 60

            
            hbox:
                style_prefix "slider"
                #box_wrap True

                vbox:

                    label _("Text Speed")
                    bar value Preference("text speed")

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                vbox:
                    #xoffset -200
                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                    if persistent.va_style == "tabitha":
                        label _("Voice Volume")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height 15
                        textbutton _("Mute All"):
                            style_prefix "check"
                            action Preference("all mute", "toggle")
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"

            ##divider frame
            frame:
                background Solid(u"#4f331d")
                xysize(500,3)
                xoffset 200

            hbox:
                vbox:
                    style_prefix "radio"
                    label _("Gore")
                    textbutton _("Full") action SetVariable("persistent.gore", True) hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"
                    textbutton _("Censored") action SetVariable("persistent.gore", False) hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"


                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton _("English{#}") action [Language(None), SetVariable("language_switcher", "English"), gui.SetPreference("interface_font", "gui/font/Klotee.ttf")] hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"
                    textbutton _("French") action [Language("french"), SetVariable("language_switcher", "French"), gui.SetPreference("interface_font", "gui/font/ColabThi.otf")] hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"

            ##divider frame
            frame:
                background Solid(u"#4f331d")
                xysize(500,3)
                xoffset 200

            vbox:
                #box_wrap True
                hbox:
                    style_prefix "check"
                    label _("VA Style")
                    spacing 10
                    textbutton _("None"):
                        yoffset 5
                        action SetVariable("persistent.va_style", "None")
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                    textbutton _("Beeps"):
                        yoffset 5
                        action SetVariable("persistent.va_style", "beeps")
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                    #textbutton _("Tabitha"):
                    #    yoffset 5
                    #    action SetVariable("persistent.va_style", "tabitha")
                    #    hover_sound "audio/sfx/gui_hover.ogg"
                    #    activate_sound "audio/sfx/gui_confirm.ogg"
                if persistent.va_style == "beeps":
                    hbox:
                        style_prefix "check"
                        label _("Shigeo")
                        spacing 10
                        textbutton _("Key"):
                            yoffset 5
                            action [SetVariable("persistent.shigeo_sfx", "keys"), Function(shigeo_define, shigeo_keys, persistent.shigeo_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Pen"):
                            yoffset 5
                            action [SetVariable("persistent.shigeo_sfx", "pens"), Function(shigeo_define, shigeo_pens, persistent.shigeo_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Bip"):
                            yoffset 5
                            action [SetVariable("persistent.shigeo_sfx", "bips"), Function(shigeo_define, shigeo_bips, persistent.shigeo_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                    hbox:
                        style_prefix "check"
                        label _("Tabitha")
                        spacing 10
                        textbutton _("Key"):
                            yoffset 5
                            action [SetVariable("persistent.tabitha_sfx", "keys"), Function(tabitha_define, amina_keys, persistent.tabitha_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Pen"):
                            yoffset 5
                            action [SetVariable("persistent.tabitha_sfx", "pens"), Function(tabitha_define, amina_pens, persistent.tabitha_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Bip"):
                            yoffset 5
                            action [SetVariable("persistent.tabitha_sfx", "bips"), Function(tabitha_define, amina_bips, persistent.tabitha_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                    hbox:
                        style_prefix "check"
                        label _("Francesco")
                        spacing 10
                        textbutton _("Key"):
                            yoffset 5
                            action [SetVariable("persistent.francesco_sfx", "keys"), Function(francesco_define, shigeo_keys, persistent.francesco_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Pen"):
                            yoffset 5
                            action [SetVariable("persistent.francesco_sfx", "pens"), Function(francesco_define, shigeo_pens, persistent.francesco_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Bip"):
                            yoffset 5
                            action [SetVariable("persistent.francesco_sfx", "bips"), Function(francesco_define, shigeo_bips, persistent.francesco_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                    hbox:
                        style_prefix "check"
                        label _("Habiki")
                        spacing 10
                        textbutton _("Key"):
                            yoffset 5
                            action [SetVariable("persistent.habiki_sfx", "keys"), Function(habiki_define, habiki_keys, persistent.habiki_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Pen"):
                            yoffset 5
                            action [SetVariable("persistent.habiki_sfx", "pens"), Function(habiki_define, habiki_pens, persistent.habiki_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Bip"):
                            yoffset 5
                            action [SetVariable("persistent.habiki_sfx", "bips"), Function(habiki_define, habiki_bips, persistent.habiki_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                    hbox:
                        style_prefix "check"
                        label _("Gaspard")
                        spacing 10
                        textbutton _("Key"):
                            yoffset 5
                            action [SetVariable("persistent.gaspard_sfx", "keys"), Function(gaspard_define, habiki_keys, persistent.gaspard_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Pen"):
                            yoffset 5
                            action [SetVariable("persistent.gaspard_sfx", "pens"), Function(gaspard_define, habiki_pens, persistent.gaspard_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Bip"):
                            yoffset 5
                            action [SetVariable("persistent.gaspard_sfx", "bips"), Function(gaspard_define, habiki_bips, persistent.gaspard_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                    hbox:
                        style_prefix "check"
                        label _("Amina")
                        spacing 10
                        textbutton _("Key"):
                            yoffset 5
                            action [SetVariable("persistent.amina_sfx", "keys"), Function(amina_define, amina_keys, persistent.amina_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Pen"):
                            yoffset 5
                            action [SetVariable("persistent.amina_sfx", "pens"), Function(amina_define, amina_pens, persistent.amina_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Bip"):
                            yoffset 5
                            action [SetVariable("persistent.amina_sfx", "bips"), Function(amina_define, amina_bips, persistent.amina_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                    hbox:
                        style_prefix "check"
                        label _("Mira")
                        spacing 10
                        textbutton _("Key"):
                            yoffset 5
                            action [SetVariable("persistent.mira_sfx", "keys"), Function(mira_define, amina_keys, persistent.mira_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Pen"):
                            yoffset 5
                            action [SetVariable("persistent.mira_sfx", "pens"), Function(mira_define, amina_pens, persistent.mira_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Bip"):
                            yoffset 5
                            action [SetVariable("persistent.mira_sfx", "bips"), Function(mira_define, amina_bips, persistent.mira_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                    hbox:
                        style_prefix "check"
                        label _("M.Voices")
                        spacing 10
                        textbutton _("Key"):
                            yoffset 5
                            action [SetVariable("persistent.male_sfx", "keys"), Function(male_define, habiki_keys, persistent.male_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Pen"):
                            yoffset 5
                            action [SetVariable("persistent.male_sfx", "pens"), Function(male_define, habiki_pens, persistent.male_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Bip"):
                            yoffset 5
                            action [SetVariable("persistent.male_sfx", "bips"), Function(male_define, habiki_bips, persistent.male_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                    hbox:
                        style_prefix "check"
                        label _("F.Voices")
                        spacing 10
                        textbutton _("Key"):
                            yoffset 5
                            action [SetVariable("persistent.female_sfx", "keys"), Function(female_define, amina_keys, persistent.female_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Pen"):
                            yoffset 5
                            action [SetVariable("persistent.female_sfx", "pens"), Function(female_define, amina_pens, persistent.female_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"
                        textbutton _("Bip"):
                            yoffset 5
                            action [SetVariable("persistent.female_sfx", "bips"), Function(female_define, amina_bips, persistent.female_sounds)]
                            hover_sound "audio/sfx/gui_hover.ogg"
                            activate_sound "audio/sfx/gui_confirm.ogg"

### PREF
style pref_label:
    top_margin 15
    bottom_margin 3

style pref_label_text:
    yalign 1.0
    

style pref_vbox:
    xsize 338


## RADIO
style radio_label:
    is pref_label

style radio_label_text:
    is pref_label_text

style radio_vbox:
    is pref_vbox
    spacing 0

style radio_button:
    foreground "gui/button/radio_[prefix_]foreground.png"
    padding (50, 13, 6, 6)

## CHECK
style check_label:
    is pref_label
style check_label_text:
    is pref_label_text

style check_vbox:
    is pref_vbox
    spacing 0

style check_button:
    foreground "gui/button/check_[prefix_]foreground.png"
    padding (45, 13, 6, 6)

## SLIDER
style slider_label:
    is pref_label
style slider_label_text:
    is pref_label_text

style slider_slider:
    xsize 400

style slider_button:
    yalign 0.5
    left_margin 15

style slider_vbox:
    #is pref_vbox
    xsize 450

