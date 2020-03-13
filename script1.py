from tkinter import *

#creates first window where all buttons and widgets will exists
window=Tk()

def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END,miles)

#actually puts button in window
#b1.pack()
#grid method gives us more control of widgets unlike pack
#command value needs to have a function but dont put the paranthesis
b1=Button(window,text="Execute",command=km_to_miles)
b1.grid(row=0,column=0)



#Entry gives us text fields for input
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

#Text gives us text field as well with height and width
t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

#this is always necessary when creating new window otherwise it will insta-close without it
window.mainloop() 