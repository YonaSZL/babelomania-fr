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

        hotspot(757, 868, 54, 35) action FilePagePrevious() focus_mask None
        hotspot(1130, 868, 66, 35) action FilePageNext() focus_mask None
        ## Buttons to access other pages.
    vbox:
        style_prefix "page"
        hbox:

            ###This will make 5 buttons
            for page in range(1, 6):
                textbutton "[page]" action SetVariable("gallery_page", page)

            add "gui/button/dec_small.png" offset(10,9)


#####Gallery screens


###For more gallery pages just copy this and increase the number (gal_6, gal_7 etc.)
screen gal_1():

    fixed:
        xsize 1500 xalign 0.5 xoffset -150

        grid 2 2:
            style_prefix "slot"
            xoffset 40


            add g.make_button("cg1", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
            add g.make_button("cg2", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
            add g.make_button("cg3", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
            add g.make_button("cg4", Transform("gui/test_cg.png", xysize=gallery_thumb_size))


screen gal_2():

    fixed:
        xsize 1500 xalign 0.5 xoffset -150

        grid 2 2:
            style_prefix "slot"
            xoffset 40


            add g.make_button("cg1", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
            add g.make_button("cg2", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
            add g.make_button("cg3", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
            add g.make_button("cg4", Transform("gui/test_cg.png", xysize=gallery_thumb_size))


screen gal_3():

    fixed:
        xsize 1500 xalign 0.5 xoffset -150

        grid 2 2:
            style_prefix "slot"
            xoffset 40


            add g.make_button("cg1", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
            add g.make_button("cg2", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
            add g.make_button("cg3", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
            add g.make_button("cg4", Transform("gui/test_cg.png", xysize=gallery_thumb_size))


screen gal_4():

    fixed:
        xsize 1500 xalign 0.5 xoffset -150

        grid 2 2:
            style_prefix "slot"
            xoffset 40


            add g.make_button("cg1", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
            add g.make_button("cg2", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
            add g.make_button("cg3", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
            add g.make_button("cg4", Transform("gui/test_cg.png", xysize=gallery_thumb_size))


screen gal_5():

    fixed:
        xsize 1500 xalign 0.5 xoffset -150

        grid 2 2:
            style_prefix "slot"
            xoffset 40


            add g.make_button("cg1", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
            add g.make_button("cg2", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
            add g.make_button("cg3", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
            add g.make_button("cg4", Transform("gui/test_cg.png", xysize=gallery_thumb_size))
