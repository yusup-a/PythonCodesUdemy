from tkinter import *
from math import *

#GUI which is capable of evaluating any mathematical expression and printing the result.

def evaluate(event):
    res.configure(text="Answer: "+ str(eval(entry.get())))

window = Tk()
Label(window,text="Your Expression:").pack()

entry = Entry(window)
entry.bind("<Return>", evaluate) #as soon as enter is pressed, the function is going to 
entry.pack()

res = Label(window)
res.pack()
window.mainloop()