init python:

    def dark_flashlight(st, at):
        return Transform("flash_circle", None, anchor=(0.5,0.5), pos=renpy.get_mouse_pos()), 1.0/30.0

##System Images

image main_menu_bg = "gui/main_menu/main_menu_bg.jpg"

image intro_00 = "gui/main_menu/intro_00.jpg"
image intro_01 = "gui/main_menu/intro_01.jpg"
image intro_02 = "gui/main_menu/intro_02.jpg"
image intro_03 = "gui/main_menu/intro_03.jpg"

##Chateau BG

image chateau_setting = "images/bgs/chateau/chateau_setting.jpg"

##Baroque Building

image bar_reception = "images/bgs/baroque/bar_reception.jpg"
image bar_corr_recep = "images/bgs/baroque/bar_corr_recep.jpg"
image bar_bathroom = "images/bgs/baroque/bar_bathroom.jpg"
image bathroom_painting = "images/bgs/baroque/bathroom_painting.jpg"

##Taisho Building

image flash_circle = "images/bgs/flash_circle.png"
image dark_flashlight = DynamicDisplayable(dark_flashlight)
image flash_1f_study = "images/bgs/taisho/flash_1f_study.jpg"
