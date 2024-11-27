##Chapter name is Android
###The items and what they need to explain:
###-Katana recovered at the battle where Ame no Murakumo was lost. It's not that old, Amina notices. Shigeo agrees, reveals Kendo BG.
###-Towels received as a present by Abe's war criminal grandfather. Motif of the Fujiwara. Shigeo enlightens on who Ikki was.
###-Scroll received as a present by the Mitsui leadership. Name doesn't ring a bell, Tabitha tells who it is. Contains stuff from that incel samurai dude.
###-Wall with picture and explanation of his travels in Japan. Says that he visited area of Battle, met guys, was there for foul.

label story_03_android:
    $ renpy.block_rollback()
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
    