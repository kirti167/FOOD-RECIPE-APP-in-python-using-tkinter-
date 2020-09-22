import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="dal1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="DAL MAKHANI",font="Helvetica 14 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=4,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t.place(x=2,y=37,height=900,width=800)
quote="""
                                                RECIPE OF DAL MAKHANI

Step 1
Pick, wash and soak sabut urad and rajma overnight in three cups of water. Drain.

Step 2
Pressure cook sabut urad and rajma in three cups of water with salt and half the
red chilli powder (you can add half the ginger too if you wish) for three
whistles in a pressure cooker. Open the lid and see if the rajma is totally
soft. If not cook on low heat till the rajma becomes totally soft.

Step 3
Heat butter and oil in a pan. Add cumin seeds. When they begin to change colour,
add ginger, garlic and onion and sauté till golden.

Step 4
Add slit green chillies, tomatoes and sauté on high heat. Add the remaining red
chilli powder and sauté till the tomatoes are reduced to a pulp.

Step 5
Add the cooked dal and rajma along with the cooking liquour. Add some water if
the mixture is too thick. Add garam masala powder and adjust salt.

Step 6
Simmer on low heat till the dals are totally soft and well blended.

Step 7
Serve hot."""

t.insert(tk.END,quote)
t.config(state="disabled")

t1=tk.Text(root,bg='white',fg='black',font="Helvetica 12 bold")
t1.place(x=803,y=37,height=204,width=600)
quote1="""
ABOUT THE DISH:

Dal makhani is one of the most popular Indian dishes.This spicy lentil
preparation is made a mix of rajmaor red kidney beans
and whole black gram or sabut urad dal and a perfect blend of whole
spices.The recipe does complete justice to the name and  uses plenty
of butter which balances out the heat from the spices and makes the final dal
rich and creamy.


"""

t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 16 bold")
t2.place(x=803,y=242,height=600,width=730)
quote2="""
INGREADIENTS:

-Whole black gram (sabut urad) 1/2 cup.
-Red kidney beans (rajma) 2 tablespoons.
-Salt to taste.
-Red chilli powder 1 teaspoon.
-Ginger grated or chopped 2 inch piece.
-Butter 3 tablespoons.
-Oil 1 tablespoon.
-Cumin seeds 1 teaspoon.
-Garlic cloves chopped 6.
-Onion chopped 1 large.
-Green chillies slit 2.
-Tomatoes chopped 3 medium.
-Garam masala powder 1 teaspoon.


"""

t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()
