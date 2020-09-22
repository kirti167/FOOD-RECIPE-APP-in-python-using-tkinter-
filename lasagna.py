import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="las1.jpg")
canvas.create_image(1400,37,anchor=NW ,image=img)

label=Label(root,text="LASAGNA",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 13 bold")
t.place(x=2,y=37,height=900,width=800)
quote="""
                    RECIPE OF LASAGNA

STEP1                    
In a Dutch oven, cook sausage, ground beef, onion, and garlic over medium heat until well browned.
STEP2
Stir in crushed tomatoes, tomato paste, tomato sauce, and water. Season with sugar, basil, fennel
seeds, Italian seasoning, 1 teaspoon salt, pepper,and 2 tablespoons parsley.
STEP3
Simmer, covered, for about 1 1/2 hours, stirring occasionally.
STEP4
Bring a large pot of lightly salted water to a boil.
STEP5
Cook lasagna noodles in boiling water for 8 to 10 minutes. Drain noodles, and rinse with cold water.
STEP6
In a mixing bowl, combine ricotta cheese , remaining parsley, and 1/2 teaspoon salt.
STEP7
Preheat oven to 375 degrees F (190 degrees C).
To assemble, spread 1 1/2 cups of meat sauce in the bottom of a 9x13 inch baking dish.
STEP8
Arrange 6 noodles lengthwise over meat sauce. Spread with one half of the ricotta cheese mixture.
STEP9
Top with a third of mozzarella cheese slices. Spoon 1 1/2 cups meat sauce over mozzarella,
and sprinkle with 1/4 cup Parmesan cheese.
STEP10
Repeat layers, and top with remaining mozzarella and Parmesan cheese.
STEP11
Cover with foil: to prevent sticking, either spray foil with cooking spray, or
make sure the foil does not touch the cheese.
STEP12
Bake in preheated oven for 25 minutes. Remove foil, and bake an additional 25 minutes.
STEP13
Cool for 15 minutes before serving."""                                   
t.insert(tk.END,quote)
t.config(state="disabled")
t1=tk.Text(root,bg='white',fg='black',font="Helvetica 11 bold")
t1.place(x=803,y=37,height=204,width=620)
quote1="""
ABOUT THE DISH
Lasagne, or the singular lasagna, is an Italian dish made of stacked layers of thin flat pasta
alternating with fillings such as ragù (ground meats and tomato sauce) and other vegetables,
cheese (which may include ricotta and parmesan), and seasonings and spices such as garlic,
oregano and basil.The dish may be topped with melted grated mozzarella cheese. 
"""
t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 15 bold")
t2.place(x=803,y=238,height=600,width=730)
quote2="""
INGREDIENTS
-1 pound sweet Italian sausage
-¾ pound lean ground beef
-½ cup minced onion
-2 cloves garlic, crushed
-1 (28 ounce) can crushed tomatoes
-2 (6 ounce) cans tomato paste
-2 (6.5 ounce) cans canned tomato sauce
-½ cup water
-2 tablespoons white sugar
-1 ½ teaspoons dried basil leaves
-½ teaspoon fennel seeds
-1 teaspoon Italian seasoning
-1 ½ teaspoons salt, divided, or to taste
-¼ teaspoon ground black pepper
-4 tablespoons chopped fresh parsley
-12 noodles lasagna noodles
-16 ounces ricotta cheese
-¾ pound mozzarella cheese, sliced
-¾ cup grated Parmesan cheese

"""
t2.insert(tk.END,quote2)
t2.config(state="disabled")


tk.mainloop()
