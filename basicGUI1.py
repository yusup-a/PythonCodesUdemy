import tkinter

window=tkinter.Tk()

window.title("My coding")

button = tkinter.Button(window,text="Hi",width=40)
button.pack(padx=20,pady=20)

clickNo=0 #count the number of clicks, starts with 0
def onClick(event):
    global clickNo #global allows functio to use the prior variable that we created
    clickNo = clickNo+1 #each time we click, computer adds 1 to counter
    if clickNo == 1:
        button.configure(text="Click 1") #configure button widget according to () text
    elif clickNo == 2:
        button.configure(text="Click 2")
    else:
        button.pack_forget() #delete button
button.bind("<ButtonRelease-1>",onClick)
#bind binds the widget (button) to function above
window.mainloop()