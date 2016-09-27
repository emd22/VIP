from lib_keyboard import *
from lib_terminal import *
import time

getchar = Getchar()

temp_file = open("temp", "w+")

current_line = ""
current_array = []
current_items = 0
line = 1
column = 0

pressed_key = getchar()
current_items += 1
current_array.append(pressed_key)
current_line = "".join(current_array)

lines_array = []
    
while True:
    Terminal.Position.reset_to(0,0)
    pressed_key = getchar()
    current_items += 1
    current_array.append(pressed_key)
    current_line = "".join(current_array)
        
    Terminal.clear()
    Terminal.print("{}{}".format("".join(lines_array), current_line))
    Terminal.print("col:{}, ln:{}".format(column, line), 0, Terminal.Position.get_height()-2-line)

    #backspace key
    if (pressed_key == "`"):
        current_line.rstrip("`")
        #current_array.remove("`")
        current_items -= 1
        column -= 2
        current_items -= 1
        current_array.pop(current_items)
        #current_items -= 1
        #current_array.pop(current_items)
    
    #enter key    
    if (pressed_key == "~"):
        current_line.rstrip("~")
        #current_array.remove("~")
        line += 1
        column = 0
        current_items = 0
        temp_file.write("{}\n".format(current_line))
        current_array = []
        #Terminal.print("")
    if ("$quit" in current_line):
        break
        
    column += 1
    
temp_file.close()
quit()
    
