import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="garlic1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="GARLIC BREAD",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 19 bold")
t.place(x=2,y=37,height=900,width=800)
quote="""
                    RECIPE OF GARLIC BREAD

STEP1
Preheat oven to 350 degrees F (175 degrees C).
STEP2
In a small saucepan over medium heat, melt butter
and mix with garlic powderand dried parsley.
STEP3
Place Italian bread on a medium baking sheet.
STEP4
Using a basting brush,brush generously with the butter mixture.
STEP5
Remove from heat. Sprinkle with mozzarella cheese
and any remaining butter mixture.
STEP6
Return to oven approximately 5 minutes,
or until cheese is melted and bread is lightly browned.                    
"""                                   
t.insert(tk.END,quote)
t.config(state="disabled")
t1=tk.Text(root,bg='white',fg='black',font="Helvetica 15 bold")
t1.place(x=803,y=37,height=204,width=620)
quote1="""
ABOUT THE DISH
Garlic bread (also called garlic toast) consists of bread ,
topped with garlic and olive oil or butter and may include
additional herbs,such as oregano or chives.It is then
either grilled or broiled until toastedor baked in a oven."""

t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 15 bold")
t2.place(x=803,y=238,height=600,width=730)
quote2="""
INGREDIENTS
-½ cup butter
-1 ½ tablespoons garlic powder
-1 tablespoon dried parsley
-1 (1 pound) loaf Italian bread, cut into 1/2 inch slices
-1 (8 ounce) package shredded mozzarella cheese."""
t2.insert(tk.END,quote2)
t2.config(state="disabled")


tk.mainloop()
