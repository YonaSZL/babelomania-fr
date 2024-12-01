#Conversation Screens with Tabitha

#Convo 01
default tabitha_01_scenario = False #Do you know what's going on?
default tabitha_01_gaspard = False #Why did you kill Gaspard?!
default tabitha_01_directive = False #You have the directive to protect me?!
default tabitha_01_rules = False #You don't have the three rules?!
default tabitha_01_human = False #What do you mean he wasn't human?!
default tabitha_conv_01 = 0

screen tabitha_conv_01:
    add "gui/talkie/bottom.png" yalign 1.0

    if tabitha_conv_01 == 5:
        textbutton _("Return") action Jump("story_03_uneasy_trio") align(1.0, 1.0) offset(-60,-10) text_size 60 hover_sound "audio/sfx/gui_hover.ogg" activate_sound "audio/sfx/gui_slots_confirm.ogg"

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
                    text _("Our Situation")
                    at btn_slide
                    if tabitha_01_scenario:
                        background "gui/talkie/button.png"
                    else:
                        background "gui/talkie/button_empty.png"
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("tabitha_01_scenario")
                button:
                    text _("Gaspard...")
                    at btn_slide
                    if tabitha_01_gaspard:
                        background "gui/talkie/button.png"
                    else:
                        background "gui/talkie/button_empty.png"
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action Jump("tabitha_01_gaspard")
                if tabitha_01_gaspard:
                    button:
                        text _("Tabitha's Programming")
                        at btn_slide
                        if tabitha_01_rules:
                            background "gui/talkie/button.png"
                        else:
                            background "gui/talkie/button_empty.png"
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                        action Jump("tabitha_01_rules")
                if tabitha_01_rules:
                    button:
                        text _("No Longer Human")
                        at btn_slide
                        if tabitha_01_human:
                            background "gui/talkie/button.png"
                        else:
                            background "gui/talkie/button_empty.png"
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                        action Jump("tabitha_01_human")
                if tabitha_01_human:
                    button:
                        text _("Tabitha's Directives")
                        at btn_slide
                        if tabitha_01_directive:
                            background "gui/talkie/button.png"
                        else:
                            background "gui/talkie/button_empty.png"
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                        action Jump("tabitha_01_directive")

        ####Indicator if viewport is scrollable
        button:
            xysize(65,65) xalign 1.0 xoffset -400
            add "gui/talkie/scroll_bg.png"
            add "gui/talkie/scroll_arrow.png" at arrow_down

label tabitha_01_scenario:
    $ renpy.block_rollback()
    pause 0.5
    sh c_half frown "You were at the reception...{w=0.5} Or at least in the same building as we were, the Baroque building.{w=0.3} Correct?"
    ta nulla "Affirmative.{w=0.3} Afterwards, the Professor desired to observe the ceremony from the upper floors for a time."
    sh surprise "He...{w=0.5} What?{w=0.3} Why would he want to do that?"
    show Tabitha bow
    ta nulla "That information is not in my possession.{w=0.3} The Professor rarely shares his inner world with others."
    sh frown "Well...{w=0.5} If you had to guess?"
    show Tabitha surprise
    ta nulla "I do not possess sufficient data to create a predictive model with an accuracy higher than 67\%, [shn].{w=0.3} Is that acceptable?"
    sh surprise "I...{w=0.5} Yeah."
    show Tabitha neutral
    ta nulla "Acknowledged.{w=0.5} Considering the data about Professor Habiki's behavioral patterns, and cross-checking it with his recent actions:{w=0.15} he is what is commonly referred to as a 'people watcher'."
    show Tabitha bow
    ta nulla "He is in the habit of trying to observe individuals of interest while hidden, as to not influence their actions with his presence.{w=0.3} I posit that it was yet another occurrence of this quirk of his."
    sh neutral "Hm.{w=0.3} Sounds like a pretty solid analysis to me...{w=0.5} Why is the accuracy in the mid-ranges, then?"
    show Tabitha neutral
    ta nulla "Unfortunately, I am unable to correctly gauge who, among the attendees, was the object of his curiosity.{w=0.3} He made sure, in the days leading up to the event, to familiarize himself with the list of invitees, but he never betrayed any interest one way or the other."
    show Tabitha surprise with dissolve
    ta nulla "With {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}one exception{/b}...{w=0.5} You, [shn]."
    sh surprise "Me...?"
    show Tabitha smile
    ta nulla "Affirmative.{w=0.3} He was, as the saying goes, tickled pink when interacting with you.{w=0.3} Your brief exchange left him quite amused."
    show Tabitha neutral
    ta nulla "It only amounts to correlation but there is a possibility that you may have joined the list of individuals to observe, despite his presence having been revealed to you."
    sh frown ".{w=0.3}.{w=0.3}.{w=0.5}which leaves us with nothing to go on, in the end.{w=0.5} Anyway."
    sh neutral "You followed him to the upper floor.{w=0.3} What transpired afterwards?"
    pause 1.5
    show Tabitha surprise with dissolve
    ta nulla ".{w=0.3}.{w=0.3}.{w=0.5}{nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}data not found{/b}."
    play sound "audio/em/em_surprise.ogg"
    show screen emote("surprise",0.15,0.5)
    sh surprise "Eh?{w=0.3} What do you mean 'data not found'?"
    show Tabitha frown
    ta nulla "This is quite anomalous...{w=0.5} I don't seem to possess any data regarding the period of time inbetween the beginning of Professor Habiki's observations and my reboot in the adjacent room."
    sh surprise "So you mean to tell me that you, too, don't have any memory of the last couple hours?!"
    sh_i frown "(No, actually...{w=0.5} Her memory loss goes even further back.{w=0.3} When they went to the upper floor, I went back to the reception room.{w=0.3} I spoke to Gaspard, then Amina and Francesco, then only afterwards did the video happen...)"
    sh_i neutral "(So whatever was done to this Android was not the same thing that happened to us...{w=0.5} But it's highly likely they're correlated.)"
    ta nulla "I apologize, [shn].{w=0.3} This is quite unbecoming."
    sh neutral "Yeah, well...{w=0.5} Nothing you could have done about it.{w=0.3} We sure couldn't."
    sh frown "And honestly...{w=0.5} I can think of things far more unbecoming than that, Android."
    show Tabitha neutral
    ta nulla "...?"
    pause 1.0
    if tabitha_01_scenario == False:
        $ tabitha_01_scenario = True
        $ tabitha_conv_01 += 1
    call screen tabitha_conv_01

label tabitha_01_gaspard:
    $ renpy.block_rollback()
    pause 0.5
    sh frown sweat "Why did you do that...?"
    show Tabitha bow
    ta nulla "Observation:{w=0.15} your query is unfortunately too vague for me to infer as to its meaning, [shn].{w=0.3} I would request you to be more precise."
    sh pain "Ugh!{w=0.3} Why...{w=0.5} Why did you...{w=0.5} Argh, I can't even say it out loud."
    pause 1.0
    show Tabitha neutral
    ta nulla ".{w=0.3}.{w=0.3}.{w=0.5}taking into consideration your state of mental distress, I hypothesize that your query concerns my neutralization of the hostile."
    sh pain "Yeah...{w=0.5} You neutralized him, alright."
    sh angry "You ripped him apart like he was made of tissue paper without even a moment's hesitation...{w=0.5} I had his guts rain on my chest!{w=0.3} I felt the impact of each and every little bit of gore...{w=0.5} Why?!{w=0.3} How?!"
    ta nulla "Queries acknowledged...{w=0.5} Why did I neutralize the hostile so:{w=0.15} after emergency analysis of the situation, I concluded that drastic and swift action was necessary."
    show Tabitha surprise
    ta nulla "The hostile's combat capabilities were a complete incognita.{w=0.3} Taking into account its closeness to [shn], and your brief period of incapacitation, I calculated that I had but milliseconds to act."
    sh surprise "What...?"
    show Tabitha neutral
    ta nulla "As I mentioned earlier, your physical integrity currently rests among my prime directives."
    show Tabitha frown
    ta nulla "Whatever transpired between the beginning of my state of dormancy and my subsequent reboot caused me to arrive almost too late...{w=0.5} I maintain that it was the only safe course of action."
    sh surprise sweat "You...{w=0.5} You mean..."
    sh pain sweat "That you tore Gaspard to shreds {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}to save me{/b}?"
    show Tabitha neutral
    ta nulla "Affirmative.{w=0.3} Thankfully, I made it in time and the hostile proved himself to be only slightly more durable than the average human."
    show Tabitha smile
    ta nulla "As for the how:{w=0.15} my chassis can exercise up to 1950 kilograms of pressure per centimeter squared.{w=0.3} Such a feat rests well within my parameters."
    play sound4 "audio/em/em_shock.ogg"
    show screen emote("surprise",0.15,0.5)
    sh shock sweat "1950...!!!{w=0.5} Why?!"
    show Tabitha neutral
    ta nulla "It was deemed to be the highest output possible while still accounting for stress of the materials.{w=0.3} The calculations-"
    play sound4 "audio/em/em_impact.ogg"
    sh angry "THAT'S NOT WHAT I MEANT!{w=0.3} Why do you have that much strength to begin with?!{w=0.3} And..."
    sh surprise "Now that I think about it..."
    pause 1.0
    if tabitha_01_gaspard == False:
        $ tabitha_01_gaspard = True
        $ tabitha_conv_01 += 1
    call screen tabitha_conv_01

label tabitha_01_rules:
    $ renpy.block_rollback()
    pause 0.5
    sh neutral -sweat "You...{w=0.5} You're Professor Habiki's creation, correct?{w=0.3} Him and him alone?"
    show Tabitha bow
    ta nulla "Affirmative, [shn].{w=0.3} I am his personal project and, quote on quote, 'the crowning achievement of his genius'."
    sh surprise "Meaning that he was the one who decided to...{w=0.5} Give you that kind of strength.{w=0.3} Which flies into the face of all international treaties about the creation of Androids and proliferation of war machines."
    show Tabitha neutral
    sh frown sweat "Japan may be lax about shapes, but they're one of the most firm upholders of the ban on war Androids...{w=0.5} Which means that he must have used his influence to register you with false information."
    ta nulla "I cannot deny nor confirm such an hypothesis, [shn]."
    sh neutral -sweat "And earlier, when you said that you didn't grab Amina before she hit the floor despite being closer to her than me...{w=0.5} I wasn't thinking clearly earlier, but that shouldn't be possible."
    sh angry "All Androids are supposed to be built according to international specifications...{w=0.5} Which include the base imperatives of not harming humans and not letting harm come to humans.{w=0.3} You...{w=0.5} You don't have that?"
    show Tabitha bow
    ta nulla "I cannot deny nor confirm such an hypothesis, [shn]."
    sh angry sweat ".{w=0.3}.{w=0.3}.{w=0.5}unbelievable.{w=0.3} Absolutely unbelievable...{w=0.5} You're a robot {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}that can use violence against human beings{/b}...{w=0.5} And can allow harm to come to them if need be."
    show Tabitha surprise
    ta nulla "Observation:{w=0.15} any Android with a failsafe against the latter while possessing no restrictions on the former would eventually fall into a perpetual feedback loop."
    sh frown "Oh, thank you {i}so much{/i} for that.{w=0.3} That paints the whole thing into a new light."
    show Tabitha smile
    ta nulla "You're quite welcome, [shn].{w=0.3} I must reiterate that I cannot deny nor confirm your hypothesis, though."
    pause 1.5
    sh pain -sweat"Ugh, getting cross at you is useless...{w=0.5} And so is sarcasm."
    show Tabitha surprise
    ta nulla "Oh, my apologies.{w=0.3} I'm not programmed for sarcasm."
    sh frown "Of course you're not...{w=0.5} Anyway, that explains it."
    show Tabitha neutral
    sh neutral "You don't have any ingrained qualms against harming human beings...{w=0.5} That's how you could do what you did to poor Gaspard."
    stop music fadeout 3.5
    pause 1.5
    show Tabitha surprise with dissolve
    pause 0.5
    ta nulla "Query:{w=0.15} [shn], when you use the name 'Gaspard' are you referring to the neutralized hostile?"
    sh pain "Who else...?"
    show Tabitha neutral
    ta nulla "Acknowledged.{w=0.3} In that case, [shn], I must correct you."
    show Tabitha bow
    ta nulla "I infer that, before the events that transpired in my absence, the hostile was classified as a human being.{w=0.3} But at the moment of neutralization..."
    show Tabitha neutral
    play sound4 "audio/sfx/gui_spook.ogg"
    ta nulla "{b}The Hostile could no longer be considered a human being{/b}."
    play music "audio/bgm/shadows_whisper.ogg"
    pause 1.5
    sh shock sweat ".{w=0.3}.{w=0.3}.{w=0.5}what?"
    pause 1.0
    if tabitha_01_rules == False:
        $ tabitha_01_rules = True
        $ tabitha_conv_01 += 1
    call screen tabitha_conv_01

label tabitha_01_human:
    $ renpy.block_rollback()
    pause 0.5
    sh shock -sweat "What...{w=0.5} What are you talking about?{w=0.3} What do you mean he was no longer human?!"
    sh pain "I...{w=0.5} I mean, there was definitely something wrong with him but...{w=0.5} What you're saying is...!{w=0.3} What proof do you have?!"
    play sound4 "audio/sfx/gui_hint.ogg"
    ta nulla "{b}Sound, [shn]{/b}."
    sh surprise "Sound...?"
    show Tabitha bow
    ta nulla "Yes.{w=0.3} I am equipped with a number of state of the art sensors.{w=0.3} My auditory sensor is among those."
    show Tabitha surprise
    ta nulla "Prior to and while engaging the hostile, he produced a number of sounds.{w=0.3} Upon repeated analysis, I can conclude with 100\% accuracy that {nw}"
    play sound4 "audio/sfx/gui_solved.ogg"
    extend "{b}no human body would be able to produce those sounds{/b}."
    play sound4 "audio/sfx/gui_shock.ogg"
    sh shock sweat "You...!{w=0.3} That can't...!!!"
    show Tabitha neutral
    ta nulla "I must clarify that my conclusions are based on the information currently included in my database.{w=0.3} If [shn] is in possession of further relevant data concerning human biology, I would be happy to readjust my model."
    sh shock ".{w=0.3}.{w=0.3}.{w=0.5}I..."
    pause 1.0
    show gaspard_turn_03:
        matrixcolor SepiaMatrix()
    with Reveal
    pause 1.5
    play sound "audio/se/glitch_attack.ogg"
    pause 0.5
    sh pain ".{w=0.3}.{w=0.3}.{w=0.5}shit...{w=0.5} You're right.{w=0.3} You're right!{w=0.3} He..."
    sh angry "He transformed...{w=0.5} He underwent a horrible, {i}terrible{/i} mutation...!{w=0.5} But how?!{w=0.3} Why?!"
    sh shock "And...{w=0.5} And is it going to happen to...?!"
    show Tabitha surprise
    ta surprise blood "Oh...{w=0.5} You believe such a drastic change may be a possibility for you as well, [shn]?"
    pause 1.0
    stop music fadeout 3.5
    hide gaspard_turn_03 with dissolve
    pause 0.5
    sh pain "I have no idea.{w=0.5} I don't know what happened to him or how, but one moment he was normal and the next..."
    show Tabitha frown
    ta nulla "Acknowledged...{w=0.5} Unacceptable by current parameters."
    show Tabitha neutral
    ta nulla "[shn].{w=0.3} I suggest we address this {i}immediately{/i}."
    pause 1.0
    if tabitha_01_human == False:
        $ tabitha_01_human = True
        $ tabitha_conv_01 += 1
    call screen tabitha_conv_01

label tabitha_01_directive:
    $ renpy.block_rollback()
    pause 0.5
    sh surprise -sweat "Why do you even...{w=0.5} Oh, right, your..."
    sh frown "You said that my safety is among your prime directives...{w=0.5} How?{w=0.3} Why?"
    show Tabitha surprise
    ta nulla ".{w=0.3}.{w=0.3}.{w=0.5}data not found."
    sh neutral "Naturally...{w=0.5} You have no idea.{w=0.3} Alright, let's try and go through this logically."
    show Tabitha neutral
    sh frown "Question one:{w=0.15} was my safety among your prime directives before your...{w=0.5} Brief window of inactivity?"
    ta nulla "Negative, [shn]."
    sh neutral "Questions two and three:{w=0.15} who currently has the authority to add prime directives to your programming?{w=0.3} And has that access list changed from what it was before your window of inactivity?"
    show Tabitha surprise
    ta nulla "Answer to first query:{w=0.3} the only person with that level of authority is {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}Professor Habiki{/b}.{w=0.3} Answer to second query:{w=0.15} the 'access list' has not been modified in the relevant time period."
    sh frown "I see...{w=0.5} Last question, is it possible that someone could have changed your prime directives without that level of access {i}and{/i} without leaving any trace?"
    show Tabitha neutral
    ta nulla "It is a possibility, [shn]."
    sh surprise "Wait, it is?{w=0.3} But-"
    sh frown "Oh, wait, right, too literal.{w=0.3} Okay, it's possible, but how {i}probable{/i} is it?"
    show Tabitha bow
    ta nulla "The probability of such an event approximates to around 2.9777777777777\%, [shn]."
    sh neutral "Does the same probability apply to the eventuality of someone other than Habiki altering your memory banks without leaving any trace?"
    show Tabitha neutral
    ta nulla "Affirmative, [shn]."
    pause 1.5
    play music "audio/bgm/measure_of_ningen.ogg"
    sh neutral "Understood...{w=0.5} Could you please state the exact wording of your prime directive, Android?"
    ta nulla "Certainly.{w=0.3} Prime directive number two is phrased as follows:{w=0.15} this Android is tasked with safeguarding the continued physical integrity of Arata Shigeo."
    show Tabitha bow
    ta nulla "This Android is also to obey their orders insofar they don't run contrary to the parameters of the directive itself, or other directives of equal and/or superior priority."
    sh_i frown "(Safeguarding my 'physical integrity'...{w=0.5} Very specific.)"
    sh neutral "You said number two...{w=0.5} Is that the priority order?"
    show Tabitha neutral
    ta nulla "Affirmative, [shn]."
    sh frown "What's prime directive number one, then?"
    show Tabitha bow
    play sound4 "audio/sfx/gui_hint.ogg"
    ta nulla "{b}This Android is to obey Professor Habiki{/b}."
    pause 1.5
    sh_i neutral "(Pretty high up on the scale...)"
    show Tabitha frown
    ta nulla "[shn], if I have answered your queries to satisfaction, I must stress the importance of addressing the matter of the mutation incognita immediately."
    sh neutral ".{w=0.3}.{w=0.3}.{w=0.5}yeah...{w=0.5} Yeah, I agree."
    sh frown sweat "And then, we're going to need to find a way out of here.{w=0.3} I'm gonna need you to-"
    am sad c_half "{cps=10}Hmmm..."
    show Tabitha surprise
    play sound4 "audio/em/em_surprise.ogg"
    show screen emote("surprise",0.15,0.5)
    sh smile -sweat "Amina!"
    pause 1.0
    show Tabitha neutral
    if tabitha_01_directive == False:
        $ tabitha_01_directive = True
        $ tabitha_conv_01 += 1
    call screen tabitha_conv_01