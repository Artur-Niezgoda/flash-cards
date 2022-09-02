import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


def new_card():
    random_card = random.choice(to_learn)
    card.itemconfig(card_title, text=languages[0])
    card.itemconfig(card_word, text=random_card[languages[0]])




data = pd.read_csv("data/french_words.csv")
languages = data.columns
to_learn = data.to_dict(orient="records")
print(languages[0])


#-------------------------UI-------------------------------#
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

# labels



# Buttons
right = tk.PhotoImage(file="images/right.png")
button_right = tk.Button(image=right, highlightthickness=0, borderwidth=0, command=new_card)
button_right.grid(row=1, column=0)

wrong = tk.PhotoImage(file="images/wrong.png")
button_wrong = tk.Button(image=wrong, highlightthickness=0, borderwidth=0, command=new_card)
button_wrong.grid(row=1, column=1)


new_card()
root.mainloop()
