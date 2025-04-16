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
        self._create_board_display()
        self._create_board_grid()

    def _create_board_display(self):
        display_frame = tk.Frame(master=self) #creates a Frame object to hold the game board; master set to self means main window is the frame's parent
        display_frame.pack(fill = tk.X) # .pack() is a geometry manager to place the frame object on main window's top border. fill = tk.X ensures frame will fill top width even if window is resized
        self.display = tk.Label( # Label object
            master=display_frame, # setting to master (which is set to display_frame above) means it will be inside frame object
            text = "Let's get Ticcy Tacty",
            font = font.Font(size=28, weight="bold"),
        )
        self.display.pack() #geometry manager to place the label in the frame
    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight='bold'),
                    fg='pink',
                    width=3,
                    height=2,
                    highlightbackground='lightblue',
                )
                self._cells[button] = (row, col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky='nsew'
                )
def main():
    board = TicTacToeBoard()
    board.mainloop()

if __name__ == "__main__":
    main()