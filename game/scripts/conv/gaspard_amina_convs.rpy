#Conversation Screens with Gaspard
#HEC Paris
#Sorbonne

default gaspmina_conv_01 = 0
default gaspmina_01_shigeo = False
default gaspmina_01_gaspardamina = False
default gaspmina_01_code = False
default gaspmina_01_phone = False

screen gaspmina_conv_01():
    add "gui/talkie/bottom.png" yalign 1.0

    if gaspmina_conv_01 == 4:
        textbutton _("Return") action Jump("story_01_taisho") align(1.0, 1.0) offset(-60,-10) text_size 60 hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"

    vbox:
        ypos 300 xpos -880 ##button positions

        ####Indicator if viewport is scrollable
        ####Scrollbar looked ugly
        button:
            xysize(65,65) xalign 1.0 xoffset -400
            add "gui/talkie/scroll_bg.png"
            add "gui/talkie/scroll_arrow.png" at arrow_up
            
        viewport:
            style_prefix "talkie"
            scrollbars "vertical" mousewheel True draggable True
            vbox:
                spacing 20
                button:
                    text _("Shigeo")
                    at btn_slide
                    if gaspmina_01_shigeo:
                        background "gui/talkie/button.png"
                    else:
                        background "gui/talkie/button_empty.png"
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("gaspmina_01_shigeo")

                button:
                    text _("Gaspard&Amina")
                    at btn_slide
                    if gaspmina_01_gaspardamina:
                        background "gui/talkie/button.png"
                    else:
                        background "gui/talkie/button_empty.png"
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("gaspmina_01_gaspardamina")

                button:
                    text _("Door Code")
                    at btn_slide
                    if gaspmina_01_code:
                        background "gui/talkie/button.png"
                    else:
                        background "gui/talkie/button_empty.png"
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("gaspmina_01_code")
                
                if gaspmina_01_code:
                    button:
                        text _("Phones")
                        at btn_slide
                        if gaspmina_01_phone:
                            background "gui/talkie/button.png"
                        else:
                            background "gui/talkie/button_empty.png"
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                        action Jump("gaspmina_01_phone")


        ####Indicator if viewport is scrollable
        button:
            xysize(65,65) xalign 1.0 xoffset -400
            add "gui/talkie/scroll_bg.png"
            add "gui/talkie/scroll_arrow.png" at arrow_down

label gaspmina_01_shigeo:
    $ renpy.block_rollback()
    pause 0.5
    ga nulla "<What were you even doing, in here?>"
    sh neutral -sweat "I wasn't exactly {i}doing{/i} anything, other than looking around.{w=0.3} I woke up in here not long ago, in complete darkness."
    show Gaspard surprise
    show Amina surprise
    am nulla "Just like us...{w=0.5} What is the last thing you remember?"
    sh frown "The wedding.{w=0.3} The start of the video, playing on the wall screen...{w=0.5} Then nothing."
    sh neutral "Next thing I know I was waking up, laying down on that couch.{w=0.3} What about the two of you?"
    show Gaspard frown
    am nulla "Pretty much the same story...{w=0.5} We woke up sprawled out on the floor in a nearby room."
    show Amina neutral
    am nulla "Last thing I remember was that video, too.{w=0.3} I mean..."
    show Amina surprise
    am nulla "Not...{w=0.5} I mean, I remember that that's what we were doing but...{w=0.5} I don't really remember {nw}"
    play sound "audio/sfx/gui_spook.ogg"
    extend "{b}anything about the contents{/b}?"
    show Gaspard surprise
    ga nulla "<You don't remember the video itself...?>"
    sh surprise "Now that you mention it...{w=0.5} You're right, I don't remember anything about that, either."
    sh frown "And yet, I'm sure that I saw at least a few seconds of it before...{w=0.5} Blacking out."
    show Amina neutral
    am nulla "That's quite odd...{w=0.5} Gaspard, how about you?"
    pause 1.0
    show Gaspard frown
    ga nulla "<If neither of you remember it and so far we've all had the same experiences, what makes you think this is any different?>"
    show Amina surprise
    am nulla "I...{w=0.5} I was just checking."
    ga nulla "<Hmph.>"
    sh neutral ".{w=0.3}.{w=0.3}."
    pause 1.0
    $ renpy.block_rollback()
    if gaspmina_01_shigeo == False:
        $ gaspmina_01_shigeo = True
        $ gaspmina_conv_01 += 1
    call screen gaspmina_conv_01

label gaspmina_01_gaspardamina:
    $ renpy.block_rollback()
    pause 0.5
    sh neutral -sweat "How long ago did you wake up?{w=0.3} Have you met anyone else?"
    ga nulla "<No one.{w=0.3} I woke up first, the room was...{w=0.5} Similar to this one.{w=0.3} A small study with awful furnishing...{w=0.5} Definitely the Taishō building.>"
    show Amina neutral
    am nulla "I woke up shortly afterwards.{w=0.3} Total darkness, lights don't work.{w=0.3} Same for the main corridor, although there's light coming through the window from outside."
    sh frown "Which means that the power failure is concentrated...{w=0.5} Maybe something happened to the transformer, or they messed with the eletrical panel."
    show Gaspard surprise
    ga nulla "<They messed with the...{w=0.5} What?{w=0.3} What's that word?>"
    sh surprise "Ah?{w=0.3} Uhm, the...{w=0.5} Damn it, I don't know the word in French..."
    am nulla "<Le tableau de distribution électrique, Gaspard.>"
    ga nulla "<Ah, that!{w=0.3} That...>"
    show Gaspard frown
    ga nulla "<Ugh, speak French already!{w=0.3} What's the matter with you?>"
    sh neutral "I'm...{w=0.5} Sorry, but I'm not fluent enough in it to properly articulate my thoughts in such a situation."
    am nulla "Gaspard, it's fine.{w=0.3} I can translate if there's anything you don't understand."
    show Gaspard angry
    ga nulla "<Oh, thank you {i}so{/i} much!{w=0.3} That's not the point!>"
    show Amina surprise
    am nulla "Gaspard...!"
    ga nulla "<Why do I have to be the one accomodating him?!{w=0.3} We're in France, damn it!{w=0.3} Speak the language if we really must suffer...>"
    pause 1.0
    show Gaspard surprise sweat with dissolve
    ga nulla "<Suffer...{w=0.5} Aaaah...>"
    pause 1.0
    show Amina sad
    pause 0.5
    sh neutral "<We're in a difficult, mysterious situation.{w=0.3} Being stressed is perfectly normal.>"
    sh frown "<I understand wanting things to feel familiar.{w=0.3} Safe.{w=0.3} But because it's a difficult situation, I need to speak the best I can.>"
    show Gaspard frown
    sh neutral "<And I'm not good enough with your language to do that.{w=0.3} But you're good enough with mine, right?{w=0.3} You told me.>"
    ga nulla "<Whatever...{w=0.5} I don't get why you're here too, anyway.>"
    show Amina neutral
    sh neutral "I've been asking myself the same question...{w=0.5} I can guess that between the two of you, any kidnapper would be able to request a hefty sum for your safe return."
    sh surprise "Not so much for me.{w=0.3} I'm a public servant, entry level, and both of my parents are middle class."
    show Gaspard -sweat
    ga nulla "<Oh, like those types understand stuff like this.{w=0.3} You were at the same reception and at our same table, they just grabbed whoever they could.>"
    sh neutral ".{w=0.3}.{w=0.3}.{w=0.5}maybe so."
    pause 1.0
    $ renpy.block_rollback()
    if gaspmina_01_gaspardamina == False:
        $ gaspmina_01_gaspardamina = True
        $ gaspmina_conv_01 += 1
    call screen gaspmina_conv_01

label gaspmina_01_code:
    $ renpy.block_rollback()
    pause 0.5
    sh neutral -sweat "Are you alright?{w=0.3} Physically, I mean.{w=0.3} You were throwing yourself against the door."
    ga nulla "<That was me, yes.{w=0.3} I'm fine.>"
    show Amina sad
    am nulla "<Just try and not do anything strenuous with your right side, for a little bit.>"
    ga nulla "<Hmph.>"
    sh surprise "I didn't know what to think for a moment, there.{w=0.3} First you were rattling the knob, then you tried breaking the door down, and then you just...{w=0.5} Opened it.{w=0.3} How?"
    show Amina neutral
    am nulla "Since this room is quite identical to the one we woke up in, door and all, I figured they worked the same.{w=0.3} Can be opened from the inside but you need a {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}code{/b} to open them from the outside."
    sh surprise "A code, you say?"
    ga nulla "<Yeah.{w=0.3} There's a keypad on the wall, outside.>"
    sh neutral "I see...{w=0.5} I must say, that was very lucky of you to be able to guess."
    show Amina surprise
    am nulla "Well, we didn't...{w=0.5} Not the code itself, anyway."
    show Amina neutral
    play sound3 "audio/se/paper_rustle.ogg"
    am nulla "I just went off a hunch based on {b}this{/b}."
    sh surprise "Hmm?{w=0.3} That's..."
    play sound "audio/sfx/gui_item_get.ogg"
    show it_taisho_note with dissolve:
        xalign 0.5 yalign 0.4 
    pause 0.5
    sh surprise "A note?"
    am nulla "With a eight digits code.{w=0.3} When we left the room we woke up in, the door locked behind us and this didn't work on that one...{w=0.5} So I figured, might as well."
    sh neutral "A note with the code needed to open the door to this room.{w=0.3} And you found it laying around?"
    ga nulla "<No.{w=0.3} I found it in my pocket when I grabbed my {b}phone{/b}.>"
    pause 0.5
    play sound "audio/em/em_shock.ogg"
    show screen emote("surprise",0.17,0.5)
    sh shock "Wait, your...{w=0.5} Your phone?!"
    hide it_taisho_note with dissolve
    pause 1.0
    $ renpy.block_rollback()
    if gaspmina_01_code == False:
        $ gaspmina_01_code = True
        $ gaspmina_conv_01 += 1
    call screen gaspmina_conv_01

label gaspmina_01_phone:
    $ renpy.block_rollback()
    pause 0.5
    sh shock "Did you just say that you found that note with your phone?!"
    show Gaspard neutral
    show Amina surprise sweatdrop
    ga nulla "<That's what I said, yeah?{w=0.3} Or maybe you don't know the French word for that?>"
    sh angry "You still have your phone.{w=0.3} {i}Your own{/i} phone?!"
    am nulla "We...{w=0.5} We both do.{w=0.3} We used the flashlight function to look around the room...{w=0.3} You mean you don't?"
    sh surprise "No...{w=0.5} I do not.{w=0.3} It's currently missing.{w=0.3} Have you tried using them already?"
    show Gaspard frown
    ga nulla "<I have.{w=0.3} Unfortunately, there's no networks available.>"
    sh surprise "Not even for Emergency Calls?{w=0.5} That's..."
    pause 1.5
    sh frown ".{w=0.3}.{w=0.3}.{w=0.5}this isn't good.{w=0.3} Not good at all."
    show Amina neutral -sweatdrop
    am nulla "It wasn't going swimmingly before...{w=0.5} But, what are you referring to?"
    sh frown "The fact that they let you keep your phone while they took away mine...{w=0.5} The implications aren't good at all."
    sh neutral "My phone is special, so to speak.{w=0.3} It's the one I use for work and, on top of having a number of useful contacts, {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}it can connect to a dedicated satellite network{/b}."
    show Gaspard surprise
    show Amina surprise
    ga nulla "<A satellite network?>"
    sh neutral "Yes.{w=0.3} There's very few places on Earth where I cannot use it, leave alone an estate in the middle of France."
    sh frown "So, the fact that they removed {i}my{/i} phone specifically while they left yours with you...{w=0.5} Implies two things.{w=0.3} First, they {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}must know what I do for a living{/b}.{w=0.3} And second..."
    show Amina frown
    am nulla "Leaving us our phones is of no consequence to whoever's doing this."
    pause 1.0
    show Gaspard frown with dissolve
    sh smile "Exactly."
    ga nulla "<Alright, hold your horses here.{w=0.3} This is all well and good but, it may just be that there's no connection in this particular area of the building.>"
    show Gaspard neutral
    ga nulla "<Meeting rooms with one-way locked doors, sound-proofing...{w=0.5} I wouldn't be surprised if the lack of connection wasn't planned, too.>"
    show Amina surprise
    am nulla "Huh...{w=0.5} That's a good point."
    sh neutral "<Very possible, indeed.>"
    show Gaspard surprise
    ga nulla "<What...?{w=0.5} No, I mean, you...>"
    show Gaspard frown
    ga nulla "<They way you were talking made it sound like...{w=0.5} We've just been kidnapped for ransom, no?{w=0.3} And you probably lost your phone while they were moving you.>"
    pause 1.0
    sh frown "I don't think so."
    show Gaspard surprise
    pause 1.0
    show Gaspard frown
    show Amina sad
    pause 1.0
    $ renpy.block_rollback()
    if gaspmina_01_phone == False:
        $ gaspmina_01_phone = True
        $ gaspmina_conv_01 += 1
    call screen gaspmina_conv_01