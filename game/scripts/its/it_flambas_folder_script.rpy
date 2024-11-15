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
    de_i surprise "(A bunch of newspaper clippings...{w=0.5} In Japanese?)"
    de_i frown "(Well, not exactly, they're printouts of newspaper clippings but still...{w=0.5} What?{w=0.3} Ugh, now I wish I took Francesco up on his lessons.)"
    