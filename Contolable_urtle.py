import turtle
from turtle import *
title("Use the Arrow Keys to Move")
bgcolor("Black")
move = Turtle()
move_a = Turtle()
move_b = Turtle()
move_c = Turtle()

move.color("red")
move_a.color("blue")
move_b.color("Orange")
move_c.color("Green")

choice = 1

def control_red():
    global choice
    choice = 1

def control_blue():
    global choice
    choice = 2

def control_orange():
    global choice
    choice = 3

def control_green():
    global choice
    choice = 4

def control_all():
    global choice
    choice = 5

def k1():
    if choice == 1 or choice == 5:
        move.forward(45)
    if choice == 2 or choice == 5:
        move_a.forward(45)
    if choice == 3 or choice == 5:
        move_b.forward(45)
    if choice == 4 or choice == 5:
        move_c.forward(45)

def k2():
    if choice == 1 or choice == 5:
        move.left(45)
    if choice == 2 or choice == 5:
        move_a.left(45)
    if choice == 3 or choice == 5:
        move_b.left(45)
    if choice == 4 or choice == 5:
        move_c.left(45)

def k3():
    if choice == 1 or choice == 5:
        move.right(45)
    if choice == 2 or choice == 5:
        move_a.right(45)
    if choice == 3 or choice == 5:
        move_b.right(45)
    if choice == 4 or choice == 5:
        move_c.right(45)

def k4():
    if choice == 1 or choice == 5:
        move.back(45)
    if choice == 2 or choice == 5:
        move_a.back(45)
    if choice == 3 or choice == 5:
        move_b.back(45)
    if choice == 4 or choice == 5:
        move_c.back(45)

onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")
onkey(control_red, 'r')
onkey(control_blue, 'b')
onkey(control_green, 'g')
onkey(control_orange, 'o')
onkey(control_all, 'a')

listen()
mainloop()



