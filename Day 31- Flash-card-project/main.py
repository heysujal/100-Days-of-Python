import random
from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# Reading data from CSV

try:
    df = pd.read_csv("./data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
    print(to_learn)
# except pd.errors.EmptyDataError:

else:
    to_learn = df.to_dict(orient="records")
    print(to_learn)

current_card = {}


# Generate New Word
def generate_new_word():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)  # GIVES ONE RANDOM FRENCH WORD WITH ITS MEANING

    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_img, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


# Flipping the card
def flip_card():
    # print('hello')

    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')


# Removing Known Word and creating new csv
def update_words_to_learn():
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)
    generate_new_word()


# ------------------------------ UI --------------------------------------#
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="./images/card_front.png")
card_img = canvas.create_image(400, 263, image=card_front_img)

card_back_img = PhotoImage(file="./images/card_back.png")

card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Calling function to fill title and word for first time


cross_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, bd=0, pady=0, command=generate_new_word)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="./images/right.png")
known_button = Button(image=check_img, highlightthickness=0, bd=0, pady=0,
                      command=update_words_to_learn)
known_button.grid(row=1, column=1)

generate_new_word()

window.mainloop()
