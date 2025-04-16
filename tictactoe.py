import tkinter as tk
# from tkinter import ttk
from tkinter import font

# #create the app's main window
# window = tk.Tk()
# window.title("Tic Tac Toe")

# def handle_button_press():
#     window.destroy()

# button = tk.Button(text= "Destroy this", command = handle_button_press)
# button.pack()

# window.mainloop()

class TicTacToeBoard(tk.Tk): # this class inherits from tk.Tk, making it have all the functionality of tk 
    def __init__(self): # __init__ means initialize
        super().__init__() #calls the superclass, tk.Tk to properly initialize the parent class
        self.title("TITTY TATTY TOE")
        self._cells = {} #initialize an empty dictionary to map the buttons or cells on the game board to corresponding coordinates on grid



