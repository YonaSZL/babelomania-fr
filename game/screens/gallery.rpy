init python:
    gallery_thumb_size = (400, 225)

    ## Set up the gallery
    g = Gallery()
    g.locked_button = Transform("gui/gallery/locked.png", xysize=gallery_thumb_size)
    g.idle_border = Transform("gui/gallery/border.png", xysize=gallery_thumb_size)
    g.hover_border = Transform("gui/gallery/border_h.png", xysize=gallery_thumb_size)



    ###Gallery buttons
    g.button("cg1")

    ###unlock_image means that the image will be unlocked once it has been shown -- no need for persistent variables
    g.unlock_image("test")

    g.button("cg2")
    g.unlock_image("test")

    g.button("cg3")
    g.unlock_image("test")

    g.button("cg4")
    g.unlock_image("test")
    ##Actual Images
    g.button("intro_01")
    g.unlock_image("intro_hand_A")

    g.button("intro_02")
    g.unlock_image("intro_corpse")

    g.button("intro_03")
    g.unlock_image("intro_hand_B")

    g.button("intro_04")
    g.unlock_image("intro_tabitha")

    g.button("intro_05")
    g.unlock_image("intro_tabitha_side")

    g.button("intro_06")
    g.unlock_image("intro_reach")

    g.button("intro_07")
    g.unlock_image("intro_phone_a")

    g.button("intro_08")
    g.unlock_image("intro_phone_b")

    g.button("intro_09")
    g.unlock_image("intro_phone_c")

    g.button("story_01_01")
    g.unlock_image("bathroom_painting")

    g.button("story_01_02")
    g.unlock_image("tabitha_grab")

    g.button("story_01_03")
    g.unlock_image("gaspard_turn_00")

    g.button("story_01_04")
    g.unlock_image("gaspard_turn_01")

    g.button("story_01_05")
    g.unlock_image("gaspard_turn_02")

    g.button("story_01_06")
    g.unlock_image("gaspard_turn_03")

    g.button("story_01_07")
    g.unlock_image("gaspard_turn_04")

    g.button("story_01_08")
    g.unlock_image("gaspard_focus_01")

    g.button("story_01_09")
    g.unlock_image("gaspard_focus_02")

    g.button("story_01_10")
    g.unlock_image("gaspard_rip")

    g.button("story_01_11")
    g.unlock_image("gaspard_tear")

    g.button("story_02_01")
    g.unlock_image("francesco_flashback")

    g.button("story_02_02")
    g.unlock_image("open_folder")

    g.button("story_02_03")
    g.unlock_image("closed_folder")

    g.button("story_02_04")
    g.unlock_image("fudo_appears_04")

    g.button("story_03_01")
    g.unlock_image("gaspard_flex")

###Test CG
image test = "gui/test_cg.png"


####---------------------
default gallery_page = 1

screen gallery():

    tag menu

    use game_menu("Gallery")
    

    use expression ("gal_"  + str(gallery_page))
    imagemap:
        idle "gui/button/dec.png"
        hover "gui/button/dec.png"

        hotspot(757, 868, 54, 35) action FilePagePrevious() focus_mask None hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg"
        hotspot(1130, 868, 66, 35) action FilePageNext() focus_mask None hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg"
        ## Buttons to access other pages.
    vbox:
        style_prefix "page"
        hbox:

            ###This will make 5 buttons
            for page in range(1, 6):
                textbutton "[page]" action SetVariable("gallery_page", page) hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg"

            add "gui/button/dec_small.png" offset(10,9)


#####Gallery screens


###For more gallery pages just copy this and increase the number (gal_6, gal_7 etc.)
screen gal_1():

    fixed:
        xsize 1500 xalign 0.5 xoffset -150

        grid 2 2:
            style_prefix "slot"
            xoffset 40


            add g.make_button("intro_01", Transform("intro_hand_A", xysize=gallery_thumb_size))
            add g.make_button("intro_02", Transform("intro_corpse", xysize=gallery_thumb_size))
            add g.make_button("intro_03", Transform("intro_hand_B", xysize=gallery_thumb_size))
            if renpy.seen_image("intro_tabitha"):
                button:
                    xysize(400,225)
                    background Transform("intro_tabitha", crop=(0,0,1920,1080), xysize=gallery_thumb_size)
                    idle_foreground Transform("gui/gallery/border.png", xysize=gallery_thumb_size)
                    hover_foreground Transform("gui/gallery/border_h.png", xysize=gallery_thumb_size)
                    action Show("intro_tabitha_viewport")
            else:
                add g.make_button("intro_04", Transform("intro_tabitha", xysize=gallery_thumb_size))

screen intro_tabitha_viewport():
    modal True
    button:
        xysize(1920,1080)
        viewport:
            xysize(1920,1080)
            pos(0, 0)
            draggable True
            add "intro_tabitha"
        action Hide("intro_tabitha_viewport")

screen gal_2():

    fixed:
        xsize 1500 xalign 0.5 xoffset -150

        grid 2 2:
            style_prefix "slot"
            xoffset 40


            if renpy.seen_image("intro_tabitha_side"):
                button:
                    xysize(400,225)
                    background Transform("intro_tabitha_side", crop=(0,0,1920,1080), xysize=gallery_thumb_size)
                    idle_foreground Transform("gui/gallery/border.png", xysize=gallery_thumb_size)
                    hover_foreground Transform("gui/gallery/border_h.png", xysize=gallery_thumb_size)
                    action Show("intro_tabitha_side_viewport")
            else:
                add g.make_button("intro_05", Transform("intro_tabitha_side", xysize=gallery_thumb_size))
            if renpy.seen_image("intro_reach"):
                button:
                    xysize(400,225)
                    background Transform("intro_reach_base", crop=(0,0,1920,1080), xysize=gallery_thumb_size)
                    idle_foreground Transform("gui/gallery/border.png", xysize=gallery_thumb_size)
                    hover_foreground Transform("gui/gallery/border_h.png", xysize=gallery_thumb_size)
                    action Show("intro_reach_base_viewport")
            else:
                add g.make_button("intro_06", Transform("intro_reach", xysize=gallery_thumb_size))
            add g.make_button("intro_07", Transform("intro_phone_a", xysize=gallery_thumb_size))
            add g.make_button("intro_08", Transform("intro_phone_b", xysize=gallery_thumb_size))

screen intro_tabitha_side_viewport():
    modal True
    button:
        xysize(1920,1080)
        viewport:
            xysize(1920,1080)
            pos(0, 0)
            draggable True
            add "intro_tabitha_side"
        action Hide("intro_tabitha_side_viewport")

screen intro_reach_base_viewport():
    modal True
    button:
        xysize(1920,1080)
        add "intro_reach_base"
        action Hide("intro_reach_base_viewport")

screen gal_3():

    fixed:
        xsize 1500 xalign 0.5 xoffset -150

        grid 2 2:
            style_prefix "slot"
            xoffset 40


            add g.make_button("intro_09", Transform("intro_phone_c", xysize=gallery_thumb_size))
            add g.make_button("story_01_01", Transform("bathroom_painting", xysize=gallery_thumb_size))
            if renpy.seen_image("tabitha_grab"):
                button:
                    xysize(400,225)
                    background Transform("tabitha_grab", crop=(880,0,1920,1080), xysize=gallery_thumb_size)
                    idle_foreground Transform("gui/gallery/border.png", xysize=gallery_thumb_size)
                    hover_foreground Transform("gui/gallery/border_h.png", xysize=gallery_thumb_size)
                    action Show("tabitha_grab_viewport")
            else:
                add g.make_button("story_01_02", Transform("tabitha_grab", xysize=gallery_thumb_size))
            add g.make_button("story_01_03", Transform("gaspard_turn_00", xysize=gallery_thumb_size))

screen tabitha_grab_viewport():
    modal True
    button:
        xysize(1920,1080)
        viewport:
            xysize(1920,1080)
            pos(0, 0)
            draggable True
            add "tabitha_grab"
        action Hide("tabitha_grab_viewport")

screen gal_4():

    fixed:
        xsize 1500 xalign 0.5 xoffset -150

        grid 2 2:
            style_prefix "slot"
            xoffset 40


            add g.make_button("story_01_04", Transform("gaspard_turn_01", xysize=gallery_thumb_size))
            add g.make_button("story_01_05", Transform("gaspard_turn_02", xysize=gallery_thumb_size))
            add g.make_button("story_01_06", Transform("gaspard_turn_03", xysize=gallery_thumb_size))
            add g.make_button("story_01_07", Transform("gaspard_turn_04", xysize=gallery_thumb_size))


screen gal_5():

    fixed:
        xsize 1500 xalign 0.5 xoffset -150

        grid 2 2:
            style_prefix "slot"
            xoffset 40


            add g.make_button("story_01_08", Transform("gaspard_focus_01", xysize=gallery_thumb_size))
            add g.make_button("story_01_09", Transform("gaspard_focus_02", xysize=gallery_thumb_size))
            add g.make_button("story_01_10", Transform("gaspard_rip", xysize=gallery_thumb_size))
            add g.make_button("story_01_11", Transform("gaspard_tear", xysize=gallery_thumb_size))

screen gal_6():

    fixed:
        xsize 1500 xalign 0.5 xoffset -150

        grid 2 2:
            style_prefix "slot"
            xoffset 40


            add g.make_button("story_02_01", Transform("francesco_flashback", xysize=gallery_thumb_size))
            add g.make_button("story_02_02", Transform("open_folder", xysize=gallery_thumb_size))
            add g.make_button("story_02_03", Transform("closed_folder", xysize=gallery_thumb_size))
            add g.make_button("story_02_04", Transform("fudo_appears_04", xysize=gallery_thumb_size))

screen gal_6():

    fixed:
        xsize 1500 xalign 0.5 xoffset -150

        grid 2 2:
            style_prefix "slot"
            xoffset 40


            add g.make_button("story_03_01", Transform("gaspard_flex", xysize=gallery_thumb_size))
            #add g.make_button("story_02_02", Transform("open_folder", xysize=gallery_thumb_size))
            #add g.make_button("story_02_03", Transform("closed_folder", xysize=gallery_thumb_size))
            #add g.make_button("story_02_04", Transform("fudo_appears_04", xysize=gallery_thumb_size))