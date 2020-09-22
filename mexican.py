import tkinter
from tkinter import *
from PIL import ImageTk, Image

root=Toplevel()
root.geometry("1400x700+0+0")
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="mexican img2.jpg")
canvas.create_image(0,0, anchor=NW, image=img)


def ebb():
    import easy
b11 = Button(root,text='EASY BBQ BEANS',command=ebb,activebackground='ivory2',bg='black',fg='white',cursor="hand2",width=20,borderwidth=3,font=('bazooka  15  bold '),padx=5,pady=10,relief=RAISED)
b11.place(x=690,y=85)

def fun2():
    import quesadilla
    
b22 = Button(root,text='QUESADILLA PANCAKES',command=fun2,activebackground='ivory2',bg='black',fg='white',cursor="hand2",width=20,borderwidth=3,font=('bazooka 15  bold '),padx=5,pady=10,relief=RAISED)
b22.place(x=690,y=200)
def fun3():
    import sweet
  
b33 = Button(root,text='SWEET POTATO SOUP',command=fun3,activebackground='ivory2',bg='black',fg='white',cursor="hand2",width=20,borderwidth=3,font=('bazooka  15  bold '),padx=5,pady=10,relief=RAISED)
b33.place(x=690,y=315)
def fun4():
    import redrice
    
b44 = Button(root,text=' MAXICAN RED RICE  ',command=fun4,activebackground='ivory2',bg='black',fg='white',cursor="hand2",width=20,borderwidth=3,font=('bazooka  15  bold '),padx=5,pady=10,relief=RAISED)
b44.place(x=690,y=430)
def fun5():
    import salsa
    
b55= Button(root,text='CORN & PEPPER SALSA  ',command=fun5,activebackground='ivory2',bg='black',fg='white',cursor="hand2",width=20,borderwidth=3,font=('bazooka  15 bold '),padx=5,pady=10,relief=RAISED)
b55.place(x=690,y=545)    

root.mainloop()
