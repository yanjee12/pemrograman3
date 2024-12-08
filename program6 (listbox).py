import tkinter as tk

top = tk.Tk()

lb1 = tk.Listbox(top)
lb1.insert(1, "Python")
lb1.insert(2, "Perl")
lb1.insert(3, "C")
lb1.insert(4, "PHP")
lb1.insert(5, "JSP")
lb1.insert(6, "Ruby")

lb1.pack()

top.mainloop()