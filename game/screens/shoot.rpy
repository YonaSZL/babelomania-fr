default disruptor_charge = 50
default base_charge = 6
default base_click_charge = 6
default shoot_tip = "SHOOT THE TARGET!"
default can_charge = True
default target_shot = False

default medium_random = [1.5,1.75,2.0,2.25,2.5,2.75,3.0]

default button_pos_1 = [None, None, None, None]
default button_pos_2 = [None, None, None, None]
default button_pos_3 = [None, None, None, None]
default button_pos_4 = [None, None, None, None]
default button_pos_5 = [None, None, None, None]
default button_pos_6 = [None, None, None, None]
default button_pos_1_start = False
default button_pos_2_start = False
default button_pos_3_start = False
default button_pos_4_start = False
default button_pos_5_start = False
default button_pos_6_start = False
default button_pos_1_next = [None, None, None, None]
default button_pos_2_next = [None, None, None, None]
default button_pos_3_next = [None, None, None, None]
default button_pos_4_next = [None, None, None, None]
default button_pos_5_next = [None, None, None, None]
default button_pos_6_next = [None, None, None, None]
#GOTTA ADD 'WASTE AMMO' FUNCTION

##placeholder targets
screen target1():
    style_prefix "target"
    timer 5.0 action [Hide("target1", vpunch)]  ### + add health loss here
    button:
        
        action Hide("target1")
        at movearound(renpy.random.randint(2, 3)), time_flash(3.5)
screen target2():
    style_prefix "target"

    ##time limit for the target
    timer 6.0 action [Hide("target2", vpunch)]  ### + add health loss here
    button:
        foreground "gui/shoot/test.png" ##add monster image here
        action Hide("target2")
        at movearound(renpy.random.randint(2, 3)), time_flash(5.0)  ##add here when it should flash that it's going to disappear

screen tutorial_target_1():
    style_prefix "target"
    button:
        if disruptor_charge >= 100:
            action [Hide("tutorial_target_1", glitch_unload), SetVariable("disruptor_charge", 0), SetVariable("target_shot", True), SetVariable("shoot_tip", "TIME IS SHORT!"), Hide("shoot_tutorial_1"), Hide("border"), Show("shoot_tutorial_2")]
        else:
            action NullAction()
        hover_sound "audio/sfx/gun_hover.ogg"
        activate_sound "audio/se/disruptor.ogg"
        align(0.5,0.5)
screen tutorial_target_2():
    style_prefix "target"
    button:
        if disruptor_charge >= 100:
            action [Hide("tutorial_target_2", glitch_unload), SetVariable("disruptor_charge", 0), SetVariable("target_shot", True), SetVariable("shoot_tip", "WATCH YOUR AMMO!"), Hide("shoot_tutorial_2"), Hide("border"), Show("shoot_tutorial_3")]
        else:
            action NullAction()
        hover_sound "audio/sfx/gun_hover.ogg"
        activate_sound "audio/se/disruptor.ogg"
        align(0.5,0.5)
        at time_flash(1.0)  ##add here when it should flash that it's going to disappear
screen tutorial_target_3():
    style_prefix "target"
    button:
        if disruptor_charge >= 100:
            action [Hide("tutorial_target_3", glitch_unload), SetVariable("disruptor_charge", 0), SetVariable("stat4", stat4 - 1), SetVariable("shoot_tip", "AIM CAREFULLY!"), SetVariable("target_shot", True), Hide("shoot_tutorial_3"), Hide("border"), Show("shoot_tutorial_final")]
        else:
            action NullAction()
        hover_sound "audio/sfx/gun_hover.ogg"
        activate_sound "audio/se/disruptor.ogg"
        align(0.5,0.5)
        at time_flash(3.0)  ##add here when it should flash that it's going to disappear
screen tutorial_target_final(rando_pos):
    style_prefix "target"
    timer 6.0 action [Hide("tutorial_target_final", vpunch), SetVariable("stat3", stat3 - 20), Play("sound7", "audio/sfx/hp_down.ogg")]  ### + add health loss here
    if button_pos_1_start:
        timer 0.9 action Function(register_new_pos, button_pos_1_next, renpy.focus_coordinates()) repeat True
    else:
        timer 0.1 action [Function(register_new_pos, button_pos_1_next, renpy.focus_coordinates()), SetVariable("button_pos_1_start", True)] repeat True
    button:
        if disruptor_charge >= 100:
            action [Hide("tutorial_target_final", glitch_unload), SetVariable("disruptor_charge", 0), SetVariable("stat4", stat4 - 1), SetVariable("target_shot", True), Hide("shoot_tutorial_final"), Hide("border"), Jump("story_02_elevator_escape")]
        else:
            action NullAction()
        hover_sound "audio/sfx/gun_hover.ogg"
        activate_sound "audio/se/disruptor.ogg"
        if button_pos_1_start:
            at movearound_fix(renpy.random.choice(medium_random), button_pos_1_next), time_flash(3.0)  ##add here when it should flash that it's going to disappear
        else:
            at movearound_fix(renpy.random.choice(medium_random), rando_pos), time_flash(3.0)  ##add here when it should flash that it's going to disappear
###--------------------------------------


###add targets here
init python:
    def show_targets():
        renpy.show_screen("target1")
        renpy.show_screen("target2")
        return
        
    def show_targets_tutorial_1():
        renpy.show_screen("tutorial_target_1")
        return

    def show_targets_tutorial_2():
        renpy.show_screen("tutorial_target_2")
        return

    def show_targets_tutorial_3():
        renpy.show_screen("tutorial_target_3")
        return

    def show_targets_tutorial_final(rando_pos):
        print(str(rando_pos))
        renpy.show_screen("tutorial_target_final",rando_pos)
        return

    def randomize_starting_pos():
        global button_pos_1
        global button_pos_2
        global button_pos_3
        global button_pos_4
        global button_pos_5
        global button_pos_6
        button_pos_1 = [(renpy.random.randint(0, config.screen_width - 500)), (renpy.random.randint(0, config.screen_height- 300)), None, None]
        button_pos_2 = [(renpy.random.randint(0, config.screen_width - 500)), (renpy.random.randint(0, config.screen_height- 300)), None, None]
        button_pos_3 = [(renpy.random.randint(0, config.screen_width - 500)), (renpy.random.randint(0, config.screen_height- 300)), None, None]
        button_pos_4 = [(renpy.random.randint(0, config.screen_width - 500)), (renpy.random.randint(0, config.screen_height- 300)), None, None]
        button_pos_5 = [(renpy.random.randint(0, config.screen_width - 500)), (renpy.random.randint(0, config.screen_height- 300)), None, None]
        button_pos_6 = [(renpy.random.randint(0, config.screen_width - 500)), (renpy.random.randint(0, config.screen_height- 300)), None, None]
        print(str(button_pos_1))
        print(str(button_pos_2))
        print(str(button_pos_3))
        print(str(button_pos_4))
        print(str(button_pos_5))
        print(str(button_pos_6))
        return

    def register_new_pos(rando_pos, button_pos):
        rando_pos = [button_pos[0], button_pos[1], None, None]
        print(str(rando_pos))
        return

screen shoot():
    timer 6.0 action [Function(renpy.restart_interaction)] repeat True
    ###janky resummon thing just to test it
    timer 6.5  action Function(show_targets)
    ###you can put a bg here if it's the same for every instance
    add "gui/shoot/darken.png"
    on "show" action Function(show_targets)
    style_prefix "shoot"
    on "show" action Show("border")

screen shoot_tutorial_1():
    add "gui/shoot/darken.png"
    on "show" action Function(show_targets_tutorial_1)
    style_prefix "shoot"
    on "show" action Show("border")
screen shoot_tutorial_2():
    add "gui/shoot/darken.png"
    on "show" action Function(show_targets_tutorial_2)
    style_prefix "shoot"
    on "show" action Show("border")
screen shoot_tutorial_3():
    add "gui/shoot/darken.png"
    on "show" action Function(show_targets_tutorial_3)
    style_prefix "shoot"
    on "show" action Show("border")
screen shoot_tutorial_final():
    timer 1.0 action Function(renpy.restart_interaction) repeat True
    if target_shot:
        timer 0.5  action [SetVariable("target_shot", False), SetVariable("button_pos_1_start", False), Function(randomize_starting_pos), Function(show_targets_tutorial_final, button_pos_1)] repeat True
    else:
        timer 6.5  action [SetVariable("button_pos_1_start", False), Function(randomize_starting_pos), Function(show_targets_tutorial_final, button_pos_1)] repeat True
    add "gui/shoot/darken.png"
    on "show" action Function(show_targets_tutorial_final, button_pos_1)
    style_prefix "shoot"
    on "show" action Show("border")

screen border():
    zorder 100
    add "gui/shoot/bg.png"

    if can_charge == False:
        timer 0.66 action SetVariable("can_charge", True)   
    timer 1.0 action [SetVariable("disruptor_charge", disruptor_charge + base_charge)] repeat True
    ###charge stuff
    hbox:
        pos(813, 938) spacing 30
        button:
            xysize(296,72) background "gui/shoot/btn.png"
            text "CHARGE" align(0.5, 0.6) font gui.interface_text_font size 45 idle_color u"#bfaa8f" hover_color u"#951b14"
            hover_sound "audio/sfx/gun_hover.ogg"
            activate_sound "audio/sfx/gui_slots_confirm.ogg"
            if can_charge:
                action SetVariable("disruptor_charge", disruptor_charge + base_click_charge)
            else:
                action NullAction()

        bar:
            value disruptor_charge
            range 100
            xysize(640,72)
            left_bar "gui/shoot/bar_full.png" right_bar "gui/shoot/bar_empty.png"


    
    button:
        yalign 1.0 offset(125, -25)
        hbox:
            spacing 25
            #add "gui/shoot/menu.png" yalign 0.5
            text "[shoot_tip]" font gui.name_text_font size 62 yalign 0.5 color "#91191b" yoffset 2
        
        action NullAction()#ShowMenu("save")
        at  button_fade




    




transform movearound(speed):
    pos(renpy.random.randint(0, config.screen_width - 500), renpy.random.randint(0, config.screen_height- 300))
    parallel:
        linear speed pos(renpy.random.randint(0, config.screen_width - 500), renpy.random.randint(0, config.screen_height- 300))
        linear speed pos(renpy.random.randint(0, config.screen_width - 500), renpy.random.randint(0, config.screen_height - 300))
        repeat
    parallel:
        easein .4 zoom 1.0
        easein .4 zoom renpy.random.random() + 0.3
transform movearound_fix(speed,rando_pos):
    pos(rando_pos[0],rando_pos[1])
    parallel:
        linear speed pos(renpy.random.randint(0, config.screen_width - 500), renpy.random.randint(0, config.screen_height- 300))
        linear speed pos(renpy.random.randint(0, config.screen_width - 500), renpy.random.randint(0, config.screen_height - 300))
        repeat
    parallel:
        easein .4 zoom 1.0
        easein .4 zoom renpy.random.random() + 0.3
transform charge_butt():

    on idle:
        easein .3 zoom 1.0
    on hover:
        easein .3 zoom 1.05
style shoot_button:
    xysize(802,170)
    padding(30, 20, 30, 20)
    background "gui/shoot/button_bg.png"

style shoot_button_text:
    align(0.5, 0.5) textalign 0.5 size 45

style my_rad_bar_style:
    fore_bar "gui/bar/cir_empt.png"
    aft_bar "gui/bar/cir_full.png"
    hover_aft_bar "gui/bar/cir_full.png"
    focus_mask True
    xysize (165, 165)
    thumb None
    hover_thumb None
    thumb_offset absolute(238.5)
    anchor(0.5, 0.5)



style target_button:
    xysize(309,309)
    background "gui/shoot/target.png"

transform time_flash(time):
    matrixcolor BrightnessMatrix(0.0)
    pause time
    linear 1.0 matrixcolor BrightnessMatrix(0.2)

        







