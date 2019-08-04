# SpiralFamily.py
# Billy Ridgeway
# Prints everybody in a familys name on the screen.

import turtle           # Imports turtle graphics.
t = turtle.Pen()        # Creates a new turtle called t.
t.speed(0)              # Sets the speed of the pen to fast.
turtle.bgcolor("black") # Sets the background color to black.

# Creates a list of colors.
colors = ["red", "yellow", "blue", "green", "orange",
          "purple", "white", "brown", "gray", "pink"]

family = []             # Sets up an empty list for family names.

# Ask for the first name.
name = turtle.textinput("My family",
                        "Enter a name, or just hit {ENTER] to end:")

# Creats a while loop that keeps asking for names.
while name != "":
    # Add their name to the family list.
    family.append(name)
    # Ask for another name, or end the program.
    name = turtle.textinput("My family",
                        "Enter a name, or just hit {ENTER] to end:")

# Create a for loop to draw a spiral of the names on the screen.
for x in range(100):                    # Sets the variable 'x' to 100.
    t.pencolor(colors[x%len(family)])   # Cycles through the colors.
    t.penup()                           # Lift the pen so it won't draw as it moves.
    t.forward(x*4)                      # Move the pen forward the value of 'x' times 4.
    t.pendown()                         # Put the pen down so it will draw.
    
    # Write a family member's name using bold Arial font size x plus 4 divided by 4.
    t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold"))
    
    t.left(360/len(family)+2)           # Turn left the value of 360 degrees divided
                                        # by the length of family plus 2.
