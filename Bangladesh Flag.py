import turtle

# Set up screen
screen = turtle.Screen()
screen.title("Flag of Bangladesh (Centered Circle)")
screen.bgcolor("white")

# Create turtle
pen = turtle.Turtle()
pen.speed(3)

# Draw green rectangle (background)
pen.penup()
pen.goto(-150, 100)  # Top-left corner of the rectangle
pen.pendown()
pen.color("green")
pen.begin_fill()
for _ in range(2):
    pen.forward(300)  # Width of the flag
    pen.right(90)
    pen.forward(200)  # Height of the flag
    pen.right(90)
pen.end_fill()

# Draw red circle (centered)
pen.penup()
pen.goto(0, -40)  # Center the circle (radius 40, so move down 40)
pen.pendown()
pen.color("red")
pen.begin_fill()
pen.circle(40)  # Radius of the circle
pen.end_fill()

# Hide turtle and finish
pen.hideturtle()
turtle.done()