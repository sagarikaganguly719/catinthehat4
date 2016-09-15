from tkinter import *

top=Tk()

w=Canvas(top,relief="sunken",bg="black",height=250,width=300)

coord1=70,50,250,50
coord2=10,50,240,210
coord3=40,20,15,56,200,150
#filename=PhotoImage(file="IMG_20140804_083420.gif")

l1=w.create_line(coord1,fill="white",width="3")
a1=w.create_arc(coord2,fill="red",start=0,extent=30)
p1=w.create_polygon(coord3,fill="yellow")
#i1=w.create_image(50,50,image=filename)

w.pack()
top.mainloop()