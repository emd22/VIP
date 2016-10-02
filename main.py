from lib_keyboard import *
from lib_terminal import *
import time
  
current_array = []
prev_lines = []
    
def main():
    global current_array
    current_line = "".join(current_array)

    line = 1
    column = len(current_line)
    term_height = Terminal.Position.get_height()-3
    prev_lines = []
    
    look = False
    look_array = []

    message = ""
    current_pressed = getch()

    while True:
        
        Terminal.Position.reset_to(column-1, 0)
        current_array.append(current_pressed)
        current_line = "".join(current_array)
        
        split_array = current_line.split("\n").pop()
        
        column = len("".join(split_array))
        
        if (current_pressed == "\x13"):
            current_array.pop()
            current_array.append("EMPTY!")
        
        elif (current_pressed == "\x08"):
            for i in range(0, 2):
                try:
                    current_array.pop()
                except:
                    main()
            column -= 2
            current_line = "".join(current_array)
            
            if (current_line == "" or current_line == "\n"):
                list_temp = prev_lines.pop()
                list_temp = list(list_temp)
                for i in range(0, len("".join(list_temp))):
                    current_array.insert(i, list_temp.pop(0))
            
        elif (current_pressed == "\r"):
            current_array.pop()
            term_height -= 1
            line += 1
            current_array.append("\n")
            prev_lines.append("".join(current_array).rstrip("\r"))
            current_array = []
            current_line = ""
        
        elif (current_pressed == ""):
            break
        
        else:
            message = "Accepted Key '{}'".format(current_pressed)  
            
        look_join = "".join(look_array)    
        if (current_pressed == "$"):
            look_array = []
            look = True
                
        if (look == True and current_pressed == "$" and look_join != ""):
            look = False
        
        message = prev_lines, current_array
        Terminal.clear()
        Terminal.Color.light_grey("{}{}".format("".join(prev_lines), current_line))
        Terminal.Color.green("column:{}, line:{}; {}".format(column, line, message), 0, term_height)
        
        current_pressed = getch()
        time.sleep(0.05)
        if (look == True):
            look_array.append(current_pressed)
            
            if ("quit" in look_join):
                break
            elif ("clean" in look_join):
                current_array = []
                look = False
              
    Terminal.clear()
    quit()
main()
            
