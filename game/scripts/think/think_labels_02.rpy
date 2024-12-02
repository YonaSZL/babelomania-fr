label think_02_organs_think:
    $ renpy.block_rollback()
    call screen think(_("What could have caused {b}his organs to wither{/b}?"), _("Sickness."), "think_02_sickness", _("Dehydration."), "think_02_dehydration", "None", "None", "None", "None")

label think_02_sickness:
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    $ renpy.block_rollback()
    sh -clothes surprise "If his organs have been damaged like that...{w=0.5} Does that mean that Gaspard was sick?{w=0.3} Before coming here?"
    am -clothes surprise "Not that I know of...{w=0.5} He didn't display any signs, at least to me."
    am -clothes neutral "Also, Gaspard was slightly hypochondriac.{w=0.3} He'd lament the end of his existence for a common cold."
    sh -clothes surprise "I see...{w=0.5} And if his {i}organs{/i} had started withering, he would have sported a series of hard to conceal symptoms."
    sh -clothes frown sweat "Which means that whatever happened, happened to him quickly...{w=0.5} Tonight."
    pause 1.0
    $ renpy.block_rollback()
    jump think_02_organs_think

label think_02_dehydration:
    play sound4 "audio/sfx/gui_hint.ogg"
    $ renpy.block_rollback()
    sh -clothes surprise "Withering organs...{w=0.5} Doesn't that sounds like a possible consequence of dehydration?"
    am -clothes shock "Dehy-{w=0.15}oh, no!"
    sh -clothes frown "Gaspard was...{w=0.5} Quite thirsty, right before the transformation, wasn't it?{w=0.3} What if it wasn't due to his nerves?"
    am -clothes sad "It was...{w=0.5} It was a symptom, wasn't it?{w=0.3} Whatever was happening to him was...{w=0.5} Using the water in his body!"
    ta smile "That is my opinion as well, [shn].{w=0.3} Upon inspection, even when accounting for the spillage that occurred during the neutralization process..."
    ta neutral "I've observed a marked absence of natural occurring bodily fluids, plus the aforementioned withering of the hostile's internal organs.{w=0.3} Which leads me to believe that, indeed, dehydration is a symptom of the drastic change."
    ta surprise "Simulteanously, however, I've observed two organs which were instead augmented in size and subsequent spread."
    am -clothes shock "A boost in size...?{w=0.5} What the hell did this thing do to him?!"
    sh -clothes neutral ".{w=0.3}.{w=0.3}.{w=0.5}would those be...?"
    pause 1.0
    $ renpy.block_rollback()
    jump think_02_growth_think

label think_02_growth_think:
    call screen think(_("Two of his organs were {b}reinforced{/b}...?"), _("Skin and lungs?"), "think_02_skin", _("Muscles and skin?"), "think_02_muscles", _("Muscles and nervous system?"), "think_02_nervous", "None", "None")

label think_02_skin:
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    $ renpy.block_rollback()

    pause 1.0
    $ renpy.block_rollback()
    jump think_02_growth_think

label think_02_muscles:
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    $ renpy.block_rollback()

    pause 1.0
    $ renpy.block_rollback()
    jump think_02_growth_think

label think_02_nervous:
    play sound4 "audio/sfx/gui_hint.ogg"
    $ renpy.block_rollback()

    pause 1.0
    $ renpy.block_rollback()
    jump think_02_growth_think