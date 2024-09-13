#Conversation Screens with Gaspard

default gaspard_01_gaspard = False
default gaspard_01_bathroom = False
default gaspard_01_wedding = False

screen gaspard_conv_01:
    text "YOWZA"

label gaspard_01_gaspard:
    pause 0.5
    ga nulla "<Since I haven't had the plesure so far, I assume you are an invitee on the groom's side.>"
    sh neutral "<Exactly.{w=0.3} I'm an old friend of Francesco...{w=0.5} And how do you know Delphine?>"
    show Gaspard smile
    ga nulla "<Oh, our families go way back...{w=0.5} When you deal with our kind of business, you end up always running in the same circles.>"
    show Gaspard neutral
    ga nulla "<We also went to the same business school.{w=0.3} We're not exactly close but, I wasn't about to rebuke a wedding invite.{w=0.3} Especially with Château de Bois-le-Dumont as a location.>"
    sh surprise "<It is an impressive estate, from what little I've seen so far...{w=0.5} You've been here before?>"
    show Gaspard frown
    ga nulla "<A few times...{w=0.5} Although this is the first time I will have to stay the night in the Taisho building.>"
    sh surprise "<I see...{w=0.5} And, is there a problem with that?>"
    ga nulla "<Not exactly a fan of the>"
    pause 1.0
    if gaspard_01_gaspard == False:
        $ gaspard_01_gaspard = True
    call screen gaspard_conv_01

label gaspard_01_gaspard:
    pause 0.5

    pause 1.0
    if gaspard_01_gaspard == False:
        $ gaspard_01_gaspard = True
    call screen gaspard_conv_01

label gaspard_01_gaspard:
    pause 0.5

    pause 1.0
    if gaspard_01_gaspard == False:
        $ gaspard_01_gaspard = True
    call screen gaspard_conv_01