import tkinter as tk

root = tk.Tk()
root.title("Tampilan Gambar")

canvas = tk.Canvas(root, bg="blue", height=250, width=300)

canvas.pack()

image = tk.PhotoImage(file="flowers.gif")

canvas.create_image(150, 150, anchor=tk.CENTER, image=image)

root.mainloop() 