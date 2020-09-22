import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="ques1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="QUESADILLA PANCAKES",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 15 bold")
t.place(x=2,y=37,height=900,width=800)
quote="""
                                   RECIPE OF QUESADILLA PANCAKES
STEP 1
Heat oven to 180C/160C fan/gas 4.
STEP 2
Scatter the peppers, cheese and coriander over 4 pancakes.
STEP 3
Season well and cover each one with another pancake to make a sandwich.
STEP 4
Place the quesadilla pancakes on baking sheets and cook for 5 mins in the
oven until the cheese starts melting (you may need to do this in batches).
STEP 5
Warm the butter in a saucepan, add the garlic and cook for 1 min until.
STEP 6
fragrant, then add the cumin and beans..
STEP 7
Stir for 2 mins, then roughly mash.
STEP 8
stir through half the lemon juice, spoon into a serving dish and top with the chilli, if using.
STEP 9
Toss the avocado in the rest of the lemon juice.
STEP 10
then serve the quesadillas with the beans, lettuce and avocado.                                   
"""
t.insert(tk.END,quote)
t.config(state="disabled")
t1=tk.Text(root,bg='white',fg='black',font="Helvetica 11 bold")
t1.place(x=803,y=37,height=204,width=620)
quote1="""
ABOUT THE DISH
Literally meaning “little cheesy thing,” quesadillas originated in northern and central
Mexicoin the 16th century.Corn tortillas were already popular among the Aztec people.
They often stuffed them with squash and pumpkin and baked them in clay ovens as a
sweet dessert.In 1521, Spanish settlers brought sheep, lambs, and cows with
them to New Spain.
"""
t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 16 bold")
t2.place(x=803,y=238,height=600,width=730)
quote2="""
INGREDIENTS
-2 red peppers , chopped into small pieces
-140g red leicester , grated
-4 tbsp chopped fresh coriander
-8 pre-made pancakes
-1 tbsp butter
-1 garlic clove , crushed
-½ tsp ground cumin
-400g can kidney beans , drained
-juice 1 lemon
-1 red chilli , deseeded if you don’t like it too hot, sliced (optional)
-2 avocados , sliced
-2 Little Gem lettuces , sliced
"""

t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()
