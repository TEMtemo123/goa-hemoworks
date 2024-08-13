from turtle import*
speed(5)
#we want to paint a house

#step 1: draw a square
width(7)
color("black")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a dor
begin_fill()
forward(70)
color("red")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(50,150)
pendown()

width(3)
right(-30)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
penup()
goto(170,150)
pendown()

forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)



exitonclick()