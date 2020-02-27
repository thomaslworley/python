import tkinter as tk

#canvas = Canvas(root,width=750,height=750)

points = 0
def write_slogan():
    global points
    points += 1
    print(points)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

slogan = tk.Button(frame,
                   text="Points",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)


#canvas.create_window(300, 600, width=150,height=50,anchor=NW, window=points)

root.mainloop()