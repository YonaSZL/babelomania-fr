default flash_zm_lvl = 1.0
default flash_zm_hpn = True

init python:

    def dark_flashlight(st, at):
        global flash_zm_lvl
        global flash_zm_hpn
        if flash_zm_hpn:
            flash_zm_lvl += 0.002
            if flash_zm_lvl >= 1.15:
                flash_zm_hpn = False
        if flash_zm_hpn == False:
            flash_zm_lvl -= 0.002
            if flash_zm_lvl <= 1.00:
                flash_zm_hpn = True
        return Transform("flash_circle", None, anchor=(0.5,0.5), zoom=flash_zm_lvl, pos=renpy.get_mouse_pos()), 1.0/30.0

##System Images

image main_menu_bg = "gui/main_menu/main_menu_bg.jpg"
image main_menu_bg_logo = "gui/main_menu/main_menu_bg_logo.jpg"
image darkness_layer = "gui/darkness_layer.png"

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

image bar_reception_mood = "images/bgs/baroque/bar_reception_mood.jpg"
image bar_reception_mood_video = "images/bgs/baroque/bar_reception_mood_video.jpg"
image bar_reception_mood_video_glitch_base = At("images/bgs/baroque/bar_reception_mood_video.jpg", Static)
image bar_reception_mood_video_glitch:
    "bar_reception_mood_video"
    xalign 0.5
    yalign 0.5
    linear 10.0 zoom 1.5

##Taishō Building

image flash_circle = "images/bgs/flash_circle.png"
image dark_flashlight = DynamicDisplayable(dark_flashlight)
image darkness_layers = ConditionSwitch(
    "dark_environ == True", "darkness_layer",
    "flashlight_use == True", "dark_flashlight"
)

image taisho_1f_study_bare = "images/bgs/taisho/1f_study_bare.jpg"
image taisho_1f_study_flashlight = "images/bgs/taisho/1f_study_flashlight.jpg"
image taisho_1f_study_base = ConditionSwitch(
    "story_progress == 0", "taisho_1f_study_flashlight",
    "story_progress > 0", "taisho_1f_study_bare"
)
layeredimage taisho_1f_study:
    group bottom:
        attribute base default:
            "taisho_1f_study_base"
    group top:
        attribute top_dark default:
            "darkness_layers"

image taisho_1f_corridor = "images/bgs/taisho/1f_corridor.jpg"
image taisho_1f_side_meet_base = "images/bgs/taisho/taisho_1f_side_meet.jpg"
layeredimage taisho_1f_side_meet:
    group bottom:
        attribute base default:
            "taisho_1f_side_meet_base"
    group top:
        attribute top_dark default:
            "darkness_layers"

image taisho_1f_tabitha_base = "images/bgs/taisho/taisho_1f_tabitha.jpg"

layeredimage taisho_1f_tabitha:
    group bottom:
        attribute base default:
            "taisho_1f_tabitha_base"
    group top:
        attribute top_dark default:
            "darkness_layer"