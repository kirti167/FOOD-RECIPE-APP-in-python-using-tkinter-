import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="chili1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="CHILLI POTATO",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 15 bold")
t.place(x=2,y=37,height=900,width=800)
quote="""
                                        RECIPE OF CHILLI POTATO

Step 1
Add potatoes in a bowl. Add corn flour, salt, and white pepper powder.
Mix well and set aside for twenty minutes.

Step 2
Heat two tablespoons oil in a non stick pan. Add onion roundels and
sauté for two minutes or until pink. Add garlic, garlic paste and sauté
for half minute.

Step 3
Heat oil in a kadai. Deep fry the potatoes till crisp. Drain on an
absorbent paper and add to the onion-garlic mixture.

Step 4
Add green chillies, soy sauce and MSG and mix well. Check the seasonings.
Add vinegar and mix well.Serve hot.                                                




"""
t.insert(tk.END,quote)
t.config(state="disabled")

t1=tk.Text(root,bg='white',fg='black',font="Helvetica 11 bold")
t1.place(x=803,y=37,height=204,width=600)
quote1="""
ABOUT THE DISH:

A hugely popular Chinese dish, Honey Chill Potato is juicy,
crunchy and full of flavour snack that you just cannot
resist. A delicious pick for kids, the great taste of honey
chilli potatoes can be brought home in a few easy steps.
Try this recipe and you'll never head to those street
stalls again!


"""

t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t2.place(x=803,y=238,height=600,width=730)
quote2="""

INGREADIENTS:

-Potatoes cut into fingers 5 medium
-Cornflour/ corn starch 3 tablespoon
-Salt to taste
-White pepper powder a pinch
-Oil 2 tbsps + to deep fry
-Onions cut 2 medium
-Garlic finely chopped 1/2 tablespoon
-Garlic paste 1/2 tablespoon
-Green chillies slit 4
-Soy sauce 2 teaspoon
-MSG optional a pinch
-Vinegar 1 teaspoon



"""

t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()
