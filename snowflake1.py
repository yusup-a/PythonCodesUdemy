import tkinter as tk
import turtle as t

root = tk.Tk()

t.speed("slow")
t.pencolor("white")
t.pensize(10)
t.Screen().bgcolor("blue")

def vsnow():
    t.right(30)
    t.forward(60)
    t.backward(60)
    t.left(60)

    t.forward(60)
    t.backward(60)
    t.right(30)

for i in range(4):
    t.forward(30)
    vsnow()
    t.backward(120)

root.mainloop()