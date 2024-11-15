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
    de_i surprise "(A bunch of newspaper clippings...{w=0.5} In Japanese?)"
    de_i frown "(Well, not exactly, they're printouts of newspaper clippings but still...{w=0.5} What?{w=0.3} Ugh, now I wish I took Francesco up on his lessons.)"
    d """「風土明王」は死刑に直面する

    20XX年11月5日、伊藤純一は彼の罪で処刑されました。死刑は、死刑囚として5年の刑期を終えた後、葛飾区の東京デンテンションハウスで執行された。31歳でした。

    奈良県生まれのこの男は、8年間に犯した11件の殺人罪で有罪判決を受けた。しかし、捜査官は、未成年者として犯された他の9つの殺人の犯人として彼を固定し、死刑を適用することはできませんでした。

    彼の独特な処刑方法と彼の行動の背後にある動機のために、マスコミと大衆は彼に「風土明王」のニックネームを与えました。
    """

label fudo_clipping_japanese:

    d """「風土明王」は死刑に直面する{nw}

    20XX年11月5日、伊藤純一は彼の罪で処刑されました。死刑は、死刑囚として5年の刑期を終えた後、葛飾区の東京デンテンションハウスで執行された。31歳でした。{nw}

    奈良県生まれのこの男は、8年間に犯した11件の殺人罪で有罪判決を受けた。しかし、捜査官は、未成年者として犯された他の9つの殺人の犯人として彼を固定し、死刑を適用することはできませんでした。{nw}
    
    彼の独特な処刑方法と彼の行動の背後にある動機のために、マスコミと大衆は彼に「風土明王」のニックネームを与えました。{nw}
    """