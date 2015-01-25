import turtle

def roo7(event):
    turtle.penup()
    turtle.onscreenclick(turtle.goto, btn=1, add=None)
    turtle.pendown()
def orsom(event):    
    turtle.ondrag(turtle.goto, add=True)
    
def bas_rasem(event):
    turtle.penup()

def reset(event):
    turtle.reset()

turtle.reset()

c=turtle.getcanvas()

c.bind("<Button-1>", roo7)
c.bind("<B1-Motion>", orsom)
c.bind("<ButtonRelease-1>", bas_rasem)
c.bind("<Escape>", reset)

turtle.mainloop()



