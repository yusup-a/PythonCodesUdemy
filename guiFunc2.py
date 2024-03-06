from tkinter import *

#converts fahrenheit to celsius and kelvin
def convert_f():
    words = fText.get() # gets input from entry box
    fTemp = float(words) #converts string to float
    cBox.delete(0, END)
    cBox.insert(0,'%.2f'% (toC(fTemp))) #inserts celsius equivalent
    kBox.delete(0, END)
    kBox.insert(0, '%.2f'% (toK(toC(fTemp))))
    return

#converts celsius to fahrenheit and kelvin
def convert_c():
    words = cText.get() # gets input from entry box
    cTemp = float(words) #converts string to float
    fBox.delete(0, END)
    fBox.insert(0,'%.2f'% (toF(cTemp))) #inserts celsius equivalent
    kBox.delete(0, END)
    kBox.insert(0, '%.2f'% (toK(cTemp)))
    return

#converts kelvin to celsius and fahrenheit
def convert_k():
    words = kText.get() # gets input from entry box
    kTemp = float(words) #converts string to float
    cBox.delete(0, END)
    cBox.insert(0,'%.2f'% (KtoC(kTemp))) #inserts celsius equivalent
    fBox.delete(0, END)
    fBox.insert(0, '%.2f'% (toF(KtoC(kTemp))))
    return


def toC(f): #converts fahrenheit to celsius
    return(f-32) * 5.0 / 9.0
def toF(c): #converts celsius to fahrenheit
    return c * 9.0 / 5.0 + 32
def KtoC(k): #converts kelvin to celsius
    return k - 273.15
def toK(c): #converts celsius to kelvin
    return c + 273.15

#main
w=Tk() #tkinter works by starting a tcl/tk interpreter under the covers,
#Creating an instance of Tk initializes this interpreter and creates the root window
w.title("My Temperature Converter")

fLabel= Label(w,text="Fahrenheit")
fLabel.grid(row=0, column=0,padx=5,pady=5,sticky =E) #E = east

cLabel= Label(w,text="Celsius")
cLabel.grid(row=1, column=0,padx=5,pady=5,sticky =E)

kLabel= Label(w,text="Kelvin")
kLabel.grid(row=2, column=0,padx=5,pady=5,sticky =E)

#Horizontally adjacent text entry boxes
fText = StringVar()
fText.set("")
fBox = Entry(w,textvariable=fText)
fBox.grid(row=0,column=1,padx=5,pady=5)

cText = StringVar()
cText.set("")
cBox = Entry(w,textvariable=cText)
cBox.grid(row=1,column=1,padx=5,pady=5)

kText = StringVar()
kText.set("")
kBox = Entry(w,textvariable=kText)
kBox.grid(row=2,column=1,padx=5,pady=5)

#Go button & functionality
fGoButton = Button(w,text="Go", command= convert_f)
fGoButton.grid(row=0, column=2, padx=5,pady=5, sticky= N+S+E+W)

cGoButton = Button(w,text="Go", command= convert_c)
cGoButton.grid(row=1, column=2, padx=5,pady=5, sticky= N+S+E+W)

kGoButton = Button(w,text="Go", command= convert_k)
kGoButton.grid(row=2, column=2, padx=5,pady=5, sticky= N+S+E+W)

#Exit button
exitButton = Button(w,text="Exit",command = quit) #quit means to close the program
exitButton.grid(row=3,column=0,padx=5,pady=5,sticky= N+S+E+W,columnspan=3)
#columnspan is used to let a widget span more than one column
#N+S+E+W means that the widget should be expanded in both directions
w.mainloop()