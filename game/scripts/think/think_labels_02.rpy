label think_02_organs_think:
    $ renpy.block_rollback()
    call screen think(_("What could have caused {b}his organs to wither{/b}?"), _("Sickness."), "think_02_sickness", _("Dehydration."), "think_02_dehydration", "None", "None", "None", "None")

label think_02_sickness:
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    $ renpy.block_rollback()
    sh naked surprise "If his organs have been damaged like that...{w=0.5} Does that mean that Gaspard was sick?{w=0.3} Before coming here?"
    am naked surprise "Not that I know of...{w=0.5} He didn't display any signs, at least to me."
    am naked neutral "Also, Gaspard was slightly hypochondriac.{w=0.3} He'd lament the end of his existence for a common cold."
    sh naked surprise "I see...{w=0.5} And if his {i}organs{/i} had started withering, he would have sported a series of hard to conceal symptoms."
    sh naked frown sweat "Which means that whatever happened, happened to him quickly...{w=0.5} Tonight."
    pause 1.0
    $ renpy.block_rollback()
    jump think_02_organs_think

label think_02_dehydration:
    play sound4 "audio/sfx/gui_hint.ogg"
    $ renpy.block_rollback()
    sh naked surprise -sweat "Withering organs...{w=0.5} Doesn't that sounds like a possible consequence of dehydration?"
    am naked shock "Dehy-{w=0.15}oh, no!"
    sh naked frown "Gaspard was...{w=0.5} Quite thirsty, right before the transformation, wasn't he?{w=0.3} What if it wasn't due to his nerves?"
    am naked sad "It was...{w=0.5} It was a symptom, wasn't it?{w=0.3} Whatever was happening to him was...{w=0.5} Using the water in his body!"
    ta smile "That is my opinion as well, [shn].{w=0.3} Upon inspection, even when accounting for the spillage that occurred during the neutralization process..."
    ta neutral "I've observed a marked absence of bodily fluids, plus the aforementioned withering of the hostile's internal organs.{w=0.3} Which leads me to believe that, indeed, dehydration is a symptom of the drastic change."
    ta surprise "Simulteanously, however, I've observed that one organ system and one type of tissue were instead augmented in size and subsequent spread."
    am naked shock "A boost in size...?{w=0.5} What the hell did this thing do to him?!"
    sh naked neutral ".{w=0.3}.{w=0.3}.{w=0.5}would they be...?"
    pause 1.0
    $ renpy.block_rollback()
    jump think_02_growth_think

label think_02_growth_think:
    call screen think(_("One organ and one type of tissue were {b}reinforced{/b}...?"), _("Skin and lungs?"), "think_02_skin", _("Muscles and skin?"), "think_02_muscles", _("Muscles and nervous system?"), "think_02_nervous", "None", "None")

label think_02_skin:
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    $ renpy.block_rollback()
    sh_i naked pain "(The Android mentioned how the skin had been changed into a metal alloy...{w=0.5} And I can't get that broken, metallic chittering screech out of my head.{w=0.3} So I guess it was his skin and lungs?)"
    sh_i naked frown "(No, wait...{w=0.5} First, skin is an organ, not tissue.{w=0.3} Also, more than reinforced, it looked like his skin had become something else entirely.{w=0.3} And it's not lungs one needs to take into account when it comes to voice, but the vocal chords.)"
    sh_i naked neutral "(Which are made of muscle tissue.{w=0.3} So the organs would actually be...)"
    pause 1.0
    $ renpy.block_rollback()
    jump think_02_growth_think

label think_02_muscles:
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    $ renpy.block_rollback()
    sh_i naked frown "(The way he threw me accross the room...{w=0.5} If his muscles had been withering, that wouldn't have been possible.{w=0.3} Yes, that's the tissue for sure.)"
    sh_i naked neutral "(And for the other one...{w=0.5} His skin?{w=0.3} Although, so far the Android has been quite literal in her description of things.)"
    sh_i naked frown "(No.{w=0.3} What happened to Gaspard's skin was more a transformation than a reinforcement.{w=0.3} It's something else.)"
    sh_i naked surprise "(Something without which no amount of muscle would do any good...)"
    pause 1.0
    $ renpy.block_rollback()
    jump think_02_growth_think

label think_02_nervous:
    $ renpy.block_rollback()
    sh_i naked frown "(His muscle mass was anything but withered.{w=0.3} I have frequent flier miles to prove it, too.)"
    sh_i naked neutral "(So it's pretty safe to assume that was the reinforced tissue type.{w=0.3} And while I can't exactly prove it...)"
    sh_i naked surprise "(Without a functioning {nw}"
    play sound4 "audio/sfx/gui_solved.ogg"
    extend "{b}nervous system{/b} the body wouldn't be able to move anymore!{w=0.3} Which means...?!)"
    sh naked surprise "The nervous system...{w=0.5} And muscles, correct?"
    ta smile "Affirmative, [shn].{w=0.3} That is indeed what I've observed."
    pause 1.0
    $ renpy.block_rollback()
    jump story_03_brainssss