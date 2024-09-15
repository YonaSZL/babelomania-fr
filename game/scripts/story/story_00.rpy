label story_00_start:
    $ renpy.block_rollback()
    stop music fadeout 0.5
    scene black with flash
    pause 3.0
    scene intro_disclaimer with dissolve
    pause 6.5
    scene black with Reveal
    pause 1.5
    show intro_babel with dissolve
    pause 4.5
    play sound "audio/se/glitch_long_01.ogg"
    pause 1.0
    play music "audio/bgm/sanity_glitch.ogg"
    pause 1.0
    scene black with glitch_unload
    pause 1.0
    scene intro_hand_A with glitch_load_5
    pause 3.5
    scene intro_corpse with glitch_load_5
    pause 3.5
    scene intro_hand_A with glitch_load_5
    pause 1.5
    scene intro_hand_B with quick_dissolve
    pause 2.0
    scene black
    pause 3.0
    show intro_tabitha:
        yalign 1.0
    with dissolve
    pause 1.5
    show intro_tabitha:
        easein 7.0 yalign 0.0
    pause 8.5
    scene black
    show intro_tabitha_side:
        yalign 0.0
    with glitch_load
    pause 1.5
    scene intro_reach with glitch_unload
    pause 2.0
    play sound "audio/se/glitch_medium_01.ogg"
    pause 1.0
    stop music fadeout 1.0
    scene black with glitch_unload_5
    pause 3.0
    jump story_00_invitation

label story_00_invitation:
    $ renpy.block_rollback()
    scene title_01 with Reveal
    pause 3.0
    scene black with Reveal5
    pause 1.5
    $ quick_menu = True
    pause 1.0
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
    d """
    From: Delphine & Francesco{nw}

    Date: Fri, 30 Apr 20XX at 19:46{nw}

    Subject: We're getting married!\n
    """
    play sound4 "audio/sfx/gui_hint.ogg"
    d """
    Dearest {b}Shigeo{/b},\n

    We're getting married (again!), and you're cordially invited.\n

    After tying the knot in the presence of our parents and siblings on Saturday, 11th April 20XX, we couldn't wait to celebrate with all our friends and family. We hope you can join us!\n

    Check out our wedding website and app to RSVP and find more information.\n

    {b}Saturday, 14 May 20XX{/b}
    """
    nvl clear
    play sound "audio/sfx/gui_phone_swipe.ogg"
    pause 0.5
    d """
    From: Delphine & Francesco{nw}

    Date: Wed, 19 Jan 20XX at 19:46{nw}

    Subject: Important Information about the Venue.\n

    Dearest Shigeo,\n

    As the countdown to our wedding day continues, we are thrilled to share some essential information to ensure your stay in France is comfortable and convenient. Below are the details regarding the accommodations for our special day on May 14th.\n

    Location:
    """
    play sound4 "audio/sfx/gui_hint.ogg"
    d """
    The {b}Château de Bois-le-Dumont{/b} is unique even among the many beautiful châteaux that populate France. It originated as an eighteenth century vanity project from an aristocrat, left unfinished in the wake of the revolution. After decades of abandon, it was eventually purchased by the eccentric {b}Abelard Du Bois{/b}, who over the following decades shaped it into the château as it is today.\n

    The ceremony and reception will take place in the {b}Baroque Building{/b}, while the guests will be accomodated in the {b}Taisho Building{/b}.\n
    """
    nvl clear
    d """
    Directions to the Venue:

    Please use the link below to find some useful information on how to reach the château. Shuttles are going to be organized at specific times for guests. If you'd rather arrange for your own personal transportation, please let us know.\n
    
    Warm regards,{nw}

    Delphine & Francesco{nw}
    
    P.S. If language is a barrier, please contact Delphine for assistance in French.
    """
    pause 1.5
    nvl clear
    scene black with Reveal3
    pause 3.0
    play music "audio/bgm/canon_in_bois.ogg"
    pause 1.0
    $ time_menu = True
    pause 1.0
    scene chateau_setting with Reveal3
    pause 3.0
    scene black with Reveal3
    pause 0.5
    play LoNoise "audio/bgs/reception_crowd.ogg" fadein 0.2
    pause 1.0
    scene bar_reception with Reveal3
    pause 1.5
    sh_xi darko frown "(I should've just sent a card...{w=0.5} This is killing me.)"
    tb_n "<And let me tell you, the attention to detail of monsieur Du Bois went far beyond just architecture!>"
    sh_xi darko neutral "(I can recognize the name of the original owner, something about architecture...{w=0.5} <Au-delà>?{w=0.3} He went beyond architecture, I guess?)"
    tb_n "<You will find, spread throughout the estate, different pieces of art collected over the course of his travels.{w=0.3} Or specially commissioned to complement specific rooms of the complex!>"
    tb_n2 "<Indeed?{w=0.5} To be honest, I don't exactly approve of a lot of the placements.{w=0.3} Like in the toilets downstairs?>"
    sh_xi darko surprise "(Now they're talking about the toilet of all things?{w=0.3} The place of the toilets??)"
    tb_n "<Indeed...{w=0.5} You have to remember, though, that the family turned the estate from museum to source of profit in 2025.{w=0.3} Afterwards, god only knows who had a hand in reshaping it and moving things around.>"
    tb_n2 "<Ah, yes.{w=0.3} That would explain that monstrosity in the bathrooms!>"
    sh_xi darko smile "(Oh, finally!{w=0.3} They're definitely talking about {nw}"
    play sound "audio/sfx/gui_hint.ogg"
    extend "{b}that painting{/b}!{w=0.3} And I guess how out of place it is?)"
    sh_x darko surprise "Uhm...{w=0.5} <At first I thought it had been put there to help.>"
    tb_n "<Huh?{w=0.5} To help?>"
    pause 1.0
    show Shigeo neutral at sh_big:
        xalign 0.5
    with Reveal
    pause 1.5
    tb_n2 "<What do you mean, monsieur {b}Arata{/b}?>"
    show Shigeo smile
    sh nulla "<Well, if you see something that creepy while entering the toilets you->"
    pause 1.0
    play sound "audio/em/em_surprise.ogg"
    show screen emote("surprise",0.5,0.05)
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
    $ renpy.block_rollback()
    pause 0.5
    sh nulla "<I mean, uhm...{w=0.5} Seeing something like that, in an unexpected place...{w=0.5} It scares you, no?>"
    show Shigeo neutral
    sh nulla "<And being scared makes the blood fast...{w=0.5} That should help, no?>"
    pause 2.0
    tb_n2 "<Hmm, I guess that is biologically true...{w=0.5} But I doubt it was the reason why they put that thing downstairs.>"
    tb_n "<Our young italian friend gives the current owners too much credit, me thinks!{w=0.3} Ahahahah!>"
    show Shigeo sad
    sh_i nulla "(Oh, thank god...{w=0.5} They don't think I'm a moron yet.{w=0.3} Emphasis on yet.)"
    jump story_00_bathroom_break

label story_00_relaxation:
    $ renpy.block_rollback()
    pause 0.5
    sh nulla "<Well, such a painting...{w=0.5} It makes you think about it.{w=0.3} About what it means.>"
    show Shigeo neutral
    sh nulla "<And if you get lost in such thoughts, it helps you relax...{w=0.5} And being relaxed is important in this situation, no?>"
    pause 2.0
    tb_n "<Quite, quite!{w=0.3} It is indeed an intriguing enough piece, especially for those not used to contemplating art.>"
    tb_n2 "<I doubt most people would expect to contemplate art in that situation...{w=0.5} Still, I doubt they did it on purpose.>"
    sh_i nulla "(Well, it seems I managed to save my hide...{w=0.5} Or at least make them continue the conversation and ignore me again.)"
    jump story_00_bathroom_break

label story_00_bathroom_break:
    show Shigeo sad -sweat
    sh_i nulla "(Ugh, this is really the worst...{w=0.5} I need some air.)"
    play sound "audio/se/item_slide.ogg"
    tb_n "<Still a shame that the original vision of Du Bois got so altered...{w=0.5} Oh, you're leaving us, young man?>"
    show Shigeo neutral
    sh nulla "<Yes, I'm sorry.{w=0.3} Talking about bathrooms made me think about it.>"
    tb_n2 "<Fair enough!{w=0.3} We won't keep you, then!>"
    show Shigeo laugh
    sh nulla "<Thank you very much.>"
    pause 0.5
    hide Shigeo with dissolve
    pause 1.0
    play sound3 "audio/se/steps_marble_walk.ogg"
    pause 0.5
    tb_n "<Peculiar young man...{w=0.5} You say he's with the groom's party?>"
    tb_n2 "<He is.{w=0.3} Wonder why he's sitting with us, then?>"
    pause 1.0
    stop LoNoise fadeout 0.5
    stop music fadeout 1.0
    scene black with dissolve
    $ move_time(0,4)
    pause 1.0
    play music "<from 39>audio/bgm/canon_in_bois_muted.ogg" fadein 0.2
    pause 0.5
    sh_i "(My name is Shigeo Arata.{w=0.3} I'm a friend of the groom at this reception...)"
    sh_i sad "(And only the groom.)"
    sh_i neutral "(I know {nw}"
    play sound "audio/sfx/gui_hint.ogg"
    extend "{b}Francesco{/b} from high school.{w=0.3} He was my best friend, truth tell.)"
    pause 1.0
    scene bar_corr_recep with Reveal3
    pause 1.5
    sh_i "(After graduation, though, we both left Italy to go study in different countries...{w=0.5} We kept in touch but, the relationship certainly wasn't as close-knit as it had once been.)"
    show Shigeo neutral at sh_big:
        xalign 0.5
    with dissolve
    sh_i nulla "(I didn't even know he had gotten married until I received the invitation...{w=0.5} At first I thought it would be a great opportunity to reconnect but I barely exchanged five words with him.)"
    show Shigeo sad
    sh_i nulla "(I don't know anyone else here.{w=0.3} And even when I try and interact, there's...)"
    pause 1.5
    show Shigeo neutral with dissolve
    pause 0.5
    sh_i nulla "(Whatever.{w=0.3} Where were the stairs, again?)"
    pause 0.5
    hide Shigeo with dissolve
    pause 1.0
    call screen exp_bar_corr with dissolve
    
label story_00_bathroom_encounters:
    pause 0.5
    show Shigeo neutral at sh_med:
        xalign 0.5
    with dissolve
    pause 0.5
    play sound4 "audio/se/steps_marble_step.ogg"
    pause 0.3
    show screen emote("surprise",0.445,0.05)
    show Shigeo surprise
    pause 0.2
    play sound "audio/se/whoosh_fast.ogg"
    show Shigeo shock at sh_med:
        linear 0.3 xalign 0.35
    sh nulla "Woah!{w=0.3} Excuse me!"
    pause 0.5
    sh_i nulla "(Geez, she was in a hurry!{w=0.3} I think it was one of the bridesmaids?)"
    show Shigeo neutral
    sh_i nulla "(I ended up being the one apologizing, too...{w=0.5} Not even a <désolée>?{w=0.3} Some people are weird.)"
    pause 1.0
    play sound "audio/se/steps_stairs_down.ogg"
    scene black with dissolve
    stop music fadeout 1.5
    pause 0.5
    $ move_time(0,3)
    pause 1.0
    play music "audio/bgm/safehouse.ogg"
    pause 1.0
    scene bar_bathroom with Reveal3
    pause 1.0
    play sound "audio/se/water_faucet.ogg"
    sh_i surprise "(Hmmm?{w=0.5} Someone else is here.)"
    pause 0.5
    show Gaspard surprise at ga_med:
        xalign 0.5
    with Reveal
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
    pause 2.0
    $ move_time(0,5)
    play sound "audio/se/water_faucet.ogg"
    pause 0.5
    scene bar_bathroom with dissolve
    pause 0.5
    sh_i neutral sweat "(.{w=0.3}.{w=0.3}.{w=0.5}that painting really is something else, isn't it?)"
    pause 1.0
    scene bathroom_painting with Reveal
    pause 1.5
    sh_i neutral -sweat "(Looking at it up close, it feels even more out of place...{w=0.5} No matter what excuses I make up.)"
    sh_i frown "(When was this made?{w=0.5} And by whom?)"
    pause 1.0
    call screen bathroom_painting_examine

label story_00_bathroom_return:
    $ renpy.block_rollback()
    pause 0.5
    sh_i smile "(There we go.)"
    pause 1.0
    scene bar_bathroom
    show Shigeo smile at sh_med:
        xalign 0.5
    with dissolve
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    show screen notify("Codex Unlocked")
    $ codex_active = True
    pause 0.5
    sh_i nulla "(Well, that was a good way to waste a few minutes and distract myself...{w=0.5} And now I have something to occupy myself further, if need be.)"
    show Shigeo neutral
    sh_i nulla "(Let's go back upstairs, now, and see if I can't actually find someone to socialize with...{w=0.5} Or maybe the bride's family may have finally relinquished their hold on Francesco.{w=0.3} That'd be nice.)"
    pause 1.0
    stop music fadeout 1.0
    scene black with dissolve
    pause 0.5
    $ move_time(0,4)
    pause 1.0
    play music "<from 39>audio/bgm/canon_in_bois_muted.ogg" fadein 0.2
    scene bar_corr_recep with Reveal3
    pause 1.5
    sh_i surprise "(Hmm?{w=0.5} What's that sm-)"
    pause 1.5
    sh_i frown "(Ugh, of course.)"
    pause 0.5
    show Shigeo frown at sh_med:
        xalign 0.7
    with dissolve
    pause 0.5
    sh_i nulla "(Someone left the door to the smoking room open...{w=0.5} And now everyone else shall partake of their breathalized cancer, too.)"
    show Shigeo at sh_med:
        easein 7.0 xalign 0.5
    sh_i nulla "(Let's close the door before the stench seeps in my clo-)"
    pause 0.5
    stop music fadeout 0.2
    play sound "audio/em/em_shock.ogg"
    show screen emote("surprise",0.5,0.05)
    pause 0.5
    show Shigeo surprise
    pause 1.5
    play music "audio/bgm/uncanny.ogg"
    play sound4 "audio/em/em_impact.ogg"
    scene black
    show tabitha_grab:
        xanchor 960 yalign 0.0 xpos 0
    with vpunch
    pause 0.5
    sh_i shock "(What...?!{w=0.5} What is...?!)"
    ta_x darko "Warning:{w=0.3} you are entering restricted personal space."
    sh_i shock sweat "(The grip is so strong but more than that, what...{w=0.5} The hand feels so cold and...{w=0.5} Weird!)"
    ta_x darko "Failure to remove yourself from the restricted area will be cause for reprisal.{w=0.3} Please acknowledge."
    sh_i fear sweat "(It's completely smooth and rigid and yet soft at the same time...?!{w=0.3} What the hell is touching me?!)"
    ta_x darko "I repeat."
    sh shock "...!{w=0.5} Ugh?!"
    pause 1.0
    show tabitha_grab:
        easein 7.0 xalign 0.0
    pause 8.0
    sh shock "What...?!"
    ta_x darko "Failure to remove yourself from the restricted area will be cause for reprisal.{w=0.3} Please acknowledge."
    sh_i surprise "(This...{w=0.5} What is this thing?!{w=0.3} It looks human...{w=0.5} It has the proportions of a human, its face looks human and yet...)"
    sh_i shock "(That sickly looking grey skin...{w=0.5} Those lifeless ashen eyes...{w=0.5} That even voice, completely devoid of emotion or inflection...)"
    sh_i angry "(What the hell is this {b}thing{/b}?!)"
    sh angry "NNGH!{w=0.3} Let go of me, you-!"
    ha_x darko "{b}Tabitha{/b}, that's quite enough."
    sh shock "...!"
    pause 1.0
    stop music fadeout 3.5
    pause 1.0
    scene bar_corr_recep
    show Tabitha neutral brief at ta_med:
        xalign 0.4
    show Shigeo shock sweat at sh_med:
        xalign 0.6
    with Reveal3
    pause 0.5
    ha_x darko "Let the young man go."
    play sound "audio/em/em_question.ogg"
    show screen emote("question",0.6,0.05)
    show Shigeo surprise
    sh nulla "Who...?"
    pause 2.0
    show Tabitha bow
    ta nulla "Acknowledged, professor."
    show Tabitha at ta_med:
        easein 5.0 xalign 0.35
    pause 2.0
    play sound "audio/se/whoosh_fast.ogg"
    show Shigeo angry at sh_med:
        linear 0.5 xalign 0.65
    pause 1.0
    show Habiki neutral at ha_med:
        xalign 0.2
    with Reveal3
    pause 0.5
    play music "audio/bgm/echo_of_mountains.ogg"
    pause 1.0
    ha_x nulla "Tabitha, my Tabitha...{w=0.5} Always so overzealous."
    show Habiki smile
    ha_x nulla "This stranger barely has the countenance of a grown man, leave alone an outlaw."
    sh nulla ".{w=0.3}.{w=0.3}.{w=0.5}you know, considering that your bucket of bolts almost attacked me, I'd think an apology would be a better introduction than veiled insults."
    pause 0.5
    show Habiki laugh
    ha_x nulla "My, such a rude young man.{w=0.3} Calling my Tabitha a bucket of bolts..."
    sh nulla "It's obviously not a person...{w=0.5} Let's call it just Android, then."
    pause 1.0
    show Shigeo surprise with dissolve
    sh nulla "I've never seen one quite like this, I'll give you that."
    pause 1.0
    show Tabitha neutral
    show Habiki neutral
    ha_x nulla "But you've seen others...?{w=0.5} They're not exactly common."
    sh nulla "Unsurprisingly, considering how much they cost...{w=0.5} And their construction being outlawed in most of the world."
    show Shigeo frown -sweat
    sh nulla "<Japan is not one such country, though.{w=0.3} Am I right?>"
    show Habiki surprise
    pause 1.0
    show Habiki neutral
    ha_x nulla "<Fully fluent, and a very light accent...{w=0.5} {nw}"
    play sound "audio/sfx/gui_hint.ogg"
    extend "A {b}hafu{/b}, then?>"
    sh nulla "<My mother's from Sapporo, my father from Genova...{w=0.5} My name's Shigeo Arata.>"
    ha_x nulla "<I see...{w=0.5} Interesting.>"
    show Habiki smile
    ha nulla "<Quite interesting indeed...{w=0.5} Please feel free to address me as {nw}"
    play sound "audio/sfx/gui_hint.ogg"
    extend "{b}Professor Habiki{/b}, Shigeo-kun.>"
    pause 1.0
    show Shigeo surprise
    sh_i nulla "(Professor...{w=0.5} {i}Habiki{/i}?)"
    pause 1.0
    scene bar_corr_recep with dissolve
    pause 1.0
    show Tabitha neutral brief at ta_big:
        xalign 0.3
    show Habiki neutral at ha_big:
        xalign 0.7
    with dissolve
    pause 1.0
    $ renpy.block_rollback()
    call screen habiki_conv_01

label story_00_meet_gaspard:
    $ renpy.block_rollback()
    show Habiki neutral
    show Tabitha neutral
    stop music fadeout 3.5
    ha nulla "Well, it's been quite the amusing encounter...{w=0.5} But we've held each other up quite enough, I believe."
    show Habiki smile
    ha nulla "Once again, apologies for the incident.{w=0.3} I'll be more mindful of my surroundings, for the duration."
    sh neutral "Appreciated...{w=0.5} No harm done, then."
    show Tabitha bow
    ha nulla "Have a good evening, Shigeo-kun...{w=0.5} Who knows, we may run into each other again, before the night is over."
    show Habiki neutral
    ha nulla "Let's go, Tabitha."
    pause 0.5
    play sound3 "audio/se/steps_marble_walk.ogg"
    hide Habiki with dissolve
    show Tabitha neutral
    pause 0.5
    hide Tabitha with dissolve
    play sound2 "audio/se/steps_marble_walk.ogg"
    pause 1.0
    show Shigeo frown at sh_big:
        xalign 0.5
    with dissolve
    pause 0.5
    sh_i nulla "(Freaky...{w=0.5} I've never seen an Android that looks so much like a human.{w=0.3} Regulations in Japan really are lax, aren't they?)"
    show Shigeo surprise
    sh_i nulla "(Also, why are they going upstairs...?{w=0.5} Oh, whatever.{w=0.3} It's none of my business.)"
    show Shigeo neutral
    sh_i nulla "(Let's just go back in.)"
    pause 1.0
    scene black with dissolve
    $ move_time(0,17)
    pause 0.5
    play music "audio/bgm/canon_in_bois.ogg"
    pause 0.5
    play LoNoise "audio/bgs/reception_crowd.ogg" fadein 0.2
    scene bar_reception with Reveal
    pause 0.5
    sh_i neutral "(People are standing up...{w=0.5} I guess we're between dishes and there's some kind of small event coming up.)"
    sh_i smile "(And lo and behold, is that Francesco away from the family table I see?!{w=0.3} Finally!)"
    sh_i laugh "(Oh, I'm going to give him so much shit for 'by the way'-ing me about his-)"
    ga_x frown "<Excuse me.{w=0.3} Monsieur?>"
    sh surprise "...!{w=0.3} Hmm?"
    pause 1.0
    show Gaspard frown at ga_med:
        xalign 0.5
    with Reveal
    pause 1.5
    sh_i surprise "(The...{w=0.5} The guy I ran into in the bathrooms?)"
    sh_i frown "(Expensive looking suit in parisian blue, similarly costly looking accessories from a number of different brands...{w=0.5} Yeah, this guy is definitely with the bride's half of the party.)"
    ga_x nulla "<Apologies for calling out to you so suddenly but, I believe we ran into each other earlier?>"
    sh neutral "<You mean downstairs?{w=0.5} Yes, that's correct.>"
    ga_x nulla "<I see...{w=0.5} I wanted to apologize.>"
    show Gaspard neutral
    ga_x nulla "<I came across as quite rude, I believe, not returning your greeting.{w=0.3} I just wasn't expecting anyone to come through the door at that precise moment.{w=0.3} I'm easily startled.>"
    sh surprise "<Oh...{w=0.5} Well, it's fine.{w=0.3} Thanks for seeking me out to apologize.>"
    show Gaspard laugh
    ga nulla "<Very gracious of you.{w=0.3} My name is {nw}"
    play sound "audio/sfx/gui_hint.ogg"
    extend "{b}Gaspard Faucigny{/b}.>"
    show Gaspard neutral
    ga nulla "<Pleased to make your acquaintance.>"
    sh surprise "<I'm called Arata.{w=0.3} Shigeo Arata...>"
    sh_i surprise "(Hmmm, I do have a window for Francesco but at the same time, it would be rude to just brush this person off...)"
    sh_i smile "(Also, the groom will eventually need to go back to his seat.{w=0.3} This guy looks to be around my same age, so a new acquaintance wouldn't hurt.)"
    sh smile "<Pleased to meet you too, Gaspard.>"
    pause 1.0
    scene bar_reception with dissolve
    pause 0.5
    show Gaspard neutral at ga_big:
        xalign 0.5
    with dissolve
    pause 0.5
    call screen gaspard_conv_01

label story_00_meet_amina:
    $ move_time(0,9)
    $ renpy.block_rollback()
    pause 0.5
    ga nulla "You must come sit with me and mine for the rest of the evening.{w=0.3} I insist."
    sh smile "I would really appreciate it, thanks.{w=0.3} I've been spending the first part of the dinner surrounded by older academics who don't speak a word of English."
    show Gaspard neutral
    ga nulla "Oh, we're at least bilingual at our table.{w=0.3} I'm sure you'll-"
    am_x darko "Gaspard?"
    pause 0.5
    show Gaspard surprise
    pause 1.0
    show Gaspard neutral with dissolve
    pause 0.5
    ga nulla "Ah, {b}Amina{/b}.{w=0.3} Perfect timing."
    sh_i surprise "(Amina?{w=0.5} Oh...)"
    pause 1.0
    show Amina neutral at am_big:
        xalign 0.85
    with Reveal3
    pause 1.0
    ga nulla "Let me introduce you to Shigeo Arata.{w=0.3} He's a childhood friend of Francesco, if you can believe it."
    show Amina surprise
    am nulla "Is he, now?{w=0.5} Interesting."
    sh smile "A pleasure to meet you.{w=0.3} I have to ask, though, why is it such a surprise to everyone whenever I mention that?"
    am nulla "Because Francesco barely talks about his life before coming to France."
    show Amina smile
    am nulla "Having a living piece of it present at his wedding is not something anyone expected...{w=0.5} I'm Amina Abbas, pleasure is mine."
    ga nulla "Also known as my beautiful girlfriend...{w=0.5} You needed something from me, <petite>?"
    pause 0.5
    show Amine neutral with dissolve
    pause 0.5
    am nulla "Your father wanted to speak to you.{w=0.3} Something about an email."
    pause 1.0
    show Gaspard frown with dissolve
    pause 0.5
    ga nulla "Ugh, honestly...{w=0.5} Not disconnecting from work even at an event like this."
    show Gaspard neutral
    ga nulla "Let me go deal with that real quick.{w=0.3} <Petite>, mind showing Shigeo to our table?{w=0.3} He will be sitting with us for the rest of the night."
    show Amina surprise
    am nulla "He is?{w=0.3} But Gaspard-"
    hide Gaspard with dissolve
    pause 1.0
    show Amina frown with dissolve
    pause 0.5
    am nulla ".{w=0.3}.{w=0.3}.{w=0.5}there are no more free seats."
    sh surprise "Oh.{w=0.3} I'm sorry, I...{w=0.5} I didn't mean to be a bother."
    am nulla "You did nothing wrong...{w=0.5} It's fine, we can just ask the caterers to add one more chair."
    show Amina surprise
    am nulla "Honestly, I'm more surprised than anything else.{w=0.3} Gaspard never hits it off so quickly with anyone, leave alone-"
    pause 1.0
    show Amina neutral
    am nulla "Ehm, nevermind that.{w=0.3} Come, I'll show you to our table."
    sh surprise "Uhm...{w=0.5} Sure.{w=0.3} Let me just-"
    stop music fadeout 3.5
    fr_x darko smile "<Counterorder, Amina.{w=0.3} I will show him to your table myself in a couple minutes.>"
    show Amina surprise sweat
    sh_i sweat surprise "(...!{w=0.5} That...{w=0.5} That voice...)"
    pause 1.0
    play music "audio/bgm/francesco.ogg"
    pause 1.5
    scene bar_reception with dissolve
    pause 0.5
    show Francesco smile at fr_med:
        xalign 0.85
    show Shigeo surprise sweat at sh_med:
        xalign 0.5
    show Amina surprise sweat at am_med:
        xalign 0.2
    with Reveal3
    pause 1.5
    sh_i nulla "(It's changed...{w=0.5} It carries something else.{w=0.3} So much else, compared to when we last met...{w=0.5} Yet, the timbre and cadence are...{w=0.5} Unmistakable, even through the filter of French.)"
    am nulla "{b}Francesco{/b}, you...{w=0.5} Scared me.{w=0.3} I didn't even hear you approach."
    show Francesco laugh
    fr nulla "Oh, you know me, soft stepped and all.{w=0.3} And I guess I felt like surprising you~"
    show Francesco smile
    fr nulla "Anyway, as I said:{w=0.3} pleeee~eeeeeease let me catch up a little with my best friend ever?{w=0.5} I only have a few minutes of freedom."
    pause 1.0
    show Amina neutral -sweat
    am nulla "Fine by me.{w=0.3} See you at the table then, Arata."
    play sound2 "audio/se/steps_stone_walk.ogg"
    pause 1.0
    show Shigeo neutral -sweat with dissolve
    pause 1.0
    sh nulla "Your best friend ever, am I...?"
    show Francesco neutral
    fr nulla "Always have been, man.{w=0.3} It's great to see you face to face again, after all these years."
    pause 1.0
    show Shigeo smile
    sh nulla "Pfft, how can you say that with a straight face...?{w=0.3} I didn't even know you had gotten married!"
    show Francesco surprise
    fr nulla "Oh, believe me, I did you a favour!{w=0.3} The ceremony at the commune was {i}such{/i} a drag!{w=0.3} And it was all in French, mandatory!"
    show Francesco smile
    fr nulla "Last I remember, you couldn't stop complaining to me about the language."
    sh nulla "And I still could, for days...{w=0.5} But leave alone the wedding, you hadn't even told me you had gotten hitched!"
    show Francesco surprise
    fr nulla "Whaaaaat?{w=0.5} I did tell you that dating was going pretty well, didn't?"
    show Shigeo laugh
    sh nulla "<Oh, you son of a bitch...!>{w=0.5} What's wrong with you?!"
    show Francesco laugh
    fr nulla "Oh, you have {i}no{/i} idea!"
    pause 1.5
    show Shigeo smile
    show Francesco smile
    with dissolve
    pause 1.0
    sh nulla "Have you been well?{w=0.3} I can tell you're doing well for yourself romance-wise but what about the rest?"
    fr nulla "Real good.{w=0.3} The in-laws are a bit much but, I can handle them.{w=0.3} I can handle most things that come my way, nowadays."
    show Francesco surprise
    fr nulla "And your parents?{w=0.3} How are they?"
    pause 0.5
    show Shigeo neutral
    sh nulla "Better...{w=0.5} Dad's gotten over what happened in Rome, adjusted to his new post."
    show Shigeo sad
    sh nulla "Still not a word from mother.{w=0.3} But I still keep in contact with uncle's kids, she's doing fine."
    fr nulla "I see...{w=0.5} It was so screwed up "