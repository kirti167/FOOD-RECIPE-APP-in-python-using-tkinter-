import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="khe1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="KHEER",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 13 bold")
t.place(x=2,y=37,height=900,width=800)
quote="""
                                    RECIPE OF KHEER


Step 1
Soak rice and boil milk.Rinse the rice and soak it for 15-20 minutes. Ensure that
the rice that you are using is aromatic. Boil the milk, and put one tablespoon of
boiled milk in a bowl. Once warm, add a few saffron strands to the tablespoon of
milk.

Step 2
Cook rice till al dente for kheer.While the milk is boiling, drain all the water
from the rice and add it to the milk. Cook the rice on low flame till it is half
cooked, then mix sugar as required, and continue cooking. Simmer till the rice is
almost cooked. The flame should be kept low and you must keep stirring.

Step 3
Simmer the kheer until it thickens and add dry fruits.Add half a teaspoon of cardamom
powder, chopped cashews, sliced pistachios and the saffron dissolved milk to the rice.
Mix and continue to cook. Once the rice grains are cooked and the kheer thickens,
scrape milk solids from the sides and add it to the kheer.

Step 4
Add golden raisins to rice kheer.Garnish with one tablespoon of golden raisins (sultana)
over the kheer, and serve hot or cold.




"""
t.insert(tk.END,quote)
t.config(state="disabled")

t1=tk.Text(root,bg='white',fg='black',font="Helvetica 11 bold")
t1.place(x=803,y=37,height=204,width=600)
quote1="""
ABOUT THE DISH:

Kheer is a nationally recognized dessert that is loved by
millions. It is a delicious pudding made by boiling milk
and sugar with rice or vermicelli and any other taste
enhancing ingredients like sugar or jaggery. A variety of
other assortments are added to further entice the palate,
such as dates, saffron, and dry fruits. Kheer is traditionally
served at auspicious occasions like festivals and special occasions

"""

t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t2.place(x=803,y=238,height=600,width=730)
quote2="""

INGREDIENTS:

- 1/2 cup basmati rice
- 250 gm sugar
- 30 gm sliced almonds
- 30 gm sliced unsalted pistachios
- 1/2 teaspoon saffron
- 2 litre full cream milk
- 2 teaspoon powdered green cardamom
- 30 gm chopped cashews
- 30 gm sultanas



"""

t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()
