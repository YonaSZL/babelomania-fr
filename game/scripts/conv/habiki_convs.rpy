#Conversation Screens with Habiki

screen habiki_conv_01:
    text "YOWZA"

init:
    default habiki_01_habiki = False
    default habiki_01_tabitha = False
    default habiki_01_wedding = False

label habiki_01_habiki:
    pause 0.5
    sh neutral "Habiki...{w=0.5} So I can call you by your first name?"
    ha nulla "As long as you remember to add 'professor'."
    sh surprise "Hm...{w=0.5} Bit odd, not going to lie."
    pause 0.5
    show Habiki smile
    ha nulla "And why would you say that?"
    sh neutral "You stress the necessity of a honorific, which means you give importance to social etiquette...{w=0.5} Or at least, to your title."
    sh frown "It's a way to put some kind of distance between you and your interlocutor, and yet you give a stranger your first name instead of your family name.{w=0.3} Kind of contradictory, don't you think?"
    ha nulla ".{w=0.3}.{w=0.3}.{w=0.5}indeed.{w=0.3} You're well steeped in our culture, I see."
    show Habiki neutral
    ha nulla "There's, though, a very logical explanation...{w=0.5} My Tabitha, here, is many things to me.{w=0.3} One of her primary functions is being my bodyguard."
    show Tabitha bow
    ha nulla "With that in mind, is it really odd that someone needing a robotic bodyguard would be quite judicious, when it came to handing out his last name?"
    sh smile ".{w=0.3}.{w=0.3}.{w=0.5}fair enough.{w=0.5} But considering the century we live in, you mean to tell me I won't find that out just by looking up 'japanese professor with android' on a search engine?"
    pause 1.5
    show Habiki smile with dissolve
    ha nulla "Quite."
    sh surprise "Quite...?{w=0.5} You mean, I won't?"
    show Habiki neutral
    show Tabitha neutral
    ha nulla "You won't."
    sh surprise "Uhm...{w=0.5} Okay, then?"
    sh_i surprise "(Is he serious...?{w=0.5} Granted, it's not the first instance I hear of someone commanding a complete information blackout on surface Internet.)"
    sh_i frown "(But the kind of power and influence you need to actually {i}obtain{/i} such a thing are...)"
    pause 1.0
    call screen habiki_conv_01

label habiki_01_tabitha:

label habiki_01_wedding:

##Original Convos cut out of Story00.
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