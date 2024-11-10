
$ entry_from = None
screen global_codex():

    tag menu

    #add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use game_menu(_("Codex"))

    #text "[persistent.gore]"


    add "gui/codex/divider.png" yalign 0.5 xoffset 500


    if current_entry:
        viewport:
            xysize(720,514) pos(720,282) scrollbars "vertical" mousewheel True draggable True
            style_prefix "entry"
            vbox:
                spacing 15
                label "Excerpt from: [entry_from]"
                use expression current_entry
                


    textbutton "" action [Hide("global_categories", dissolve) , Hide("global_entries", dissolve), Return()] keysym ['K_ESCAPE', 'K_MENU', 'K_PAUSE', 'mouseup_3']
    #on 'replace' action Show("global_categories")
    



init python:
    global_events = []
    global_items = []
    global_people = []
    global_locations = []



    def global_codex_list():


        global global_events
        global global_items 
        global global_people
        global global_locations

        global_events = shigeo_events
        global_events.extend(delphine_events)

        global_people = shigeo_people
        global_people.extend(delphine_people)

        global_locations = shigeo_locations
        global_locations.extend(delphine_locations)

        global_items = shigeo_items
        global_items.extend(delphine_items)




screen global_categories():

    on "show" action Function(global_codex_list)

    viewport:
        style_prefix "cat"
        yalign 0.5 xpos 350 ysize 400 xsize 380 scrollbars "vertical" mousewheel True draggable True
        vbox:
            spacing 30
            button:
                    xysize(350,75)
                    add "gui/codex/btn_bg.png"
                    text "People" 
                    action [Hide("global_categories"),Show("global_entries", dissolve, global_people)]
            button:
                    xysize(350,75)
                    add "gui/codex/btn_bg.png"
                    text "Events" 
                    action [Hide("global_categories"),Show("global_entries", dissolve, global_events)]
            button:
                    xysize(350,75)
                    add "gui/codex/btn_bg.png"
                    text "Locations" 
                    action [Hide("global_categories"),Show("global_entries", dissolve, global_locations)]
            button:
                    xysize(350,75)
                    add "gui/codex/btn_bg.png"
                    text "Items" 
                    action [Hide("global_categories"),Show("global_entries",dissolve, global_items)]




screen global_entries(cat):
    viewport:
        style_prefix "cat"
        yalign 0.5 xpos 350 ysize 400 xsize 380 scrollbars "vertical" mousewheel True draggable True
        

        vbox:
            spacing 30
            for i in cat:
                button:
                        xysize(350,75)
                        add "gui/codex/btn_bg.png"
                        text i.title
                        action [SetVariable("current_entry", i.scr), SetVariable("entry_from", i.owner), Show("global_codex", dissolve)]



    button:
        xysize(86,86) pos(482,750)
        add "gui/codex/cat_btn.png"
        add "gui/codex/cat.png" at button_fade_light

        action [Hide("global_entries", dissolve), Show("global_categories", dissolve)]