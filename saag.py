import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="sag1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="SARSO KA SAAG",font="Helvetica 14 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=4,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 16 bold")
t.place(x=2,y=37,height=900,width=800)
quote="""
                                 RECIPE OF SAAG

1.Clean all the leaves and wash them thoroughly.
2.One good way to wash your green is to fill a large pot with water.
3.Dip your greens in water.
4.Let it stay for a minute.
5.All the impurities will settle down.
6.Gently take out the leaves without disturbing the water.
7.Repeat the process 2-3 times.
8.Chop the greens and add them in a pressure cooker.
9.Add tomato, onion, ginger, garlic, radish, green chilli, salt and
a cup of water.
10.Pressure cook for one whistle on high heat.
11.Remove the pressure cooker from heat and let it cool.
12.Once cooled, blend the greens in a blender to make a coarse paste.
( I like my saag a little coarse. If you like it smooth, grind the
greens till smooth )
13.Transfer the paste in the pressure cooker.
14.Dissolve makke ka atta in little water and add it in the cooker.
15.Add red chilli powder and hing and cook for 3-5 minutes.
16.For tempering, heat ghee in a pan.
17.Add onion and garlic and fry till golden brown.
18.Pour the tadka over the saag.
19.Serve hot with makke ki roti and white butter.

"""
t.insert(tk.END,quote)
t.config(state="disabled")

t1=tk.Text(root,bg='white',fg='black',font="Helvetica 13 bold")
t1.place(x=803,y=37,height=204,width=600)
quote1="""
ABOUT THE DISH:

Sarson Ka Saag is a traditional Punjabi recipe made
with Mustard greens and other leafy vegetables and
a delicious tempering of onion and garlic in ghee.
Served with a dollop of White Butter or Makkhan and
crispy warm Makki Ki Roti, this dish is soul-warming.
Here is how to make the Sarso Ka Saag recipe.
"""

t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 12 bold")
t2.place(x=803,y=242,height=600,width=730)
quote2="""
INGREADIENTS:

-200 g Mustard Greens/ Sarson
-35 g Spinach/ Palak
-35 g Radish Greens/ Mooli ke Patte
-35 g Chenopodium/ Bathua
-35 g Fenugreek Leaves/ Methi
-1 cup Tomato ( Chopped)
-1 cup Onion (Chopped)
-1/4 cup radish (Chopped)
-1 inch Ginger (Chopped)
-(8-10) cloves Garlic (Chopped)
-(2-3) Green Chilli (Chopped)
-1 tsp Red Chilli Powder
-(1/4) tsp Hing
-Salt to taste
-2 tbsp Corn Meal/ Makki ka Atta

For tempering:
-2 tbsp Ghee
-(1/4) cup Onion (Finely Chopped)
-(3-4) cloves Garlic (Smashed)


"""

t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()
