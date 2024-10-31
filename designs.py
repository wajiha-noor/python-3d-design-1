from turtle import *
import colorsys

# Set up the drawing environment
bgcolor("white")  # Set background color
speed(-4)  # Set turtle speed
h = 0  # Initialize hue for color

# Draw a colorful 3D illusion pattern
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)  # Generate color using HSV model
        color(c)  # Set the turtle color
        h += 0.005  # Increment hue for color transition
        right(90)
        circle(150 - j * 6, 90)  # Draw circle segment
        left(90)
        circle(150 - j * 6, 90)
        right(180)  # Turn around to draw the next segment
    penup()  # Lift the pen to move without drawing
    circle(40, 24)  # Small offset for spiral effect
    pendown()  # Put the pen down to draw

# Close the window on click
exitonclick()  # This allows closing the window by clicking on it

done()  # Complete the drawing
