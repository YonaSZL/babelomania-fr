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
    jump think_01_door

label think_01_comein:
    play sound4 "audio/sfx/gui_hint.ogg"
    $ renpy.block_rollback()
    sh_i nulla "(Because it's locked...{w=0.5} The door is locked.{w=0.3} Or rather...)"
    show Shigeo surprise with dissolve
    sh_i nulla "(It can't be opened from the outside...{w=0.5} This is a meeting room, isn't it?{w=0.3} I see no keyhole, nor a card-reader...{w=0.5} So to open it from this side, all you need do is work the handle.)"
    show Shigeo frown with dissolve
    sh_i nulla "(So, whoever put me in here...{w=0.5} Put me in a room with security shutters...{w=0.5} And a door that can be easily opened from the inside, but is locked from the outside.{w=0.5} Because...)"
    pause 1.0
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
    pause 1.0
    jump think_01_door

label think_01_protect:
    play sound4 "audio/sfx/gui_hint.ogg"
    $ renpy.block_rollback()
    
    pause 1.0
    jump think_01_room