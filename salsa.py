import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="corn-salsa1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="CORN & PEPPER SALSA",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 24 bold")
t.place(x=2,y=37,height=900,width=800)
quote="""
                    RECIPE OF CORN & PEPPER SALSA
STEP1
Stir the corn, orange bell pepper, jalapeno pepper,
red onion,cilantro, lime juice, crushed red pepper,
honey, salt,and pepper together in a bowl.
STEP2
Chill until ready to serve.                                   

                                 
"""
t.insert(tk.END,quote)
t.config(state="disabled")
t1=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t1.place(x=803,y=37,height=204,width=620)
quote1="""
ABOUT THE DISH
Corn Red Pepper Salsa made easy! Veggies drizzled with honey
for a sweet,crunchy salsa for chips or garnish for spicy dishes.
This salsa is versatile andcan be made to suit your tastes.
"""
t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 18 bold")
t2.place(x=803,y=238,height=600,width=730)
quote2="""
INGREDIENTS
-1 (15.25 ounce) can sweet corn, drained
-1 orange bell pepper, chopped
-1 jalapeno pepper, seeded and minced
-1 red onion, chopped
-1 tablespoon chopped fresh cilantro, or more to taste
-1 tablespoon fresh lime juice, or to taste
-½ teaspoon crushed red pepper
-1 teaspoon honey
-salt and black pepper to taste"""
t2.insert(tk.END,quote2)
t2.config(state="disabled")


tk.mainloop()
