import time
from turtle import *

#screen/canvas

#The Turtles

eli = Turtle()

dunlap = Turtle()

chase = Turtle()
chase.color(15 / 255, 215 / 255, 15 / 155)
chase.shape("turtle")

#helper functions

def draw_four_squ():
    for i in range(4):
        for i in range(4):
            eli.fd(100);
            eli.dot(20, (100 / 255,0 / 255,100 / 255));
            eli.fd(100);
            eli.right(90)
        eli.left(90)

def draw_octagon():
    for i in range(4):
        for i in range(8):
            dunlap.forward(45)
            dunlap.right(45)
        dunlap.right(90)


def turn_to_pointer(x, y):
    direction = chase.towards(x, y)
    chase.setheading(direction)
    print(str(direction))
    chase.moving = True
    
def reset():
    eli.reset()
    dunlap.reset()
    chase.reset()

def get_choice():
    print(" ")
    choice = input("Do you want to move with the arrow keys or mouse click? 'k for keys' 'm for mouse'")
    print(" ")
    print("Thanks! Remember pressing 'r' will boot the program with only the controlable Turtle.")
    if choice == 'k':
        return 1
    elif choice == 'm':
        return 2

def k1():
    chase.left(45)

def k2():
    chase.back(45)

def k3():
    chase.forward(45)

def k4():
    chase.right(45)

#play
    
choice = get_choice()

if choice == 2:
    chase.moving = True
    
draw_four_squ()

if choice == 2:
    onscreenclick(turn_to_pointer)

draw_octagon()

if choice == 2:
    while True:
        if chase.moving:
            chase.forward(5)
            chase.dot(5, 15 / 255,15 / 255,200 / 255)
            listen()
            onkey(reset, 'r')

if choice == 1:
    listen()
    onkey(k1, 'a')
    onkey(k2, 's')
    onkey(k3, 'w')
    onkey(k4, 'd')
    onkey(reset, 'r')

