import tkinter
from tkinter import *
from PIL import ImageTk, Image

root=Toplevel()
root.geometry("1400x700+0+0")
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="chineese.jpg")
canvas.create_image(0,0, anchor=NW, image=img)

def man():
    import manchurian
b11 = Button(root,text='MANCHURIAN ',command=man,activebackground='ivory2',bg='black',fg='white',width=13,cursor="hand2",borderwidth=3,font=('bazooka  16  bold '),padx=5,pady=10,relief=RAISED)
b11.place(x=140,y=520)
def noo():
    import noodles

b22 = Button(root,text=' NOODLES',command=noo,activebackground='ivory2',bg='black',fg='white',width=13,cursor="hand2",borderwidth=3,font=('bazooka 16  bold '),padx=5,pady=10,relief=RAISED)
b22.place(x=380,y=520)
def mo():
    import momos
b33 = Button(root,text='MOMOS  ',command=mo,activebackground='ivory2',bg='black',fg='white',width=13,cursor="hand2",borderwidth=3,font=('bazooka  16  bold '),padx=5,pady=10,relief=RAISED)
b33.place(x=630,y=520)
def chi():
    import chilipotato

b44 = Button(root,text=' CHILLI POTATO  ',command=chi,activebackground='ivory2',bg='black',fg='white',cursor="hand2",width=13,borderwidth=3,font=('bazooka  16  bold '),padx=5,pady=10,relief=RAISED)
b44.place(x=870,y=520)
def spri():
    import springroll

b55= Button(root,text=' SPRING ROLL  ',command=spri,activebackground='ivory2',bg='black',fg='white',cursor="hand2",width=13,borderwidth=3,font=('bazooka  16 bold '),padx=5,pady=10,relief=RAISED)
b55.place(x=1090,y=520)    

root.mainloop()
