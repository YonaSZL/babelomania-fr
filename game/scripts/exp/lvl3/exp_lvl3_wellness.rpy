default lvl3_wellness_explore_01 = 0
default exp_lvl3_wellness_01_shelves = False
default exp_lvl3_wellness_01_fridge = False
default exp_lvl3_wellness_01_bed = False

screen lvl3_wellness_explore_01():

    tag exploration

    button:
        pos(993,454)
        xysize(128,297)
        background None
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_confirm.ogg"
        action Jump("exp_lvl3_wellness_01_bed")
        tooltip _("Cot")

    if exp_lvl3_wellness_01_bed:
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_lvl3_wellness_01_fridge")
            tooltip _("Fridge")
    
    if exp_lvl3_wellness_01_fridge:
        button:
            pos(993,454)
            xysize(128,297)
            background None
            hover_sound "audio/sfx/gui_hover.ogg"
            activate_sound "audio/sfx/gui_confirm.ogg"
            action Jump("exp_lvl3_wellness_01_shelves")
            tooltip _("Shelves")

label exp_lvl3_wellness_01_shelves:
    $ renpy.block_rollback()
    pause 0.5
    de_i neutral "(Fake plants, a bunch of self-help books, a little narrative...{w=0.5} And they're all absolutely immaculate.)"
    de_i frown "(Guess whoever staffs this place isn't in the habit of reading...{w=0.5} Or maybe they don't like the selection.{w=0.3} Can't blame them, I sure at hell don't, either.)"
    de_i surprise "(Although...{w=0.5} The {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}languages{/b} make me think...{w=0.5} What is this?)"
    pause 1.0
    show Delphine frown with dissolve:
        xalign 0.5
    at de_big
    de_i nulla "(There's books in French and English, but also...{w=0.5} Japanese?{w=0.3} And these few with titles in cyrillic...)"
    play sound3 "audio/se/object_grab.ogg"
    pause 1.0
    show Delphine surprise with dissolve
    pause 1.5
    show Delphine frown with Reveal
    pause 1.5
    play sound4 "audio/sfx/gui_spook.ogg"
    de nulla "<{b}Russian{/b}...>"
    show Delphine angry
    de nulla "<I knew it...{w=0.5} Mom was right, she always was.>"
    show Delphine surprise
    de nulla "<But why target me at my wedding?{w=0.3} Is it because the château is isolated?{w=0.3} How long have they been planning this?{w=0.3} And...>"
    pause 1.0
    show Delphine angry with Reveal
    de_i nulla "(If they touched {i}one hair{/i} on dad or Francesco...)"
    pause 1.0
    scene lvl3_wellness_dim with dissolve
    if exp_lvl3_wellness_01_shelves == False:
        $ exp_lvl3_wellness_01_shelves = True
        $ lvl3_wellness_explore_01 += 1
    pause 1.0
    if lvl3_wellness_explore_01 == 3:
        jump 
    call screen lvl3_wellness_explore_01

label exp_lvl3_wellness_01_fridge:
    $ renpy.block_rollback()
    pause 0.5
    de_i surprise sweat "(Nooo, nononononono...{w=0.5} Okay, let's...{w=0.5} Check myself real quick, here.)"
    play sound "audio/se/cloth_rustle.ogg"
    pause 0.2
    show Delphine surprise sweat with dissolve:
        xalign 0.5
    at de_med
    pause 0.5
    de_i nulla "(Okay, the...{w=0.5} My dress is intact and so is everything else.{w=0.3} I don't feel pain or bruises anywhere...{w=0.5} Slowly...)"
    pause 1.5
    show Delphine neutral with dissolve
    pause 0.5
    de_i nulla "(Alright, it...{w=0.5} It seems that nothing was done to me while I was out cold.{w=0.3} I just feel very thirsty.)"
    show Delphine surprise
    de_i nulla "(This fridge seems on...{w=0.5} I hope there's some bottled water or something, inside.)"
    play sound4 "audio/sfx/fridge_open.ogg"
    pause 0.5
    show Delphine smile with dissolve
    de nulla "Ugh, Perrier...{w=0.5} Better than nothing, I guess."
    hide Delphine with dissolve
    play sound4 "audio/sfx/bottle_fizz.ogg"
    pause 0.5
    de_i laugh "(Huuuuuff, that hit the spot...{w=0.5} I'm feeling better already.)"
    de_i surprise "(Also, if they have Perrier in stock, at the very least {nw}"
    play sound4 "audio/sfx/gui_hint.ogg"
    extend "{b}I'm still in France{/b}...{w=0.5} But we're a decently sized country so that's not exactly helpful.)"
    de_i frown "(Although, now that I look more closely at this Fridge...{w=0.5} It's quite hi-tech, isn't it?)"
    de_i neutral "(Can't think of many big corporations who'd spend this much on furniture...{w=0.5} But they also wouldn't be in the business of kidnapping random brides.)"
    de_i frown "(.{w=0.3}.{w=0.3}.{w=0.5}except I'm not a random bride, am I?)"
    if exp_lvl3_wellness_01_fridge == False:
        $ exp_lvl3_wellness_01_fridge = True
        $ lvl3_wellness_explore_01 += 1
    pause 1.0
    call screen lvl3_wellness_explore_01

label exp_lvl3_wellness_01_bed:
    $ renpy.block_rollback()
    pause 0.5
    de_i neutral "(They were nice enough to lay me to rest on a bed, at least...{w=0.5} Except.)"
    de_i frown "(It's good enough to lay down on, certainly, but not my first choice if I had to take a nap...{w=0.5} I feel a bit sore under my right shoulderblade.)"
    de_i surprise "(And then there's also the music in the background...{w=0.5} I can't hear anything but, nothing coming in from the outside, and the rest of the furniture...?)"
    pause 1.5
    de_i frown "(Ugh, I think I got it.{w=0.3} This is a {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend "{b}corporate wellness room{/b}, isn't it?)"
    de_i neutral "(I remember seeing a couple at the HQ of dad's company.{w=0.5} Made so that people could come and isolate themselves from the outside, relax a little bit...{w=0.5} but not overstay their welcome.)"
    de_i frown "(Which means I'm no longer at the château but in some random office building...?{w=0.3} What kind of stupid-)"
    show screen emote("surprise",0.17,0.5)
    play sound "audio/em/em_surprise.ogg"
    de surprise sweat "<Wait a minute...!{w=0.3} There's no such buildings for miles, in any directions from the château!>"
    de shock "<How long was I out...?!>"
    if exp_lvl3_wellness_01_bed == False:
        $ exp_lvl3_wellness_01_bed = True
        $ lvl3_wellness_explore_01 += 1
    pause 1.0
    call screen lvl3_wellness_explore_01