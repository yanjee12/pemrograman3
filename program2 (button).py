import tkinter as tk
from tkinter import messagebox

top = tk.Tk()

def hello_callback():
    messagebox.showwarning("Hello Python", "This is a friendly message.")

button = tk.Button(top, text="Hello", command=hello_callback)
button.pack()  # Add the button to the window

top.mainloop()