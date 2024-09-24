##Defining The Calendar

default hours = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
default minutes = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
"21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", 
"47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]
default current_hours = 20
default dis_hours = hours[current_hours]
default current_minutes = 37
default dis_minutes = minutes[current_minutes]

init python:
    def move_time(ins_hours,ins_minutes):
        global current_hours
        global current_minutes
        global dis_hours
        global dis_minutes
        global hours
        global minutes
        global days
        current_hours = current_hours + ins_hours
        if current_hours > 23:
            current_hours = current_hours - 24
            current_day = current_day + 1
        current_minutes = current_minutes + ins_minutes
        if current_minutes > 59:
            current_minutes = current_minutes - 60
            current_hours = current_hours + 1
            if current_hours > 23:
                current_hours = current_hours - 24
                current_day = current_day + 1
        dis_hours = hours[current_hours]
        dis_minutes = minutes[current_minutes]