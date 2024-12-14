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
    sh_i shock sweat "\"{b}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHH...!!!\""
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
    sh surprise sweat "<That's... {w=0.5}{nw}"
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
    sh frown "<I feel fine...{w=0.5} And I'd rather clean myself up, first.{w=0.3} I have chunks of...>"
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
    extend "{b}Your physical integrity, on the other hand, is{/b}."
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
    sh nulla "I have some questions for you, Android."
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
    $ move_time(0,13)
    $ renpy.block_rollback()
    scene taisho_1f_side_meet_base
    show darkness_layer
    with dissolve
    pause 1.0
    show Shigeo smile c_half at sh_med:
        xalign 0.55 yoffset 150
    show Tabitha blood neutral at ta_med:
        xalign 0.88
    with dissolve
    pause 0.5
    show Amina sad c_half at am_med:
        xalign 0.29 yoffset 185 transform_anchor True rotate -5
    with Reveal
    sh nulla "Thank god...!{w=0.5} How do you feel?"
    am nulla "I...{w=0.5} Fine, I think.{w=0.3} I must have passed out when..."
    pause 1.0
    show Amina shock sweat with Reveal
    pause 0.5
    play sound4 "audio/se/whoosh_fast.ogg"
    show Amina shock sweat c_half at am_med:
        easein 0.1 xalign 0.21 yoffset 185 transform_anchor True rotate -5
    am nulla "Ah...!{w=0.3} AAAAAAH!{w=0.3} SHIGEO, SHE...!{w=0.3} THAT...?!"
    show Shigeo shock
    sh nulla "Amina, no, it's alright!{w=0.3} The Android means no harm!"
    pause 1.0
    show Amina surprise
    am nulla "A...{w=0.5} Android?"
    show Tabitha bow
    ta nulla "[shn], I must insist that we address-"
    play sound4 "audio/em/em_angry.ogg"
    show Shigeo angry
    show screen emote("angry",0.55,0.2)
    sh nulla "WILL YOU {b}SHUT UP{/b} ALREADY?!{w=0.3} You...!"
    show Shigeo pain
    show Amina shock
    show Tabitha neutral
    sh nulla "Ugh, wasted breath...{w=0.5} Android, listen."
    show Shigeo frown
    sh nulla "You are to obey all of my orders within reason, correct?"
    ta nulla "Affirmative, [shn].{w=0.3} With one caveat."
    show Tabitha surprise
    show Amina surprise
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    $ stat2_show = True
    ta nulla "Exertions with a higher than average power output necessitate a period of {nw}"
    extend "{b}cooldown for my servomotors{/b}.{w=0.3} Otherwise, overheating may cause me to become temporarily incapacitated."
    show Tabitha bow
    ta nulla "I shall advise if the task you require from me would push me over the threshold."
    sh nulla "I see...{w=0.5} Anyway, I need you to go back into the library."
    show Shigeo neutral
    sh nulla "I need you to analyze the body.{w=0.3} Get as much information as possible from it regarding the mutation.{w=0.3} Afterwards..."
    show Shigeo frown
    sh nulla "I need you to collect the lighter from the cigar box near the bonsai, and enough flammable material to start a controlled fire.{w=0.3} Then, come back.{w=0.3} Am I clear?"
    show Tabitha smile
    ta nulla "Acknowledged.{w=0.3} I will be back shortly, [shn]."
    show Tabitha frown
    ta nulla "Please do try and avoid leaving the premises of this room in the meantime."
    $ stat2 -= 25
    stop music fadeout 3.5
    pause 1.0
    play sound2 "audio/se/steps_wood_slow.ogg"
    hide Tabitha with dissolve
    pause 0.5
    am nulla "What was that all about...?{w=0.3} Shigeo, what is that thing?"
    sh nulla "An advanced Android, the creation of one of the invitees.{w=0.3} Francesco's mentor, Professor Habiki."
    am nulla "Habiki...{w=0.5} The name sounds familiar, but I'm pretty sure I did not see him nor that Android at the reception."
    show Shigeo neutral
    sh nulla "They weren't here from the beginning.{w=0.3} They arrived pretty late, and I ran into them by chance while going to the bathroom...{w=0.5} Anyway."
    pause 1.0
    show Shigeo sad with dissolve
    pause 0.5
    sh nulla "Amina, I...{w=0.5} I'm so sorry."
    pause 1.0
    show Amina sad with dissolve
    am nulla ".{w=0.3}.{w=0.3}.{w=0.5}Gaspard, he...{w=0.5} He really is gone, isn't he?"
    show Shigeo pain
    sh nulla "Yes, she...{w=0.5} It!{w=0.3} The Android dispatched him to protect me.{w=0.3} I couldn't...{w=0.5} I couldn't do anything."
    pause 1.5
    show Amina neutral -sweat with dissolve
    play music "audio/bgm/lonely_piano.ogg"
    am nulla "Shigeo, I think Gaspard was gone even before that happened."
    pause 0.5
    show Shigeo surprise
    sh nulla "Amina..."
    am nulla "You stopped me from getting closer to him, remember?{w=0.3} You had noticed something was wrong with him...{w=0.5} And..."
    show Amina fear sweat
    am nulla "The way he moved...{w=0.5} Those sunken eyes, the growth on his body...{w=0.5} {i}That terrible sound he made...!{/i}"
    show Shigeo neutral sweat
    sh nulla "Yeah, the Android...{w=0.5} It confirmed that no human could produce such a sound."
    show Shigeo pain
    sh nulla "What does that to a person...?!{w=0.3} {i}Who{/i} does that?!"
    pause 1.0
    play sound4 "audio/em/em_surprise.ogg"
    show screen emote("surprise",0.4,0.39)
    show Amina surprise
    am nulla "Who?{w=0.3} You mean...?!"
    show Shigeo frown
    sh nulla "I don't understand how it all comes together yet, nor the reasons behind any of it, but there's no way this is all a coincidence."
    show Shigeo surprise -sweat
    sh nulla "We've been trapped in someone's sick game or test, I'm sure of it...{w=0.5} And this transformation that happened to Gaspard is just another challenge for us to deal with."
    show Shigeo frown
    sh nulla "So that we'd start being wary of each other, on top of the environment."
    show Amina shock
    am nulla "You mean that what happened to him could happen to us as well?!"
    show Shigeo pain
    sh nulla "I don't know...{w=0.5} I don't know.{w=0.3} We need more information.{w=0.3} We need to think."
    show Shigeo neutral
    sh nulla "We need to untangle the mystery, expose the reasons behind this and the identity of the {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}Mastermind{/b}...{w=0.5} I'm going to need your help."
    show Amina surprise
    am nulla "My help...?"
    sh nulla "Think about it.{w=0.3} We're still at the château.{w=0.3} Not enough time elapsed for them to bring us anywhere else, and by that same coin..."
    show Shigeo angry
    sh nulla "There wasn't enough time for anyone to reach the facility, either.{w=0.5} The Mastermind, or whoever's observing and running this for them, {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}was already at the château when we passed out{/b}."
    play sound4 "audio/em/em_shock.ogg"
    show screen emote("surprise",0.4,0.39)
    show Amina shock
    am nulla "...!!!{w=0.3} So it could be one of the invitees!"
    show Shigeo frown
    sh nulla "Or someone from the catering, or the estate security...{w=0.5} But the invitees would be more probable, I think."
    show Shigeo neutral
    sh nulla "Still, I don't know anyone who was here tonight other than Francesco...{w=0.5} That's why I need your help.{w=0.3} And, Amina?"
    show Amina surprise
    show Shigeo angry
    sh nulla "I swear to you, on what I hold most sacred:{w=0.15} I will do {i}everything{/i} in my power to protect you and anyone else we may chance upon."
    pause 1.5
    show Amina smile with dissolve
    pause 0.5
    am nulla "Heh...{w=0.5} Hehehehe, you know...{w=0.5} It's funny."
    show Shigeo surprise
    sh nulla "What is?"
    am nulla "I have some knowledge of a lot of people at the wedding but...{w=0.5} Not everyone.{w=0.3} And even then, nothing deep.{w=0.3} But Gaspard?"
    pause 1.5
    show Amina cry -sweat with dissolve
    pause 0.5
    am nulla "{cps=15}Gaspard was a terrible busybody...{w=0.5} A control freak, who made it his mission in life to know angels and demons of anyone around him...{w=0.5} If he was still here, he would have been able to help you...{w=0.5} So much better than me."
    pause 1.0
    show Shigeo pain sweat with dissolve
    pause 1.5
    stop music fadeout 3.5
    scene black with Reveal3
    pause 1.5
    $ move_time(0,13)
    pause 1.0

label story_03_reasoning:
    $ renpy.block_rollback()
    play music "audio/bgm/setting_sun.ogg"
    $ stat2 += 5
    pause 1.0
    sh surprise "What do you have there, Android?"
    ta neutral "I'm happy to share that I identified my {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}briefcase{/b} in the room where I booted up, [shn].{w=0.3} Although it has been emptied of most of the objects I was carrying for Professor Habiki."
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    $ briefcase_carry = True
    pause 1.5
    scene taisho_1f_side_meet_base
    show darkness_layer
    show Amina neutral at am_med:
        xalign 0.2
    show Shigeo neutral at sh_med:
        xalign 0.43
    show Tabitha bow at ta_med:
        xalign 0.72
    with Reveal
    ta nulla "Just as well, though.{w=0.3} I took the liberty of collecting some useful items alongside the ones you had expressely asked for, [shn]."
    play sound "audio/sfx/gui_inventory.ogg"
    pause 1.0
    show Shigeo surprise
    show Amina surprise
    sh nulla "The stuff from the fridge...{w=0.5} Right, I forgot in the chaos."
    am nulla "Also, that...{w=0.5} That {i}phone{/i}...?"
    show Tabitha neutral
    ta nulla "I found it in the pocket of a discarded jacket in a corner of the room.{w=0.3} I surmise that it must have once belonged to the neutralized hostile."
    pause 1.0
    show Shigeo pain
    show Amina sad
    pause 0.5
    sh nulla "Amina, I'm sorry, we...{w=0.5} We could need it.{w=0.3} I have to ask your permission to..."
    am nulla "It's...{w=0.5} It's alright.{w=0.3} If he kept notes on it, it might help us with your investigation, too.{w=0.3} I'll show you how to unlock it later."
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    show screen notify(_("Received Smartphone."))
    $ shigeo_inventory.append(item_smartphone)
    pause 1.0
    show Tabitha bow
    ta nulla "I shall keep hold of the items you asked me to acquire and everything else you may deem useful to carry, [shn].{w=0.3} Do not hesitate to rely on me."
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    show screen notify(_("Received Lighter."))
    $ shigeo_inventory.append(item_lighter)
    show Shigeo neutral
    sh nulla "Oh, believe me I won't, Android.{w=0.3} And speaking of which."
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    show screen notify(_("Received Papers."))
    $ shigeo_inventory.append(item_papers)
    show Shigeo frown
    sh nulla "Before we do anything else, my next order:{w=0.3} you shall protect Amina as you would me.{w=0.3} Understood?"
    show Tabitha neutral
    show Amina surprise
    ta nulla "Acknowledged, [shn].{w=0.3} I need to clarify though that the order shall still fall second to the prime directive of preserving your physical integrity, in case of emergency."
    am nulla "Well, at least she's agreeable...{w=0.5} I mean it...?{w=0.3} Is agree...?"
    show Amina frown
    am nulla "Ugh, this is {i}so{/i} frustrating!{w=0.3} What's your name, Android?{w=0.3} Do you have one?"
    show Shigeo surprise
    ta nulla "Professor Habiki has given me the name Tabitha."
    am nulla "Tabitha...{w=0.5} Sure.{w=0.3} Counting on you then, Tabitha."
    show Shigeo frown
    sh nulla "I would avoid getting too familiar with it, Amina.{w=0.3} Remember what I told you?"
    am nulla "I'm not lowering my guard.{w=0.3} But I'm not used to calling anything I can talk to by 'it', it doesn't really exist in French.{w=0.3} It just gets confusing."
    show Amina neutral
    show Shigeo surprise
    sh nulla "Oh, right...{w=0.5} Would it help if I also started referring to it by 'she'?"
    show Amina smile
    am nulla "It would, yeah.{w=0.3} <Merci, Shigeo>."
    show Tabitha bow
    ta nulla "Observation:{w=0.15} I'm ready to discuss the findings of my inspection at your leisure, [shn]."
    show Tabitha frown
    show Amina neutral
    show Shigeo frown
    ta nulla "But considering the need for timeliness on the mutation issue, I would suggest we address them {i}immediately{/i}."
    sh nulla "Hmph.{w=0.3} Fair enough...{w=0.5} Proceed, then."
    show Tabitha neutral
    ta nulla "Thank you, [shn].{w=0.3} In the meantime, may I have your clothes?"
    pause 1.0
    play sound4 "audio/em/em_question.ogg"
    show screen emote("question",0.47,0.05)
    show screen emote2("question",0.28,0.15)
    show Shigeo surprise
    show Amina surprise
    sh nulla "I beg your pardon...?"
    show Tabitha bow
    ta nulla "The cleaning products I usually carry due to Professor Habiki's messy eating habits were left in my briefcase.{w=0.3} Inspection confirms that they were not tampered with."
    show Tabitha smile
    ta nulla "My make and programming allows me to subroutinize a number of less complex tasks.{w=0.3} To optimize time, I would clean and disinfect the clothes that have come in contact with the hostile's blood while I relay information."
    show Tabitha neutral
    ta nulla "I've taken the liberty of already cleaning my garments and chassis, as to avoid cross-contamination during the process."
    pause 1.0
    show Shigeo blush with dissolve
    sh nulla "Ehm...{w=0.5} That is efficient, I guess, but-"
    show Amina neutral
    am nulla "Makes sense to me.{w=0.3} Here."
    play sound "audio/se/clothes_rustle.ogg"
    show Amina c_half with dissolve
    play sound4 "audio/em/em_blush.ogg"
    show screen emote("blush",0.47,0.05)
    show Shigeo shock
    sh nulla "A-{w=0.15}AMINA!"
    show Amina surprise
    am nulla "What?{w=0.5} She's right, better if she does this while we talk.{w=0.3} If it's some kind of infection, we're strapped for time.{w=0.3} Don't be prudish, now, it's just our upper garments."
    pause 1.0
    show Shigeo frown with dissolve
    sh_n nulla "\"Uhm, aah...{w=0.5}{cps=10}*mumblegrumble*"
    pause 1.0
    scene black with dissolve
    play sound "audio/se/clothes_rustle.ogg"
    $ move_time(0,3)
    pause 0.5
    sh naked frown blush "So, uhm, this report?"
    ta bow "Thank you for entrusting your clothes to me, [shn].{w=0.3} Now commencing report..."
    ta neutral "An in-depth analysis of the neutralized hostile was easier than projected thanks to its present physical state.{w=0.3} Upon inspection, I found that its physical structure and overall anatomy resemble that of the human body 76.999998\%."
    ta surprise "This was found to be in line with [shn]'s statement regarding the hostile being previously identifiable as the individual 'Gaspard'."
    am sad naked ".{w=0.3}.{w=0.3}.{w=0.5}what happened to him exactly?"
    ta neutral "The hostile underwent a number of sweeping and irreversible changes.{w=0.3} The nature of these changes doesn't find precedent in the available data."
    pause 0.5
    scene gaspard_turn_00 with Reveal
    pause 0.5
    ta neutral "Change number one:{w=0.15} the skin of the hostile had transformed into an unidentified {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}carbon-based alloy{/b}."
    am shock naked "Carbon-based...?!{w=0.3} His skin has become some kind of metal?!"
    sh surprise naked "Which explains how he was able to gouge that table with his...{w=0.5} Claws."
    ta smile "Affirmative.{w=0.3} The transformed skin had also been arranged and molded into a variety of shapes.{w=0.3} I observed a tendency to increase the edge of a human body's naturally sharp areas."
    sh frown naked "Fingers, elbows, shoulders, toes...{w=0.5} What else?"
    pause 1.0
    scene gaspard_rip with Reveal
    pause 0.5
    ta bow "Change number two:{w=0.15} upon inspection, I found that most of the hostile's {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}internal organs had withered{/b}."
    sh surprise naked "His organs had withered...?{w=0.5} Wait."
    pause 1.0
    $ overlay_off()
    jump think_02_organs_think

label story_03_brainssss:
    $ overlay_on()
    scene gaspard_turn_03 with Reveal
    pause 0.5
    am naked surprise "So you're telling me that...{w=0.5} This virus, or whatever it is, consumes all the water in your body...{w=0.5} While reinforcing your muscles and nerves?"
    sh naked frown sweat "Looks like it...{w=0.5} Android, I imagine the state of the organs would be unsuitaible to sustain life?"
    ta bow "Affirmative, [shn].{w=0.3} We can confidently consider the human named as Gaspard and the neutralized hostile as two separate entities."
    ta neutral "The latter arose when the afflicting patogen, whatever its nature, repurposed the body of the deceased human into the being that attacked [shn]."
    pause 1.0
    am naked sweat sad "Two...{w=0.5} Two questions.{w=0.3} Did you...{w=0.5} Whatever its nature means that you couldn't...{w=0.5} See anything?{w=0.3} Do you even have that kind of equipment?"
    ta frown "I am equipped with advanced ocular sensors, and Professor Habiki often employs them in his lab work.{w=0.3} I was perfectly qualified to complete [shn]'s request to satisfaction."
    ta neutral "In my investigation, I couldn't find any trace of a possible culprit pathogen.{w=0.5} I hypothize that, considering the pattern of alteration, we may found some traces if we were to investigate the inside of the cranium."
    sh naked pain sweat ".{w=0.3}.{w=0.3}.{w=0.5}I'm going to have to ask you to abstain from that."
    ta bow "A wise choice, [shn].{w=0.3} In an uncontrolled environment such as this, we wouldn't want to risk you being contaminated during examination."
    sh naked frown sweat "Not the main reason why I asked but...{w=0.5} Sure, let's go with that."
    am naked sweat fear "The brain, yeah...{w=0.5} That's my second question.{w=0.3} Shigeo, from the way you're making it sound, it feels like whatever this thing is, it kills its victims and...{w=0.5} Reduces them to the basic function of a meatsuit that can move."
    am naked sweat shock "If that is the case...{w=0.5} If it doesn't need any of the other organs nor fluids to exist...{w=0.5} Then {nw}"
    stop music fadeout 3.5
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}wouldn't that imply...?{/b}"
    pause 3.0
    scene taisho_1f_side_meet_base
    show darkness_layer
    play sound "audio/em/em_impact.ogg"
    show Shigeo naked shock sweat at sh_big:
        xalign 0.5
    sh nulla "{b}IT'S STILL ALIVE!{/b}{w=0.3} THAT THING IS STILL ALIVE?!"
    ta neutral "I indeed registered some responses during my investigation, [shn]."
    show Shigeo angry
    sh nulla "WHY THE {b}FUCK{/b} DIDN'T YOU LEAD WITH THAT?!"
    ta neutral "Owing to its current state of physical integrity, it is unable to present any resistance.{w=0.3} Even in its full state, it has proven to be easily dispatchable."
    ta bow "Consequently, it is not an immediate threat.{w=0.3} The investigation into the nature of the pathogen and the decontamination of your garments were of higher priority."
    am naked shock sweat "<Ya Allah!>{w=0.3} Please tell me you're done, Tabitha!"
    play sound3 "audio/se/clothes_rustle.ogg"
    ta smile "Quite.{w=0.3} The subroutined task has been completed within the expected time parameters."
    show Shigeo frown
    sh nulla ".{w=0.3}.{w=0.3}.{w=0.5}this is why I hate androids."
    pause 1.0
    scene black with dissolve
    $ amina_blood = "None"
    $ shigeo_blood = "None"
    play sound "audio/se/clothes_rustle.ogg"
    $ move_time(0,19)
    pause 0.5
    scene taisho_1f_corridor with Reveal
    $ stat2 -= 5
    pause 0.5
    sh frown "Time to get out of here."
    am surprise "We're looking for a smoke detector, right?{w=0.3} I believe that's it."
    sh surprise "Yup...{w=0.5} Alright, now I just need to {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}set the papers in place{/b} and then {b}light them on fire{/b}."
    pause 0.5
    $ current_puzzle = "taisho_fire"
    call screen pzl_taisho_1f_fire

label story_03_fire_starter:
    $ renpy.block_rollback()
    $ current_puzzle = "None"
    scene taisho_1f_corridor
    show pzl_papers:
        xpos 796 ypos 699
    pause 1.0
    sh frown "Alright, be ready.{w=0.3} The moment the fire alarm goes on the door should unlock...{w=0.5} But I don't know for how long."
    ta neutral "Worry not, [shn].{w=0.3} I shall keep it open as long as needed."
    sh neutral "Hmm...{w=0.5} Here goes nothing."
    play sound "audio/se/lighter.ogg"
    pause 1.5
    play LoNoise "audio/bgs/fire_small.ogg" fadein 0.5
    scene taisho_1f_corridor
    show pzl_papers_fire:
        xpos 796 ypos 699
    with dissolve
    pause 0.5
    play sound4 "audio/sfx/gui_solved.ogg"
    pause 1.0
    am smile "Flames took to them nicely.{w=0.3} Good selection."
    ta bow "Of course.{w=0.3} I took care to choose only the most suitable kind of paper, from books that I would not expect [shn] to mind the destruction of."
    show screen emote("question",0.15,0.5)
    play sound4 "audio/em/em_question.ogg"
    sh surprise "Excuse me?{w=0.3} How would you even know about something like-"
    play LoNoise2 "audio/bgs/alarm_beep.ogg" fadein 0.1
    pause 1.5
    play sound3 "audio/se/door_heavy_unlock.ogg"
    play LoNoise "audio/bgs/rain_inside.ogg" fadein 0.1
    scene taisho_1f_corridor_open
    show rain_overlay
    with dissolve
    sh smile "Nevermind that!{w=0.3} It worked!"
    ta frown "Allow me, [shn]."
    play sound "audio/se/whoosh_medium.ogg"
    pause 0.2
    show Tabitha frown brief behind rain_overlay:
        zoom 0.14 xpos 930 ypos 395
    with dissolve
    pause 0.5
    am surprise "She's quick on her feet, isn't she?{w=0.3} What is she made of?"
    sh frown ".{w=0.3}.{w=0.3}.{w=0.5}some kind of carbon alloy.{w=0.3} And I'm only half kidding, here."
    show Tabitha neutral
    ta neutral "The stairwell is clear, [shn].{w=0.3} Please."
    sh neutral "You first, Amina."
    am neutral "Yes.{w=0.3} Thank you."
    pause 0.5
    show Amina neutral behind rain_overlay:
        zoom 0.14 xpos 1015 ypos 445
    with dissolve
    pause 1.0
    show Amina sad with dissolve
    pause 0.5
    am_i sad "(Goodbye, Gaspard...)"
    hide Amina with dissolve
    pause 0.5
    show Tabitha surprise
    ta surprise "[shn]?"
    sh frown "I'm coming...{w=0.5} Just...{w=0.5} You barricated all the doors, right?"
    ta bow "Affirmative, [shn]."
    sh_i frown sweat "(.{w=0.3}.{w=0.3}.{w=0.5}don't take this the wrong way, Gaspard, but I hope I never see your mug again as long as I live.)"
    pause 1.0
    scene black with Reveal
    pause 1.5
    stop LoNoise2 fadeout 7.0
    scene taisho_1f_library_base
    show darkness_layer
    show rain_overlay
    with Reveal3
    pause 3.0
    show intro_corpse behind rain_overlay
    with Reveal3
    pause 3.0
    play sound4 "audio/se/sting.ogg"
    show gaspard_flex behind rain_overlay
    pause 1.5
    stop LoNoise fadeout 0.5
    scene black
    pause 3.0
    $ renpy.block_rollback()

label story_03_taisho_lower:
    $ renpy.block_rollback()
    $ stat2 -= 2
    $ move_time(0,2)
    play music "audio/bgm/setting_sun.ogg"
    $ dark_environ = True
    pause 1.0
    $ shigeo_inventory.remove(item_papers)
    $ shigeo_inventory.remove(item_taisho_note)
    sh_i sweat "(Alright, I have no more need of this note...{w=0.5} Might as well throw it away.)"
    play sound4 "audio/se/paper_rustle.ogg"
    pause 1.0
    play sound "audio/se/door_heavy_unlock.ogg"
    pause 1.0
    scene taisho_foyer with Reveal3
    pause 1.5
    ta bow "I deem this a safe environment, [shn].{w=0.3} Please proceed."
    sh neutral "For now...{w=0.5} At least we can see the outside, from here."
    am neutral "Through tempered glass...{w=0.5} How probable would you say the front door being locked is?"
    ta neutral "Considering pregress circumstances as detailed by [shn], I calculate a 93.2 percent probability."
    am surprise "Ehm, right.{w=0.3} Thank you, Tabitha."
    ta bow "You are welcome."
    sh_n frown "*sigh*{w=0.5}\"Anyway."
    show Amina surprise:
        yanchor 1.0 xpos 375 ypos 867 zoom 0.148
    show Shigeo neutral:
        yanchor 1.0 xpos 265 ypos 880 zoom 0.15
    show Tabitha neutral brief:
        yanchor 1.0 xpos 540 ypos 880 zoom 0.15
    with dissolve
    play sound2 "audio/se/door_heavy_rattle.ogg"
    sh neutral "I see no padlock or input panel on this one...{w=0.5} Just a keyhole."
    show Amina surprise
    am surprise "No code puzzle this time, then...{w=0.5} We need to {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}find the key{/b}."
    pause 1.0
    show taisho_foyer_door with Reveal
    pause 1.0
    show Shigeo surprise
    sh surprise "Either that or tear it down...{w=0.5} Android, would you be-"
    show Shigeo pain
    sh pain "No, wait, bad idea.{w=0.3} Nevermind."
    show Tabitha surprise
    ta surprise "[shn], I'm positive I would be able to dispose of this door."
    show Shigeo neutral
    sh neutral "Not without considerable expense of time and heating up, I imagine.{w=0.3} I'd rather you save that energy for emergencies."
    show Shigeo frown sweat
    pause 1.0
    hide taisho_foyer_door with dissolve
    pause 0.5
    sh frown sweat "We're in completely uncharted territory, here.{w=0.3} If more of those things show up, you're our only line of defense."
    ta surprise "So you'd have me prioritize long term energy efficiency over possible short-term gains."
    show Tabitha neutral
    ta neutral "Acknowledged.{w=0.3} I shall endeavour to function by your guidelines as closely as possible, [shn]."
    show Shigeo neutral -sweat
    sh neutral -sweat "Do that.{w=0.3} Now let's look for that key."
    show Amina neutral
    am neutral "If the keycode debacle was any indication, it is not going to be straightforward at all...{w=0.5} Let's not overlook anything."
    show Amina surprise
    am surprise "Also, speaking of lines of defense:{w=0.3} we should try and {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}find something we can use as a weapon{/b}."
    show Tabitha smile
    ta smile "A wise observation, miss Amina.{w=0.3} [shn], do I have your authorization to include that in my list of tasks?"
    sh neutral "Please do...{w=0.5} Let's get to work, now."
    $ story_progress = 2
    pause 1.0
    $ stat2 -= 3
    $ move_time(0,3)
    scene taisho_foyer with dissolve
    $ renpy.block_rollback()
    call screen taisho_foyer_explore with dissolve