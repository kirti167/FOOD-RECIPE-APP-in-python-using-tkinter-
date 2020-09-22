import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="red1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="MAXICAN RED RICE ",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 17 bold")
t.place(x=2,y=37,height=900,width=800)
quote="""
                                   RECIPE OF MAXICAN RED RICE

STEP1                                   
In a large heavy saucepan, heat the vegetable oil on medium-high heat. Add the rice, onions and garlic.
STEP2
Saute until the rice has an opaque color and is fragrant, about 2 minutes.
STEP3
Add the  tomato paste and salt. Mix well to incorporate evenly.
STEP4
Then add in the chile and cilantro sprig.
STEP5
Cover, reduce the heat to low, and simmer until rice is ready, about 30 minutes.
STEP6
Fluff with a fork and serve immediately.
                                  
"""
t.insert(tk.END,quote)
t.config(state="disabled")
t1=tk.Text(root,bg='white',fg='black',font="Helvetica 13 bold")
t1.place(x=803,y=37,height=204,width=620)
quote1="""
ABOUT THE DISH
Red rice is a variety of rice that is colored red by its
anthocyanin content.It is usually eaten unhulled or partially hulled,
and has a red husk,rather than the more common brown. Red rice has
a nutty flavor. Compared to polished rice,it has the highest nutritional
value of rices eaten with the germ intact.


"""
t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 18 bold")
t2.place(x=803,y=238,height=600,width=730)
quote2="""
INGREDIENTS
-1 tablespoon vegetable oil
-1 cup long grain white rice
-1/3 cup finely chopped white onion
-1 clove garlic, minced
-2 1/4 cups chicken broth
-3 tablespoons tomato paste
-1 1/4 teaspoon kosher salt
-1 serrano chile
-1 fresh cilantro sprig
"""


t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()
