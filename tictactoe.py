import tkinter as tk
from tkinter import font

#create the app's main window
window = tk.Tk()
window.title("Tic Tac Toe")

def handle_button_press():
    window.destroy()

button = ttk.Button(text= "Destroy this", command = handle_button_press)
button.pack()

window.mainloop()