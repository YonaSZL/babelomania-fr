##From the Japanese version of a Buddhist deity.
default fudo_shot_distance = 0
default fudo_damage_distance = 3

image fudo_body_base = "images/chs/fudo/body_base.png"
image fudo_clothes_full = "images/chs/fudo/clothes_full.png"
image fudo_acc_blood_1 = "images/chs/fudo/acc_blood_1.png"
image fudo_acc_blood_2 = "images/chs/fudo/acc_blood_2.png"
image fudo_acc_blood_3 = "images/chs/fudo/acc_blood_3.png"
image fudo_acc_blood = ConditionSwitch(
    "fudo_damage_distance == 0", None,
    "fudo_damage_distance == 1", "fudo_acc_blood_1",
    "fudo_damage_distance == 2", "fudo_acc_blood_2",
    "fudo_damage_distance == 3", "fudo_acc_blood_3"
)
image fudo_acc_burn_1 = "images/chs/fudo/acc_burn_1.png"
image fudo_acc_burn_2 = "images/chs/fudo/acc_burn_2.png"
image fudo_acc_burn_3 = "images/chs/fudo/acc_burn_3.png"
image fudo_acc_burn = ConditionSwitch(
    "fudo_shot_distance == 0", None,
    "fudo_shot_distance == 1", "fudo_acc_burn_1",
    "fudo_shot_distance == 2", "fudo_acc_burn_2",
    "fudo_shot_distance == 3", "fudo_acc_burn_3"
)

layeredimage Fudo:
    group body:
        attribute base default:
            "fudo_body_base"
    group clothes:
        attribute c_full default:
            "fudo_clothes_full"
    attribute blood default:
        "fudo_acc_blood"
    attribute burn default:
        "fudo_acc_burn"
    
    #at character_sprites_fudo