#Mira 'Zurawski' which is actually 'Zhuravskiy'. Mira is Peace, the Surname is Peace, her dead name is Miro.
#Parents, Russian. Her? Transgender. Age 33.

default mira_clothes_state = "Base"

image mira_body_base = "images/chs/amina/body_base.png"
image mira_clothes_full = "images/chs/amina/clothes_full.png"
image mira_acc_blush = "images/chs/amina/acc_blush.png"
image mira_acc_sweat = "images/chs/amina/acc_sweat.png"
image mira_acc_sweatdrop = "images/chs/amina/acc_sweatdrop.png"

image mira_exp_neutral = "images/chs/amina/exp_neutral.png"
image mira_exp_smile = "images/chs/amina/exp_smile.png"
image mira_exp_shock = "images/chs/amina/exp_shock.png"
image mira_exp_surprise = "images/chs/amina/exp_surprise.png"
image mira_exp_sad = "images/chs/amina/exp_sad.png"
image mira_exp_frown = "images/chs/amina/exp_frown.png"
image mira_exp_laugh = "images/chs/amina/exp_laugh.png"
image mira_exp_angry = "images/chs/amina/exp_angry.png"
image mira_exp_fear = "images/chs/amina/exp_fear.png"
image mira_exp_pain = "images/chs/amina/exp_pain.png"

layeredimage Mira:
    group body:
        attribute base default:
            "mira_body_base"
    group clothes:
        attribute c_full default:
            "mira_clothes_full"
    group face:
        attribute neutral default:
            "mira_exp_neutral"
        attribute smile:
            "mira_exp_smile"
        attribute shock:
            "mira_exp_shock"
        attribute surprise:
            "mira_exp_surprise"
        attribute sad:
            "mira_exp_sad"
        attribute frown:
            "mira_exp_frown"
        attribute laugh:
            "mira_exp_laugh"
        attribute angry:
            "mira_exp_angry"
        attribute fear:
            "mira_exp_fear"
        attribute pain:
            "mira_exp_pain"
    group accessories:
        attribute blush:
            "mira_acc_blush"
    group accessories_2:
        attribute sweat:
            "mira_acc_sweat"
    group accessories_3:
        attribute sweatdrop:
            "mira_acc_sweatdrop"
    #at character_sprites_mira

#Portrait Images
image mira_por_body_base = "images/chs/amina/por/body_base.png"
image mira_por_clothes_full = "images/chs/amina/por/clothes_full.png"
image mira_por_acc_blush = "images/chs/amina/por/acc_blush.png"
image mira_por_acc_sweat = "images/chs/amina/por/acc_sweat.png"
image mira_por_acc_sweatdrop = "images/chs/amina/por/acc_sweatdrop.png"

image mira_por_exp_neutral = "images/chs/amina/por/exp_neutral.png"
image mira_por_exp_smile = "images/chs/amina/por/exp_smile.png"
image mira_por_exp_shock = "images/chs/amina/por/exp_shock.png"
image mira_por_exp_surprise = "images/chs/amina/por/exp_surprise.png"
image mira_por_exp_sad = "images/chs/amina/por/exp_sad.png"
image mira_por_exp_frown = "images/chs/amina/por/exp_frown.png"
image mira_por_exp_laugh = "images/chs/amina/por/exp_laugh.png"
image mira_por_exp_angry = "images/chs/amina/por/exp_angry.png"
image mira_por_exp_fear = "images/chs/amina/por/exp_fear.png"
image mira_por_exp_pain = "images/chs/amina/por/exp_pain.png"
image mira_por_exp_cloudy = "images/chs/amina/por/exp_cloudy.png"
image mira_por_acc_static = "images/chs/mira/por/acc_static.png"

layeredimage Mira_por:
    group body:
        attribute base default:
            "mira_por_body_base"
    group clothes:
        attribute c_full default:
            "mira_por_clothes_full"
    group face:
        attribute neutral default:
            "mira_por_exp_neutral"
        attribute smile:
            "mira_por_exp_smile"
        attribute shock:
            "mira_por_exp_shock"
        attribute surprise:
            "mira_por_exp_surprise"
        attribute sad:
            "mira_por_exp_sad"
        attribute frown:
            "mira_por_exp_frown"
        attribute laugh:
            "mira_por_exp_laugh"
        attribute angry:
            "mira_por_exp_angry"
        attribute fear:
            "mira_por_exp_fear"
        attribute pain:
            "mira_por_exp_pain"
        attribute cloudy:
            "mira_por_exp_cloudy"
    group accessories:
        attribute blush:
            "mira_por_acc_blush"
    group accessories_2:
        attribute sweat:
            "mira_por_acc_sweat"
    group accessories_3:
        attribute sweatdrop:
            "mira_por_acc_sweatdrop"
    attribute static:
        "mira_por_acc_static"