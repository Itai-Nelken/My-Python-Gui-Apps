#!/usr/bin/env python

from guizero import App, Text

app = App(title="hello, world!")
message = Text(app, text="welcome to my python gui coded using guizero")

app.display()
