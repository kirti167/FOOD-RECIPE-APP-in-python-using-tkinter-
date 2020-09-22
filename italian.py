import tkinter
from tkinter import *
from PIL import ImageTk, Image

root=Toplevel()
root.geometry("1400x700+0+0")
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="italian.jpg")
canvas.create_image(0,0, anchor=NW, image=img)
def msp():
    import mixpasta

b11 = Button(root,text='MIXED SAUCE PASTA  ',command=msp,activebackground='ivory2',bg='chartreuse3',fg='white',cursor="hand2",width=18,borderwidth=3,font=('bazooka  15  bold '),padx=5,pady=10,relief=RAISED)
b11.place(x=390,y=85)
def mp():
    import pizza

b22 = Button(root,text=' MARGHERITA PIZZA ',command=mp,activebackground='ivory2',bg='chartreuse3',fg='white',cursor="hand2",width=18,borderwidth=3,font=('bazooka 15  bold '),padx=5,pady=10,relief=RAISED)
b22.place(x=390,y=200)
def mr():
    import risotto
    
b33 = Button(root,text=' MUSHROOM RISOTTO ',command=mr,activebackground='ivory2',bg='chartreuse3',fg='white',cursor="hand2",width=18,borderwidth=3,font=('bazooka  15  bold '),padx=5,pady=10,relief=RAISED)
b33.place(x=390,y=315)
def las():
    import lasagna
    
b44 = Button(root,text=' LASAGNA ',command=las,activebackground='ivory2',bg='chartreuse3',fg='white',width=18,cursor="hand2",borderwidth=3,font=('bazooka  15  bold '),padx=5,pady=10,relief=RAISED)
b44.place(x=390,y=430)
def gb():
    import garlicbread
    
b55= Button(root,text=' GARLIC BREAD  ',command=gb,activebackground='ivory2',bg='chartreuse3',fg='white',cursor="hand2",width=18,borderwidth=3,font=('bazooka  15 bold '),padx=5,pady=10,relief=RAISED)
b55.place(x=390,y=545)    

root.mainloop()
