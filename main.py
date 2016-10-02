from lib_keyboard import *
from lib_terminal import *
import time
  
current_array = []
prev_lines = []

def main():
    save_filename = ""  
    
    global current_array
    global prev_lines
    
    current_line = "".join(current_array)

    line = 1
    column = len(current_line)
    remove_from_term_height = 3
    term_height = Terminal.Position.get_height()-remove_from_term_height
    
    prev_lines = []
    current_words = []
    
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
        
        #^s Key
        if (current_pressed == "\x13"):
            current_array.pop()
            if (save_filename == ""):
                message = "type $filename$ to choose filename."
            else:
                save_file = open("."+save_filename, "w")
                save_file.write("".join(prev_lines)+current_line)
                save_file.close()
                message = "created file '{}'".format(save_filename)
        
        #BACK Key
        elif (current_pressed == "\x08" or current_pressed == "[3~"):
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
            
        #ENTER Key
        elif (current_pressed == "\r"):
            current_array.pop()
            remove_from_term_height += 1
            line += 1
            current_array.append("\n")
            prev_lines.append("".join(current_array).rstrip("\r"))
            current_array = []
            current_line = ""
        
        #ESCAPE Key
        elif (current_pressed == ""):
            break
        
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
            
            if (look_join == "quit" or look_join == "exit"):
                break
            elif (look_join == "clean" or look_join == "clear"):
                current_array = []
                prev_lines = []
                current_line = ""
                look = False
            elif (look_join == "filename"):
                save_filename = input("set filename: ")
                message = "filename set."
        term_height = Terminal.Position.get_height()-remove_from_term_height
              
    Terminal.clear()
    quit()
main()
            
