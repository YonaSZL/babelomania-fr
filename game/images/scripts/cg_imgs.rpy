#Chapter Titlecards
image title_01 = "gui/titlecards/ch_01.jpg"

#Intro Sequence
image white = "gui/transitions/white.jpg"

image babelomania_logo = At("gui/babelomania_logo.png", glow_outline(4, "#951B14"))

image intro_disclaimer = "images/cgs/intro/intro_disclaimer.jpg"

image intro_babel = At("images/cgs/intro/intro_babel.png", redStatic)

image intro_hand_A = "images/cgs/intro/intro_hand_A.jpg"

image intro_hand_B = "images/cgs/intro/intro_hand_B.jpg"

image intro_corpse = "images/cgs/intro/intro_corpse.jpg"

image intro_tabitha = "images/cgs/intro/intro_tabitha.jpg"

image intro_tabitha_side = "images/cgs/intro/intro_tabitha_side.jpg"

image intro_reach_base = At("images/cgs/intro/intro_reach.jpg", Static)

image intro_reach:
    "intro_reach_base"
    xalign 0.5
    yalign 0.5
    linear 10.0 zoom 1.5

image intro_phone_a = "images/cgs/intro/intro_phone_a.jpg"
image intro_phone_b = "images/cgs/intro/intro_phone_b.jpg"
image intro_phone_c = "images/cgs/intro/intro_phone_c.jpg"

#Chapter 00

image tabitha_grab = "images/cgs/chapter_00/tabitha_grab.jpg"
image bathroom_painting = "images/cgs/chapter_00/bathroom_painting.jpg"
image bathroom_painting_glitch_base = At("images/cgs/chapter_00/bathroom_painting.jpg", Static)
image bathroom_painting_glitch:
    "bathroom_painting_glitch_base"
    alpha 0.0
    linear 0.2 alpha 0.5
    pause 0.2
    linear 0.2 alpha 0.0
image bathroom_painting_glitch_2:
    "bathroom_painting_glitch_base"
    alpha 0.0
    zoom 1.5
    linear 0.2 alpha 0.5
    pause 0.2
    linear 0.2 alpha 0.0

image gaspard_turn_00 = "images/cgs/chapter_00/gaspard/gaspard_turn_00.jpg"
image gaspard_turn_01 = "images/cgs/chapter_00/gaspard/gaspard_turn_01.jpg"
image gaspard_turn_02 = "images/cgs/chapter_00/gaspard/gaspard_turn_02.jpg"
image gaspard_turn_03 = "images/cgs/chapter_00/gaspard/gaspard_turn_03.jpg"
image gaspard_turn_04 = "images/cgs/chapter_00/gaspard/gaspard_turn_04.jpg"

image gaspard_rip = "images/cgs/chapter_00/gaspard/gaspard_rip.jpg"
image gaspard_tear = ConditionSwitch(
    "persistent.gore == True", "images/cgs/chapter_00/gaspard/gaspard_tear.jpg",
    "persistent.gore == False", "images/cgs/chapter_00/gaspard/gaspard_tear_censor.jpg"
) 