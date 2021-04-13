#!/usr/bin/env python

import turtle
import random

pat = turtle.Turtle()
tscreen = turtle.Screen()
colors = ["cyan", "red", "white", "orange", "blue", "green", "purple", "pink", "brown", "black", "grey"]
pat.speed(1)


pat.penup()
pat.forward(90)
pat.left(45)
pat.pendown()
def branch():
    for i in range(3):
        for i in range(3):
            pat.forward(30)
            pat.backward(30)
            pat.right(45)
        pat.left(90)
        pat.backward(30)
        pat.left(45)
    pat.right(90)
    pat.forward(90)
    pat.color(random.choice(colors))
    tscreen.bgcolor(random.choice(colors))
for i in range(8):
    branch()
    pat.left(45)

#tscreen.bgcolor(random.choice(colors))
#pat.color("cyan")
#pat.color(random.choice(colors))


#for i in range(10):
 #   pat.right(36)
  #  for i in range(2):
   #     pat.forward(100)
    #    pat.right(60)
     #   pat.forward(100)
      #  pat.right(120)
      


      

    
