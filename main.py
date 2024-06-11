import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
#---------------------------Creating Fash Cards----------------------------#
try:
    data=pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel((flip_timer))
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_head, fill="blue")
    canvas.itemconfig(card_head2, text="The English word for given French word pops in 3 sec..", fill="blue")
    canvas.itemconfig(background, image = front_img)
    flip_timer = window.after(3000, func=flip_cards)

#---------------------------Flipping the Cards-----------------------------#

def flip_cards():
    canvas.itemconfig(card_title, text='English', fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(background, image = back_img)
    canvas.itemconfig(card_head, fill="yellow")
    canvas.itemconfig(card_head2, text= "Did you get it right? Click ✅", fill ="yellow")

#-------Saving progress and removing the words that user already knows-----#

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=FALSE)
    next_card()

#-----------------------------------UI-------------------------------------#

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func = flip_cards)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")
background = canvas.create_image(400, 263, image=front_img)
card_head = canvas.create_text(400, 80, text="Welcome to Flash Cards!", fill= "blue", font=("Ariel", 20, "bold"))
card_head2 = canvas.create_text(400, 110, text="The English word for given French word pops in 3 sec..", fill= "blue", font=("Ariel", 15, ))
card_title = canvas.create_text(400, 190, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 280, text="", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

check_image = PhotoImage(file="right.png")
right_button = Button(image=check_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
