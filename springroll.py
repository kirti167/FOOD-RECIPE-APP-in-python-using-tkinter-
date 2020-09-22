import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="spring1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="SPRING ROLL",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t.place(x=2,y=37,height=900,width=800)
quote=""" 
                                RECIPE OF SPRING ROLL

Step 1
To make the stuffing, heat 2 tbsps oil in a non stick wok. Add
onion, spring onions, carrots, capsicum, cabbage and salt and
toss.

Step 2
Add pepper powder and soy sauce and mix. Add bean sprouts and
spring onion greens and mix. Cook till the vegetables soften.

Step 3
Take the wok off the heat and set aside to cool. Heat sufficient
oil in a wok. Make a paste of cornflour with 2 tbsps water.

Step 4
Spread the spring roll wrappers on the work top. Divide the
stuffing into 10 portions and place a portion on one side of
each wrapper. Fold in the edges and roll tightly.

Step 5
Apply cornflour paste to open end and seal. Keep the rolls
under a damp cloth. Gently slide into the hot oil and deep
fry till golden and crisp.

Step 6
Drain on absorbent paper. Cut into smaller pieces and serve.                                        





"""
t.insert(tk.END,quote)
t.config(state="disabled")

t1=tk.Text(root,bg='white',fg='black',font="Helvetica 10 bold")
t1.place(x=803,y=37,height=204,width=600)
quote1="""
ABOUT THE DISH:

This deep fried starter is very popular in South East
Asia and parts around it. Made with ready to use
spring roll wrappers this recipe is really a quick
starter to prepare and delicious to eat. The filling
is made with a mix of veggies stir fried with oriental
sauces. Crispy on the outside and juicy inside these
are a favourite recipe for kids’ parties or for that
matter any party! 


"""

t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t2.place(x=803,y=238,height=600,width=730)
quote2="""

INGREADIENTS:

-Spring roll wrappers 10
-Spring onions thinly sliced 2
-Onion thinly sliced 1 medium
-Carrots cut into thin strips 2 medium
-Green capsicum cut into thin strips 1 medium
-Cabbage finely shredded 1/2 small
-Oil 2 tablespoon
-Salt to taste
-White pepper powder 1/4 teaspoon
-Soy sauce 1 tablespoon
-Bean sprouts 3/4 cup
-Spring onion greens chopped 2 stalks
-Cornflour/ corn starch 1 tablespoon




"""

t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()
