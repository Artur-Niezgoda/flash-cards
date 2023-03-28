import tkinter as tk
import pandas as pd
import random
from tkinter import messagebox

# Constants
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# Global variables
current_card = {}
active_side = 0

def know_word():
    """Callback function for when the user knows the word on the flash card."""
    if len(to_learn) > 0:
        # Remove the current card from the "to_learn" list.
        to_learn.remove(current_card)
        # Create a new pandas DataFrame with the remaining cards and save it to a CSV file.
        new_database = pd.DataFrame(to_learn)
        new_database.to_csv("data/to_learn.csv", index=False)
        # Show a new flash card.
        new_card()
    else:
        # Show a message box informing the user that there are no more cards left.
        messagebox.showinfo(title="Out of Cards", message="There are no cards left.")


def not_know_word():
    """Callback function for when the user does not know the word on the flash card."""
    if len(to_learn) > 0:
        # Show a new flash card.
        new_card()
    else:
        # Show a message box informing the user that there are no more cards left.
        messagebox.showinfo(title="Out of Cards", message="There are no cards left.")


def new_card():
    """Show a new flash card."""
    global current_card, active_side
    # Reset the active side to the front of the card.
    active_side = 0
    if len(to_learn)!=0:
        # Choose a random card from the "to_learn" list and display its front side.
        current_card = random.choice(to_learn)
        card.itemconfig(card_title, text=languages[0])
        card.itemconfig(card_word, text=current_card[languages[0]])
    else:
        # Show a message box informing the user that there are no more cards left.
        messagebox.showinfo(title="Out of Cards", message="There are no cards left.")


def turn_card():
    """Flip the flash card over to the other side."""
    global active_side
    # Increment the active side (0 for front, 1 for back).
    active_side += 1
    # Switch the image of the card to the front or back depending on the active side.
    card.itemconfig(card_image, image=[card_front, card_back][active_side % 2])
    # Switch the title and word text depending on the active side.
    card.itemconfig(card_title, text=languages[active_side % 2])
    card.itemconfig(card_word, text=current_card[languages[active_side % 2]])

try:
    # Try to read the "to_learn.csv" file as a pandas DataFrame.
    data = pd.read_csv("data/to_learn.csv")
except (FileNotFoundError, pd.errors.EmptyDataError):
    # If the file does not exist or is empty, read the "french_words.csv" file instead.
    data = pd.read_csv("data/french_words.csv")

# Get the column names (languages) and create a list of dictionaries with the card data.
languages = data.columns
to_learn = data.to_dict(orient="records")

# Create the root window
root = tk.Tk()

# Set the title and size of the window, and the background color and padding
root.title("Flash Cards")
root.geometry("900x1200")
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Create a canvas to display the card image
card = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

# Load the front and back card images
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")

# Display the front card image on the canvas, along with the card title and word
card_image = card.create_image(400, 263, image=card_front)
card_title = card.create_text(400, 150, text="title", font=TITLE_FONT)
card_word = card.create_text(400, 263, text="word", font=WORD_FONT)

# Place the card canvas in the root window
card.grid(row=0, column=0, columnspan=2)

# -------------------------------------- BUTTONS -------------------------------------- #

# Load and create the "right" button, which marks the card as known
right = tk.PhotoImage(file="images/right.png")
button_right = tk.Button(image=right, highlightthickness=0, borderwidth=0, command=know_word,
                         activebackground=BACKGROUND_COLOR)
button_right.grid(row=1, column=0)

# Load and create the "wrong" button, which marks the card as unknown
wrong = tk.PhotoImage(file="images/wrong.png")
button_wrong = tk.Button(image=wrong, highlightthickness=0, borderwidth=0, command=not_know_word,
                         activebackground=BACKGROUND_COLOR)
button_wrong.grid(row=1, column=1)

# Load and create the "turn over" button, which flips the card over
turn_over = tk.PhotoImage(file="images/button_turn-over.png")
turn = tk.Button(image=turn_over, width=260, height=90, highlightthickness=0, borderwidth=0, command=turn_card,
                 bg=BACKGROUND_COLOR,
                 activebackground=BACKGROUND_COLOR)
turn.grid(row=2, column=0, columnspan=2)

# Display the first card on the canvas
new_card()

# Start the main event loop to display the window
root.mainloop()
