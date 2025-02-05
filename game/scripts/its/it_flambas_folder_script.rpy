label flambas_folder_reveal:
    $ renpy.block_rollback()
    show Delphine neutral at de_med:
        xalign 0.5
    with dissolve
    pause 1.0
    scene closed_folder with Reveal
    pause 1.0
    play sound4 "audio/se/paper_shuffle.ogg"
    scene open_folder with dissolve
    pause 0.5
    de_i surprise "(A bunch of newspaper clippings...{w=0.5} In Japanese?{w=0.5} And a transcript of the thing.)"
    de_i disgust "(The originals are a bit faded, I guess...{w=0.5} Anyway, what?{w=0.3} Ugh, now I wish I took Francesco up on his lessons offer.)"
    d """{cps=15}{font=gui/font/ShipporiMincho-Medium.ttf}{size=40}「不動明王」は死刑に直面する{/size}\n"""
    d """{cps=15}{font=gui/font/ShipporiMincho-Medium.ttf}20XX年11月5日、伊藤純一は彼の罪で処刑されました。死刑は、死刑囚として5年の刑期を終えた後、葛飾区の東京拘置所で執行された。31歳でした。"""
    d """{cps=15}{font=gui/font/ShipporiMincho-Medium.ttf}奈良県生まれのこの男は、8年間に犯した11件の殺人罪で有罪判決を受けた。また、彼が18歳になる前に、他にも9件の殺人事件が起きている。"""
    d """{cps=15}{font=gui/font/ShipporiMincho-Medium.ttf}彼の独特な実行方法と彼の行動の背後にある動機のために、彼を「不動明王」と呼ぶ人もいます。"""
    de_i frown "(I doubt it's anything important, otherwise they wouldn't have left it just laying around...{w=0.5} Still, curious.)"
    de_i neutral "(I can't read a single word but the picture...{w=0.5} That's a {nw}"
    play sound4 "audio/sfx/gui_spook.ogg"
    extend"{b}mugshot{/b}, isn't it?)"
    $ delphine_items.append(c_newspaper_clippings)
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    show screen notify(_("New Codex Entry: Newspaper Clippings."))
    pause 1.0
    scene lvl3_meeting with dissolve
    if flambas_folder_inspected == False:
        $ flambas_folder_inspected = True
        $ lvl3_meeting_examine_01 += 1
    pause 1.0
    call screen lvl3_meeting_examine_01