import tkinter

window=tkinter.Tk() #tkinter works by starting a tcl/tk interpreter under the covers,
#creating an instance of Tk intializes this interpreter and creates the root window
window.title("My GUI")

#Create a label
tkinter.Label(window,text="Enter text: ").grid(row=0,column=0)

#Create text entry box
entry = tkinter.Entry(window, width=20, bg="pink")
entry.grid(row=1,column=0)

#checkbutton
tkinter.Checkbutton(window,text="Checkbutton 1").grid(row=3,column=0)
tkinter.Checkbutton(window,text="Checkbutton 2").grid(row=4,column=0)

#scale bar
tkinter.Scale(window,from_=0, to = 100, orient=tkinter.HORIZONTAL).grid(row=4,column=1)

#canvas, space for drawing
tkinter.Canvas(window,bg="red",width=150,height=100).grid(row=4,column=2)

window.mainloop()