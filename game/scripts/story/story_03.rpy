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
    sh shock sweat "\"{b}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHH...!!!\""
    pause 1.0
    scene tabitha_hand with Reveal3
    pause 1.0
    sh_i shock sweat "(Blood...!{w=0.3} Gaspard!{w=0.3} Monster!{w=0.3} ANDROID!{w=0.3} BLOOD!{w=0.3} {b}SO MUCH BLOOD!{/b})"
    ta 