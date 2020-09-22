import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="noodle1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="NOODLES",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 13 bold")
t.place(x=2,y=37,height=900,width=800)
quote="""
                                                RECIPE OF NOODLES

Step 1
Heat 7 cups water in a deep non-stick pan. Add salt and place a colander in it.
Put the noodles in the colander and allow them to cook.

Step 2
String beans, slit them lengthwise and then cut them diagonally or cut
into diamonds.

Step 3
Slice onion and shred cabbage. You can use a slicer to shred the cabbage.

Step 4
When the noodles are done, lift the colander with the noodles and put into another
pan with cold water.

Step 5
Heat 2 tbsps oil in a non-stick wok. Add onion, French beans, carrot and toss. Add
cabbage and toss.

Step 6
Remove the colander with the noodles from cold water and add to the vegetables.

Step 7
Add 1 tbsp oil. Add salt, pepper powder, soy sauce and toss on high heat. Add capsicum,
bean sprouts and vinegar and toss again.

Step 8
Serve hot.


"""
t.insert(tk.END,quote)
t.config(state="disabled")

t1=tk.Text(root,bg='white',fg='black',font="Helvetica 11 bold")
t1.place(x=803,y=37,height=204,width=600)
quote1="""
ABOUT THE DISH:

Noodles are something that can make even full grown adultsfeel like kids and no
you don’t need to go the a Chinese restaurant to satisfy your noodle craving.
In this recipe we show you how to make the most perfect hakka
noodles in just three easy steps. Once you have your
veggies prepped it’s just a matter of minutes before you have
a plate of piping hot noodles ready to dig into!

"""

t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t2.place(x=803,y=238,height=600,width=730)
quote2="""

INGREADIENTS:

-Noodles 400 grams
-Salt to taste
-French beans 6-8
-Onions 1 medium
-Cabbage finely shredded ¼ small
-Oil 3 tablespoons
-Carrot cut into thin strips 1 medium
-White pepper powder ¼ teaspoon
-Soy sauce 1 tablespoon
-Green capsicum cut into thin strips 1 medium
-Bean sprouts ½ cup
-Vinegar 1 tablespoon


"""

t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()
