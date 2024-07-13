import turtle

def draw_box(text, x, y, width=300, height=60):  # Set default width and height
    # Adjust width for specific steps
    if text == "Multiply Ingredients by Number of Batches":
        width = 400  # Increase width specifically for the fourth step
    # Draw the box
    turtle.penup()
    turtle.goto(x - width / 2, y + height / 2)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    # Add the text
    turtle.penup()
    turtle.goto(x, y - 10)
    turtle.pendown()
    turtle.write(text, align="center", font=("Arial", 12, "normal"))
    turtle.penup()

def draw_arrow(start_x, start_y, end_x, end_y):
    # Draw the arrow
    turtle.penup()
    turtle.goto(start_x, start_y - 30)
    turtle.pendown()
    turtle.goto(end_x, end_y + 30)
    turtle.penup()
    turtle.goto(end_x, end_y + 30)
    turtle.setheading(turtle.towards(start_x, start_y))
    turtle.right(30)
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.goto(end_x, end_y + 30)
    turtle.setheading(turtle.towards(start_x, start_y))
    turtle.left(30)
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.setheading(0)

# Set up the turtle screen size
turtle.setup(width=800, height=1200)  # Adjust the window size to fit the diagram
turtle.speed(0)

# List of steps with their positions
steps = [
    ("Start", 0, 500),
    ("Gather Ingredients", 0, 400),
    ("Determine Number of Batches", 0, 300),
    ("Multiply Ingredients by Number of Batches", 0, 200),
    ("Mix Ingredients", 0, 100),
    ("Preheat Oven to 350°F", 0, 0),
    ("Shape Cookies on Baking Sheet", 0, -100),
    ("Bake for 10-12 Minutes", 0, -200),
    ("Cool Cookies", 0, -300),
    ("Serve and Enjoy", 0, -400),
    ("End", 0, -500),
]

# Draw the steps
for text, x, y in steps:
    draw_box(text, x, y)

# Draw the arrows
for i in range(len(steps) - 1):
    draw_arrow(steps[i][1], steps[i][2], steps[i + 1][1], steps[i + 1][2])

turtle.hideturtle()
turtle.done()
