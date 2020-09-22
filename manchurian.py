import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="manch1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="MANCHURIAN",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 13 bold")
t.place(x=2,y=37,height=900,width=800)
quote="""
                                                RECIPE OF MANCHURIAN

Step 1
Mix three tablespoons of cornflour in one cup of water. Reserve spring onion
greens for garnish. Mix cabbage, carrot and French beans in a bowl and
thoroughly rub in one teaspoon of salt.

Step 2
Add spring onion, capsicum, refined flour and one-fourth cup of cornflour.
Mix thoroughly. Shape into lemon sized balls.

Step 3
Heat sufficient oil in a wok and deep-fry vegetable balls in small batches
for three to four minutes on medium heat or until golden brown. Drain on
absorbent paper.

Step 4
Heat two tablespoons of oil in a wok or a pan and stir fry the ginger and
garlic half a minute. Add the celery, green chillies and stir-fry for half
a minute more.

Step 5
Add soy sauce, sugar, MSG and salt. Stir in vegetable stock and bring to a
boil. Stir in cornflour mixture and cook for a couple of minutes or until
the sauce starts to thicken, stirring continuously.

Step 6
Add the fried vegetable balls, vinegar and mix well. Serve hot, garnished
with the reserved spring onion greens                                                
                                        


"""
t.insert(tk.END,quote)
t.config(state="disabled")

t1=tk.Text(root,bg='white',fg='black',font="Helvetica 10 bold")
t1.place(x=803,y=37,height=204,width=620)
quote1="""
ABOUT THE DISH:

This one is a favourite for people who like Indo-Chinese food.
Deep-fried mixed vegetable dumplings in a spicy gravy, the
consistency of which you can adjust depending on if you want to
enjoy it as a starter or main course. You can easily find veg
Manchurian on restaurant menus across India but you ought to try
out this Manchurian recipe in your home kitchen too. It uses very
simple ingredients, does involve a bit of chopping and prep but
the final dish is well worth the effort!

"""

t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 11 bold")
t2.place(x=803,y=238,height=600,width=730)
quote2="""
INGREADIENTS:

-Cabbage grated 1 medium
-Carrot grated 1 medium
-French beans finely chopped 8-10
-Spring onions with greens finely chopped 3 medium
-Green capsicum finely chopped 1 medium
-Salt to taste
-Refined flour (maida) 1/4 cup
-Cornflour/ corn starch 1/4 cup
-Oil to deep fry
-Sauce
-Oil 2 tablespoons
-Ginger finely chopped 4-6 cloves
-Celery finely chopped 2 inch stick
-Green chillies finely chopped 3
-Soy sauce 2 tablespoons
-Sugar 1 teaspoon
-MSG 1/4 teaspoon
-Salt to taste
-Vegetable stock 2 1/2 cups
-Cornflour/ corn starch 3 tablespoon
-Vinegar 1 tablespoon
"""

t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()
