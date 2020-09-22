import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

win1 = Tk()
win1.geometry("1350x700+0+0") 
canvas = Canvas(win1, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="picture1.jpg")
canvas.create_image(0,0, anchor=NW, image=img)

def register():
    root = Toplevel(win1)
    root.title("REGISTER HERE")
    root.geometry('1700x1700')
    root.config(bg="cadet blue")
    left_label=Label(root,bg="powder blue")
    left_label.place(x=0,y=0,relheight=1,width=700)

    f1 = Frame(root,bd=10,bg='white')
    f1.place(x=350,y=30,width=700,height=640)
    label = Label(f1,text='REGISTERATION FORM',font=("times new roman",18),bg='dark turquoise',fg='black')
    label.place(x=200,y=10)
    
    l1 = Label(f1,text='FIRST NAME',font=("times new roman",15,"bold"),bd=4,padx=5,pady=5,bg='dark turquoise',fg='black',width=17)
    l1.place(x=60,y=70)
    e1 = Entry(f1,width=19,font="arial 15",bd=4,relief=SUNKEN)
    e1.place(x=60,y=120)
    
    l2 = Label(f1,text='LAST NAME',font=("times new roman",15,"bold"),bd=4,padx=5,pady=5,bg='dark turquoise',fg='black',width=17)
    l2.place(x=400,y=70)
    e2 = Entry(f1,width=19,font="arial 15",bd=4,relief=SUNKEN)
    e2.place(x=400,y=120)

    l3 = Label(f1,text=' CONTACT ',font=("times new roman",15,"bold"),bd=4,padx=5,pady=5,bg='dark turquoise',fg='black',width=17)
    l3.place(x=60,y=170)
    e3 = Entry(f1,width=19,font="arial 15",bd=4,relief=SUNKEN)
    e3.place(x=60,y=220)
    
    l4 = Label(f1,text='EMAIL-ID ',font=("times new roman",15,"bold"),bd=4,padx=5,pady=5,bg='dark turquoise',fg='black',width=17)
    l4.place(x=400,y=170)
    e4 = Entry(f1,width=19,font="arial 15",validate="key",bd=4,relief=SUNKEN)
    e4.place(x=400,y=220)
    
    l5 = Label(f1,text='   AGE   ',font=("times new roman",15,"bold"),bd=4,padx=5,pady=5,bg='dark turquoise',fg='black',width=17)
    l5.place(x=60,y=270)
    e5 = Entry(f1,width=19,font="arial 15",bd=4,relief=SUNKEN)
    e5.place(x=60,y=320)

    l6 = Label(f1,text='  GENDER ',font=("times new roman",15,"bold"),bd=4,padx=5,pady=5,bg='dark turquoise',fg='black',width=17)
    l6.place(x=400,y=270)
    cmb = ttk.Combobox(f1,font=("arial",14),state='readonly',justify=CENTER)
    cmb['values']=("Select","MALE","FEMALE")
    cmb.place(x=400,y=320)
    cmb.current(0)
    

    l7 = Label(f1,text=' PASSWORD',font=("times new roman",15,"bold"),bd=4,padx=5,pady=5,bg='dark turquoise',fg='black',width=17)
    l7.place(x=60,y=370)
    e7 = Entry(f1,width=19,font="arial 15",show="*",bd=4,relief=SUNKEN)
    e7.place(x=60,y=420)

    l8 = Label(f1,text='CONFIRM PASSWORD',font=("times new roman",15,"bold"),bd=4,padx=5,pady=5,bg='dark turquoise',fg='black',width=17)
    l8.place(x=400,y=370)
    e8 = Entry(f1,width=19,font="arial 15",show="*",bd=4,relief=SUNKEN)
    e8.place(x=400,y=420)

    chk = IntVar()
    cb = Checkbutton(f1, text='I Agree The Terms & Conditions',variable=chk,offvalue=0,onvalue=1,bd=3,bg='white')
    cb.place(x=60,y=460)

    def clear():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
    def register_data():
        if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or cmb.get()=="SELECT" or e7.get()=="" or e8.get()=="":
            messagebox.showerror("Error","All fields are required",parent=root)
        elif e7.get()!=e8.get():
            messagebox.showerror("Error","Password must be same",parent=root)
        elif chk.get()==0:
            messagebox.showerror("Error","Please Agree out terms and conditions",parent=root)
        else :
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="project")
                cur=con.cursor()
                cur.execute("select * from project1 where l4=%s",e4.get())
                row = cur.fetchone()
                #print(row)
                if row!=None:
                     messagebox.showerror("Error","User already Exist,Please try with another Email",parent=root)
                else:
                    cur.execute("insert into project1 (l1,l2,l3,l4,l5,l6,l7,l8) values (%s,%s,%s,%s,%s,%s,%s,%s)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),cmb.get(),e7.get(),e8.get()))
                con.commit()
                con.close()
                messagebox.showerror("Congrats!!!","Register Successful",parent=root)
                import project
                
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)
                
                
    but1 = Button(f1,text='Click here to register',font=("times new roman",18),cursor="hand2",fg='black',bg='dark turquoise',width=18,command=register_data)
    but1.place(x=200,y=520)
    
def login():
    new1 = Toplevel(win1)
    new1.title("login here")
    new1.geometry('1700x1700')
    new1.configure(bg="powder blue")
    lbltitle=Label(new1,text="LET'S COOK WITH HK",font=('arial',50,"bold"),bg="cadet blue",fg='black')
    lbltitle.pack(fill=X)
    
    l1=Label(new1,text="USERNAME",font=("times new roman",20,"bold"),bd=4,padx=10,pady=5,bg='cadet blue',fg='cornsilk',width=20)
    l1.place(x=330,y=240)
    l1_entry = Entry(new1,width=20,font="arial 20",bd=7,relief=SUNKEN)
    l1_entry.place(x=730,y=240)
    l2=Label(new1,text="PASSWORD",font=("times new roman",20,"bold"),bd=4,padx=10,pady=5,bg='cadet blue',fg='cornsilk',width=20)
    l2.place(x=330,y=300)
    l2_entry = Entry(new1,width=20, font="arial 20",show="*",bd=7,relief=SUNKEN)
    l2_entry.place(x=730,y=300)
    
    def login_data():
        if l1_entry.get()=="" or l2_entry.get()=="":
            messagebox.showerror("Error","All fields are required",parent=new1)
        else :
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="project")
                cur=con.cursor()
                cur.execute("select * from project1 where l4=%s and l7=%s",(l1_entry.get(),l2_entry.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username or Password",parent=new1)
                else:
                    messagebox.showinfo("SUCCESS!!!","Welcome",parent=new1)
                    import project
                con.close()    
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=new1)

    

    blogin=Button(new1,text="Login",command=login_data,font=("times new roman",20,"bold"),cursor="hand2",bd=4,padx=10,pady=3,width=8)
    blogin.place(x=620,y=400)
   
b1 = Button(win1, text='REGISTER',font=("times new roman",20,"bold"),bd=4,fg='white',cursor="hand2",bg='black',padx=10,pady=10,command=register)
b1.place(x=340,y=250)

b2 = Button(win1, text='  LOGIN ',width=10,font=("times new roman",20,"bold"),bd=4,fg='white',cursor="hand2",bg='black',padx=10,pady=10,command=login)
b2.place(x=340,y=400)

win1.mainloop()
