import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="risso1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="MARGHERITA PIZZA",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 12 bold")
t.place(x=2,y=37,height=900,width=800)
quote=""" 
                    RECIPE OF MARGHERITA PIZZA

Step 1
Stir flour and 1 teaspoon salt in a bowl. Set aside.

Step 2
Mix water, yeast, and sugar in a large bowl. Let stand until yeast begins to form a creamy foam,
about 5 minutes.

Step 3
Stir half the flour mixture into yeast mixture until no dry spots remain.Stir in remaining flour,
1/2 cup at a time, mixing well after each addition. When dough pulls together, turn it out onto
a lightly floured surface and knead until smooth and elastic, about 8 minutes.

Step 4
Lightly oil a large bowl, then place dough in the bowl and turn to coat with oil. Cover with a
light cloth and let rise in a warm place(80 to 95 degrees F (27 to 35 degrees C)) until doubled
in volume, about 1 hour. Punch dough down, divide into 4 equal pieces, and form each into a ball.

Step 5
Preheat oven with a pizza stone to 500 degrees F (260 degrees C).

Step 6
Stretch out and pat 1 dough ball to form a circle 10 to 12 inches in diameter.Place dough on a
lightly floured pizza peel. Top with 1/2 cup of tomato sauce and spread to cover within an
inch of the edge of the dough. Arrange 5 slices of mozzarella cheese on top of the tomato sauce,
then place 5 basil leaves on top. Drizzle pizza with 1 tablespoon olive oil and sprinkle with
sea salt to taste. Repeat for 3 remaining dough balls.

Step 7
Slide each pizza onto the pizza stone in the preheated oven.Bake until cheese is bubbly and the
underside of the crust isgolden brown, 5 to 7 minutes.


                       

"""
t.insert(tk.END,quote)
t.config(state="disabled")

t1=tk.Text(root,bg='white',fg='black',font="Helvetica 11 bold")
t1.place(x=803,y=37,height=204,width=600)
quote1="""
ABOUT THE DISH:

Pizza Margherita is a classic cheesy pizza with
the authentic Italian flavours comprising of
only pizza sauce with loads of mozzarella cheese
and basil. Serve this delicious Pizza with Fresh
Tomato Basil Pasta, Herb Mushroom Bruschetta and
Tiramisu for a weekend dinner



"""

t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t2.place(x=803,y=238,height=600,width=730)
quote2="""

INGREDIENTS:

- 3 ½ cups all-purpose flour
- 1 teaspoon salt
- 1 cup water
- 1 (.25 ounce) package active dry yeast
- 1 pinch white sugar
- ¼ cup flour for dusting
- 2 cups pizza sauce
- 20 slices fresh mozzarella cheese
- 20 leaves fresh basil
- olive oil
- sea salt to taste




"""

t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()
