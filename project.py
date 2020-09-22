import tkinter
from tkinter import *
from PIL import ImageTk, Image


win = Toplevel()


win.geometry('1400x1400')
canvas = Canvas(win, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="cook.jpg")
canvas.create_image(0,0, anchor=NW, image=img)

l1 = Label(win,text = " LETS COOK WITH HK",bd = 12,relief = GROOVE,fg = 'white',bg = 'black',font=("times new roman",30,"bold"),pady = 1, width=20)
l1.place(x=860,y=10)
def ind_food():
    import indian

b1 = Button(win,text=' INDIAN FOOD ',command=ind_food,activebackground='ivory2',bg='black',fg='white',cursor="hand2",width=17,borderwidth=3,font='bazooka  15  bold ',padx=5,pady=10,relief='raised')
b1.place(x=1000,y=120)
def it_food():
    import italian
b2 = Button(win,text=' ITALIAN FOOD',command=it_food,activebackground='ivory2',bg='black',fg='white',cursor="hand2",width=17,borderwidth=3,font='bazooka  15  bold ',padx=5,pady=10,relief='raised')
b2.place(x=1000,y=210)
def ch_food():
    import chinese
b3 = Button(win,text=' CHINESE FOOD',command=ch_food,activebackground='ivory2',bg='black',fg='white',cursor="hand2",width=17,borderwidth=3,font='bazooka  15  bold ',padx=5,pady=10,relief='raised')
b3.place(x=1000,y=300)

def mexic_food():
    import mexican

b4 = Button(win,text=' MEXICAN FOOD',command=mexic_food,activebackground='ivory2',bg='black',fg='white',cursor="hand2",width=17,borderwidth=3,font='bazooka  15  bold ',padx=5,pady=10,relief='raised')
b4.place(x=1000,y=390)

win.mainloop()
