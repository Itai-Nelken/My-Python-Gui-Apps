from guizero import App, Text, Picture

app = App("Wanted!")
app.bg = "#aaaaaa"
app.height = 610
wanted_text = Text(app, "WANTED")
wanted_text.text_size = 50
wanted_text.font="Times New Roman"
burglar = Picture(app, image="burglar.png")



app.display()