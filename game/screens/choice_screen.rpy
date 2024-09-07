
## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing 33

style choice_button:
    is default # This means it doesn't use the usual button styling
    xysize (1003, None)
    background Frame("gui/button/choice_idle_background.png",
        150, 34, 150, 34, tile=True)
    #padding (12, 12)
    top_padding 16 bottom_padding 16
    left_padding 55 right_padding 55

style choice_button_text:
    is default # This means it doesn't use the usual button text styling
    xalign 0.5 yalign 0.5
    textalign 0.5
    idle_color '#bfaa8f'
    hover_color '#951b14'
    insensitive_color "#444"
