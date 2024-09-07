# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image ctc_blink:
    "gui/ctc.png"
    alpha 1.0
    easein 1 alpha .0
    easein 1 alpha 1.0
    repeat

define e = Character("Eileen",ctc="ctc_blink", ctc_position="nestled")

define s = Character("Other Eileen", image="eileen", what_xoffset=35,ctc="ctc_blink", ctc_position="nestled")


image side eileen = "gui/side_image.png"

##User Defined Transitions

define Reveal = Dissolve(2.0, alpha=False, time_warp=None)
define Reveal3 = Dissolve(3.0, alpha=False, time_warp=None)
define Reveal5 = Dissolve(5.0, alpha=False, time_warp=None)
define quick_dissolve = Dissolve(0.20, alpha=False, time_warp=None)


label splashscreen:
    scene black
    pause 3.0
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
    return

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus accumsan congue dui. Vestibulum vel efficitur nisl. Pellentesque sagittis sagittis risus, sed cursus mauris fermentum sed. Nullam imperdiet massa sit amet arcu consectetur accumsan"

    s "Donec cursus malesuada risus, eu pulvinar diam tempor at. Vestibulum in est posuere, porta massa eget, porttitor mi. Nunc lacus risus, consectetur in nisi vel, blandit rhoncus est. Phasellus quis quam pellentesque diam viverra mattis."

    e "Sed mollis, est eget finibus commodo, ligula mauris scelerisque sapien, ut tempus tortor ligula nec metus. Curabitur in metus egestas, sollicitudin ipsum in, interdum orci."


    $ renpy.notify("This is a notification")

    menu:
        "This is a sample choice menu"
        "Choice 1":
            pass
        "Choice 2":
            pass
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus accumsan congue dui. Vestibulum vel efficitur nisl.":
            pass
    # This ends the game.

    return
