
####Test variables
init python:
    class Item:
        def __init__(self, name, img, drop):
            self.name = name ##not shown but just in case
            self.img = img ##item icon
            self.drop = drop ##which dropdown menu will be shown


    test_item = Item("Apple", "gui/inventory/test.png", "item_drop")

default inventory = [test_item,test_item,test_item,test_item,test_item]
screen inventory():

    modal True
    add "gui/inventory/bg.png"

    ###Title and close button
    label _("Inventory") text_font "gui/font/Sok Brubah.ttf" text_color "#951b14" text_size 42 xalign 0.5 ypos 199 
    textbutton _("Close") action Hide("inventory"):
        text_font "gui/font/Klotee.ttf" 
        text_size 38 
        xalign 0.5 ypos 658
        text_hover_color '#bfaa8f'
        text_selected_color '#bfaa8f'
        text_idle_color "#876263"
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_inventory.ogg"


    ##Calculating how man rows are needed
    if len(inventory) % 4 != 0:
        $ grid_horizontal = int((len(inventory) / 4)) + 1
    else:
        $ grid_horizontal = len(inventory) / 4


    #Double checking row number calc
    #vbox:
    #    text "[grid_horizontal]"

    ##The item grid
    if len(inventory) != 0:
        viewport:
            scrollbars "vertical" mousewheel True draggable True
            pos(616,287) xysize(700,317)


            grid 4 grid_horizontal:
                xspacing 20 yspacing 10
                for i in inventory:
                    button:
                        add "gui/inventory/cell.png"
                        idle_foreground i.img
                        hover_foreground  At(i.img, outline_transform(2, "#876a33", 4.0))
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_item.ogg"
                        action CaptureFocus(i.drop)
    else:
        text _("Inventory empty") align(0.5, 0.5) yoffset -100 size 40 font "gui/font/Klotee.ttf" color '#bfaa8f'




    #####Dropdown menu for item uses
    #####Each item needs its own section
    if GetFocusRect("item_drop"):
        dismiss action ClearFocus("item_drop")
        nearrect:
            focus "item_drop"
            frame:
                style_prefix "dropdown"
                #modal True

                has vbox

                textbutton _("Inspect") action [ ClearFocus("item_drop"), Hide("inventory") ] hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg"###Add whatever action is needed
                textbutton _("Use") action [ ClearFocus("item_drop"), Hide("inventory") ] hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_item_use.ogg"
                

style dropdown_vbox:
    spacing -5
style dropdown_button:
    padding (10, 15, 10, 15)
    xsize 153
style dropdown_text:
    xalign 0.5
    textalign 0.5
style dropdown_frame:
    xsize 153

