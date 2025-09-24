import tkinter as tk
from tkinter import ttk

# This section creates the Tkinter window and adds the required elements to it
window = tk.Tk()
window.title('Tkinter Text Entry Widget')
window.geometry('400x400')

# This is our entry widget
string_var = tk.StringVar()
Text_entry = ttk.Entry(master = window, textvariable = string_var, font = "Calibri 24 bold")

# Pack elements in frames ready to push onto form/window
Text_entry.pack();

# run the program to generate window with all packed elements for user interaction
window.mainloop()

