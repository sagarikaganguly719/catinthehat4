from tkinter import *
from tkinter import messagebox

top=Tk()

cv1=IntVar()
cv2=IntVar()

c1=Checkbutton(top,text="Love",variable=cv1,height="5",onvalue=1,offvalue=0,width="20")
c2=Checkbutton(top,text="War",variable=cv2,height="5",onvalue=1,offvalue=0,width="20")

'''if(cv2==0):
    else:
        messagebox.showinfo("Lulu","Love")
if(cv1==0):
    return
else:
    messagebox.showinfo("Wuwu","War")
if(cv1==1 and cv2==1):
    return
else:
    messagebox.showinfo("bleh","none were selected")'''

b1=Button(top,text="Ok",bg="yellow",fg="black",command=lovewar)

c1.pack()
c2.pack()
b1.pack()
top.mainloop()
