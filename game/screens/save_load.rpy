## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load


## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 384
define config.thumbnail_height = 216


screen save():

    tag menu

    #add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use file_slots(_("Save"))


screen load():

    tag menu

    #add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(
        pattern=_("Page {}"), auto=_("Automatic saves"),
        quick=_("Quick saves"))

    use game_menu(title)

    fixed:
        xsize 1500 xalign 0.5 xoffset -150
        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The page name, which can be edited by clicking on it.
        ## This can be pretty easily removed if you want.
        ## Don't forget to also remove the `default` at the top if so.
        button:
            style "page_label"
            key_events True
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value
            at page_rotate

        ## The grid of file slots.
        grid 2 2:
            style_prefix "slot"
            xoffset 40

            for i in range(2*2):
                $ slot = i + 1

                button:
                    action NullAction()
                    #has vbox
                    hover_sound "audio/sfx/gui_hover.ogg"
                    
                    
                    frame:
                        background None
                        add "gui/button/time_bg.png" at save_time
                        text FileTime(slot,
                                format=_("{#file_time}%a, %b %d %Y, %H:%M"),
                                empty=_("empty slot")):
                            style "slot_time_text"
                            
                            at save_time
                    add "gui/button/slot_idle_background.png" offset(-15,-15)
                    add FileScreenshot(slot) xalign 0.5 xysize(370,203) offset(-1,7)


                    button:
                        background None focus_mask True
                        xysize(101,101) yoffset 40 xoffset -72
                        add "gui/button/del_bg.png"
                        add "gui/button/del.png" at button_fade
                        action FileDelete(slot)
                        activate_sound "audio/sfx/gui_slots_confirm.ogg"
                        
                    hbox:
                        style_prefix "quick"
                        offset(-0, 25)

                        textbutton _("Save") action FileSave(slot) text_selected_hover_color '#bfaa8f' text_selected_idle_color "#876263" activate_sound "audio/sfx/gui_slots_confirm.ogg"
                        textbutton _("Load") action FileLoad(slot) text_selected_hover_color '#bfaa8f' text_selected_idle_color "#876263" activate_sound "audio/sfx/gui_slots_confirm.ogg"

                    ## https://www.fabriziomusacchio.com/blog/2021-08-15-strftime_Cheat_Sheet/

                

                    # This means the player can hover this save
                    # slot and hit delete to delete it
                    key "save_delete" action FileDelete(slot)

                    
                    

        imagemap:
            idle "gui/button/save_idle.png"
            hover "gui/button/save_hover.png"

            hotspot(757, 868, 54, 35) action FilePagePrevious() focus_mask None hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"
            hotspot(1130, 868, 66, 35) action FilePageNext() focus_mask None hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"
        ## Buttons to access other pages.
        vbox:
            style_prefix "page"
            hbox:
                
                #textbutton _("<") action FilePagePrevious()

                

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page) hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"

                #textbutton _(">") action FilePageNext()




style page_label:
    xpadding 75
    ypadding 5
    xalign 1.0
    yalign 0.5
    xoffset 10


style page_label_text:
    textalign 0.5
    layout "subtitle"
    idle_color u"#4f331d"
    hover_color '#bfaa8f'
    font gui.name_text_font

style slot_grid:
    xalign 0.5
    yalign 0.5
    yspacing 50
    xspacing 75

style slot_time_text:
    size 20 yoffset 10
    xalign 0.5
    font gui.interface_text_font
    color '#bfaa8f'

style slot_vbox:
    spacing 12

style slot_button:
    xysize (414, 246)
    padding (15, 15, 15, 15)
    #background "gui/button/slot_idle_background.png"

style slot_button_text:
    size 21
    xalign 0.5
    idle_color '#aaaaaa'
    hover_color '#ff8335'
    selected_idle_color '#ffffff'

style page_hbox:
    xalign 0.5
    spacing -13

style page_vbox:
    #xalign 0.5
    #yalign 1.0
    spacing 5
    pos(806, 865)

style page_button:
    padding (15, 6, 15, 6)
    xalign 0.5
style page_button_text:
    size 35
    idle_color u"#8c5a5b"
    hover_color u"#bfaa8f"
    selected_idle_color u"#bfaa8f"

