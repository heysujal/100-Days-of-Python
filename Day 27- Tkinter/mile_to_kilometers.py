from tkinter import *

window = Tk()
window.title("Miles to Kilometers")
# window.minsize(height=300, width=300)
window.config(padx=20, pady=20)

input_here = Entry(width=10)
input_here.grid(row=0, column=1)
miles_label = Label(text='miles')
miles_label.grid(row=0, column=2)
label1 = Label(text='is equal to')
label1.grid(row=1, column=0)

output_label = Label(text='0')
output_label.grid(row=1, column=1)
km_label = Label(text='Km')
km_label.grid(row=1, column=2)


def convert_val():
    value = float(input_here.get())
    answer = value * 1.60934
    output_label.config(text=answer)


button = Button(text='Calculate', command=convert_val)
button.grid(row=2, column=1)

window.mainloop()
