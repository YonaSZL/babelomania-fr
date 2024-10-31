﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image ctc_blink:
    "gui/ctc.png"
    alpha 1.0
    easein 1 alpha .0
    easein 1 alpha 1.0
    repeat

define e = Character("Eileen",ctc="ctc_blink", ctc_position="nestled")
define d = Character(None, kind=nvl, ctc="ctc_blink", ctc_position="nestled")

define s = Character("Other Eileen", image="eileen", what_xoffset=35,ctc="ctc_blink", ctc_position="nestled")
image side eileen = "gui/side_image.png"

##Shigeo
define sh = Character(_("Shigeo Arata"), what_prefix='\"', what_suffix='\"', image="shigeo", ctc="ctc_blink", ctc_position="nestled")
define sh_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="shigeo", ctc="ctc_blink", ctc_position="nestled")
define sh_xi = Character(_("?????"), what_prefix='{i}', image="shigeo", ctc="ctc_blink", ctc_position="nestled")
define sh_n = Character(_("Shigeo Arata"), what_suffix='\"', image="shigeo", ctc="ctc_blink", ctc_position="nestled")
define sh_i = Character(_("Shigeo Arata"), what_prefix='{i}', image="shigeo", ctc="ctc_blink", ctc_position="nestled")
define sh_st = Character(_("Shigeo Arata"), what_prefix='{u}\"', what_suffix='\"', image="shigeo", ctc="ctc_blink", ctc_position="nestled")
image side shigeo = LayeredImageProxy("Shigeo_por")
image side shigeo nulla = Null()
image side shigeo darko = LayeredImageProxy("Shigeo_por", Transform(matrixcolor=TintMatrix(Color("#000", alpha=0.85))))

##Tabitha
define ta = Character(_("Tabitha"), what_prefix='\"', what_suffix='\"', image="tabitha", ctc="ctc_blink", ctc_position="nestled")
define ta_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="tabitha", ctc="ctc_blink", ctc_position="nestled")
define ta_n = Character(_("Tabitha"), what_suffix='\"', image="tabitha", ctc="ctc_blink", ctc_position="nestled")
define ta_st = Character(_("Tabitha"), what_prefix='{u}\"', what_suffix='\"', image="tabitha", ctc="ctc_blink", ctc_position="nestled")
image side tabitha = LayeredImageProxy("Tabitha_por")
image side tabitha nulla = Null()
image side tabitha darko = LayeredImageProxy("Tabitha_por", Transform(matrixcolor=TintMatrix(Color("#000", alpha=0.85))))

##Amina
define am = Character(_("Amina Abbas"), what_prefix='\"', what_suffix='\"', image="amina", ctc="ctc_blink", ctc_position="nestled")
define am_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="amina", ctc="ctc_blink", ctc_position="nestled")
define am_n = Character(_("Amina Abbas"), what_suffix='\"', image="amina", ctc="ctc_blink", ctc_position="nestled")
define am_st = Character(_("Amina Abbas"), what_prefix='{u}\"', what_suffix='\"', image="amina", ctc="ctc_blink", ctc_position="nestled")
image side amina = LayeredImageProxy("Amina_por")
image side amina nulla = Null()
image side amina darko = LayeredImageProxy("Amina_por", Transform(matrixcolor=TintMatrix(Color("#000", alpha=0.85))))

##Francesco
define fr = Character(_("Francesco Colombo"), what_prefix='\"', what_suffix='\"', image="francesco", ctc="ctc_blink", ctc_position="nestled")
define fr_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="francesco", ctc="ctc_blink", ctc_position="nestled")
define fr_n = Character(_("Francesco Colombo"), what_suffix='\"', image="francesco", ctc="ctc_blink", ctc_position="nestled")
define fr_xst = Character(_("?????"), what_prefix='{u}\"', what_suffix='\"', image="francesco", ctc="ctc_blink", ctc_position="nestled")
define fr_st = Character(_("Francesco Colombo"), what_prefix='{u}\"', what_suffix='\"', image="francesco", ctc="ctc_blink", ctc_position="nestled")
image side francesco = LayeredImageProxy("Francesco_por")
image side francesco nulla = Null()
image side francesco darko = LayeredImageProxy("Francesco_por", Transform(matrixcolor=TintMatrix(Color("#000", alpha=0.85))))

##Gaspard
define ga = Character(_("Gaspard Faucigny"), what_prefix='\"', what_suffix='\"', image="gaspard", ctc="ctc_blink", ctc_position="nestled")
define ga_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="gaspard", ctc="ctc_blink", ctc_position="nestled")
define ga_n = Character(_("Gaspard Faucigny"), what_suffix='\"', image="gaspard", ctc="ctc_blink", ctc_position="nestled")
define ga_i = Character(_("Gaspard Faucigny"), what_prefix='{i}', image="gaspard", ctc="ctc_blink", ctc_position="nestled")
define ga_st = Character(_("Gaspard Faucigny"), what_prefix='{u}\"', what_suffix='\"', image="gaspard", ctc="ctc_blink", ctc_position="nestled")
image side gaspard = LayeredImageProxy("Gaspard_por")
image side gaspard nulla = Null()
image side gaspard darko = LayeredImageProxy("Gaspard_por", Transform(matrixcolor=TintMatrix(Color("#000", alpha=0.85))))

##Habiki
define ha = Character(_("Professor Habiki"), what_prefix='\"', what_suffix='\"', image="habiki", ctc="ctc_blink", ctc_position="nestled")
define ha_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="habiki", ctc="ctc_blink", ctc_position="nestled")
define ha_n = Character(_("Professor Habiki"), what_suffix='\"', image="habiki", ctc="ctc_blink", ctc_position="nestled")
define ha_st = Character(_("Professor Habiki"), what_prefix='{u}\"', what_suffix='\"', image="habiki", ctc="ctc_blink", ctc_position="nestled")
image side habiki = LayeredImageProxy("Habiki_por")
image side habiki nulla = Null()
image side habiki darko = LayeredImageProxy("Habiki_por", Transform(matrixcolor=TintMatrix(Color("#000", alpha=0.85))))

##Minor Characters
define tb_n = Character(_("Academic Invitee"), what_prefix='\"', what_suffix='\"', ctc="ctc_blink", ctc_position="nestled")
define tb_n2 = Character(_("Fashionable Invitee"), what_prefix='\"', what_suffix='\"', ctc="ctc_blink", ctc_position="nestled")

##Delphine
define de = Character(_("Delphine Colombo"), what_prefix='\"', what_suffix='\"', image="delphine", ctc="ctc_blink", ctc_position="nestled")
define de_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="delphine", ctc="ctc_blink", ctc_position="nestled")
define de_xi = Character(_("?????"), what_prefix='{i}', image="delphine", ctc="ctc_blink", ctc_position="nestled")
define de_i = Character(_("Delphine Colombo"), what_prefix='{i}', image="delphine", ctc="ctc_blink", ctc_position="nestled")
define de_n = Character(_("Delphine Colombo"), what_suffix='\"', image="delphine", ctc="ctc_blink", ctc_position="nestled")
define de_st = Character(_("Delphine Colombo"), what_prefix='{u}\"', what_suffix='\"', image="delphine", ctc="ctc_blink", ctc_position="nestled")
image side delphine = LayeredImageProxy("Delphine_por")
image side delphine nulla = Null()
image side delphine darko = LayeredImageProxy("Delphine_por", Transform(matrixcolor=TintMatrix(Color("#000", alpha=0.85))))

##User Defined Transitions

define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define blood = Fade(0.1, 0.0, 0.1, color="#8A0707")
define bloodo = Fade(0.1, 3.0, 3.0, color="#8A0707")

define Reveal = Dissolve(2.0, alpha=False, time_warp=None)
define Reveal3 = Dissolve(3.0, alpha=False, time_warp=None)
define Reveal5 = Dissolve(5.0, alpha=False, time_warp=None)
define quick_dissolve = Dissolve(0.20, alpha=False, time_warp=None)

define glitch_load = ImageDissolve("gui/transitions/glitch.jpg", 0.35, 32)
define glitch_unload = ImageDissolve("gui/transitions/glitch.jpg", 0.35, 32, reverse=True)

define glitch_load_5 = ImageDissolve("gui/transitions/glitch.jpg", 0.5, 32)
define glitch_unload_5 = ImageDissolve("gui/transitions/glitch.jpg", 0.5, 32, reverse=True)

define glitch_load15 = ImageDissolve("gui/transitions/glitch.jpg", 1.5, 32)
define glitch_unload15 = ImageDissolve("gui/transitions/glitch.jpg", 1.5, 32, reverse=True)

##Default Variables
default persistent.vertical_clear = False
default persistent.gore = True
default tooltip = "None"
default mouse_pos = None
default story_progress = 0
default current_location = "None"
default dark_environ = False
default briefcase_carry = False
default numeric_puzzle_input = "None"
default language_switcher = "English"
#Defining Music Channels
init python:
    renpy.music.register_channel("LoNoise", "sfx",)
    renpy.music.register_channel("LoNoise2", "sfx",)
    renpy.music.register_channel("LoNoise3", "sfx",)
    renpy.music.register_channel("sound2", "sfx", loop=False) #Pan Left Channel
    renpy.music.register_channel("sound3", "sfx", loop=False) #Pan Right Channel
    renpy.music.register_channel("sound4", "sfx", loop=False)
    renpy.music.register_channel("sound5", "sfx", loop=False)
    renpy.music.register_channel("sound6", "sfx", loop=False)
    renpy.music.register_channel("sound7", "sfx", loop=False)

init -1:
    transform ta_big:
        yoffset 30
        transform_anchor True
    transform ta_med:
        yoffset 70
        zoom 0.70
        transform_anchor True
    transform ga_big:
        yoffset 117
        transform_anchor True
    transform ga_med:
        yoffset 175
        zoom 0.70
        transform_anchor True
    transform sh_big:
        yoffset 123
        transform_anchor True
    transform sh_med:
        yoffset 185
        zoom 0.70
        transform_anchor True
    transform ha_big:
        yoffset 215
        zoom 0.90
        transform_anchor True
    transform ha_med:
        yoffset 290
        zoom 0.61
        transform_anchor True
    transform am_big:
        yoffset 185
        transform_anchor True
    transform am_med:
        yoffset 260
        zoom 0.70
        transform_anchor True
    transform fr_big:
        yoffset 123
        transform_anchor True
    transform fr_med:
        yoffset 185
        zoom 0.70
        transform_anchor True
    transform de_big:
        yoffset 123
        transform_anchor True
    transform de_med:
        yoffset 185
        zoom 0.70
        transform_anchor True

label splashscreen:
    scene black
    pause 1.5
    call screen language with dissolve
    scene black
    pause 1.5
    scene intro_00 with dissolve
    pause 2.5
    scene black with Reveal3
    pause 0.5
    scene intro_01 with dissolve
    pause 1.0
    play music "audio/bgm/babelomania.ogg"
    pause 1.5
    scene black with Reveal3
    pause 0.5
    scene intro_02 with dissolve
    pause 3.0
    scene black with Reveal3
    pause 0.5
    scene intro_03 with dissolve
    pause 2.5
    scene black with Reveal3
    pause 0.5
    scene main_menu_bg with Reveal3
    pause 3.0
    play sound "audio/sfx/gui_slots_confirm.ogg"
    scene main_menu_bg_logo with glitch_load_5
    pause 1.5
    scene white with quick_dissolve
    pause 0.5
    return
