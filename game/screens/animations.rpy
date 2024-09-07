transform save_time():
    yoffset 0
    on idle:
        linear .3 yoffset 0
    on hover:
        linear .3 yoffset -50


transform button_fade():
    alpha 0.4
    on idle:
        linear .15 alpha 0.3
    on hover:
        linear .15 alpha 1.0
    on insensitive:
        alpha 0.2

transform page_rotate():
    rotate 90


