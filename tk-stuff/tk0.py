import tkinter as tk

window=tk.Tk()

label = tk.Label(
    text="Hello, World!",
    foreground="blue",
    #background="black"
)

button=tk.Button(
    text="A button!",
    fg="#F1EAE5",
    bg="green",
    width=10,
    height=1
)

entry=tk.Entry(
    #fg="white",
    #bg="black",
)

label.pack()
entry.pack()
button.pack()
window.mainloop()
