import sys, os, random

####################################
#  Terminal(print, getsize, etc.)  #
####################################

class Terminal():
    class Position():
        def reset_to(x, y):
            Terminal.print("\033[{};{}H".format(x, y))
            
        def get_height():
            size = os.popen('stty size', 'r').read().split()
            height = int(size.pop(0))
            
            return int(height)
            
        def get_width():
            size = os.popen('stty size', 'r').read().split()
            width = int(size.pop(1))
                
            return int(width)

        def set(x, y):
            for i in range(0, x):
                Terminal.print(" ", end="")
            for i in range(0, y):
                Terminal.print("\n", end="")  

    def clear():
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix" or os.name == "unix":
            os.system("clear")
        else:
            print("\n"*Terminal.Position.get_height)

    def print(message, x=0, y=0, end="\n"):
        Terminal.Position.set(x, y)
        sys.stdout.write("{}{}".format(message, end))
        sys.stdout.flush() 
        
    class Color():
        def red(message, x=0, y=0, end="\n"): 
            Terminal.print("\033[91m{}\033[00m".format(message), x, y, end)
            
        def green(message, x=0, y=0, end="\n"): 
            Terminal.print("\033[92m{}\033[00m".format(message), x, y, end)
            
        def yellow(message, x=0, y=0, end="\n"): 
            Terminal.print("\033[93m{}\033[00m".format(message), x, y, end)
            
        def light_purple(message, x=0, y=0, end="\n"): 
            Terminal.print("\033[94m {}\033[00m".format(message), x, y, end)
            
        def purple(message, x=0, y=0, end="\n"): 
            Terminal.print("\033[95m{}\033[00m".format(message), x, y, end)
            
        def cyan(message, x=0, y=0, end="\n"): 
            Terminal.print("\033[96m{}\033[00m".format(message), x, y, end)
            
        def light_grey(message, x=0, y=0, end="\n"):
            Terminal.print("\033[97m{}\033[00m".format(message), x, y, end)
            
        def black(message, x=0, y=0, end="\n"): 
            Terminal.print("\033[98m{}\033[00m".format(message), x, y, end)
  
rect = ""

class Draw():
    class Rectangle():
        rect = ""
        
        def create(width, height, character=":"):
            global rect
            for cur_height in range(0, height):
                rect = rect+"\n"
                for cur_width in range(0, width):
                    rect = rect+character          
        def draw(x, y):
            Terminal.Position.set(x, y)
            return str(rect)
        def reset():
            rect = ""
            
    class Ground():
        platform = ""
        class Platform():  
            def create(width, height, random_pos=False, random_limit_x=0, random_limit_y=0):
                Draw.Rectangle.create(width, height)
                random_x = random.randrange(0, random_limit_x)
                random_y = random.randrange(0, random_limit_y)
            def draw(x, y):
                if random_pos == True:
                    return Draw.Rectangle.draw(random_x, random_y)
                else:
                    return Draw.Rectangle.draw(x, y)
                
        class Solid():
            def create(height):  
                height = height  
                Draw.Rectangle.create(Terminal.Position.get_width(), height)
                return height
            def draw(height):
                return Draw.Rectangle.draw(0, Terminal.Position.get_height()-height)
        
        
        
        
