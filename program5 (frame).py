import tkinter as tk

root = tk.Tk()

button_frame = tk.Frame(root)
button_frame.pack()

red_button = tk.Button(button_frame, text="Red", fg="red")
red_button.pack(side=tk.LEFT)

green_button = tk.Button(button_frame, text="Brown", fg="brown")
green_button.pack(side=tk.LEFT)

blue_button = tk.Button(button_frame, text="Blue", fg="blue")
blue_button.pack(side=tk.LEFT)

black_button = tk.Button(button_frame, text="Black", fg="black")
black_button.pack(side=tk.BOTTOM)

root.mainloop()