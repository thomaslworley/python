import tkinter as tk
from tkinter import Canvas, NW, Button

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("Epic Fortnite Clicker ROLAYE")

canvas = Canvas(root,width=750,height=750)
canvas.grid()
canvas.focus_set()
#cookie = canvas.create_oval(200,200,500,500,fill = 'white')
font = tkFont.Font(size=32)
tit = canvas.create_text(375,50,text = "Clicker Money",font = font)

total_list=[]

#def drawChips(event):
#    global total_list
#    total_list.append(repr(event.char))
#    canvas.create_oval(event.x, event.y,
#        event.x+30, event.y+35, fill='brown')

#def drawgreenSprink(event):
#    global total_list
#    total_list.append(repr(event.char))
#    canvas.create_rectangle(event.x, event.y,
#        event.x+5, event.y+15, fill='green')
        

#bind keyboard press event to event handler
#canvas.bind('c',drawChips)
#canvas.bind('g',drawgreenSprink)        

cookieText = canvas.create_text(300,550,text='Click to gain points',anchor=NW)                

points = 0
def write_slogan():
    global points
    points += 1
    print(points)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

points = tk.Button(frame,
                   text="Points",
                   command=write_slogan)
points.pack(side=tk.LEFT)
#canvas.create_window(300, 600, width=150,height=50,anchor=NW, window=points)

myText = canvas.create_text(50,75,text='0', anchor= NW)

root.mainloop()