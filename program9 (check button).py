import tkinter as tk

root = tk.Tk()

music_var = tk.IntVar(value=0)  
video_var = tk.IntVar(value=0)  

music_checkbox = tk.Checkbutton(root, text="Music", variable=music_var, onvalue=1, offvalue=0, height=5, width=20)
video_checkbox = tk.Checkbutton(root, text="Video", variable=video_var, onvalue=1, offvalue=0, height=10, width=10)

music_checkbox.pack()
video_checkbox.pack()

root.mainloop()