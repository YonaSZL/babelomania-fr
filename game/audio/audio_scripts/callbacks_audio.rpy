##Functions that make beeps happen with certain characters.

define shigeo_keys = ["audio/va/beeps/shigeo_type_a.ogg", "audio/va/beeps/shigeo_type_b.ogg", "audio/va/beeps/shigeo_type_c.ogg", "audio/va/beeps/shigeo_type_d.ogg"]

init python:
    #Shigeo Beeps
    def shigeo_beep(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show":
        
            for i in range (50):
                renpy.sound.queue(renpy.random.choice(shigeo_keys), channel='beeps')
        
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel='beeps', fadeout=0.1)