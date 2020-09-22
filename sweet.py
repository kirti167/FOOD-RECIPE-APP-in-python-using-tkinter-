import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="sweet1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="SWEET POTATO SOUP",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 20 bold")
t.place(x=2,y=37,height=900,width=800)
quote="""
                                   RECIPE OF SWEET POTATO SOUP

STEP1                                   
Heat the oil in a large, lidded saucepan over a medium-high heat.
STEP2
Add the onion and carrots and cook until softened.
STEP3
Stir in the ginger, garlic and chilli flakes and fry for 2–3 minutes, or until fragrant.
STEP4
Stir in the sweet potatoes and stock. Turn up the heat and
bring the pan to the boil.
STEP5
Reduce the heat to low and simmer with the lid on for 15 minutes, or
until the sweet potato is tender.
STEP6
Remove the pan from the heat and blend the soup, using a stick blender, until smooth.
Alternatively, tip it into a food processor and blend.
STEP7
Season to taste and serve.                                  
"""
t.insert(tk.END,quote)
t.config(state="disabled")
t1=tk.Text(root,bg='white',fg='black',font="Helvetica 13 bold")
t1.place(x=803,y=37,height=204,width=620)
quote1="""
ABOUT THE DISH
Sweet potato soup is a big bowl of comfort.
it is a mexican special soup.
It's vegan, has cheap ingredients, is quick and easy to make.
It can also be frozen for future lunches and dinners. Perfection!


"""
t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 18 bold")
t2.place(x=803,y=238,height=600,width=730)
quote2="""
INGREDIENTS
-1 tbsp olive oil.
-1 onion, roughly chopped.
-2 large carrots, peeled and roughly chopped.
-4cm/1½ inches fresh root ginger, finely chopped.
-1 garlic clove, crushed.
-½ tsp dried red chilli flakes.
-700g/1lb 10oz sweet potatoes, peeled and cubed.
-1.2 litres/2 pints vegetable stock.
-salt and freshly ground black pepper."""


t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()
