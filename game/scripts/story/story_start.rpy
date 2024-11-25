# The game starts here.

label start:
    scene main_menu_bg
    $ quick_menu = False
    $ time_menu = False
    $ inventory_show = False
    $ stat1_show = False
    $ stat2_show = False
    d """{b}WARNING{/b}\n
    
    Due to some of the Themes and Events depicted in this Fictional Story, it is intended for consumption from a Mature Audience, where Mature stands for: having reached a stage of mental or emotional development characteristic of an adult.\n

    This game contains elements that may be disturbing or triggering to some players, including but not limited to:{nw}

    Blood{nw}
    
    Gore{nw}
    
    Violence{nw}
    
    Intense fear{nw}
    
    Jump scares{nw}
    
    Explicit language{nw}
    
    Death{nw}
    
    Trauma{nw}
    
    PTSD{nw}
    
    Panic Attacks{nw}
    
    Prejudice{nw}
    
    Xenophobia{nw}

    Player discretion is advised."""
    nvl clear

menu:
    "Do you understand?"

    "Yes.":
        jump gore_selection

    "No.":
        return

menu gore_selection:
    "What level of gore would you prefer? (This setting can be changed at any time from the OPTIONS menu.)"
    
    "Full gore.":
        $ persistent.gore = True
        jump story_00_start

    "Censored gore.":
        $ persistent.gore = False
        jump story_00_start