from tkinter import *

window = Tk()
window.title("my first GUI program")
window.minsize(height=600, width=600)

# label
greeting = Label(text="Hello")
greeting.pack()


def change_text():
    new_text = entry.get()

    greeting.config(text=new_text)


button = Button(text="Click me!", command=change_text)
button.pack()

entry = Entry(width=10)
entry.pack()

# name = entry.get()
# greeting.config(text=name)
window.mainloop()
