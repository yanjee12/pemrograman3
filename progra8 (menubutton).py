import tkinter as tk

root = tk.Tk()

mb = tk.Menubutton(root, text="Condiments", relief=tk.RAISED)
mb.grid()

menu = tk.Menu(mb, tearoff=1)
mb["menu"] = menu

mayoVar = tk.IntVar()
ketchVar = tk.IntVar()

menu.add_checkbutton(label="Mayo", variable=mayoVar)
menu.add_checkbutton(label="Ketchup", variable=ketchVar)

root.mainloop()