label flambas_folder_reveal:
    $ renpy.block_rollback()
    show Delphine neutral at de_med:
        xalign 0.5
    with dissolve
    pause 1.0
    scene closed_folder with Reveal
    pause 1.0
    play sound4 "audio/se/paper_shuffle.ogg"
    scene open_folder with dissolve
    pause 0.5
    