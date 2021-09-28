# importing tkinter
import tkinter as tk

def one():
  movie_func.insert(input())

# create root window
root = tk.Tk()
 
# root window title and dimension
root.title("Film Catcher")
root.geometry("380x400")
 
# creating button
btn = tk.Button(root, text="Press", command=lambda: function.one())
btn.pack()
 
# running the main loop
root.mainloop()