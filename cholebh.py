import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="bhature1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="CHOLE BHATURE",font="Helvetica 14 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=4,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 11 bold")
t.place(x=2,y=37,height=900,width=800)
quote="""
                                                RECIPE OF CHOLE BHATURE
                                        
Step 1
Take chickpeas in a pressure cooker. Add tea bags, 6-8 cups water and salt, cover and cook for 15-20 minutes or
till fully done and soft. Drain the chickpeas, discard the tea bags and reserve the stock.

Step 2
Sieve together flour, baking powder, baking soda, salt and powdered sugar in a parat. Add yogurt and mix well.

Step 3
Add some water and knead into a soft dough. Add 1 tablespoon oil and knead well.Set aside for 15-20 minutes.

Step 4
Heat ghee in a non-stick pan. Add cumin seeds and green chillies and sauté for 30 seconds.

Step 5
Add ginger-green chilli paste and sauté for 30 seconds. Add coriander powder, cumin powder and chilli powder
and mix.

Step 6
Add chole masala and dried mango powder and mix. Add reserved stock, mix and bring mixture to boil.

Step 7
Add boiled chickpeas and ¾ cup water, mix and cook on medium heat for 8-10 minutes. Lightly mash.

Step 8
Add dried pomegranate powder and garam masala powder and mix. Add ¼ cup water.Chop tomatoes, add to pan,
mix and cook for 2-3 minutes.

Step 9
Heat sufficient oil in a kadai. Divide the dough into equal portions and shapeinto balls. Grease worktop
with some oil and roll each ball into thick discs.

Step 10
Deep-fry each disc in hot oil till light golden and puffed up. Drain on absorbent paper.

Step 11
Garnish chole with a coriander sprig and serve hot with bhature."""

t.insert(tk.END,quote)
t.config(state="disabled")

t1=tk.Text(root,bg='white',fg='black',font="Helvetica 13 bold")
t1.place(x=803,y=37,height=204,width=600)
quote1="""
ABOUT THE DISH:

Chole bhature is a food dish originating from northern India.There is a
distinct Punjabi variant of the dish.Chhole bhature is often
eaten as a breakfast dish, sometimes accompanied with lassi.
It can also be street food or acomplete meal and may be accompanied
with onions, pickled carrots, green chutney or achaar.
"""

t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 13 bold")
t2.place(x=803,y=242,height=600,width=730)
quote2="""
INGREADIENTS:

-Chickpeas (kabuli chana) soaked overnight and drained
 1 cup
-Tea bags 2
-Salt to taste
-Ghee 2 tablespoons
-Cumin seeds 1 teaspoon
-Green chillies slit 2
-Ginger-green chilli paste 1 tablespoon
-Coriander powder 1 tablespoon
-Cumin powder ½ teaspoon
-Red chilli powder 1 teaspoon
-Chole masala 1 teaspoon
-Dried mango powder ½ teaspoon
-Dried pomegranate seeds (anardana) roasted and coarsely
 crushed 1 tablespoon
-Garam masala powder 1 teaspoon
-Fresh coriander sprigs for garnishing
-Bhature
-Refined flour (maida) 2½ cups
-Baking powder ½ teaspoon
-Baking soda a pinch
-Salt to taste
-Powdered sugar 2 teaspoons
-Yogurt ½ cup
-Oil 1 tablespoon + for greasing and to deep fry
"""

t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()
