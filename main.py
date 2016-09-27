from lib_keyboard import *
from lib_terminal import *
import time
  
current_array = []
    
def main():
    global current_array
    current_line = "".join(current_array)

    line = 1
    column = len(current_line)
    term_height = Terminal.Position.get_height()-3
    prev_lines = []
    last_line_len = 0
    
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
        
        if (current_pressed == "\x08"):
            for i in range(0, 2):
                try:
                    current_array.pop()
                except:
                    main()
            #amount_items -= 1
            column -= 2
            current_line = "".join(current_array)
            
        elif (current_pressed == "\r"):
            current_array.pop()
            term_height -= 1
            line += 1
            #current_array = []
            current_array.append("\n")
        
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
            message = "look = False"
        
        #message = current_array
        Terminal.clear()
        Terminal.Color.light_grey("{}".format(current_line))
        Terminal.Color.purple("column:{}, line:{}, last:{}; {}".format(column, line, last_line_len, message), 0, term_height)
          
        prev_lines = "".join(current_array).split("\n")
        last_line = prev_lines.pop(line-2)
        last_line_len = len(str(last_line))
        current_pressed = getch()
        time.sleep(0.03)
        if (look == True):
            look_array.append(current_pressed)
            message = look_join
            
            if ("quit" in look_join):
                break
            elif ("clean" in look_join):
                current_array = []
                look = False
                message = "look = False"
              
    Terminal.clear()
    quit()
main()
            