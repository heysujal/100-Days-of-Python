from tkinter import *

window = Tk()
window.title("my first GUI program")
window.minsize(height=600, width=600)
window.config(padx=60, pady=60)
# label
greeting = Label(text="Hello", bg='blue', font=('Arial', 24, 'bold'))
# greeting.pack()

greeting['text'] = 'Bye'
greeting.config(text='not yet')
greeting.grid(column=0, row=0)
greeting.config(padx=60, pady=60)


def change_text():
    new_text = entry.get()

    greeting.config(text=new_text)


button = Button(text="Click me!", command=change_text)
button.grid(column=1, row=1)
# button.pack()

entry = Entry(width=10)
entry.grid(row=2, column=3)
# entry.pack()

# name = entry.get()
# greeting.config(text=name)


new_button = Button(text='I am new Button')
new_button.grid(row=0, column=2)
window.mainloop()
