#Delphine Badeaux. Gullible now, originally from Warrior.
default delphine_clothes_state = "Base"

image delphine_body_base = "images/chs/delphine/body_base.png"
image delphine_clothes_ruined = "images/chs/delphine/clothes_ruined.png"
image delphine_clothes_gown = "images/chs/delphine/clothes_gown.png"
image delphine_clothes_action = "images/chs/delphine/clothes_action.png"
image delphine_clothes = ConditionSwitch(
    "delphine_clothes_state == 'Base'", "delphine_clothes_gown",
    "delphine_clothes_state == 'Ruined'", "delphine_clothes_ruined",
    "delphine_clothes_state == 'Action'", "delphine_clothes_action",
)
image delphine_acc_blush = "images/chs/delphine/acc_blush.png"
image delphine_acc_sweat = "images/chs/delphine/acc_sweat.png"
image delphine_acc_sweatdrop = "images/chs/delphine/acc_sweatdrop.png"

image delphine_exp_neutral = "images/chs/delphine/exp_neutral.png"
image delphine_exp_smile = "images/chs/delphine/exp_smile.png"
image delphine_exp_shock = "images/chs/delphine/exp_shock.png"
image delphine_exp_surprise = "images/chs/delphine/exp_surprise.png"
image delphine_exp_sad = "images/chs/delphine/exp_sad.png"
image delphine_exp_frown = "images/chs/delphine/exp_frown.png"
image delphine_exp_laugh = "images/chs/delphine/exp_laugh.png"
image delphine_exp_angry = "images/chs/delphine/exp_angry.png"
image delphine_exp_fear = "images/chs/delphine/exp_fear.png"
image delphine_exp_pain = "images/chs/delphine/exp_pain.png"

layeredimage Delphine:
    group body:
        attribute base default:
            "delphine_body_base"
    group clothes:
        attribute c_full default:
            "delphine_clothes"
    group face:
        attribute neutral default:
            "delphine_exp_neutral"
        attribute smile:
            "delphine_exp_smile"
        attribute shock:
            "delphine_exp_shock"
        attribute surprise:
            "delphine_exp_surprise"
        attribute sad:
            "delphine_exp_sad"
        attribute frown:
            "delphine_exp_frown"
        attribute laugh:
            "delphine_exp_laugh"
        attribute angry:
            "delphine_exp_angry"
        attribute fear:
            "delphine_exp_fear"
        attribute pain:
            "delphine_exp_pain"
    group accessories:
        attribute blush:
            "delphine_acc_blush"
    group accessories_2:
        attribute sweat:
            "delphine_acc_sweat"
    group accessories_3:
        attribute sweatdrop:
            "delphine_acc_sweatdrop"
    #at character_sprites_delphine

#Portrait Images
image delphine_por_body_base = "images/chs/delphine/por/body_base.png"
image delphine_por_clothes_full = "images/chs/delphine/por/clothes_full.png"
image delphine_por_acc_blush = "images/chs/delphine/por/acc_blush.png"
image delphine_por_acc_sweat = "images/chs/delphine/por/acc_sweat.png"
image delphine_por_acc_sweatdrop = "images/chs/delphine/por/acc_sweatdrop.png"

image delphine_por_clothes_ruined = "images/chs/delphine/por/clothes_ruined.png"
image delphine_por_clothes_gown = "images/chs/delphine/por/clothes_gown.png"
image delphine_por_clothes_action = "images/chs/delphine/por/clothes_action.png"
image delphine_por_clothes = ConditionSwitch(
    "delphine_clothes_state == 'Base'", "delphine_por_clothes_gown",
    "delphine_clothes_state == 'Ruined'", "delphine_por_clothes_ruined",
    "delphine_clothes_state == 'Action'", "delphine_por_clothes_action",
)

image delphine_por_exp_neutral = "images/chs/delphine/por/exp_neutral.png"
image delphine_por_exp_smile = "images/chs/delphine/por/exp_smile.png"
image delphine_por_exp_shock = "images/chs/delphine/por/exp_shock.png"
image delphine_por_exp_surprise = "images/chs/delphine/por/exp_surprise.png"
image delphine_por_exp_sad = "images/chs/delphine/por/exp_sad.png"
image delphine_por_exp_frown = "images/chs/delphine/por/exp_frown.png"
image delphine_por_exp_laugh = "images/chs/delphine/por/exp_laugh.png"
image delphine_por_exp_angry = "images/chs/delphine/por/exp_angry.png"
image delphine_por_exp_fear = "images/chs/delphine/por/exp_fear.png"
image delphine_por_exp_pain = "images/chs/delphine/por/exp_pain.png"
image delphine_por_exp_cloudy = "images/chs/delphine/por/exp_cloudy.png"

layeredimage Delphine_por:
    group body:
        attribute base default:
            "delphine_por_body_base"
    group clothes:
        attribute c_full default:
            "delphine_por_clothes"
    group face:
        attribute neutral default:
            "delphine_por_exp_neutral"
        attribute smile:
            "delphine_por_exp_smile"
        attribute shock:
            "delphine_por_exp_shock"
        attribute surprise:
            "delphine_por_exp_surprise"
        attribute sad:
            "delphine_por_exp_sad"
        attribute frown:
            "delphine_por_exp_frown"
        attribute laugh:
            "delphine_por_exp_laugh"
        attribute angry:
            "delphine_por_exp_angry"
        attribute fear:
            "delphine_por_exp_fear"
        attribute pain:
            "delphine_por_exp_pain"
        attribute cloudy:
            "delphine_por_exp_cloudy"
    group accessories:
        attribute blush:
            "delphine_por_acc_blush"
    group accessories_2:
        attribute sweat:
            "delphine_por_acc_sweat"
    group accessories_3:
        attribute sweatdrop:
            "delphine_por_acc_sweatdrop"