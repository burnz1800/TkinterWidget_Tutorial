import tkinter as tk 
from tkinter import ttk

# This section creates the Tkinter window and adds the required elements to it

window = tk.Tk()
window.title('Tkinter Text Entry Widget')
window.geometry('400x400')

# button - when pressed runs the function that calculates the Grade "get_grade()"
button_1 =ttk.Button(master = window, text = "BUTTON 1", command = get_button1_text) 
button_2 =ttk.Button(master = window, text = "BUTTON 2", command = get_button2_text) 

#output label
output_string = tk.StringVar()
output_label = ttk.Label(master = window, textvariable=output_string)

