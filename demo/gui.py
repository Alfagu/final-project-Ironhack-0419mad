import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import time

root = Tk()

#### CENTER THE WINDOW
# Gets the requested values of the height and widht.
rootWidth = root.winfo_reqwidth()
rootHeight = root.winfo_reqheight()
print("Width",rootWidth,"Height",rootHeight)
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - rootWidth/2)
positionDown = int(root.winfo_screenheight()/2 - rootHeight/2)
 
# Positions the window in the center of the page.
root.title("FilmFounder")
root.geometry("+{}+{}".format(positionRight, positionDown))

#### FUNCTIONS FOR BUTTONS
# We are going to make 2 function to the same button.
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

# Button and action of the progressBar.
def clicked():
    lbl.configure(text="Searching")
    progressBar['maximum'] = 100
    for i in range(101):
        time.sleep(0.02)
        progressBar["value"] = i
        progressBar.update()
        progressBar["value"] = 0  
        
#### Function for entry fields
def save_entry_fields():
    var_1 = e1.get()
    var_2 = e2.get()
    #print("Genre: %s\nDate: %s" % (e1.get(), e2.get()))

        
# cofigurations of the differents features.        
lbl = Label(root, text="Insert Genre/Movie or Date")
lbl.grid(row=0, column=2)

tk.Label(root, text="Genre").grid(row=1, column=1)
tk.Label(root, text="Date").grid(row=2, column=1)

e1 = tk.Entry()
e2 = tk.Entry()

e1.grid(row=1, 
        column=2)
e2.grid(row=2, 
        column=2)

tk.Button(root, text='Search', command = combine_funcs(clicked, save_entry_fields)).grid(row=3, 
                                                               column=2, 
                                                               sticky=tk.W, 
                                                               pady=4)

progressBar = ttk.Progressbar(root, orient='horizontal', length=200, mode="determinate")
progressBar.grid(column=2, row = 4, pady=10)

root.mainloop()