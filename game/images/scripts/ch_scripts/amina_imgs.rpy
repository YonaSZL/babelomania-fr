#Name of the character is Amina bint Hassan ibn Abbas al-Bel
default amina_blood = "None"

image amina_body_base = "images/chs/amina/body_base.png"
image amina_clothes_full = "images/chs/amina/clothes_full.png"
image amina_clothes_blood = "images/chs/amina/clothes_blood.png"
image amina_clothes = ConditionSwitch(
    "amina_blood == 'None'", "amina_clothes_full",
    "amina_blood == 'blood'", "amina_clothes_blood"
)
image amina_clothes_half = "images/chs/amina/clothes_half.png"
image amina_acc_blush = "images/chs/amina/acc_blush.png"
image amina_acc_sweat = "images/chs/amina/acc_sweat.png"
image amina_acc_sweatdrop = "images/chs/amina/acc_sweatdrop.png"
image amina_acc_light = "images/chs/amina/acc_light.png"
image amina_acc_blood_base = "images/chs/amina/acc_blood.png"
image amina_acc_blood:
    "amina_acc_blood_base"
    blend "multiply"
image amina_exp_neutral = "images/chs/amina/exp_neutral.png"
image amina_exp_smile = "images/chs/amina/exp_smile.png"
image amina_exp_cry = "images/chs/amina/exp_cry.png"
image amina_exp_shock = "images/chs/amina/exp_shock.png"
image amina_exp_surprise = "images/chs/amina/exp_surprise.png"
image amina_exp_sad = "images/chs/amina/exp_sad.png"
image amina_exp_frown = "images/chs/amina/exp_frown.png"
image amina_exp_laugh = "images/chs/amina/exp_laugh.png"
image amina_exp_angry = "images/chs/amina/exp_angry.png"
image amina_exp_fear = "images/chs/amina/exp_fear.png"
image amina_exp_pain = "images/chs/amina/exp_pain.png"

layeredimage Amina:
    group body:
        attribute base default:
            "amina_body_base"
    group clothes:
        attribute c_full default:
            "amina_clothes"
        attribute c_half:
            "amina_clothes_half"
    group face:
        attribute neutral default:
            "amina_exp_neutral"
        attribute smile:
            "amina_exp_smile"
        attribute shock:
            "amina_exp_shock"
        attribute cry:
            "amina_exp_cry"
        attribute surprise:
            "amina_exp_surprise"
        attribute sad:
            "amina_exp_sad"
        attribute frown:
            "amina_exp_frown"
        attribute laugh:
            "amina_exp_laugh"
        attribute angry:
            "amina_exp_angry"
        attribute fear:
            "amina_exp_fear"
        attribute pain:
            "amina_exp_pain"
    group accessories:
        attribute blush:
            "amina_acc_blush"
    group accessories_2:
        attribute sweat:
            "amina_acc_sweat"
    group accessories_3:
        attribute sweatdrop:
            "amina_acc_sweatdrop"
    group accessories_4:
        attribute light:
            "amina_acc_light"
    attribute blood:
        "amina_acc_blood"
    #at character_sprites_amina

#Portrait Images
image amina_por_body_base = "images/chs/amina/por/body_base.png"
image amina_por_clothes_full = "images/chs/amina/por/clothes_full.png"
image amina_por_clothes_blood = "images/chs/amina/por/clothes_blood.png"
image amina_por_clothes_half = "images/chs/amina/por/clothes_half.png"
image amina_por_acc_blush = "images/chs/amina/por/acc_blush.png"
image amina_por_acc_sweat = "images/chs/amina/por/acc_sweat.png"
image amina_por_acc_sweatdrop = "images/chs/amina/por/acc_sweatdrop.png"
image amina_por_acc_blood_base = "images/chs/amina/por/acc_blood.png"
image amina_por_acc_blood:
    "amina_por_acc_blood_base"
    blend "multiply"

image amina_por_clothes = ConditionSwitch(
    "amina_blood == 'None'", "amina_por_clothes_full",
    "amina_blood == 'blood'", "amina_por_clothes_blood"
)

image amina_por_exp_neutral = "images/chs/amina/por/exp_neutral.png"
image amina_por_exp_smile = "images/chs/amina/por/exp_smile.png"
image amina_por_exp_shock = "images/chs/amina/por/exp_shock.png"
image amina_por_exp_surprise = "images/chs/amina/por/exp_surprise.png"
image amina_por_exp_sad = "images/chs/amina/por/exp_sad.png"
image amina_por_exp_cry = "images/chs/amina/por/exp_cry.png"
image amina_por_exp_frown = "images/chs/amina/por/exp_frown.png"
image amina_por_exp_laugh = "images/chs/amina/por/exp_laugh.png"
image amina_por_exp_angry = "images/chs/amina/por/exp_angry.png"
image amina_por_exp_fear = "images/chs/amina/por/exp_fear.png"
image amina_por_exp_pain = "images/chs/amina/por/exp_pain.png"

layeredimage Amina_por:
    group body:
        attribute base default:
            "amina_por_body_base"
    group clothes:
        attribute c_full default:
            "amina_por_clothes"
        attribute c_half:
            "amina_por_clothes_half"
    group face:
        attribute neutral default:
            "amina_por_exp_neutral"
        attribute smile:
            "amina_por_exp_smile"
        attribute shock:
            "amina_por_exp_shock"
        attribute cry:
            "amina_por_exp_cry"
        attribute surprise:
            "amina_por_exp_surprise"
        attribute sad:
            "amina_por_exp_sad"
        attribute frown:
            "amina_por_exp_frown"
        attribute laugh:
            "amina_por_exp_laugh"
        attribute angry:
            "amina_por_exp_angry"
        attribute fear:
            "amina_por_exp_fear"
        attribute pain:
            "amina_por_exp_pain"
    group accessories:
        attribute blush:
            "amina_por_acc_blush"
    group accessories_2:
        attribute sweat:
            "amina_por_acc_sweat"
    group accessories_3:
        attribute sweatdrop:
            "amina_por_acc_sweatdrop"
    attribute blood:
        "amina_por_acc_blood"