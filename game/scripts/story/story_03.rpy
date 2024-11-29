##Chapter name is Android
###The items and what they need to explain:
###-Katana recovered at the battle where Ame no Murakumo was lost. It's not that old, Amina notices. Shigeo agrees, reveals Kendo BG.
###-Towels received as a present by Abe's war criminal grandfather. Motif of the Fujiwara. Shigeo enlightens on who Ikki was.
###-Scroll received as a present by the Mitsui leadership. Name doesn't ring a bell, Tabitha tells who it is. Contains stuff from that incel samurai dude.
###-Wall with picture and explanation of his travels in Japan. Says that he visited area of Battle, met guys, was there for foul.

label story_03_android:
    $ renpy.block_rollback()
    $ move_time(0,1)
    $ flashlight_consume = False
    $ shigeo_blood = "blood"
    $ amina_blood = "blood"
    $ current_char = "shigeo"
    pause 1.5
    scene title_03 with Reveal
    pause 3.0
    scene black with Reveal5
    pause 1.5
    $ quick_menu = True
    $ time_menu = True
    $ codex_active = True
    $ inventory_show = True
    $ flashlight_on = False
    $ flashlight_use = False
    $ stat1_show = True
    $ stat3_show = True
    $ stat4_show = True
    play music "audio/bgm/shadows_breathe.ogg"
    sh_i shock blood sweat "\"{b}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHH...!!!\""
    pause 1.0
    scene tabitha_hand with Reveal3
    pause 1.0
    sh_i shock sweat "(Blood...!{w=0.3} Gaspard!{w=0.3} Monster!{w=0.3} ANDROID!{w=0.3} BLOOD!{w=0.3} {b}SO MUCH BLOOD!{/b})"
    ta r_neutral blood "{cps=10}.{w=0.3}.{w=0.3}.{w=0.5}harm.{w=0.3} Please re.{w=0.3}.{w=0.3}."
    sh_i fear sweat "(She...!{w=0.3} It!!!{w=0.3} IT RIPPED HIM APART!{w=0.3} HIS GUTS...!{w=0.3} I-)"
    ta r_neutral blood "Switching to Japanese.{w=0.5} <Please calm down.>"
    stop music fadeout 3.5
    play sound4 "audio/em/em_shock.ogg"
    show screen emote("surprise",0.15,0.5)
    sh surprise sweat "...!"
    pause 1.0
    scene tabitha_face with Reveal3
    pause 1.0
    sh shock sweat "{cps=15}Aaaah...{w=0.5} Aaaah..."
    ta r_neutral blood "<Arata-san.{w=0.3} I mean you no harm.{w=0.3} Please relax and allow me to inspect you for injuries.>"
    sh surprise sweat "{cps=15}<.{w=0.3}.{w=0.3}.{w=0.5}you...?>"
    play music "audio/bgm/measure_of_ningen.ogg"
    pause 1.5
    scene taisho_1f_library_base:
        xalign 0.5
    show darkness_layer
    show Tabitha r_neutral blood at ta_med:
        xalign 0.5
    with Reveal3
    pause 1.5
    sh surprise sweat "<That's...{w=0.5}{nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}Hokkaidō-ben{/b}?>"
    ta nulla "<That is correct.{w=0.3} You have mentioned to Professor Habiki a matrilineage originating from Sapporo.>"
    show Tabitha bow with dissolve
    ta nulla "<I could surmise that you would have been exposed to the regional dialect in a family setting.{w=0.3} Thus...>"
    show Tabitha neutral with dissolve
    ta nulla "<I hypothized that switching to the specific vernacular would add a sense of familiarity to my pleas.{w=0.3} With this, I hoped to break you out of your heightened state of shock.>"
    sh neutral sweat "<.{w=0.3}.{w=0.3}.{w=0.5}I see.{w=0.3} Guess it worked.>"
    play sound2 "audio/se/clothes_rustle.ogg"
    show Tabitha surprise with dissolve
    ta nulla "<I would suggest you stay seated until I have inspected you for injuries, Arata-san.>"
    sh frown "<I feel fine...{w=0.5} And I'd rather clean myself off, first.{w=0.3} I have chunks of...>"
    sh pain "<.{w=0.3}.{w=0.3}.{w=0.5}Gaspard...{w=0.5} Shit.{w=0.3} ShitshitSH-{nw}"
    am cry blood "{cps=10}Why...?"
    play sound "audio/em/em_shock.ogg"
    show screen emote("surprise",0.15,0.5)
    sh shock "...!{w=0.3} Amina!"
    pause 1.0
    show Amina blood cry at am_med:
        xalign 0.25
    show Shigeo shock at sh_med:
        xalign 0.75
    with Reveal
    pause 0.5
    am nulla "{cps=10}Why...{w=0.5} Why is this happening?{w=0.5} I don't understand...{w=0.3} Why is he gone?"
    pause 1.0
    show Shigeo sweat pain with dissolve
    pause 1.0
    show Tabitha neutral
    am nulla "{cps=10}Who's doing this to us?{w=0.3} Why are they hurting us?{w=0.3} Why did he...?"
    pause 1.0
    show Amina shock sweat with Reveal
    pause 0.5
    am_i nulla "{cps=10}\"Why...{w=0.5} {b}Why did SHE...?!?!?!\"{/b}"
    pause 1.0
    show Amina cry
    show Shigeo shock sweat
    play sound2 "audio/se/body_fall.ogg"
    hide Amina with dissolve
    show Shigeo shock sweat at sh_med:
        linear 0.2 xalign 0.3
    sh nulla "AMINA!!!"
    ta nulla "<I advise against sudden movements until we've ascertained the extent of your injuries, Arata-san.>"
    show Shigeo angry sweat
    sh nulla "Why didn't you grab her?!{w=0.3} She almost hit her head!"
    ta nulla "Switching to English...{w=0.5} And, Mr Arata."
    show Tabitha bow with dissolve
    ta nulla "The preservation of this woman's physical integrity is not among my directives.{w=0.3} {nw}"
    play sound "audio/sfx/gui_spook.ogg"
    extend "{b}Your wellbeing, on the other hand, is{/b}."
    pause 0.5
    show Shigeo surprise
    sh nulla "E...{w=0.5} Excuse me?{w=0.3} What does that even-"
    show Shigeo angry
    sh nulla "Oh, whatever!{w=0.3} Later!{w=0.3} Help me carry her to the other room!"
    show Tabitha surprise with dissolve
    ta nulla "Observation:{w=0.15} you intend to physically exert yourself despite the incognita presented by your physical state."
    show Tabitha neutral
    ta nulla "I shall acquiesce, Mr Arata."
    show Shigeo frown
    sh nulla "You'd better.{w=0.3} Gently, now."
    pause 1.0
    scene black with dissolve
    pause 1.0
    $ move_time(0,7)
    pause 0.5
    sh neutral c_half ".{w=0.3}.{w=0.3}.{w=0.5}pulse is steady.{w=0.3} Only light bruises from when Gaspard hit her...{w=0.5} Thank goodness."
    ta smile blood "I'm happy to report that your injuries are also within the realm of acceptability, Mr Arata."
    sh frown c_half "No.{w=0.3} You're not."
    ta neutral blood "...?"
    pause 1.0
    scene taisho_1f_side_meet_base
    show darkness_layer
    show Shigeo frown c_half at sh_med:
        xalign 0.35 yoffset 200
    show Tabitha blood neutral at ta_med:
        xalign 0.68
    with dissolve
    pause 1.0
    sh nulla "Happy.{w=0.3} You're not able to feel happiness, or concern, or anything like it...{w=0.5} You're a tin-can with legs."
    ta nulla "That is correct.{w=0.3} My positronic brain, while extremely sophisticated, does not possess the human capacity for emotion."
    show Tabitha bow
    play sound2 "audio/se/clothes_rustle.ogg"
    hide Shigeo with dissolve
    ta nulla "It is, though, an integral part of the human experience and it influences it on many layers, up to and including colloquialism.{w=0.3} Professor Habiki deemed it necessary that I speak in a manner as close to human as feasible and legal."
    show Shigeo frown c_half at sh_med:
        xalign 0.35
    with dissolve
    show Tabitha surprise
    ta nulla "I do happen to find some imprecision with the 'tin-can' descriptor, though.{w=0.3} My physical appearance is very much humanoid, after all."
    sh nulla ".{w=0.3}.{w=0.3}.{w=0.5}did the professor not include the concept of insults and snide remarks in your 'extremely sophisticated' brain?"
    ta nulla "Oh, so that was meant to be derogatory?{w=0.5} I apologize."
    show Tabitha bow
    show Shigeo surprise
    ta nulla "It is quite the creative area of human linguistic production, and depending on the culture it can hinge quite heavily on context.{w=0.3} I shall add it to my database, Mr Arata."
    pause 1.0
    show Shigeo pain with dissolve
    sh_n nulla "*groan*{w=0.5}\"Just...{w=0.5} Nevermind.{w=0.3} And don't call me Mr Arata, that's my father."
    show Tabitha neutral
    ta nulla "Acknowledged.{w=0.3} Would you rather I address you as Arata-kun like Professor Habiki, then?"
    show Shigeo frown
    sh nulla "Absolutely {b}not{/b}.{w=0.3} Sheesh, hinging on cultural context indeed..."
    show Shigeo neutral
    sh nulla "Let's see, you can call me..."
    pause 0.5

menu arata_nicknaming:

    sh nulla "You can call me..."

    "Arata-sama.":
        $ shn = "Arata-sama"
        jump story_03_aratanicknamed
    "Arata-dono.":
        $ shn = "Arata-dono"
        jump story_03_aratanicknamed
    "Arata-san.":
        $ shn = "Arata-san"
        jump story_03_aratanicknamed
    "Something else...":
        $ shn = renpy.input(prompt="You can call me...", default='Arata-dono', length=10, copypaste=True)
        jump story_03_aratanicknamed

label story_03_aratanicknamed:
    $ renpy.block_rollback()
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    show Tabitha bow
    ta nulla "Acknowledged.{w=0.3} I shall henceforth address you as [shn]."
    show Tabitha neutral
    ta nulla "If you ever change your mind, {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}please feel free to tell me so at any time{/b}."
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    $ tabitha_cmp = True
    pause 1.5
    sh nulla "Will do...{w=0.5} And speaking of addressing, while we wait for Amina to recover."
    show Shigeo frown
    sh nulla "I have some questions for you, android."
    show Tabitha bow
    ta nulla "I shall do my best to answer them in a satisfactory manner, [shn]."
    pause 1.0
    scene taisho_1f_side_meet_base
    show darkness_layer
    with dissolve
    pause 0.5
    show Tabitha blood neutral at ta_big:
        xalign 0.5
    with Reveal
    pause 1.0
    $ move_time(0,5)
    $ renpy.block_rollback()
    call screen tabitha_conv_01

label story_03_uneasy_trio:
    "OHNOES"