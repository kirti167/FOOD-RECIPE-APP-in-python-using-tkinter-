import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="momo1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="MOMOS",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t.place(x=2,y=37,height=900,width=800)
quote="""
                                                RECIPE OF MOMOS

Step 1
Mix the refined flour with five tablespoons of water and knead into a stiff
dough. Cover with a damp cloth and set aside for fifteen minutes.

Step 2
For the filling, combine the French beans, carrot, mushrooms, spring onions,
bean sprouts, cashewnuts, ginger, green chilli, peppercorns, soy sauce,
sesame oil, MSG and salt in a large bowl.

Step 3
Divide the dough into sixteen equal portions and roll into small thin discs.
Place a spoonful of the vegetable filling in the centre of each disc and bring
the sides together in the centre, pinching firmly together to form a dumpling.

Step 4
Line a steamer rack with a clean, damp piece of muslin and arrange the momos on
it. Place the rack in the steamer, cover and steam for eight to ten minutes,
until the momos are cooked through.

Step 5
Transfer to a serving plate. Garnish with spring onion greens and serve hot
with Sichuan sauce.



"""
t.insert(tk.END,quote)
t.config(state="disabled")

t1=tk.Text(root,bg='white',fg='black',font="Helvetica 11 bold")
t1.place(x=803,y=37,height=204,width=600)
quote1="""
ABOUT THE DISH:

A plate of hot momos on a cold winter night are one of the most perfect combos
just imagine soft delicate refined flour dumplings filled with a delicious
mix of sautéed vegetables and served piping hot with a spicy dipping sauce.
The best part about momos is that you can play around with everything
right from the filling to the sauce to the shapes. So, it is fun food to prepare
and is extremely delicious to eat – plus healthy and nutritious too!

"""

t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t2.place(x=803,y=238,height=600,width=730)
quote2="""

INGREADIENTS:

-Refined flour 1 cup
-French beans finely chopped 10
-Carrot finely chopped 1 medium
-Fresh button mushrooms finely chopped 4-5
-Spring onions finely chopped 2
-Bean sprouts 1/4 cup
-Cashewnuts chopped 8-10
-Ginger finely chopped 1 inch piece
-Green chilli finely chopped 1
-Black peppercorns crushed 8-10
-Light soy sauce 1/2 tablespoon
-Sesame oil (til oil) 1 teaspoon
-MSG optional 1/4 teaspoon
-Salt to taste
-Spring onion greens chopped 1


"""

t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()
