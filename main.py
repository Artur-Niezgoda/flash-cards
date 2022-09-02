import tkinter as tk
import pandas as pd
import random
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
current_card = {}
active_side = 0


def know_word():
    if len(to_learn) > 0:
        to_learn.remove(current_card)
        new_database = pd.DataFrame(to_learn)
        new_database.to_csv("data/to_learn.csv", index=False)
        new_card()
    else:
        messagebox.showinfo(title="Out of Cards", message="There are no cards left.")


def not_know_word():
    if len(to_learn) > 0:
        new_card()
    else:
        messagebox.showinfo(title="Out of Cards", message="There are no cards left.")


def new_card():
    global current_card, active_side
    active_side = 0
    if len(to_learn)!=0:
        current_card = random.choice(to_learn)
        card.itemconfig(card_title, text=languages[0])
        card.itemconfig(card_word, text=current_card[languages[0]])
    else:
        messagebox.showinfo(title="Out of Cards", message="There are no cards left.")



def turn():
    global active_side
    active_side += 1
    card.itemconfig(card_title, text=languages[active_side % 2])
    card.itemconfig(card_word, text=current_card[languages[active_side % 2]])


try:
    data = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")

languages = data.columns
to_learn = data.to_dict(orient="records")

# ---------------------------- UI SETUP ------------------------------- #

root = tk.Tk()
root.title("Flash Cards")
root.geometry("900x1200")
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas with the card image
card = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")
card.create_image(400, 263, image=card_front)
card_title = card.create_text(400, 150, text="title", font=TITLE_FONT)
card_word = card.create_text(400, 263, text="word", font=WORD_FONT)
card.grid(row=0, column=0, columnspan=2)

# Buttons
right = tk.PhotoImage(file="images/right.png")
button_right = tk.Button(image=right, highlightthickness=0, borderwidth=0, command=know_word,
                         activebackground=BACKGROUND_COLOR)
button_right.grid(row=1, column=0)

wrong = tk.PhotoImage(file="images/wrong.png")
button_wrong = tk.Button(image=wrong, highlightthickness=0, borderwidth=0, command=not_know_word,
                         activebackground=BACKGROUND_COLOR)
button_wrong.grid(row=1, column=1)

turn_over = tk.PhotoImage(file="images/button_turn-over.png")
turn = tk.Button(image=turn_over, width=260, height=90, highlightthickness=0, borderwidth=0, command=turn,
                 bg=BACKGROUND_COLOR,
                 activebackground=BACKGROUND_COLOR)
turn.grid(row=2, column=0, columnspan=2)

new_card()
root.mainloop()
