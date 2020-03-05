import tkinter as tk
from tkinter import * 
from tkinter.ttk import *

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

global points
global uplvl

uplvl = 0
points = 0
pointer = tk.Label(root, text=points)
pointer.pack()

def ps():
    global points
    points += 1
    pointer['text'] = str(points)

click = tk.Button(frame,
                   text = 'Points',
                   command=ps)
click.pack(side=tk.LEFT)

def pup():
    global points
    pointer['text'] = str(points)
    pointer.after(1000, pup)
    points += 10

def upgrade():
    global points
    global uplvl
    if uplvl == 0:
        uplvl += 1 
        points -= 10
        pup()

upgrade1 = tk.Button(frame, text = 'Upgrade', command=upgrade)
upgrade1.pack(side=tk.RIGHT)


root.mainloop()