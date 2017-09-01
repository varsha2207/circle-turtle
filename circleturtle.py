import turtle
import random

colors = ["red","green","blue","orange","purple","pink","yellow"]
my_turtle = turtle.Turtle()
my_turtle.speed(0)
def square(length, angle):
    for count in range(4):
        color = random.choice(colors)
        my_turtle.forward(length)
        my_turtle.right(angle)
        my_turtle.color(color)
        
    """
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    """
for i in range(100):    
    square(0,31)
    square(100,90)
   
