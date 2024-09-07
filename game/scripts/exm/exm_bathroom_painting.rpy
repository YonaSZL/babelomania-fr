
screen bathroom_painting_examine():
    return

label exm_bathroom_painting_subject:
    pause 0.5
    sh_i frown "(A city tall enough to reach the sky and beyond, built in a spiral like pattern.{w=0.3} Rivers of blood rivulet off from it, making a desolate landscape even more derelict...)"
    play sound "audio/sfx/gui_hint.ogg"
    sh_i surprise "(This must be...{w=0.5} A reinterpretation of the {b}Tower of Babel{/b}, right?{w=0.5} I've never seen one quite like this.)"
    sh_i neutral "(The ones I've seen are usually...{w=0.5} Nicer.{w=0.3} They feature the tower and the community that grew up around it, or they showcase it as it is being built...)"
    sh_i frown "(This feels more like a depiction of what came after the big G went all old testament on humanity...{w=0.5} Although that doesn't explain the rivers of blood.)"
    sh_i surprise "(.{w=0.3}.{w=0.3}.{w=0.5}or maybe it does?)"
    pause 1.0
    call screen bathroom_painting_examine

label exm_bathroom_painting_title:
    pause 0.5
    sh_i neutral "(Doesn't feel like the original frame of the painting...{w=0.5} Still, there's a plaque at the bottom.)"
    play sound "audio/sfx/gui_hint.ogg"
    sh_i frown "({b}'The Festering Wound'{/b}...{w=0.5} Geez, talk about resentment.)"
    sh_i amused "(Whoever made this was either {i}very{/i} religious, or not at all...{w=0.5} Or maybe both at different points in time.)"
    sh_i surprise "(I wonder, though...{w=0.5} Was the painter resenting God himself, or is the whole thing just a metaphor?{w=0.3} Not a question you can answer without knowing the author.)"
    pause 1.0
    call screen bathroom_painting_examine

label exm_bathroom_painting_signature:
    pause 0.5
    play sound "audio/sfx/gui_hint.ogg"
    sh_i surprise "(Huh...{w=0.5} That spot on the canvas is {b}ruined{/b}.)"
    sh_i frown "(Is that where the signature of the author was?{w=0.5} It's all blurred and ruined, I can barely make out half of the date...)"
    sh_i neutral "(19...{w=0.5} Well, at least I know it was made in the previou century, so that's something...?)"
    pause 1.0
    call screen bathroom_painting_examine

label exm_bathroom_painting_return:
    pause 0.5
    jump story_00_bathroom_returns