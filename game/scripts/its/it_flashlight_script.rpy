label it_flashlight_use:
    play sound "audio/se/flashlight_on.ogg"
    $ flashlight_use = True
    if story_progress == 0 and current_location == "taisho_1f_study":
        jump story_01_be_light
    else:
        $ flashlight_consume = True
        call screen VARIABLE