default lvl3_wellness_explore_01 = 0
default exp_lvl3_wellness_01_shelves = False
default exp_lvl3_wellness_01_fridge = False
default exp_lvl3_wellness_01_bed = False

screen lvl3_wellness_explore_01():

    tag exploration

    button:
        pos(546,664)
        xysize(388,416)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_lvl3_wellness_01_bed")
        tooltip _("Cot")

    if exp_lvl3_wellness_01_bed:
        button:
            pos(960,465)
            xysize(274,461)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_lvl3_wellness_01_fridge")
            tooltip _("Fridge")
    
    if exp_lvl3_wellness_01_fridge:
        button:
            pos(1493,294)
            xysize(427,613)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_lvl3_wellness_01_shelves")
            tooltip _("Shelves")

label exp_lvl3_wellness_01_shelves:
    $ renpy.block_rollback()
    pause 0.5
    de_i neutral "(Fake plants, a bunch of self-help books, a small offer of narrative...{w=0.5} And they're all absolutely immaculate.)"
    de_i smile "(Guess whoever staffs this place isn't in the habit of reading, or maybe they don't like the selection...{w=0.5} Well, I can't exactly disagree.{w=0.3} Atlas Shrugged?{w=0.3} Really?)"
    de_i surprise "(Also...{w=0.5} The {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}languages{/b} give me pause, too.)"
    pause 1.0
    show Delphine frown at de_big:
        xalign 0.5
    with dissolve
    de_i nulla "(There's books in French and English, but also...{w=0.5} Japanese?{w=0.3} And these few with titles in cyrillic...)"
    play sound3 "audio/sfx/item_use.ogg"
    pause 1.0
    show Delphine shock sweat with dissolve
    pause 1.5
    play sound4 "audio/sfx/gui_spook.ogg"
    de nulla "<{b}Russian{/b}...>"
    pause 1.0
    show Delphine surprise
    de nulla "<This...{w=0.5} This can't be what I think it is, is it?{w=0.5} It can't be that mom...>"
    pause 1.5
    show Delphine frown with dissolve
    de nulla "<No.{w=0.3} No, hold your horses, Delphine.{w=0.3} Let's not go down that road, you've seen where it led {i}her{/i}.>"
    show Delphine neutral
    de nulla "<Russians were employed and lived in the rest of the world {i}before{/i} the war.{w=0.3} Even more so now, after the {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}collapse of the Federation{/b}.{w=0.3} This means nothing.>"
    show Delphine surprise -sweat
    de nulla "<Granted, there's foul at play here, but...{w=0.3} It doesn't mean they're after you specifically.{w=0.3} There was a whole party at the château, wasn't there?{w=0.3} And...>"
    pause 1.5
    show Delphine angry with Reveal
    de_i nulla "(If they touched {i}one hair{/i} on dad or Francesco...)"
    pause 1.0
    scene lvl3_wellness_dim with dissolve
    if exp_lvl3_wellness_01_shelves == False:
        $ exp_lvl3_wellness_01_shelves = True
        $ lvl3_wellness_explore_01 += 1
    pause 1.0
    if lvl3_wellness_explore_01 == 3:
        jump story_02_wellness_done
    call screen lvl3_wellness_explore_01

label exp_lvl3_wellness_01_fridge:
    $ renpy.block_rollback()
    pause 0.5
    de_i surprise sweat "(Nooo, nononononono...{w=0.5} Okay, let's...{w=0.5} Check real quick, here.)"
    play sound "audio/se/clothes_rustle.ogg"
    pause 1.0
    show Delphine surprise sweat at de_med:
        xalign 0.5
    with dissolve
    pause 0.5
    de_i nulla "(Okay, the...{w=0.5} Dress is intact, and so is everything else.{w=0.3} No pain or bruises anywhere, only discomfort in the shoulder because I slept on that eyesore...{w=0.5} Slowly, now.)"
    pause 1.5
    show Delphine neutral with dissolve
    pause 1.0
    de_i nulla "(Alright, it...{w=0.5} It seems nothing was done to me while I was out cold.{w=0.3} Just, shit, I'm thirsty.)"
    show Delphine surprise
    de_i nulla "(This fridge seems on...{w=0.5} Hope there's some bottled water or something, inside.)"
    play sound4 "audio/se/door_fridge_open.ogg"
    pause 1.5
    show Delphine disgust with dissolve
    de nulla "<Ugh, {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}Perrier{/b}.{w=0.5} Someone will pay for this carbonated affront.>"
    $ stat3_show = True
    hide Delphine with dissolve
    play sound4 "audio/se/food_soda.ogg"
    pause 1.0
    if exp_lvl3_wellness_01_fridge == False:
        $ stat3 += 25
    pause 0.5
    de_i smile "(Huuuuuff, still hit the spot...{w=0.5} And the ceremony's done with, anyway, I can afford not fitting in the dress anymore.)"
    de_i surprise "(Also, if they have Perrier in stock, at the very least {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}I'm still in France{/b}...{w=0.5} But being the decently sized country we are, that's not exactly helpful.)"
    de_i frown "(Although, now that I look more closely at this fridge...{w=0.5} It's quite hi-tech, isn't it?)"
    de_i neutral "(Can't think of many big corporations who'd spend this much on furniture.{w=0.5} But they also wouldn't be in the business of kidnapping random brides.)"
    pause 1.5
    de_i frown "(.{w=0.3}.{w=0.3}.{w=0.5}except I'm no random bride, am I?)"
    if exp_lvl3_wellness_01_fridge == False:
        $ exp_lvl3_wellness_01_fridge = True
        $ lvl3_wellness_explore_01 += 1
    pause 1.0
    call screen lvl3_wellness_explore_01

label exp_lvl3_wellness_01_bed:
    $ renpy.block_rollback()
    pause 0.5
    de_i neutral "(They were nice enough to not just drop me on the floor, but...{w=0.5} What even is this thing?)"
    de_i frown "(I have no idea why anyone would choose to lay down on it, let alone nap...{w=0.5} Ugh, it's the reason why my shoulderblade's sore, isn't it?)"
    de_i surprise "(Then there's this music in the background...{w=0.5} And I don't hear nothing coming in from outside.)"
    pause 1.5
    de_i frown "(Ugh, I think I got it.{w=0.3} This is a {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}corporate wellness room{/b}, isn't it?)"
    de_i neutral "(I remember seeing a couple at dad's HQ.{w=0.5} For the office drones to isolate themselves from the outside, and go one more day without shooting up the place...{w=0.5} but it still tells you not to overstay your welcome.)"
    de_i frown "(So I'm no longer at the château but in some random office building...?{w=0.3} What kind of moronic-)"
    pause 1.5
    show screen emote("surprise",0.17,0.5)
    play sound "audio/em/em_surprise.ogg"
    de surprise sweat "<Wait a minute...!{w=0.3} There's no such buildings for miles, in any direction from the château!>"
    de shock "<How {i}long{/i} was I out...?!>"
    if exp_lvl3_wellness_01_bed == False:
        $ exp_lvl3_wellness_01_bed = True
        $ lvl3_wellness_explore_01 += 1
    pause 1.0
    call screen lvl3_wellness_explore_01