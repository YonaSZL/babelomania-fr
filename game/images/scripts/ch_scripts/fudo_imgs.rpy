##From the Japanese version of a Buddhist deity.
default fudo_shot_distance = 0
default fudo_damage_distance = 0
default fudo_state = "chase"

image fudo_body_normal = "images/chs/fudo/body_base.png"
image fudo_body_atk = "images/chs/fudo/body_atk.png"
image fudo_body_base = ConditionSwitch(
    "fudo_state == 'chase'", "fudo_body_normal",
    "fudo_state == 'atk'", "fudo_body_atk"
)

image fudo_bandages_base = "images/chs/fudo/fudo_bandages_base.png"
image fudo_bandages_blood_1 = "images/chs/fudo/fudo_bandages_blood_1.png"
image fudo_bandages_blood_2 = "images/chs/fudo/fudo_bandages_blood_2.png"
image fudo_bandages = ConditionSwitch(
    "fudo_damage_distance == 0", "fudo_bandages_base",
    "fudo_damage_distance == 1", "fudo_bandages_blood_1",
    "fudo_damage_distance == 2", "fudo_bandages_blood_2",
)

image fudo_acc_blood_1_chase:
    "images/chs/fudo/acc_blood_1_chase.png"
    blend "multiply"
image fudo_acc_blood_2_chase:
    "images/chs/fudo/acc_blood_2_chase.png"
    blend "multiply"
image fudo_acc_blood_1_atk:
    "images/chs/fudo/acc_blood_1_atk.png"
    blend "multiply"
image fudo_acc_blood_2_atk:
    "images/chs/fudo/acc_blood_2_atk.png"
    blend "multiply"
image fudo_acc_blood_1 = ConditionSwitch(
    "fudo_state == 'chase'", "fudo_acc_blood_1_chase",
    "fudo_state == 'atk'", "fudo_acc_blood_1_atk"
)
image fudo_acc_blood_2 = ConditionSwitch(
    "fudo_state == 'chase'", "fudo_acc_blood_2_chase",
    "fudo_state == 'atk'", "fudo_acc_blood_2_atk"
)
image fudo_acc_blood = ConditionSwitch(
    "fudo_damage_distance == 1", "fudo_acc_blood_1",
    "fudo_damage_distance == 2", "fudo_acc_blood_2",
)

image fudo_acc_burn_1_chase:
    "images/chs/fudo/acc_burn_1_chase.png"
    blend "multiply"
image fudo_acc_burn_2_chase:
    "images/chs/fudo/acc_burn_2_chase.png"
    blend "multiply"
image fudo_acc_burn_1_atk:
    "images/chs/fudo/acc_burn_1_atk.png"
    blend "multiply"
image fudo_acc_burn_2_atk:
    "images/chs/fudo/acc_burn_2_atk.png"
    blend "multiply"
image fudo_acc_burn_1 = ConditionSwitch(
    "fudo_state == 'chase'", "fudo_acc_burn_1_chase",
    "fudo_state == 'atk'", "fudo_acc_burn_1_atk"
)
image fudo_acc_burn_2 = ConditionSwitch(
    "fudo_state == 'chase'", "fudo_acc_burn_2_chase",
    "fudo_state == 'atk'", "fudo_acc_burn_2_atk"
)
image fudo_acc_burn = ConditionSwitch(
    "fudo_shot_distance == 1", "fudo_acc_burn_1",
    "fudo_shot_distance == 2", "fudo_acc_burn_2",
)
image fudo_acc_smoke:
    "images/chs/fudo/acc_smoke.png"

layeredimage Fudo:
    attribute bandages default:
        "fudo_bandages"
    group body:
        attribute base default:
            "fudo_body_base"
        attribute atk:
            "fudo_body_atk"
    attribute blood:
        "fudo_acc_blood"
    attribute burn:
        "fudo_acc_burn"
    attribute smoke:
        "fudo_acc_smoke"
    
    #at character_sprites_fudo