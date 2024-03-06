import tkinter as tk
import turtle

root = tk.Tk()

def rect(h,v,c):
    turtle.pendown() #put the pen down to start drawing
    turtle.pensize(2)

    turtle.color(c)
    turtle.begin_fill()

    for i in range(1,3):
        turtle.forward(h)
        turtle.left(90)
        turtle.forward(v)
        turtle.left(90)
    
    turtle.end_fill()
    turtle.penup() #pull pen up to stop drawing
    turtle.speed("slow")

rect(50,15,'blue')
root.mainloop()