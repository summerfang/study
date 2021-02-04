import tkinter as tk
from typing import Text

def click():
    txt=word.get()
    greeting.config(text=txt)

def close():
    window.attributes('-alpha', 1)
    win2.attributes('-alpha',0)

def another():
    window.attributes('-alpha', 0)
    win2.attributes('-alpha', 1)
    win2.mainloop()

window = tk.Tk()
greeting = tk.Label(text="HelloWorld")
greeting.pack()
btn = tk.Button(text="Click me", command=click)
btn.pack()
word = tk.Entry()
word.pack()
other = tk.Button(text="Another windows", command=another)
other.pack()

win2 = tk.Tk()
win2.attributes('-alpha',0)
btn1 = tk.Button(win2, text="close", command=close)
btn1.pack()

window.mainloop()

