#!/usr/bin/python3
#imports
from guizero import App, Text, PushButton
from random import choice

#functions
def choose_name():
     #print("Button was pressed")
    first_names = ["Furious", "SuperSpy", "Smokey", "BigSpy", "Ruby", "Mr", "SpybigSpy"]
    last_names = ["Spindelshanks", "Mysterioso", "Dungeon", "Catseye", "Darkmeyer", "Flamingobreath", "the Furious"]
    spy_name = choice(first_names) + " " + choice(last_names)
#     print(spy_name)
    name.value = spy_name
    
     

#app
app = App("TOP SECRET!")
app.height = 350

#widgets
title = Text(app, "Push the red button to find out your spy name")
title.font = "Monospace"
title.text_size = 14

button = PushButton(app, choose_name, text="Tell me!")
button.text_size = 25
button.width= 10
button.height=5
button.bg = "red"

name = Text(app, text=" ")
name.text_size = 20
name.font = "Times New Roman"

#display
app.display()