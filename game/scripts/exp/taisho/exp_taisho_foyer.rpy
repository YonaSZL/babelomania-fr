#Aims for this puzzle: you need to input 'Shinzo Abe' using the wooden exposition panel. But written 'Abe Shinzo', surname first.
#Haiku Hint
##darkness returning
##from grandfather inherited
##by a son cut down
default taisho_foyer_explore = 0
default taisho_foyer_explore_timer = False
default taisho_foyer_gaspard_gone = False

default exp_taisho_foyer_amina = False
default exp_taisho_foyer_tabitha = False
default exp_taisho_foyer_door = False
default exp_taisho_foyer_stairs = False
default exp_taisho_foyer_exposition = False

screen taisho_foyer_explore():

    tag exploration

    button:
        pos(612,549)
        xysize(98,240)
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_foyer_amina")
        tooltip _("Amina{#explore_foyer}")
    button:
        pos(1314,537)
        xysize(181,464)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_foyer_tabitha")
        tooltip _("The Android{#explore_foyer}")
    button:
        pos(144,505)
        xysize(114,384)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_foyer_door")
        if flashlight_use:
            tooltip _("Door to Outside{#explore_foyer}")
        else:
            tooltip _("?????")
    button:
        pos(2654,341)
        xysize(226,551)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_foyer_stairs")
        if flashlight_use:
            tooltip _("Door to Stairways{#explore_foyer}")
        else:
            tooltip _("?????")
    button:
        pos(1868,697)
        xysize(123,65)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_taisho_foyer_exposition")
        if flashlight_use:
            tooltip _("Exposition")
        else:
            tooltip _("?????")

label exp_taisho_foyer_door:
    $ renpy.block_rollback()
    if flashlight_use == False:
        sh_i neutral "(It's too dark.{w=0.3} I need to use the flashlight to look around.)"
    else:
        $ flashlight_consume = False
        pause 0.5
        sh_i neutral "(The door to the outside.{w=0.3} Only a scant few centimeters separating us from...)"
        sh_i frown "(From what, really?)"
        pause 1.0
        show taisho_foyer_door with dissolve
        pause 0.5
        sh_i neutral "(Logically, I know that once we leave the Taisho building, we'll be in the {nw}"
        play sound4 "audio/sfx/gui_hint.ogg"
        extend "{b}Great Courtyard{/b} of the château.{w=0.3} But I wouldn't call us home-free.)"
        sh_i frown "(I doubt whoever's doing this would be done with us so soon...{w=0.5} Considering the average class and job of the people at the reception, they have maybe twentyfour hours before anyone comes looking.)"
        sh_i neutral "(Which means that, whatever their intentions, they only have so much time to squeeze us.{w=0.3} Which makes me worry.)"
        sh_i frown sweat "(A building like the Taisho is a more controlled environment for them to plan around...{w=0.5} But at the same time, it limits the things they can throw at us.)"
        sh_i neutral sweat "(Once out in the open, we'll both lose a modicum of control over our surroundings.{w=0.3} And that worries me in a completely new way, considering...)"
        pause 1.5
        sh_i frown "(We'll cross that bridge when we come to it.{w=0.3} Staying put is not an option in our current situation.)"
        pause 0.5
        if exp_taisho_foyer_door == False:
            play sound4 "audio/sfx/gui_slots_confirm.ogg"
            show screen notify(_("Codex Entry Updated: Chateau de Bois II."))
            $ c_chateau_dubois_config = True
            $ exp_taisho_foyer_door = True
            $ taisho_foyer_explore += 1
            $ stat2 -= 1
            $ move_time(0,1)
        $ flashlight_consume = True
    hide taisho_foyer_door with dissolve
    pause 1.0
    call screen taisho_foyer_explore
    with dissolve

label exp_taisho_foyer_amina:
    scene taisho_foyer
    show Amina
    with dissolve
    $ renpy.block_rollback()
    $ flashlight_consume = False
    pause 0.5
    sh surprise "Found anything of interest?"
    am neutral "Maybe...{w=0.5} These doors lead to the {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}bedrooms{/b} area."
    pause 0.5
    show Shigeo surprise:
        zoom 0.18 xpos 480 ypos 500
    with dissolve
    sh surprise "The bedrooms...{w=0.5} Right, we were going to stay overnight in this building, weren't we?"
    am neutral "Which means this is where, technically, everyone's luggage should have been brought."
    show Amina surprise
    am surprise "Let's say we find your luggage.{w=0.3} Anything useful we could grab from there?"
    show Shigeo neutral
    sh neutral "Other than a {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}charger for the flashlight{/b}, not really.{w=0.3} I'm on leave so, other than my phone, I didn't bring anything else work related."
    show Shigeo smile sweatdrop
    sh smile sweatdrop "And even if I did bring my ordnance weapon, I'm not exactly the ace of the shooting range...{w=0.5} I'm an analyst, remember?"
    show Amina smile
    am smile "I'll keep that in mind...{w=0.5} I guess not everyone can be a Derek Mountain, agency or not."
    pause 0.5
    play sound4 "audio/em/em_question.ogg"
    show screen emote("question",0.5,0.35)
    show Shigeo surprise
    sh surprise "Derek...{w=0.5} Mountain?{w=0.3} Who's that?"
    show Amina surprise blush
    am surprise blush "Oh, uhm, he's...{w=0.5} A character from a tv series from the early 2000s.{w=0.3} Criminal Brains, ever heard of it?"
    sh surprise "Oh, yeah, it does sound familiar...{w=0.5} Sorry, I've never seen it.{w=0.3} I don't like watching police procedurals, tell you the truth."
    show Shigeo smile
    sh smile "I already get enough of that kind of fare at work.{w=0.3} I could tell you stories, if only I had the clearance."
    show Amina smile -blush
    am smile -blush "Heh, fair enough...{w=0.5} What do you like, then?"
    sh smile "A lot of anime...{w=0.5} Being Japanese and Italian, I had no chance in hell to not end up like that."
    show Amina laugh
    am laugh "Oh, I like animation too.{w=0.3} We could recommend each other some stuff later, then.{w=0.3} But anyway."
    show Amina neutral
    am neutral "I believe it's worth checking out, for all we know the key may be in there...{w=0.5} Still, let's keep it for after we finish with the foyer."
    show Shigeo neutral
    sh neutral "Absolutely agree.{w=0.3} There'll be no splitting up, here."
    show Shigeo frown
    sh frown "We're deep enough inside a horror flick as is.{w=0.3} Let's avoid at least {i}that{/i} trope."
    if exp_taisho_foyer_amina == False:
        $ exp_taisho_foyer_amina = True
        $ taisho_foyer_explore += 1
        $ stat2 -= 2
        $ move_time(0,2)
    $ flashlight_consume = True
    pause 1.0
    hide Shigeo
    scene taisho_foyer
    call screen taisho_foyer_explore
    with dissolve

label exp_taisho_foyer_tabitha:
    $ renpy.block_rollback()
    $ flashlight_consume = False
    pause 0.5
    sh_i surprise "(Is it just...{w=0.5} Standing around?{w=0.3} No, wait.)"
    sh_i frown sweat "(Its eyes are just...{w=0.5} Following me around the room, slowly.{w=0.3} So creepy.{w=0.3} Anyway, why isn't she looking?)"
    sh frown -sweat "What are you doing, Android?"
    ta smile "Surveying our surroundings, [shn].{w=0.3} I'm happy to inform that there's no immediate threat in range of my sensors."
    pause 1.0
    show Shigeo neutral with dissolve:
        zoom 0.2 xpos 669 ypos 480
    sh neutral "Yeah, about those sensors...{w=0.5} Have you also been surveying the surroundings for clues?"
    show Tabitha surprise
    ta surprise "Query:{w=0.15} clues referring to what incognita, [shn]?"
    pause 0.5
    show Shigeo surprise
    sh surprise "Uhm, the...{w=0.5} They key.{w=0.3} We're looking for the key to the front door, remember?"
    show Tabitha bow
    ta neutral "Affirmative.{w=0.3} Apologies but I haven't been able to locate any object of the sort."
    sh surprise "I get, I didn't expect you to...{w=0.5} But what about a hiding place for it?"
    show Tabitha surprise
    ta surprise "A hiding place?{w=0.3} So the key to the exit door has been absconded by someone?"
    sh surprise "Yes!{w=0.3} Obviously!{w=0.3} What do you think the situation we find ourselves in is?!"
    show Tabitha neutral
    ta neutral "Observation:{w=0.15} [shn] and miss Amina currently find themselves detained by unknown subjects.{w=0.3} We are thus looking for a way to leave the current premises."
    show Tabitha bow
    ta bow "We also currently find ourselves facing the incognita of a possible mysterious infection, and the appearance of hostiles.{w=0.3} End of observation."
    show Shigeo frown
    sh frown "Ugh, right, have to be literal...{w=0.5} Android, listen.{w=0.3} Yes, the key to the door has been hidden.{w=0.3} We need to look for its hiding place and then find a way to open it."
    show Tabitha neutral
    ta neutral "Acknowledged, [shn].{w=0.3} What characteristics would this hiding place have?"
    pause 1.0
    show Shigeo surprise
    sh surprise "I...{w=0.5} I don't know.{w=0.3} That's why we're...{w=0.5} We're looking around?"
    show Tabitha surprise
    ta surprise "[shn], I must say that this course of conduct seems quite inefficient.{w=0.3} If we have no information regarding to the hiding place, shouldn't we focus on collecting that first?"
    sh surprise "But that's what we're doing!{w=0.3} It's just that we also have no idea where that information may lay, and..."
    pause 1.0
    show Shigeo frown with dissolve
    sh frown ".{w=0.3}.{w=0.3}.{w=0.5}you can't do anything without a frame of reference, can't you?"
    show Tabitha neutral
    ta neutral "Approximate but truthful, [shn].{w=0.3} Professor Habiki prides itself in the horsepower of my chassis and the processing power of my positronic brain."
    show Tabitha surprise
    ta surprise "Alas, I am still a machine.{w=0.3} Asking me to perform a task without any precise data or input would send me into a potentially endless endeavour."
    show Tabitha bow
    ta bow "In a situation where any input is considered valid and of the same importance, {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}I would not be able to prioritize one element over the other{/b}.{w=0.3} I would simply have to go through each of them in the most efficient order."
    sh frown "You have no emotions, no istinct, no biases...{w=0.5} And thus no intuition."
    show Tabitha smile
    ta smile "Affirmative, [shn].{w=0.3} For the sake of efficiency, in observation of your energy-saving guidelines, I shall occupy myself with surveying our surroundings for possible threats unless prompted otherwise."
    show Tabitha bow
    show Shigeo neutral
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    ta bow "{b}If you ever have a precisely defined task for me to aid you with, you need only ask{/b}."
    sh neutral ".{w=0.3}.{w=0.3}.{w=0.5}I'll keep that in mind."
    if exp_taisho_foyer_tabitha == False:
        $ exp_taisho_foyer_tabitha = True
        $ taisho_foyer_explore += 1
        $ tabitha_cheats = True
    $ flashlight_consume = True
    pause 1.0
    call screen taisho_foyer_explore
    with dissolve

label exp_taisho_foyer_exposition:
    $ renpy.block_rollback()
    $ flashlight_consume = False
    pause 0.5
    
    if exp_taisho_foyer_exposition == False:
        $ exp_taisho_foyer_exposition = True
        $ taisho_foyer_explore += 1
    $ flashlight_consume = True
    pause 1.0
    call screen taisho_foyer_explore
    with dissolve

label exp_taisho_foyer_stairs:
    $ renpy.block_rollback()
    $ flashlight_consume = False
    pause 0.5
    
    if exp_taisho_foyer_stairs == False:
        $ exp_taisho_foyer_stairs = True
        $ taisho_foyer_explore += 1
    $ flashlight_consume = True
    pause 1.0
    call screen taisho_foyer_explore
    with dissolve