from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=1)

        # Entry box... (row 1)
        self.start_amount_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.start_amount_entry.grid(row=2)

        # Play Button (row 2)
        self.lowstakes_button = Button(text="Low ($5)",
                                       command=lambda: self.to_game(1))
        self.lowstakes_button.grid(row=2, pady=10)

    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()
        Game(self, stakes, starting_balance)


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # disable low stakes button
        partner.lowstakes_button.config(state=DISABLED)

        # initialise variables
        self.balance = IntVar()

        # Set starting balance to amount entered by user at start of game
        self.balance = IntVar()

        # Set starting balance to amount entered byy user at start of game
        self.balance.get(starting_balance)

        # CUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Rov
        self.heading_label = Label(self.game_frame, text="Heading",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Balance Label
        self.balance_label = Label(self.game_frame, text="Balance...")
        self.balance_label.grid(row=2)

        self.play_button = Button(self.gamne_frame, text="Gain")
                                padx=10, pady=10, command=self.reveal_boxes
        self.paly_button.grid(row=3)

    def reveal_boxes(self):
        # retrieve the balance from the initial function...
        current_balance= self.balance.get()

        # Adjust the balance (subtract game cost and add pay out)
        # For testing purposes, just add 2
        cureent_balance += 2

        # Set balance to adjusted balance
        self.balance.set(cureent_balance)

        # Edit label so user can see their balance
        self.balance_label.configure(text="Balance: ()".format(cureent_balance))

# main routine
if  _name_  ==" main ":
    root=TK()

