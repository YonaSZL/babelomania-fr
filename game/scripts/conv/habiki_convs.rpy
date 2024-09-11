#Conversation Screens with Habiki

screen habiki_conv_01:
    text "YOWZA"


label habiki_01_gaspard:
    

##Original Convos cut out of Story00.
    sh nulla "Ugh...{w=0.5} If this thing answers to you, may I kindly ask:{w=0.15} what the hell?"
    
    
    show Shigeo surprise -sweat
    sh nulla "And you are...?{w=0.5} I don't think I've seen you at the ceremony, nor the reception so far.{w=0.3} I would remember an elderly academic shadowed by a two meters tall android."
    show Habiki laugh
    ha_x nulla "Oh, you would be surprised...{w=0.5} But indeed, we've but recently arrived."
    show Habiki smile
    ha_x nulla "The drive to the château was quite long and tiring...{w=0.5} Hence the need to indulge in my little vice.{w=0.3} But I fear that I could not persuade Tabitha to fully close the door."
    pause 1.0
    show Shigeo frown
    sh nulla "You could not...{w=0.5} Persuade it?"
    pause 1.5
    show Habiki neutral with dissolve
    pause 0.5
    ha_x nulla "Oh, if I really wanted I could've ordered her to...{w=0.5} But I find that going against actions dictated by her prime directives is quite disruptive."
    show Habiki smile
    show Tabitha bow
    ha nulla "In this case, the directive is to protect me from any and all threats...{w=0.5} And with that, let me belatedly introduce myself as {b}professor Habiki{/b}."
    pause 1.5
    show Shigeo neutral
    sh nulla "Keeping your last name close to your chest, are you?"
    ha nulla "If I could share it willy nilly, I wouldn't be in need of a 6'6'' tall robotic bodyguard...{w=0.5} I'm afraid you'll have to make do with that, and the knowledge that I am with the groom's party."
    show Habiki neutral
    ha nulla "And so do you, I believe."
    show Shigeo surprise
    sh nulla ".{w=0.3}.{w=0.3}.{w=0.5}how can you tell?"
    show Habiki laugh
    ha nulla "Are you kidding me?{w=0.5} Delphine's family and male acquaintances wouldn't be caught dead in an Italian-cut suit."
    pause 1.0
    show Shigeo frown
    sh nulla "I did notice a certain...{w=0.5} Conforming on that front, yeah."
    show Habiki neutral
    ha nulla "So you did.{w=0.5} Well, it's been quite the amusing encounter."
    show Habiki smile
    ha nulla "Have a good evening, mister Arata...{w=0.5} Who knows, we may run into each other again, before the night is over."
    stop music fadeout 3.5
    show Habiki neutral
    ha nulla "Let's go, Tabitha."
    pause 1.5
    play sound3 "audio/se/steps_marble_slow.ogg"
    hide Habiki with dissolve
    show Tabitha neutral
    pause 0.5
    play sound2 "audio/se/steps_marble_slow.ogg"
    pause 1.0
    show Shigeo frown with dissolve
    pause 0.5
    sh_i nulla "(Freaky...{w=0.5} I've never seen an android that looks so much like a human.{w=0.3} Regulations in Japan really are lax, aren't they?)"
    show Shigeo surprise
    sh_i nulla "(Also, why are they going upstairs...?{w=0.5} Oh, whatever.{w=0.3} It's none of my business.)"
    show Shigeo sad
    sh_i nulla "(Let's just go back in...)"
    pause 1.0