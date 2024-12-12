label conv_tabitha_exp:
    $ renpy.block_rollback()
    pause 0.5
    ta neutral "[shn].{w=0.3} How can I be of service?"
    pause 0.5

menu choose_name:

    sh nulla "You can call me..."

    "Arata-sama.":
        $ shn = "Arata-sama"
        jump name_chosen
    "Arata-dono.":
        $ shn = "Arata-dono"
        jump name_chosen
    "Arata-san.":
        $ shn = "Arata-san"
        jump name_chosen

label name_chosen:
    $ renpy.block_rollback()
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    ta bow "Acknowledged.{w=0.3} I shall henceforth address you as [shn]."
    pause 1.0
    return
