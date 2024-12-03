default pzl_papers_used = False

screen pzl_taisho_1f_fire():

    tag puzzle_screen

    if pzl_papers_used == True:
        imagebutton:
            sensitive False
            idle "images/pzl/pzl_papers.ogg"
            idle "images/pzl/pzl_papers.ogg"
            xpos 207
            ypos 577
            action Show("notify", None, _("The papers are in place. Now I need to light them up."))