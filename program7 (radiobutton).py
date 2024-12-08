import tkinter as tk
def sel():

    selection = "You selected the option " + str(var.get())
    label.config(text=selection)

root = tk.Tk()

var = tk.IntVar()

R1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
R1.pack(anchor=tk.W)

R2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
R2.pack(anchor=tk.W)

R3 = tk.Radiobutton(root, text="Option 3", variable=var, value=3, command=sel)
R3.pack(anchor=tk.W)

label = tk.Label(root)
label.pack()

root.mainloop()