screen talk():

    
    add "gui/talkie/bottom.png" yalign 1.0

    textbutton "Back" action Return() align(1.0, 1.0) offset(-60,-10) text_size 60

    
    vbox:
        ypos 300 xpos -880 ##button positions



        ####Indicator if viewport is scrollable
        ####Scrollbar looked ugly
        button:
            xysize(65,65) xalign 1.0 xoffset -400
            add "gui/talkie/scroll_bg.png"
            add "gui/talkie/scroll_arrow.png" at arrow_up
            
        viewport:
            style_prefix "talkie"
            scrollbars "vertical" mousewheel True draggable True
            vbox:
                spacing 20
                button:
                    text "Test"
                    at btn_slide

                    ## you can put a simple variable/renpy.seen_label here to determine which bg is shown
                    ## button.png -> with the X
                    ## button_empty.png -> without X
                    background "gui/talkie/button.png"
                    action NullAction()


                button:
                    text "Longer Test"
                    at btn_slide
                    background "gui/talkie/button_empty.png"
                    action NullAction()


                button:
                    text "Even longer test"
                    at btn_slide
                    background "gui/talkie/button_empty.png"
                    action NullAction()


                button:
                    text "The longest text to ever exists oooooo yeah!"
                    at btn_slide
                    background "gui/talkie/button_empty.png"
                    action NullAction()


                button:
                    text "Test"
                    at btn_slide
                    background "gui/talkie/button_empty.png"
                    action NullAction()



        ####Indicator if viewport is scrollable
        button:
            xysize(65,65) xalign 1.0 xoffset -400
            add "gui/talkie/scroll_bg.png"
            add "gui/talkie/scroll_arrow.png" at arrow_down
            

            
    



####ANIMATIONS AND STYLES--------------------------
transform arrow_up():
    subpixel True
    yzoom -1
    linear .5 yoffset -2
    linear .5 yoffset 5
    repeat
transform arrow_down():
    subpixel True
    linear .5 yoffset 2
    linear .5 yoffset -5
    repeat

transform btn_slide():
    xoffset -40
    on idle:
        easein .3 xoffset -40

    on hover:
        easein .3 xoffset 0
style talkie_vscrollbar:
    ypos 331 xpos -880
style talkie_viewport:
    ysize 560 xsize 1512
    
style talkie_text:
    align (1.0, 0.5)
    xsize 450
    xoffset -130 yoffset -2 line_spacing -10
    size 37
    #font  "gui/font/Klotee.ttf"
    idle_color "#876263"
    ## The color that is used for buttons and bars that are hovered.
    hover_color '#951b14'
    ## The color used for a text button when it is selected but not focused. A
    ## button is selected if it is the current screen or preference value.
    selected_color '#bfaa8f'
    ## The color used for a text button when it cannot be selected.
    insensitive_color '#8888887f'

style talkie_button:
    xysize(1512,119)
    #background "gui/talkie/button_empty.png"
    