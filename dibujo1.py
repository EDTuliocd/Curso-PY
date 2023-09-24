from turtle import*
title ("jugando")
#bgcolor("orange")
"""
forward(100)
right(90)
forward(100)
left(90)
forward(100)
backward(50)
left(90)
forward(100)
"""
#circulo
"""
circle(60)
circle(100)
"""
#cuadrado
"""
pencolor('red')
pensize(3)
forward(100)
right(90)
penup()
pensize(5)
pencolor('green')
forward(100)
right(90)
pendown()
pensize(7)
pencolor('yellow')
forward(100)
right(90) 
pendown()
pensize(9)
pencolor('blue')
forward(100)
"""
for i in range(4):
    fillcolor('red')
    begin_fill()
    forward(100)
    right(90)
    end_fill()

mainloop()