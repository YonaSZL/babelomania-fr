default shigeo_blood = "None"

image shigeo_body_base = "images/chs/shigeo/body_base.png"
image shigeo_clothes_full = "images/chs/shigeo/clothes_full.png"
image shigeo_clothes_blood = "images/chs/shigeo/clothes_blood.png"
image shigeo_acc_blush = "images/chs/shigeo/acc_blush.png"
image shigeo_acc_sweat = "images/chs/shigeo/acc_sweat.png"
image shigeo_acc_sweatdrop = "images/chs/shigeo/acc_sweatdrop.png"

image shigeo_exp_neutral = "images/chs/shigeo/exp_neutral.png"
image shigeo_exp_smile = "images/chs/shigeo/exp_smile.png"
image shigeo_exp_shock = "images/chs/shigeo/exp_shock.png"
image shigeo_exp_surprise = "images/chs/shigeo/exp_surprise.png"
image shigeo_exp_sad = "images/chs/shigeo/exp_sad.png"
image shigeo_exp_frown = "images/chs/shigeo/exp_frown.png"
image shigeo_exp_laugh = "images/chs/shigeo/exp_laugh.png"
image shigeo_exp_angry = "images/chs/shigeo/exp_angry.png"
image shigeo_exp_fear = "images/chs/shigeo/exp_fear.png"
image shigeo_exp_pain = "images/chs/shigeo/exp_pain.png"
image shigeo_exp_cloudy = "images/chs/shigeo/exp_cloudy.png"

layeredimage Shigeo:
    group body:
        attribute base default:
            "shigeo_body_base"
    group clothes:
        if shigeo_blood == "None":
            attribute c_full default:
                "shigeo_clothes_full"
        elif shigeo_blood == "blood":
            attribute c_blood default:
                "shigeo_clothes_blood"
    group face:
        attribute neutral default:
            "shigeo_exp_neutral"
        attribute smile:
            "shigeo_exp_smile"
        attribute shock:
            "shigeo_exp_shock"
        attribute surprise:
            "shigeo_exp_surprise"
        attribute sad:
            "shigeo_exp_sad"
        attribute frown:
            "shigeo_exp_frown"
        attribute laugh:
            "shigeo_exp_laugh"
        attribute angry:
            "shigeo_exp_angry"
        attribute fear:
            "shigeo_exp_fear"
        attribute pain:
            "shigeo_exp_pain"
        attribute cloudy:
            "shigeo_exp_cloudy"
    group accessories:
        attribute blush:
            "shigeo_acc_blush"
    group accessories_2:
        attribute sweat:
            "shigeo_acc_sweat"
    group accessories_3:
        attribute sweatdrop:
            "shigeo_acc_sweatdrop"
    #at character_sprites_shigeo

#Portrait Images
image shigeo_por_body_base = "images/chs/shigeo/por/body_base.png"
image shigeo_por_clothes_full = "images/chs/shigeo/por/clothes_full.png"
image shigeo_por_clothes_blood = "images/chs/shigeo/por/clothes_blood.png"
image shigeo_por_acc_blush = "images/chs/shigeo/por/acc_blush.png"
image shigeo_por_acc_sweat = "images/chs/shigeo/por/acc_sweat.png"
image shigeo_por_acc_sweatdrop = "images/chs/shigeo/por/acc_sweatdrop.png"

image shigeo_por_exp_neutral = "images/chs/shigeo/por/exp_neutral.png"
image shigeo_por_exp_smile = "images/chs/shigeo/por/exp_smile.png"
image shigeo_por_exp_shock = "images/chs/shigeo/por/exp_shock.png"
image shigeo_por_exp_surprise = "images/chs/shigeo/por/exp_surprise.png"
image shigeo_por_exp_sad = "images/chs/shigeo/por/exp_sad.png"
image shigeo_por_exp_frown = "images/chs/shigeo/por/exp_frown.png"
image shigeo_por_exp_laugh = "images/chs/shigeo/por/exp_laugh.png"
image shigeo_por_exp_angry = "images/chs/shigeo/por/exp_angry.png"
image shigeo_por_exp_fear = "images/chs/shigeo/por/exp_fear.png"
image shigeo_por_exp_pain = "images/chs/shigeo/por/exp_pain.png"

layeredimage Shigeo_por:
    group body:
        attribute base default:
            "shigeo_por_body_base"
    group clothes:
        if shigeo_blood == "None":
            attribute c_full default:
                "shigeo_por_clothes_full"
        elif shigeo_blood == "blood":
            attribute c_blood default:
                "shigeo_por_clothes_blood"
    group face:
        attribute neutral default:
            "shigeo_por_exp_neutral"
        attribute smile:
            "shigeo_por_exp_smile"
        attribute shock:
            "shigeo_por_exp_shock"
        attribute surprise:
            "shigeo_por_exp_surprise"
        attribute sad:
            "shigeo_por_exp_sad"
        attribute frown:
            "shigeo_por_exp_frown"
        attribute laugh:
            "shigeo_por_exp_laugh"
        attribute angry:
            "shigeo_por_exp_angry"
        attribute fear:
            "shigeo_por_exp_fear"
        attribute pain:
            "shigeo_por_exp_pain"
    group accessories:
        attribute blush:
            "shigeo_por_acc_blush"
    group accessories_2:
        attribute sweat:
            "shigeo_por_acc_sweat"
    group accessories_3:
        attribute sweatdrop:
            "shigeo_por_acc_sweatdrop"