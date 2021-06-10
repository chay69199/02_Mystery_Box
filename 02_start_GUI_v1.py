from tkinter import *
from functools import partial   # To prevent unvanted vindovs
import random


class Converter:
    def __init__(self,parent):

        # GUI to get starting balance and stakes
        self.starts_frame = Frame(padx=10, pady=10)
        self.starts_frame.grid()

        # Mystery Heading(row 0)
        self.mystery_box_label  = Label(self.starts_frame, text="Mystery Box Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        # Initial Instructions (row 1)
        self.mystery_box_label = Label(self.starts_frame, font="Arial 10 italic",
                                        text="please enter a dollar amount "
                                             "(between $5 and $50)in the box "
                                             "below.   Then choose the the "
                                             "stakes.  The higher the stakes, "
                                             "the more you can win!",
                                        wrap=275, justify=LEFT, padx=10, pady=10)
        self.mystery_instructions.grid(row=1)

        # Entry box (row 2)
        self.starts_amount_entry = Entry(self.starts_frame, font="Arial 19 bold")
        self.starts_amount_entry.grid(row=2)

        # button frame (row 3)
        self.starts_frame = Frame(self.starts_frame)
        self.starts_frame.grid(row=3)

        # Buttons go here...
        button_front = "Arial 12 bold"
        # 0range low stakes button...
        self.lowstakes_button = Button(self.starts_frame, text="Low($5)",
                                       command=lambda: self.to_game(1),
                                       font=vutton_font, bg="#FF9933")
        self.lowstakes_button.grid(row=0, column=0, pady=10)

        # Yellow medium stakes button...
        self.lowstakes_button = Button(self.starts_frame, text="Medium ($10)",
                                       command=lambda: self.to_game(2),
                                       font=button_font, bg="#FFF33")
        self.lowstakes_button.grid(row=0, column=1, padx=5, pady=10)

        # Green high stakes button...
        self.lowstakes_button = Button(self.stakes_frame, text="High($15)",
                                       command=lambda: self.to_game(3),
                                       font=button_front, bg="#99FF33")
        self.lowstakes_button.grid(row=0, column=2, pady=10)

        # Help Button
        self.help_button = Button(self.starts_frame, text="How to play",
                                  bg="#808080", fg="white", font=button_front)
        self.help_button.grid(row=4, pady=10)

    def to_game(self, stakes):
        starting_balance = self.starts_amount_entry.get()

        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white (for testing purposes) ...
        self.starts_amount_entry.config(bg="white")
        self.amount_error_label.config(tex="")

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors ="yes"
                error_feedback = "Sorry, the least you " \
                                 "can play with is $5"
            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "Too high! The most you can risk in " \
                                 "this game is $50"
            elif starting_balance < 10 and (stakes == 2 or stakes == 3):
                has_errors ="yes"
                error_feedback = "Sorry, you can only afford to " \
                                 "play a low stakes game."
            elif starting_balance < 15 and low stakes == 3:
                has_errors = "yes"
                error_feedback = "Sorry, you can only afford to " \
                                 "play a low stakes game."

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a dollar amount (no text / decimals)"

        if has_errors == "yes":
            self.starts_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:
            Game(self, stakes, starting_balance)

            # hide start up window
            # root.withdraw()


class Game:
    def __int__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)





