##Chapter name is Android
###The items and what they need to explain:
###-Katana recovered at the battle where Ame no Murakumo was lost. It's not that old, Amina notices. Shigeo agrees, reveals Kendo BG.
###-Towels received as a present by Abe's war criminal grandfather. Motif of the Fujiwara. Shigeo enlightens on who Ikki was.
###-Scroll received as a present by the Mitsui leadership. Name doesn't ring a bell, Tabitha tells who it is. Contains stuff from that incel samurai dude.
###-Wall with picture and explanation of his travels in Japan. Says that he visited area of Battle, met guys, was there for foul.

label story_03_android:
    $ renpy.block_rollback()
    $ move_time(0,1)
    $ time_menu = True
    $ codex_active = True
    $ inventory_show = True
    $ flashlight_consume = False
    $ shigeo_blood = "blood"
    $ amina_blood = "blood"
    $ current_char = "shigeo"
    pause 1.5
    scene title_03 with Reveal
    pause 3.0
    scene black with Reveal5
    pause 1.5
    play music "audio/bgm/shadows_breathe.ogg"
    sh shock blood sweat "\"{b}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHH...!!!\""
    pause 1.0
    scene tabitha_hand with Reveal3
    pause 1.0
    sh_i shock blood sweat "(Blood...!{w=0.3} Gaspard!{w=0.3} Monster!{w=0.3} ANDROID!{w=0.3} BLOOD!{w=0.3} {b}SO MUCH BLOOD!{/b})"
    ta r_neutral blood "{cps=10}.{w=0.3}.{w=0.3}.{w=0.5}harm.{w=0.3} Please re.{w=0.3}.{w=0.3}."
    sh_i fear blood sweat "(She...!{w=0.3} It!!!{w=0.3} IT RIPPED HIM APART!{w=0.3} HIS GUTS...!{w=0.3} I-)"
    ta r_neutral blood "Switching to Japanese.{w=0.3}<Please calm down.>"
    stop music fadeout 3.5
    play sound4 "audio/em/em_shock.ogg"
    show screen emote("surprise",0.15,0.5)
    sh surprise blood sweat "...!"
    pause 1.0
    scene tabitha_face with Reveal3
    pause 1.0
    sh shock blood sweat "Aaaah...{w=0.5} Aaaah..."
    ta r_neutral blood "<Arata-san.{w=0.3} I mean you no harm.{w=0.3} Please relax and allow me to inspect you for injuries.>"
    sh surprise blood sweat "<.{w=0.3}.{w=0.3}.{w=0.5}you...?>"
    play music "audio/bgm/measure_of_ningen.ogg"
    pause 1.5
    scene taisho_1f_library_base:
        xalign 0.5
    show Tabitha r_neutral blood at ta_med:
        xalign 0.5
    with Reveal3
    pause 1.5
    sh surprise blood sweat "<That's...{w=0.5}{nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}Hokkaidō-ben{/b}?>"
    ta nulla "<That is correct.{w=0.3} You have mentioned to Professor Habiki a matrilineage originating from Sapporo.>"
    show Tabitha bow with dissolve
    ta nulla "<I could surmise that you would have been exposed to the regional dialect in a family setting.{w=0.3} Thus...>"
    show Tabitha neutral with dissolve
    ta nulla "<I hypothized that switching to the specific vernacular would add a sense of familiarity to my pleas.{w=0.3} With this, I hoped to break you out of your heightened state of shock.>"
    sh neutral blood sweat "<.{w=0.3}.{w=0.3}.{w=0.5}I see.{w=0.3} Guess it worked.>"
    play sound2 "audio/se/clothes_shuffle.ogg"
    show Tabitha surprise with dissolve
    ta nulla "<I would suggest you stay seated until I have inspected you for injuries, Arata-san.>"
    sh frown blood "<I feel fine...{w=0.5} And I'd rather clean myself off, first.{w=0.3} I have chunks of...>"
    sh pain blood "<.{w=0.3}.{w=0.3}.{w=0.5}Gaspard...{w=0.5} Shit.{w=0.3} ShitshitSH-{nw}"
    am cry blood "{cps=10}Why...?"
    play sound "audio/em/em_shock.ogg"
    show screen emote("surprise",0.95,0.5)
    sh shock blood "...!{w=0.3} Amina!"
    show Amina blood cry:
        xalign 0.25
    show Shigeo shock blood:
        xalign 0.75
    with Reveal
    pause 0.5
    am nulla "{cps=10}Why...{w=0.5} Why is this happening?{w=0.5} I don't understand...{w=0.3} Why is he gone?"
    pause 1.0
    show Tabitha neutral
    show Shigeo pain
    pause 1.0
    am nulla "{cps=10}Who's doing this to us?{w=0.3} Why are they hurting us?{w=0.3} Why did he...?"
    pause 1.0
    show Amina shock sweat with dissolve
    pause 0.5
    am_i nulla "{cps=10}\"Why...{w=0.5} {b}Why did SHE...?!?!?!{/b}"
    pause 1.0
    show Amina cry
    play sound2 "audio/se/body_fall.ogg"
    hide Amina with dissolve
    show Shigeo shock sweat:
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
    $ move_time(0,7)
    pause 1.5
    sh 