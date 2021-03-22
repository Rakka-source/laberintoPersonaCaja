import turtle                    # import turtle library
import time
import sys

wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("black")                # set the background colour
wn.title("Laberinto")
wn.setup(1300,700)                  # setup the dimensions of the working window


# this is the class for the Maze
class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("white")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)

# this is the class for the finish line - green square in the maze
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


# this is the class for the yellow or turtle
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)




grid= [["#","#","#",".","."],
        ["#","#","#",".","#"],
        ["#","#","D",".","#"],
        [".",".",".",".","#"],
        ["P","#","C","#","#"],
        [".",".",".",".","#"]]



def setup_maze(grid):                          # define a function called setup_maze
    for y in range(len(grid)):                 # read in the grid line by line
        for x in range(len(grid[y])):          # read each cell in the line
            character = grid[y][x]           # assign the varaible "character" the the x and y location od the grid
            screen_x = -588 + (x * 24)         # move to the x location on the screen staring at -588
            screen_y = 288 - (y * 24)          # move to the y location of the screen starting at 288

            if character == "#":
                blue.goto(screen_x,screen_y)
                blue.stamp()

            if character == "." or character == "D":
                maze.goto(screen_x, screen_y)       
                maze.stamp()

            if character == "D":
                green.color("purple")
                green.goto(screen_x, screen_y)       # send green sprite to screen location
                green.stamp()
                green.color("green")

            if character == "C":
                yellow.color("purple")
                yellow.goto(screen_x, screen_y)       # send green sprite to screen location
                start_cx, start_cy = screen_x, screen_y
            if character == "P":
                red.goto(screen_x, screen_y)
                start_px, start_py = screen_x, screen_y
    return start_cx, start_cy,start_px, start_py

def dimension(x,y):
    screen_x = -588 + (x * 24)  
    screen_y = 288 - (y * 24) 
    return screen_x,screen_y

def paint(ruta,px,py,cx,cy):
    print("asd")
    sc_x,sc_y=dimension(px,py)
    for i in range (len(ruta)):
        print(sc_y)
        if ruta[i] == "p-d": #abajo
            sc_y+=24
            
        if ruta[i] == "p-u": #arriba
            sc_y-=24
        if ruta[i] == "p-r": #derecha
            sc_x+=24
        if ruta[i] == "p-r": #izquierda
            sc_x-=24
        print("hola")
        green.color("purple")
        green.goto(sc_x, sc_y)       # send green sprite to screen location
        green.stamp()
        green.color("green")
        





def endProgram():
    wn.exitonclick()
    sys.exit()



# set up classes
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()




# main program starts here ####
start_cx, start_cy,start_px, start_py=setup_maze(grid)

ruta=['p-d', 'p-r', 'p-r', 'c-u', 'p-u', 'c-u']
paint(ruta,start_px, start_py,start_cx, start_cy)

wn.exitonclick()