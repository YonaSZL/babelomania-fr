menu think_01_door:
    sh_i surprise "(Why are they {b}trying{/b} to open the door?)"

    "Because they want to come in.":
        jump think_01_comein

    "Because the door is locked.":
        jump think_01_locked

label think_01_comein:
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    $ renpy.block_rollback()
    sh_i nulla "(They're trying to come in, obviously...{w=0.5} But it's not so much about that.{w=0.3} Their intentions are clear...)"
    show Shigeo frown with dissolve
    sh_i nulla "(The real question is, why haven't they come in yet?)"
    pause 1.0
    $ renpy.block_rollback()
    jump think_01_door

label think_01_locked:
    play sound4 "audio/sfx/gui_hint.ogg"
    $ renpy.block_rollback()
    sh_i nulla "(Because it's locked...{w=0.5} The door is locked.{w=0.3} Or rather...)"
    show Shigeo surprise with dissolve
    sh_i nulla "(It can't be opened from the outside...{w=0.5} This is a meeting room, isn't it?{w=0.3} I see no keyhole, nor a card-reader...{w=0.5} So to open it from this side, all you need do is work the handle.)"
    show Shigeo frown with dissolve
    sh_i nulla "(So, whoever put me in here...{w=0.5} Put me in a room with security shutters...{w=0.5} And a door that can be easily opened from the inside, but is locked from the outside.{w=0.5} Because...)"
    pause 1.0
    $ renpy.block_rollback()
    jump think_01_room

menu think_01_room:
    sh_i frown "(Why did they put me in a room {b}locked from the outside{/b}?)"

    "Because they wanted to trap me.":
        jump think_01_trap

    "Because they wanted to protect me.":
        jump think_01_protect
    
label think_01_trap:
    play sound4 "audio/sfx/gui_slots_confirm.ogg"
    $ renpy.block_rollback()
    sh_i nulla "(Trap me?{w=0.3} No, it doesn't make sense.{w=0.3} They could have tied me down, too...{w=0.5} I don't have my phone, yes, but...)"
    show Shigeo surprise with dissolve
    sh_i nulla "(A door easily opened from inside but not outside...{w=0.5} Unless this is a special room that can only be opened from outside?{w=0.3} Which just so happens to look like a meeting room?{w=0.3} That's...{w=0.5} Unlikely.)"
    show Shigeo frown with dissolve
    pause 1.0
    $ renpy.block_rollback()
    jump think_01_room

label think_01_protect:
    $ renpy.block_rollback()
    play sound3 "audio/se/doorknob_rattle.ogg"
    sh_i nulla "(Whoever stuffed me in here, then locked the door from outside.{w=0.3} If it was the same person now at the door they would be able to get in again no issue...)"
    show Shigeo surprise with dissolve
    sh_i nulla "(So it's not the same person and...{w=0.5} If the door can be opened from my side...{w=0.5} {nw}"
    play sound4 "audio/sfx/gui_solved.ogg"
    extend "{b}They put me in here to hide me{/b}!)"
    pause 1.0
    $ renpy.block_rollback()
    jump story_01_door_opens