##Functions that make beeps happen with certain characters.
default va_style = "None"

define shigeo_keys = ["audio/va/beeps/shigeo_type_a.ogg", "audio/va/beeps/shigeo_type_b.ogg", "audio/va/beeps/shigeo_type_c.ogg", "audio/va/beeps/shigeo_type_d.ogg"]
define shigeo_pens = ["audio/va/beeps/shigeo_pen_a.ogg", "audio/va/beeps/shigeo_pen_b.ogg", "audio/va/beeps/shigeo_pen_c.ogg", "audio/va/beeps/shigeo_pen_d.ogg"]
define shigeo_bips = ["audio/va/beeps/shigeo_beep_a.ogg"]
default shigeo_sounds = None

init python:
    #Shigeo Beeps

    def shigeo_define(voice_bundle, shigeo_sounds):
        shigeo_sounds = voice_bundle
        return

    def shigeo_beep(event, interact=True, **kwargs):
        global va_style
        if not interact:
            return
        if va_style != "beeps":
            return
        if event == "show":
        
            for i in range (50):
                renpy.sound.queue(renpy.random.choice(shigeo_keys), channel='beeps')
        
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel='beeps', fadeout=0.1)