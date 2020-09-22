import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="kadhai1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="KADAI PANEER",font="Helvetica 14 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t.place(x=2,y=37,height=900,width=800)
quote="""
                                     RECIPE OF KADAI PANEER


Step 1
Heat ghee in a kadai and saute the cottage cheese pieces till golden brown.
Soak them in 5 cups water.

Step 2
In the same pan add bay leaf, cloves, cinnamon sticks, onion paste and
ginger garlic paste. Saute well till lightly golden.

Step 3
Add red chilli powder, coriander powder, turmeric powder, garam masala and
little water. Mix well and allow the mixture to boil. Add tomato puree and
mix again.

Step 4
Cover and cook for five minutes till oil surfaces.Add salt and drained
cottage cheese pieces. Garnish with coriander leaves and serve hot.                                    
                                        
"""

t.insert(tk.END,quote)
t.config(state="disabled")

t1=tk.Text(root,bg='white',fg='black',font="Helvetica 11 bold")
t1.place(x=803,y=37,height=204,width=600)
quote1="""
ABOUT THE DISH:

The traditional Kadai Paneer recipe is a perfect mix of
spices, paneer and cream. If you are bored with the
usual paneer recipes like shahi paneer, palak paneer,
paneer bhurji; then this one is a must try for you,
especially if you are looking for something spicy and
delicious! This easy to prepare paneer recipe makes for
a perfect main course dish and it tastes best when served
with naan, jeera rice, veg biryani and butter tandoori roti. 

"""

t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 12 bold")
t2.place(x=803,y=242,height=600,width=730)
quote2="""
INGREDIENTS:


-Paneer (cottage cheese) cut into cubes 250 grams
-Onions pureed 3 medium
-Tomatoes pureed 3 large
-Ginger-garlic paste 2 teaspoons
-Red chilli powder 1 teaspoon
-Coriander powder 1 teaspoon
-Turmeric powder 1/4 teaspoon
-Garam masala 1 teaspoon
-Bay leaf 2
-Cloves 3
-Cinnamon 1 inch sticks
-Coriander leaves a few
-Ghee 2 tablespoons
-Salt to taste


"""

t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()
