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

def draw_loop(start_x, start_y, end_x, end_y):
    # Draw the loop arrow
    turtle.penup()
    turtle.goto(start_x, start_y - 20)
    turtle.pendown()
    turtle.goto(start_x, start_y - 60)
    turtle.goto(end_x - 300, start_y - 60)
    turtle.goto(end_x - 300, end_y + 20)
    turtle.goto(end_x, end_y + 20)
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
turtle.setup(width=800, height=1200)  # Adjust the window size to fit the diagram
turtle.speed(0)

# List of steps with their positions
steps = [
    ("Start", 0, 500),
    ("Determine Number of Batches", 0, 440),
    ("Get 4 cups of flour per batch", 0, 380),
    ("Get 1/3 cup of sugar per batch", 0, 320),
    ("Get 1/5 cup of butter per batch", 0, 260),
    ("Get 1/4 Teaspoon baking powder per batch", 0, 200),
    ("Get 1 egg per batch", 0, 140),
    ("Get 2 Teaspoons of milk per batch", 0, 80),
    ("More Batches?", 0, 20),
    ("Mix Ingredients", 0, -40),
    ("Preheat oven to 350 degrees", 0, -100),
    ("Put Cookies on the Baking Sheet", 0, -160),
    ("Bake Cookies for 15 minutes", 0, -220),
    ("Cool Cookies", 0, -280),
    ("Serve", 0, -340),
    ("End", 0, -400),
]

# Draw the steps
for text, x, y in steps:
    draw_box(text, x, y)

# Draw the loop for batches
for i in range(2, 8):  # Loop from "Get 4 cups of flour per batch" to "More Batches?"
    draw_arrow(steps[i][1], steps[i][2], steps[i + 1][1], steps[i + 1][2])
draw_loop(steps[8][1], steps[8][2], steps[2][1], steps[2][2])

# Draw the remaining arrows
for i in range(8, len(steps) - 1):
    draw_arrow(steps[i][1], steps[i][2], steps[i + 1][1], steps[i + 1][2])

turtle.hideturtle()
turtle.done()
