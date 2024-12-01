##Functions that make beeps happen with certain characters.
default va_style = "None"

define shigeo_keys = ["audio/va/beeps/shigeo_type_a.ogg", "audio/va/beeps/shigeo_type_b.ogg", "audio/va/beeps/shigeo_type_c.ogg", "audio/va/beeps/shigeo_type_d.ogg"]
define shigeo_pens = ["audio/va/beeps/shigeo_pen_a.ogg", "audio/va/beeps/shigeo_pen_b.ogg", "audio/va/beeps/shigeo_pen_c.ogg", "audio/va/beeps/shigeo_pen_d.ogg"]
define shigeo_bips = ["audio/va/beeps/shigeo_beep_a.ogg"]
default shigeo_sounds = []
default francesco_sounds = []

init python:
    #Shigeo Beeps

    def shigeo_define(voice_bundle, shigeo_sounds):
        shigeo_sounds.clear()
        shigeo_sounds.extend(voice_bundle)
        return

    def shigeo_beep(event, interact=True, **kwargs):
        global va_style
        if not interact:
            return
        if va_style != "beeps":
            return
        if event == "show":
        
            for i in range (50):
                renpy.sound.queue(renpy.random.choice(shigeo_sounds), channel='beeps')
        
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel='beeps', fadeout=0.1)

    def francesco_define(voice_bundle, francesco_sounds):
        francesco_sounds.clear()
        francesco_sounds.extend(voice_bundle)
        return

    def francesco_beep(event, interact=True, **kwargs):
        global va_style
        if not interact:
            return
        if va_style != "beeps":
            return
        if event == "show":
        
            for i in range (50):
                renpy.sound.queue(renpy.random.choice(francesco_sounds), channel='beeps')
        
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel='beeps', fadeout=0.1)

define habiki_keys = ["audio/va/beeps/habiki_type_a.ogg", "audio/va/beeps/habiki_type_b.ogg", "audio/va/beeps/habiki_type_c.ogg", "audio/va/beeps/habiki_type_d.ogg"]
define habiki_pens = ["audio/va/beeps/habiki_pen_a.ogg", "audio/va/beeps/habiki_pen_b.ogg", "audio/va/beeps/habiki_pen_c.ogg", "audio/va/beeps/habiki_pen_d.ogg"]
define habiki_bips = ["audio/va/beeps/habiki_beep_a.ogg"]
default habiki_sounds = []
default gaspard_sounds = []

init python:
    #habiki Beeps

    def habiki_define(voice_bundle, habiki_sounds):
        habiki_sounds.clear()
        habiki_sounds.extend(voice_bundle)
        return

    def habiki_beep(event, interact=True, **kwargs):
        global va_style
        if not interact:
            return
        if va_style != "beeps":
            return
        if event == "show":
        
            for i in range (50):
                renpy.sound.queue(renpy.random.choice(habiki_sounds), channel='beeps')
        
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel='beeps', fadeout=0.1)

    #gaspard Beeps

    def gaspard_define(voice_bundle, gaspard_sounds):
        gaspard_sounds.clear()
        gaspard_sounds.extend(voice_bundle)
        return

    def gaspard_beep(event, interact=True, **kwargs):
        global va_style
        if not interact:
            return
        if va_style != "beeps":
            return
        if event == "show":
        
            for i in range (50):
                renpy.sound.queue(renpy.random.choice(gaspard_sounds), channel='beeps')
        
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel='beeps', fadeout=0.1)

define amina_keys = ["audio/va/beeps/amina_type_a.ogg", "audio/va/beeps/amina_type_b.ogg", "audio/va/beeps/amina_type_c.ogg", "audio/va/beeps/amina_type_d.ogg"]
define amina_pens = ["audio/va/beeps/amina_pen_a.ogg", "audio/va/beeps/amina_pen_b.ogg", "audio/va/beeps/amina_pen_c.ogg", "audio/va/beeps/amina_pen_d.ogg"]
define amina_bips = ["audio/va/beeps/amina_beep_a.ogg"]
default amina_sounds = []
default delphine_sounds = []
default tabitha_sounds = []

init python:
    #Amina Beeps

    def amina_define(voice_bundle, amina_sounds):
        amina_sounds.clear()
        amina_sounds.extend(voice_bundle)
        return

    def amina_beep(event, interact=True, **kwargs):
        global va_style
        if not interact:
            return
        if va_style != "beeps":
            return
        if event == "show":
        
            for i in range (50):
                renpy.sound.queue(renpy.random.choice(amina_sounds), channel='beeps')
        
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel='beeps', fadeout=0.1)
    
    def delphine_define(voice_bundle, delphine_sounds):
        delphine_sounds.clear()
        delphine_sounds.extend(voice_bundle)
        return

    def delphine_beep(event, interact=True, **kwargs):
        global va_style
        if not interact:
            return
        if va_style != "beeps":
            return
        if event == "show":
        
            for i in range (50):
                renpy.sound.queue(renpy.random.choice(delphine_sounds), channel='beeps')
        
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel='beeps', fadeout=0.1)
    
    def tabitha_define(voice_bundle, tabitha_sounds):
        tabitha_sounds.clear()
        tabitha_sounds.extend(voice_bundle)
        return

    def tabitha_beep(event, interact=True, **kwargs):
        global va_style
        if not interact:
            return
        if va_style != "beeps":
            return
        if event == "show":
        
            for i in range (50):
                renpy.sound.queue(renpy.random.choice(tabitha_sounds), channel='beeps')
        
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel='beeps', fadeout=0.1)