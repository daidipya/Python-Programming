#!/usr/bin/python

from Tkinter import *
top = Tk(className="First GUI")
foo = Label(top,text="This is just a label!!!")
foo.pack()

def act():
    print "Button pressed!!!"
f1 = Button(top,text="Press ME",command=act)
f1.pack()

str = StringVar()
inputbox = Entry(top,textvariable=str)
inputbox.pack()
def act1():
    print "you entered %s" % str.get()
btn1 = Button(top,text="Get Me", command=act1)
btn1.pack()





top.mainloop()


