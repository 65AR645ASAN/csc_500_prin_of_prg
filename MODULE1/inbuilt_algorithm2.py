import turtle

def draw_box(text, x, y, width=300, height=40):  # Set default width and height, reduced height for compression
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
    turtle.goto(start_x, start_y - 20)  # Adjusted for reduced height
    turtle.pendown()
    turtle.goto(end_x, end_y + 20)  # Adjusted for reduced height
    turtle.penup()
    turtle.goto(end_x, end_y + 20)
    turtle.setheading(turtle.towards(start_x, start_y))
    turtle.right(30)
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.goto(end_x, end_y + 20)
    turtle.setheading(turtle.towards(start_x, start_y))
    turtle.left(30)
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.setheading(0)

# Set up the turtle screen size
turtle.setup(width=800, height=1000)  # Adjust the window size to fit the diagram
turtle.speed(0)

# List of steps with their positions
steps = [
    ("Start", 0, 400),
    ("Determine Number of Batches", 0, 340),
    ("Get 4 cups of flour per batch", 0, 280),
    ("Get 1/3 cup of sugar per batch", 0, 220),
    ("Get 1/5 cup of butter per batch", 0, 160),
    ("Get 1/4 Teaspoon baking powder per batch", 0, 100),
    ("Get 1 egg per batch", 0, 40),
    ("Get 2 Teaspoons of milk per batch", 0, -20),
    ("Mix Ingredients", 0, -80),
    ("Preheat oven to 350 degrees", 0, -140),
    ("Put Cookies on the Baking Sheet", 0, -200),
    ("Bake Cookies for 15 minutes", 0, -260),
    ("Cool Cookies", 0, -320),
    ("Serve", 0, -380),
    ("End", 0, -440),
]

# Draw the steps
for text, x, y in steps:
    draw_box(text, x, y)

# Draw the arrows
for i in range(len(steps) - 1):
    draw_arrow(steps[i][1], steps[i][2], steps[i + 1][1], steps[i + 1][2])

turtle.hideturtle()
turtle.done()
