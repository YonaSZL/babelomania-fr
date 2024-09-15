
init python:
    class Entry:
        def __init__(self, title, scr, locked):
            self.title = title
            self.scr = scr
            self.locked = locked

    test_entry = Entry("Test title", "stuff", False)

    c_people = [test_entry,test_entry,test_entry,test_entry,test_entry]
    c_events = [test_entry,test_entry,test_entry,test_entry]
    c_locations = [test_entry,test_entry]
    c_items = [test_entry,test_entry,test_entry,test_entry,test_entry, test_entry,test_entry]






default current_entry = None
screen codex_main():

    tag menu
    add "gui/codex/bg.png"

    button:
        xysize(165,165)
        add "gui/codex/return_bg.png"
        add "gui/gm/return.png" align(0.5, 0.5) xoffset -2 at button_fade
        pos(1722, 728)
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_codex_close.ogg"
        action Return()



    if current_entry:
        viewport:
            xysize(1000,514) pos(572,282) scrollbars "vertical" mousewheel True draggable True
            style_prefix "entry"
            vbox:
                spacing 15
                
                use expression current_entry

    on 'show' action Show("categories")
    on 'hide' action SetVariable("current_entry", None)
            






screen categories():
    
    viewport:
        style_prefix "cat"
        yalign 0.5 xpos 141 ysize 400 xsize 380 scrollbars "vertical" mousewheel True draggable True
        vbox:
            spacing 30
            button:
                    xysize(350,75)
                    add "gui/codex/btn_bg.png"
                    text _("People" )
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action [Hide("categories"),Show("entries", dissolve,c_people)]
            button:
                    xysize(350,75)
                    add "gui/codex/btn_bg.png"
                    text _("Events" )
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action [Hide("categories"),Show("entries", dissolve, c_events)]
            button:
                    xysize(350,75)
                    add "gui/codex/btn_bg.png"
                    text _("Locations" )
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action [Hide("categories"),Show("entries", dissolve, c_locations)]
            button:
                    xysize(350,75)
                    add "gui/codex/btn_bg.png"
                    text _("Items" )
                    hover_sound "audio/sfx/gui_hover.ogg"
                    activate_sound "audio/sfx/gui_confirm.ogg"
                    action [Hide("categories"),Show("entries",dissolve, c_items)]

screen entries(cat):

    viewport:
        style_prefix "cat"
        yalign 0.5 xpos 141 ysize 400 xsize 380 scrollbars "vertical" mousewheel True draggable True

        
        vbox:
            spacing 30
            for i in cat:
                button:
                        xysize(350,75)
                        add "gui/codex/btn_bg.png"
                        text i.title
                        hover_sound "audio/sfx/gui_hover.ogg"
                        activate_sound "audio/sfx/gui_confirm.ogg"
                        action [SetVariable("current_entry", i.scr), Show("codex_main", dissolve)]


    button:
        xysize(86,86) pos(267,822)
        add "gui/codex/cat_btn.png"
        add "gui/codex/cat.png" at button_fade_light
        hover_sound "audio/sfx/gui_hover.ogg"
        activate_sound "audio/sfx/gui_codex_close.ogg"
        action [Hide("entries"), Show("categories", dissolve)]
            

                
style cat_text:
    idle_color '#bfaa8f'
    hover_color "#951b14"
    align(0.5, 0.5) yoffset 3
    font "gui/font/Klotee.ttf"
style cat_vscrollbar:
    xoffset -400
style entry_text:
    justify True
    color '#bfaa8f'
style entry_vscrollbar:
    xoffset 10






#######PLACEHOLDER
screen stuff():
    label "Title"
    text """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla gravida tincidunt pharetra. In fringilla odio id tortor rhoncus, vel malesuada magna elementum. Curabitur hendrerit arcu vel pellentesque accumsan. Aenean ultricies ex quam, vitae pulvinar magna sagittis eget. Praesent scelerisque risus a mattis consectetur. Aenean rhoncus congue erat, non dictum eros consequat sed. Vestibulum pulvinar congue est, et commodo dolor ullamcorper in. Vivamus auctor rutrum purus quis porta. In congue accumsan hendrerit. Quisque placerat felis at sem dignissim, placerat vehicula est efficitur. Praesent in lorem tristique, ornare magna at, finibus tortor. Maecenas vel consectetur mauris. Maecenas lorem lectus, pulvinar ac porta at, dictum et ipsum. Nulla vitae eleifend est, ut porta lorem. Donec cursus eros sit amet laoreet vestibulum."""

    text """Aenean tincidunt enim non consequat fringilla. Maecenas iaculis ex id ipsum blandit porta sed sed nulla. Etiam tristique libero vitae ipsum gravida, a dapibus nisl viverra. Aliquam pretium mauris eu lorem lobortis scelerisque. Sed quis condimentum nisl, ultrices interdum tellus. Suspendisse vel varius nulla, eu eleifend sapien. Etiam et lorem eget felis hendrerit scelerisque. Integer in nisl quis mi facilisis posuere et sit amet nulla. Donec molestie hendrerit nibh, ut imperdiet metus commodo nec. Donec ut neque dolor."""

    text """Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec eget eros sed lectus facilisis euismod. Praesent lacus libero, lacinia eu volutpat vel, aliquet quis felis. Nulla mollis nisi ac diam interdum vestibulum. Curabitur purus est, tristique eu lacinia a, tincidunt sit amet dolor. Fusce interdum nunc ligula, vitae mattis odio porttitor non. Phasellus efficitur, felis vel faucibus sodales, risus lorem venenatis nulla, eu venenatis augue erat nec metus. Morbi eros mauris, rhoncus et consectetur non, efficitur vel massa."""
            