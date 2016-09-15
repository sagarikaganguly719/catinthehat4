
from tkinter import *
from tkinter import messagebox

top=Tk()
def helloCallBack():
    messagebox.showinfo("Hello world","hello")

r=Button(top,text="red",fg="white",relief="raised",bg="red",width="5",command=helloCallBack)
b=Button(top,text="blue",fg="white",relief="raised",bg="blue",width="5",command=helloCallBack)
g=Button(top,text="green",fg="white",relief="raised",bg="green",width="5")
y=Button(top,text="yellow",relief="raised",bg="yellow",width="5")
r.pack(side="left")
b.pack(side="left")
g.pack(side="left")
y.pack(side="left")
top.mainloop()


















