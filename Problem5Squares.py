# Patric Natindim
# March 12 2025

#Problem 5: Draws an image of a square

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of size sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)
        
wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

size = 100  
for i in range(5):  
    drawSquare(alex, size)
    size -= 20  
    alex.penup()
    alex.forward(10)  
    alex.right(90)
    alex.forward(10) 
    alex.left(90)
    alex.pendown()

wn.exitonclick()
