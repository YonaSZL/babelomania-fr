
####Test variables
init python:
    class Item:
        def __init__(self, name, img, drop):
            self.name = name ##not shown but just in case
            self.img = img ##item icon
            self.drop = drop ##which dropdown menu will be shown


    test_item = Item("Apple", "gui/inventory/test.png", "item_drop")

default item_flashlight = Item(_("Flashlight"), "gui/inventory/flashlight.png", "flashlight_drop")
default item_taisho_note = Item(_("Door Code Note"), "gui/inventory/taisho_note.png", "taisho_note_drop")
default item_smartwatch = Item(_("Smartwatch"), "gui/inventory/smartwatch.png", "smartwatch_drop")

default inventory = []
default shigeo_inventory = [item_flashlight]
default delphine_inventory = [test_item]
screen inventory():

    modal True
    add "gui/inventory/bg.png"

    ###Title and close button
    label _("Inventory") text_font gui.name_text_font text_color "#951b14" text_size 42 xalign 0.5 ypos 199 
    textbutton _("Close") action Hide("inventory"):
        text_font gui.interface_text_font 
        text_size 38 
        xalign 0.5 ypos 658
        text_hover_color '#bfaa8f'
        text_selected_color '#bfaa8f'
        text_idle_color "#876263"
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_inventory.ogg"

    if current_char == "shigeo":
        $ char_inv = shigeo_inventory
    else:
        $ char_inv = delphine_inventory
    ##Calculating how man rows are needed
    if len(char_inv) % 4 != 0:
        $ grid_horizontal = int((len(char_inv) / 4)) + 1
    else:
        $ grid_horizontal = len(char_inv) / 4


    #Double checking row number calc
    #vbox:
    #    text "[grid_horizontal]"

    ##The item grid
    if len(char_inv) != 0:
        viewport:
            scrollbars "vertical" mousewheel True draggable True
            pos(616,287) xysize(700,317)


            grid 4 grid_horizontal:
                xspacing 20 yspacing 10
                for i in char_inv:
                    button:
                        idle_background "gui/inventory/cell.png"
                        hover_background "gui/inventory/cell_hover.png"
                        add i.img
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_item.ogg"
                        action CaptureFocus(i.drop)
    else:
        text _("Inventory empty") align(0.5, 0.5) yoffset -100 size 40 font gui.interface_text_font color '#bfaa8f'




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
    if GetFocusRect("flashlight_drop"):
        dismiss action ClearFocus("flashlight_drop")
        nearrect:
            focus "flashlight_drop"
            frame:
                style_prefix "dropdown"
                #modal True

                has vbox

                textbutton _("Inspect") action [ ClearFocus("flashlight_drop"), Show("notify", None, _("It's a rechargeable flashlight. Nothing remarkable about it.")) ] hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg"###Add whatever action is needed
                if flashlight_allowed:
                    if story_progress > 0:
                        if stat1 > 0:
                            if flashlight_use:
                                if flashlight_consume:
                                    textbutton _("Use") action [ ClearFocus("flashlight_drop"), Hide("inventory"), Play("sound4","audio/se/flashlight_off.ogg"), SetVariable("dark_environ", True), SetVariable("flashlight_use", False), SetVariable("flashlight_consume", False) ] hover_sound "audio/sfx/gui_hover.ogg"
                            else:
                                textbutton _("Use") action [ ClearFocus("flashlight_drop"), Hide("inventory"), Play("sound4","audio/se/flashlight_on.ogg"), SetVariable("dark_environ", False), SetVariable("flashlight_use", True), SetVariable("flashlight_consume", True) ] hover_sound "audio/sfx/gui_hover.ogg"
                        else:
                            textbutton _("Use") action Null() hover_sound "audio/sfx/gui_hover.ogg" tooltip _("Battery's Dead.")
                    else:
                        textbutton _("Use") action [ ClearFocus("flashlight_drop"), Hide("inventory"), Play("sound4","audio/se/flashlight_on.ogg"), Jump("first_flashlight_use") ] hover_sound "audio/sfx/gui_hover.ogg"
    if GetFocusRect("taisho_note_drop"):
        dismiss action ClearFocus("taisho_note_drop")
        nearrect:
            focus "taisho_note_drop"
            frame:
                style_prefix "dropdown"
                #modal True

                has vbox
                if taisho_note_inspected:
                    textbutton _("Inspect") action [ ClearFocus("taisho_note_drop"), Show("notify", None, _("It's the note Amina gave me. The code written on it is 19120730.")) ] hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg"###Add whatever action is needed
                else:
                    textbutton _("Inspect") action [ ClearFocus("taisho_note_drop"), Hide("inventory"), Jump("exp_taisho_1f_corridor_01_taisho_note") ] hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg"###Add whatever action is needed
                textbutton _("Use") action [ ClearFocus("taisho_note_drop"), Show("notify", None, _("There's nothing I can do with this.")) ] hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_item_use.ogg"
    if GetFocusRect("smartwatch_drop"):
        dismiss action ClearFocus("smartwatch_drop")
        nearrect:
            focus "smartwatch_drop"
            frame:
                style_prefix "dropdown"
                #modal True

                has vbox

                textbutton _("Inspect") action [ ClearFocus("smartwatch_drop"), Show("notify", None, _("It's a Smartwatch I got from Gaspard. It connects wirelessly to a phone.")) ] hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_confirm.ogg"###Add whatever action is needed

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

