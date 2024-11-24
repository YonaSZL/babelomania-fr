##LVL3 Locations
image lvl3_wellness_dim = "images/bgs/lab/lvl3/lvl3_wellness_dim.jpg"
image lvl3_wellness_bright = "images/bgs/lab/lvl3/lvl3_wellness_bright.jpg"

image base_lvl3_corridor = "images/bgs/lab/lvl3/lvl3_corridor.jpg"
image base_lvl3_corridor_dark = "images/bgs/lab/lvl3/lvl3_corridor_dark.jpg"

layeredimage lvl3_corridor:
    group body:
        attribute base default:
            "base_lvl3_corridor"
    if exp_lvl3_corridor_01_elevators:
        "images/bgs/lab/lvl3/lvl3_corridor_blood.png"

image lvl3_meeting = "images/bgs/lab/lvl3/lvl3_meeting.jpg"
image lvl3_meeting_dark = "images/bgs/lab/lvl3/lvl3_meeting_dark.jpg"

##Common Locations

image elevator_closed = "images/bgs/lab/elevator_closed.jpg"
image elevator_open = "images/bgs/lab/elevator_open.jpg"
image elevator_panel = "images/bgs/lab/elevator_panel.jpg"