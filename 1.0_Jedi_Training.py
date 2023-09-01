'''
1.0 Jedi Training (17pts)  Name:________________


1. Define Forking (1pt): 
Copying a code template from a repository on to your local repository.
2. Define Cloning (1pt): 
Downloading the code from your repository to your local device.
3. Define Branching (1pt):
Using the master code to make a separate "branch" of your code that can be uploaded to the master code.
4. Define Committing (1pt): 
Saving your code.
5. Define Merging (1pt): 
Putting branches or code into the master code.
6. Define Pushing (1pt):
Uploading code from your device to your repository.
7. Define Pull Request (1pt):
Requesting to have your code uploaded to the master code in the main repository.

8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''

import turtle
import random

tina = turtle.Turtle()
tommy = turtle.Turtle()

tina.color('blue')
tommy.color('green')

tina.shape('turtle')
tommy.shape('turtle')
tommy.speed(1000)
tina.speed(1000)

tina.ht()
tommy.pendown()
turtle.bgcolor('black')
tommy.ht()

color_list = ['red','orange','yellow']

for number in range(150):
    tommy.forward(number+1)
    tina.forward(number+1)
    tommy.left(75)
    tina.left(55)
    if number%2==0:
        tommy.color(color_list[0])
        tina.color(color_list[0])
    else:
        tommy.color(color_list[1])
        tina.color(color_list[1])


tina.penup()
tina.goto(175,-160)
tina.color('red')
tina.write('"Rose"',font=("Arial", 16, "normal"))
tina.goto(175,-175)
tina.color('red')
tina.write('Truman Folkers',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
