import tkinter as tk
import turtle as t

root = tk.Tk()
e = int(input("How many edges should the each arm of the snowflake have? "))
a = int(input("How many arms should the snowflake have? "))
t.speed("slow")
t.pencolor("white")
t.pensize(5)
t.Screen().bgcolor("blue")

def vsnow():
    t.right(30)
    t.forward(60)
    t.backward(60)
    t.left(60)

    t.forward(60)
    t.backward(60)
    t.right(30)
def snowArm():
    for i in range(e):
        t.forward(30)
        vsnow()
    t.backward(e*30) #go back to starting location

#repeat the snowflake arm
def snowf():
    for x in range(a):
        snowArm()
        t.right(360/a)
snowf()

root.mainloop()