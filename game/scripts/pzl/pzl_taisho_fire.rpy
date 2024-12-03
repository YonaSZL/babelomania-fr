default pzl_papers_used = False
image pzl_papers = "images/pzl/pzl_papers.png"
image pzl_papers_fire = "images/pzl/pzl_papers_fire.png"
screen pzl_taisho_1f_fire():

    tag puzzle_screen

    if pzl_papers_used == True:
        imagebutton:
            sensitive False
            idle "pzl_papers"
            hover "pzl_papers"
            xpos 855
            ypos 759
            action Show("notify", None, _("The papers are in place. Now I need to light them up."))