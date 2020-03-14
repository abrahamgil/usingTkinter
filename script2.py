from tkinter import *

window=Tk()

def kg_to_pounds():
    pounds = float(e1_value.get())*2.2
    t1.insert(END,pounds)
    print("Did I make it")

b1=Button(window,text="convert",command=kg_to_pounds)
b1.grid(row=0,column=3)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=2)

t0=Text(window,height=1,width=2)
t0.insert(INSERT, "Kg")
t0.grid(row=0,column=0)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=2)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=3)

window.mainloop()