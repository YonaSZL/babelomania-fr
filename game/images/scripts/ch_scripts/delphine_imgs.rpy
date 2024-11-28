#Delphine Badeaux. Gullible now, originally from Warrior.
default delphine_clothes_state = "Base"

image delphine_body_base = "images/chs/francesco/body_base.png"
image delphine_clothes_ruined = "images/chs/francesco/clothes_ruined.png"
image delphine_clothes_gown = "images/chs/francesco/clothes_full.png"
image delphine_clothes_action = "images/chs/francesco/clothes_action.png"
image delphine_clothes = ConditionSwitch(
    "delphine_clothes_state == 'Base'", "delphine_clothes_gown",
    "delphine_clothes_state == 'Ruined'", "delphine_clothes_ruined",
    "delphine_clothes_state == 'Action'", "delphine_clothes_action",
)
image delphine_acc_blush = "images/chs/francesco/acc_blush.png"
image delphine_acc_sweat = "images/chs/francesco/acc_sweat.png"
image delphine_acc_sweatdrop = "images/chs/francesco/acc_sweatdrop.png"

image delphine_exp_neutral = "images/chs/francesco/exp_neutral.png"
image delphine_exp_smile = "images/chs/francesco/exp_smile.png"
image delphine_exp_shock = "images/chs/francesco/exp_shock.png"
image delphine_exp_surprise = "images/chs/francesco/exp_surprise.png"
image delphine_exp_sad = "images/chs/francesco/exp_sad.png"
image delphine_exp_frown = "images/chs/francesco/exp_frown.png"
image delphine_exp_laugh = "images/chs/francesco/exp_laugh.png"
image delphine_exp_angry = "images/chs/francesco/exp_angry.png"
image delphine_exp_fear = "images/chs/francesco/exp_fear.png"
image delphine_exp_pain = "images/chs/francesco/exp_pain.png"

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
image delphine_por_body_base = "images/chs/francesco/por/body_base.png"
image delphine_por_acc_blush = "images/chs/francesco/por/acc_blush.png"
image delphine_por_acc_sweat = "images/chs/francesco/por/acc_sweat.png"
image delphine_por_acc_sweatdrop = "images/chs/francesco/por/acc_sweatdrop.png"

image delphine_por_clothes_ruined = "images/chs/francesco/por/clothes_ruined.png"
image delphine_por_clothes_gown = "images/chs/francesco/por/clothes_full.png"
image delphine_por_clothes_action = "images/chs/francesco/por/clothes_action.png"
image delphine_por_clothes = ConditionSwitch(
    "delphine_clothes_state == 'Base'", "delphine_por_clothes_gown",
    "delphine_clothes_state == 'Ruined'", "delphine_por_clothes_ruined",
    "delphine_clothes_state == 'Action'", "delphine_por_clothes_action",
)

image delphine_por_exp_neutral = "images/chs/francesco/por/exp_neutral.png"
image delphine_por_exp_smile = "images/chs/francesco/por/exp_smile.png"
image delphine_por_exp_shock = "images/chs/francesco/por/exp_shock.png"
image delphine_por_exp_surprise = "images/chs/francesco/por/exp_surprise.png"
image delphine_por_exp_sad = "images/chs/francesco/por/exp_sad.png"
image delphine_por_exp_frown = "images/chs/francesco/por/exp_frown.png"
image delphine_por_exp_laugh = "images/chs/francesco/por/exp_laugh.png"
image delphine_por_exp_angry = "images/chs/francesco/por/exp_angry.png"
image delphine_por_exp_fear = "images/chs/francesco/por/exp_fear.png"
image delphine_por_exp_pain = "images/chs/francesco/por/exp_pain.png"
image delphine_por_exp_cloudy = "images/chs/francesco/por/exp_cloudy.png"

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