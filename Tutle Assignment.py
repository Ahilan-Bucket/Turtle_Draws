# Title : Sickle and Hammer Drawer
# Author Name : Ahilan Kumaresan
# Date : 10-11-2024

#This line has exactly 100 characters (including the period), use it to keep each line under limit.

# Necessary Imports
import turtle 
import math
import numpy as np


# Funtions

# Golden ratio and constants for the spiral equation
# WIth some specific configrations so that my sickele hammer wont interfere
# This is to replace random points generator to have a more structured points created    

# Function with a return value
def golden_spiral_points(num_points=1000):
    phi = (1 + np.sqrt(5)) / 2
    b = np.log(phi) / np.pi
    a = 200  # scale of spiral
    
    # Arrays to store the coordinates (Does not exist outside this def)
    x_coords = []
    y_coords = []
    
    # Generate points along the spiral
    i = 1
    while len(x_coords) <= (num_points): # A while Loop
        theta = i * 1  # Increment theta to get more points
        sickle_radius = a * np.exp(b * theta)
        i +=1
        # Stop if the length_of_canvas exceeds the canvas length_of_canvas
        if sickle_radius > 400:
            break
        
        # Convert polar to Cartesian coordinates
        x = sickle_radius * np.cos(theta)
        y = sickle_radius * np.sin(theta)
        if (x > 50 or y > 50 or x < -50 or y < -50):
            x_coords.append(x)
            y_coords.append(y)
        
    return x_coords, y_coords

# Draw Stars 
# function with no return loop
def draw_star(scale=1):
    worker.fillcolor("black")
    worker.begin_fill()
    for i in range (5):
        worker.forward(30*scale)
        worker.right(108)
        worker.forward(30*scale)
        worker.left(36)
    worker.end_fill()    


# Start of Code
worker = turtle.Turtle()

# Set up the background color
turtle.bgcolor("dark blue")

worker.penup() # penup()
worker.goto(0,0)
worker.circle(10)
worker.speed(0.5)
worker.pen(pensize=0)


# Main Oval for the Main Sickle
sickle_x_position = 0
sickle_y_position = 0
sickle_radius = 20
worker.goto(sickle_x_position,sickle_y_position)
worker.fillcolor("red") # COlour first then circle to aviod the Outline
worker.pencolor("dark blue")
worker.shape("circle")
worker.shapesize(sickle_radius,sickle_radius*(3.7/3.2),0)
worker.stamp()


# Subtractive Moon
subtract_sickle_x = sickle_x_position - sickle_radius/2
subtract_sickle_y = sickle_y_position + sickle_radius/3.4
worker.goto(subtract_sickle_x,subtract_sickle_y)
worker.fillcolor("dark blue")
worker.stamp()

# Draw Sickle Base Rod
rod_x_position = math.sqrt((sickle_x_position - subtract_sickle_x)**2 + 
                           (sickle_y_position - subtract_sickle_y)**2)

base_position_x = rod_x_position - 100
base_position_y = -190

worker.goto(base_position_x,base_position_y)

worker.setheading(180+45) # Needs an Angle in deg
worker.pendown() # pendown()
worker.color("red")
worker.width(17)
worker.forward(40)

worker.shape("circle")
worker.shapesize(2.5,2,0) 
# turtle.turtlesize(stretch perpendicular, stretchin direction, width)
worker.fillcolor("red")
worker.stamp()

worker.forward(20)
worker.shape("circle")
worker.shapesize(2.5,4,0) 
# turtle.turtlesize(stretch perpendicular, stretchin direction, width)
worker.fillcolor("red")
worker.stamp()


worker.penup()
worker.setheading(180+45)
worker.forward(50)
worker.shapesize(1.5,10,1)
worker.fillcolor("red")
worker.stamp()


# Draw Hammer 
worker.goto(base_position_x + 400, base_position_y-100)
worker.setheading(135)
worker.stamp()
worker.pendown()
worker.forward(500)
worker.width(70)

# Draw Hammer Head (Trapezoid)
worker.width(2)
h_top = 120
h_base = (2/1.5) *h_top
h_height = (0.7/1.5)*h_top
worker.color("red")
worker.begin_fill()
worker.left(90)
worker.forward(h_top*(2/3))
worker.left(90)
worker.forward(h_height)
worker.left(90)
worker.forward(h_base)

angel_turned = 90+45
worker.left(angel_turned)

l = h_height/(math.sin(np.deg2rad(180-angel_turned)))
worker.forward(l)
worker.left(180-angel_turned)
worker.forward(h_top*1/3)
worker.end_fill()
worker.penup()



# Draw Stars
nos = 4 # Number of stars
x_coords, y_coords = golden_spiral_points(nos)  # Get the spiral points


i = 0
while i < nos:
    worker.penup()          
    worker.goto(x_coords[i],y_coords[i])
    worker.pendown()
    draw_star()
    i += 1

# Draw grid of all coordinates (Hehe Funny Stars Laughing Emoji's ahha)
worker.penup()
worker.speed(0)
worker.color("red")
for x in range(-700, 701, 100):  # Draw grid from -300 to 300 with step size 50
    for y in range(-500, 501, 100):
        worker.goto(x, y)
        worker.dot(3)  # Mark each coordinate with a small dot
        #worker.write(f"({x}, {y})", align="left", font=("Arial", 8, "normal"))

# Hide the turtle and finish
worker.hideturtle()
turtle.done()