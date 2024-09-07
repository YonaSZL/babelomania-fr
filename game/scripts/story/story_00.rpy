label story_00_start:
    $ quick_menu = False
    $ time_menu = False
    stop music fadeout 0.5
    scene black with flash
    pause 2.0
    scene babel_tale with quick_dissolve
    pause 3.0 #Or however is needed
    play music "audio/bgm/intro_track.ogg"
    pause 1.0
    play sound "audio/sfx/gui_glitch.ogg"
    scene black with glitch
    pause 1.0
    scene intro_00 with dissolve
    pause 1.5
    scene intro_01 with dissolve
    pause 1.5
    scene intro_02 with dissolve
    pause 1.5
    scene black
    show intro_03:
        yalign 1.0# yanchor 1.0
    with dissolve
    pause 1.5
    show intro_03:
        linear 3.0 yalign 1.5
    pause 0.5
    scene intro_04 with dissolve
    pause 1.5
    play sound "audio/sfx/gui_glitch.ogg"
    stop music fadeout 0.5
    scene black with glitch
    pause 3.0
    jump story_00_invitation

label story_00_invitation:
    $ quick_menu = False
    $ time_menu = False
    pause 0.5
    scene intro_phone_a with Reveal
    pause 1.5
    play sound "audio/sfx/gui_notification.ogg"
    pause 0.2
    scene intro_phone_b
    pause 1.5
    play sound "audio/sfx/gui_phone_unlock.ogg"
    scene intro_phone_c
    pause 1.5
    play sound "audio/sfx/gui_phone_swipe.ogg"
    pause 0.5
    phnv """From: Delphine & Francesco
    Date: Fri, 30 Apr 20XX at 19:46
    Subject: We're getting married!

    Dearest Shigeo,

    We're getting married (again!), and you're cordially invited.

    After tying the knot in the presence of our parents and siblings on Saturday, 11th April 20XX, we couldn't wait to celebrate with all our friends and family. We hope you can join us!

    Check out our wedding website and app to RSVP and find more information.

    {b}Saturday, 14 May 20XX{/b}
    {clear}
    From: Delphine & Francesco
    Date: Wed, 19 Jan 20XX at 19:46
    Subject: Important Information about the Venue

    Dearest Shigeo,

    As the countdown to our wedding day continues, we are thrilled to share some essential information to ensure your stay in France 
    is comfortable and convenient. Below are the details regarding the accommodations for our special day on May 14th.

    Location:
    The {b}Château de Bois-le-Dumont{/b} is unique even among the many beautiful châteaux that populate France. It originated as an eighteenth century vanity project from an aristocrat, left unfinished in the wake of the revolution.
    After decades of abandon, it was eventually purchased by the eccentric Abelard Du Bois, who over a period of thirty years shaped it into the château as it is today.

    The ceremony and reception will take place in the {b}Baroque Building{/b}, while the guests will be accomodated in the {b}Shoin Building{/b}.

    Directions to the Venue:
    Please use the link below to find some useful information on how to reach the château. Shuttles are going to be organized at specific times for guests.
    If you'd rather arrange for your own personal transportation, please let us know.

    Warm regards,

    Delphine & Francesco

    P.S. If language is a barrier, please contact Delphine for assistance in French.
    """
    nvl clear
    pause 1.5
    scene black with Reveal2
    pause 1.0
    play music "audio/bgm/canon_in_bois.ogg"
    pause 1.0
    $ time_menu = True
    pause 0.5
    scene chateau_air with Reveal2
    pause 3.0
    scene black with Reveal2
    pause 0.5
    play LoNoise "audio/bgs/reception_crowd.ogg" fadein 0.2
    pause 1.0
    scene bar_reception with Reveal2
    pause 1.5
    sh_xi nulla "(I should've just sent a card...{w=0.5} This is killing me.)"
    tb_n "<And let me tell you, the attention to detail of monsieur Du Bois went far beyond just architecture!>"
    sh_xi nulla "(I can recognize the name of the original owner, something about architecture...{w=0.5} Au-delà?{w=0.3} He went beyond architecture, I guess?)"
    tb_n "<You will find, spread out throughout the buildings, different pieces of art collected over the course of his travels.{w=0.3} Or personally commissioned to complement specific rooms of the complex!>"
    tb_n2 "<Indeed?{w=0.5} To be honest, I don't exactly approve of a lot of the placements.>"
    sh_xi nulla "(Now they're talking about the toilet of all things?{w=0.3} The place of the toilets??)"
    tb_n "<Indeed...{w=0.5} You have to remember, though, that the family sold the estate in 2025.{w=0.3} After that, god only knows who had a hand in reshaping it and moving things around.>"
    tb_n2 "<Ah, yes.{w=0.3} That would explain the painting in the bathrooms!>"
    sh_xi nulla "(Oh, finally!{w=0.3} They're definitely talking about the painting in the toilets!{w=0.3} And I guess how out of place it was?)"
    sh_x darko "Uhm...{w=0.5} <At first I thought it had been put there to help.>"
    tb_n "<Huh?{w=0.5} To help?>"
    pause 1.0
    show Shigeo neutral with Reveal
    pause 0.5
    tb_n2 "<What do you mean, monsieur {b}Arata{/b}?>"
    #Intro Screen for Characters, for Arata
    show Shigeo smile
    sh nulla "<Well, if you see something that creepy while entering the toilets you->"
    pause 1.0
    play sound "audio/em/em_surprise.ogg"
    show screen emote("surprise",0.5,-0.05)
    show Shigeo surprise sweat
    sh_i nulla "(Aw, crap!{w=0.3} There's no such thing as scared shitless in French!{w=0.3} They say that you have a 'blue fear'!)"
    tb_n "<Yes, yes, the subject matter is quite fascinatingly grotesque...{w=0.5} So?>"
    sh_i nulla "(Damn it, Shigeo...{w=0.3} Think, think, think!{w=0.3} Bullshit your way out of this one, already!)"
    pause 1.0
    jump story_00_shit

menu story_00_shit:

    "It favours the blood flow.":
        jump story_00_concentration

    "It favours relaxation.":
        jump story_00_relaxation
    

label story_00_concentration:
    pause 0.5
    sh nulla "<I mean, uhm...{w=0.5} Seeing something like that, in an unexpected place...{w=0.5} It scares you, no?>"
    show Shigeo neutral
    sh nulla "<And being scared makes the blood fast...{w=0.5} That should help, no?>"
    pause 2.0
    tb_n2 "<Hmm, I guess that is biologically true...{w=0.5} But I doubt it was the reason why they put that painting in the toilets.>"
    tb_n "<Our young italian friend gives the current owners too much credit, me thinks!{w=0.3} Ahahahah!>"
    show Shigeo sad
    sh_i nulla "(Oh, thank god...{w=0.5} They don't think I'm a moron yet.{w=0.3} Emphasis on yet.)"
    jump story_00_bathroom_break

label story_00_relaxation:
    pause 0.5
    sh nulla "<Well, such a painting...{w=0.5} It makes you think about it.{w=0.3} About what it means.>"
    show Shigeo neutral
    sh nulla "<And if you get lost in such thoughts, it helps you relax...{w=0.5} And being relaxed is important in this situation, no?>"
    pause 2.0
    tb_n "<Quite, quite!{w=0.3} It is indeed an intriguing enough painting, especially for those not used to contemplating art.>"
    tb_n2 "<I doubt most people would expect to contemplate art while going to the bathroom...{w=0.5} Still, I doubt they did that on purpose.>"
    sh_i nulla "(Well, it seems I managed to save my hide...{w=0.5} Or at least make them continue the conversation and ignore me again.)"
    jump story_00_bathroom_break

label story_00_bathroom_break:
    show Shigeo sad
    sh_i nulla "(Ugh, this is really the worst...{w=0.5} I need some air.)"
    play sound "audio/se/chair_pull.ogg"
    tb_n "<Still a shame that the original vision of Du Bois got so altered...{w=0.5} Oh, you're leaving us, young man?>"
    show Shigeo neutral
    sh nulla "<Yes, I'm sorry.{w=0.3} Talking about bathrooms made me think about it.>"
    tb_n2 "<Fair enough!{w=0.3} We won't keep you, then!>"
    show Shigeo laugh
    sh nulla "<Thank you very much.>"
    pause 0.5
    hide Shigeo with dissolve
    pause 1.0
    play sound3 "audio/se/steps_marble_slow.ogg"
    pause 0.5
    tb_n "<Peculiar young man...{w=0.5} You say he's with the groom's party?>"
    tb_n2 "<He is.{w=0.3} Wonder why he's sitting with us, then?>"
    pause 1.0
    stop LoNoise fadeout 0.5
    stop music fadeout 0.5
    scene black with dissolve
    $ move_time(0,0,4)
    pause 0.5
    play music "<from 39>audio/bgm/canon_in_bois_muted.ogg" fadein 0.2
    pause 0.5
    sh_i "(My name is Shigeo Arata.{w=0.3} I'm a friend of the groom at this reception...)"
    sh_i sad "(And only the groom.{w=0.3} I know literally no one else, here.)"
    sh_i neutral "(I know Francesco from high school.{w=0.3} He was my best friend, truth tell.)"
    pause 1.0
    scene bar_corr_recep with Reveal
    pause 1.5
    sh_i "(After graduation, though, we both left Italy to go study in another country...{w=0.5} We kept in touch but, the relationship certainly wasn't as close-knit as it had once been.)"
    show Shigeo neutral with dissolve
    sh_i nulla "(I didn't even know he had gotten married until I received the invitation...{w=0.5} At first I thought it would be a great opportunity to reconnect but, I barely exchanged five words with him.)"
    show Shigeo sad
    sh_i nulla "(I don't know anyone else here.{w=0.3} And even when I try and interact...)"
    pause 1.5
    show Shigeo neutral with dissolve
    pause 0.5
    sh_i nulla "(Whatever.{w=0.3} Where were the stairs, again?)"
    pause 0.5
    hide Shigeo with dissolve
    pause 0.5
    sh_i neutral "(The bathrooms are {b}downstairs{/b}...)"
    pause 1.0
    call screen exp_bar_corr
    
label story_00_bathroom_encounters:
    sh_i neutral "(There we are.{w=0.3} The stairs going down.)"
    pause 0.5
    show Shigeo neutral with dissolve:
        xalign 0.5
    pause 0.5
    play sound3 "audio/se/steps_stairs_coming_up.ogg" fadein 0.2
    pause 0.3
    show screen emote("surprise",0.45,-0.05)
    show Shigeo surprise
    pause 0.2
    play sound "audio/se/swoosh_quick.ogg"
    show Shigeo shock:
        linear 0.3 xalign 0.35
    sh nulla "Woah!{w=0.3} Excuse me!"
    pause 0.5
    sh_i nulla "(Gee, she was in a hurry!{w=0.3} I think that was one of the bridemaids?)"
    show Shigeo neutral
    sh_i nulla "(I ended up being the one apologizing, too...{w=0.5} Not even a <désolée>?{w=0.3} Some people are weird.)"
    pause 1.0
    scene black with dissolve
    stop music fadeout 1.5
    pause 0.5
    $ move_time(0,0,3)
    pause 1.0
    play music "audio/bgm/safehouse.ogg"
    pause 1.0
    scene bar_bathroom with Reveal
    pause 1.0
    play sound "audio/se/water_faucet.ogg"
    sh_i surprise "(Hmmm?)"
    pause 0.5
    show Gaspard surprise with Reveal
    pause 1.5
    sh neutral "Uhm, hello...{w=0.3} <Good evening?>"
    pause 0.5
    show Gaspard frown with dissolve
    pause 1.0
    hide Gaspard with dissolve
    play sound "audio/se/door_swivel.ogg"
    pause 0.5
    sh_i frown "(Once again...{w=0.5} Some people are weird.)"
    pause 0.5
    play sound3 "audio/se/door_stall.ogg"
    scene black with dissolve
    pause 1.5
    play sound2 "audio/se/water_flush.ogg"
    pause 1.0
    scene bar_bathroom with dissolve
    pause 0.5
    play sound "audio/se/water_faucet.ogg"
    sh_i neutral sweat "(.{w=0.3}.{w=0.3}.{w=0.5}that painting really is something else, isn't it?)"
    pause 1.0
    scene bathroom_painting with Reveal
    pause 1.5
    sh_i neutral "(Looking at it up close, it feels even more out of place...{w=0.5} No matter what excuses I can make up.)"
    sh_i frown "(When was this made?{w=0.5} And by whom?)"
    pause 1.0
    call screen bathroom_painting_examine

label story_00_bathroom_painting_photo:
    sh_i neutral "(That seems to be everything I can surmise from this painting...{w=0.5} Too bad about the missing author, now I want to know more.)"
    sh_i smile "(Let me take a picture of it.{w=0.3} I can Coogle it later, or show someone back home.{w=0.3} Dorothy would know.)"
    play sound "audio/sfx/gui_phone_unlock.ogg"
    call screen phone_camera("bathroom_painting", "story_00_bathroom_return")

label story_00_bathroom_return:
    scene bathroom_painting with phone_pic
    pause 0.5
    sh_i smile "(There we go.)"
    show screen record_made("")
    pause 1.0
    scene bar_bathroom
    show Shigeo smile
    with dissolve
    pause 0.5
    sh_i nulla "(Well, that was a good way to waste a few minutes and distract myself...{w=0.5} I have something to occupy myself, too.)"
    show Shigeo neutral
    sh_i nulla "(Let's go back upstairs, now, and see if I can't actually find someone to socialize with...{w=0.5} Or maybe the bride's family may have finally relinquished their hold on Francesco, that'd be nice.)"
    pause 1.0
    stop music fadeout 0.5
    scene black with dissolve
    pause 0.5
    $ move_time(0,0,4)
    pause 1.0
    scene bar_corr_recep