import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="pasta1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="MIXED SAUCE PASTA",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t.place(x=2,y=37,height=900,width=800)
quote=""" 
                    RECIPE OF MIXED SAUCE PASTA

Step 1
Boil 1 potato overnight for about an hour. Next morning, peel
the skin of the potatoes and mash them. Then blend it in the
mixer along with tomatoes.

Step 2
On the other hand, start boiling the macaroni and add salt and
oil to the pot. Boil it for about 10 minutes. Also, slice the
other potato finely and add it to the mix.

Step 3
Turn off the flame once the macaroni is boiled. Grease the baking
dish and pour the pasta mix in it. Add, bread crumbs, chopped
capsicum and cabbage to the pasta mix.

Step 4
Next, add potato-tomato sauce on it. Then, add salt, butter, black
pepper and mustard powder to the baking dish as per your taste.

Step 5
Start baking the pasta in the oven for about 15 minutes or so at
180 degree Celsius. Once baked, take out the tray and serve hot
along with the remaining sauce.                                

"""
t.insert(tk.END,quote)
t.config(state="disabled")

t1=tk.Text(root,bg='white',fg='black',font="Helvetica 11 bold")
t1.place(x=803,y=37,height=204,width=600)
quote1="""
ABOUT THE DISH:

Mixed pasta is an Italian style mixed pasta
recipe cooked in a savory tomato based sauce.
An Italian delicacy famous worldwide and favorite
of all.Cooked in a tomato base puree with the
flavors of garlic and melting cheese spiced with
herbs make a complete meal option.The boiled
colorful and differently shaped pasta tossed with
sauces


"""

t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t2.place(x=803,y=238,height=600,width=730)
quote2="""

INGREDIENTS:

- 1 cup pasta macaroni
- 1/4 teaspoon black pepper
- 1/2 cup bread crumbs
- 2 potato
- 2 1/2 tomato
- 1/4 cup capsicum (green pepper)
- 1/2 cup cabbage
- salt as required
- 1/4 teaspoon mustard powder
- 1/4 cup milk
- 1 teaspoon refined oil
- 1 cup water



"""

t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()
