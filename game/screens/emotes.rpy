image bubble_base:
    "gui/emotes/base.png"
    yzoom 0 xzoom 0 xanchor 1.0 yanchor 1.0 xoffset 170 yoffset 270
    easein 0.3 yzoom 1.2 xzoom 1.1
    easein 0.3 yzoom 1 xzoom 1
    pause 1.2
    easein 0.2 alpha 0 xoffset 160



image angry_1:
    "gui/emotes/angry_1.png"
    xanchor 0.5 yanchor 0.5 xoffset 70 yoffset 80 rotate -30
    alpha 0.0 zoom 1.3
    pause 0.6
    easein 0.2 alpha 1 zoom 0.8 rotate 0
    easein 0.1 zoom 1
    pause 0.9
    easein 0.2 alpha 0 xoffset 60

image angry_2:
    "gui/emotes/angry_2.png"
    xanchor 0.5 yanchor 0.5 xoffset 100 yoffset 160 rotate 30
    alpha 0.0 zoom 1.3
    pause 0.6
    easein 0.2 alpha 1 zoom 0.8 rotate 0
    easein 0.1 zoom 1
    pause 0.9
    easein 0.2 alpha 0 xoffset 90

image sweat_1:
    "gui/emotes/sweat1.png"
    xanchor 0.5 yanchor 0.0 xoffset 70 yoffset 20
    alpha 0.0 yzoom 0.9
    pause 0.6
    easein 0.2 alpha 1 yzoom 1.2 yoffset 50
    easein 0.1 yzoom 1
    pause 0.9
    easein 0.2 alpha 0 xoffset 60

image sweat_2:
    "gui/emotes/sweat2.png"
    xanchor 0.5 yanchor 0.0 xoffset 120 yoffset 40
    alpha 0.0 yzoom 0.9
    pause 0.6
    easein 0.2 alpha 1 yzoom 1.2 yoffset 110
    easein 0.1 yzoom 1
    pause 0.9
    easein 0.2 alpha 0 xoffset 110

image blush_1:
    "gui/emotes/blush_1.png"
    subpixel True
    xanchor 0.5 yanchor 0.5 xoffset 80 yoffset 80 rotate 0
    parallel:
        alpha 0.0
        pause 0.6
        easein 0.2 alpha 1
        easein 0.1
        pause 0.9
        easein 0.2 alpha 0 xoffset 60
    parallel:
        rotate 0
        linear 1 rotate 360
        repeat

image blush_2:
    "gui/emotes/blush_2.png"
    subpixel True
    xanchor 0.5 yanchor 0.5 xoffset 110 yoffset 150 rotate 0
    parallel:
        alpha 0.0
        pause 0.6
        easein 0.2 alpha 1
        easein 0.1
        pause 0.9
        easein 0.2 alpha 0 xoffset 100
    parallel:
        rotate 0
        linear 1 rotate 360
        repeat


image surprise:
    "gui/emotes/surprise.png"
    xanchor 0.5 yanchor 1.0 xoffset 85 yoffset 175
    alpha 0.0 yzoom 0
    pause 0.6
    easein 0.2 alpha 1 yzoom 1.2
    easein 0.1 yzoom 1
    pause 0.9
    easein 0.2 alpha 0 xoffset 75

image question:
    "gui/emotes/question.png"
    xanchor 0.5 yanchor 1.0 xoffset 85 yoffset 175 rotate -30
    alpha 0.0 yzoom 0
    pause 0.6
    easein 0.2 alpha 1 yzoom 1.2 rotate 10
    easein 0.1 yzoom 1 rotate 0
    pause 0.9
    easein 0.2 alpha 0 xoffset 75

image frustration:
    "gui/emotes/frust_1.png"
    pause 0.1
    "gui/emotes/frust_2.png"
    pause 0.1
    "gui/emotes/frust_3.png"
    pause 0.1
    "gui/emotes/frust_4.png"
    pause 0.1
    "gui/emotes/frust_5.png"
    pause 0.1
    repeat
transform frust():
    alpha 0.0
    pause 0.6
    easein 0.2 alpha 1
    pause 1
    easein 0.2 alpha 0 xoffset -10

screen emote(emotion,x,y):

    key "dismiss" action Hide('emote')
    frame:
        xsize 169 ysize 266
        background None
        ypos y xpos x xoffset -250
        add "bubble_base" offset (0,-20)
        if emotion == "angry":
            add "angry_1"
            add "angry_2"
        if emotion == "sweat":
            add "sweat_1" xoffset -10
            add "sweat_2" xoffset -10

        if emotion == "surprise":
            add "surprise"
        if emotion == "question":
            add "question"
        if emotion == "frustration":
            add "frustration" at frust
        if emotion == "blush":
            add "blush_1" xoffset -10
            add "blush_2" xoffset -10
            add "gui/emotes/littlesparkle.png" at frust yoffset 40 xoffset 25
    timer 2 action Hide('emote')
