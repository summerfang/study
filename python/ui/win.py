import tkinter as tk
#import Tkinter as tk  # for python 2
    
def create_window():
    window = tk.Toplevel(root)

root = tk.Tk()
b = tk.Button(root, text="Create new window", command=create_window)
b.pack()

root.mainloop()