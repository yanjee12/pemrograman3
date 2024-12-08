import tkinter as tk
# Create the main window

root = tk.Tk()
root.title("Contoh")  # Set a title for the window

# Create the canvas widget
canvas = tk.Canvas(root, bg="blue", height=250, width=300)
canvas.pack()  # Pack the canvas into the window

# Define coordinates and create the arc
coordinates = (100, 10, 1000, 1000)  # Use a tuple for coordinates
arc_id = canvas.create_arc(coordinates, start=0, extent=150, fill="red")

# Run the main event loop
root.mainloop()