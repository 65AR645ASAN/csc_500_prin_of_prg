import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def draw_box(ax, text, x, y, width=6, height=1.5):  # Set default width to 6
    # Adjust width for specific steps
    if text == "Multiply Ingredients by Number of Batches":
        width = 8  # Increase width specifically for the fourth step
    # Draw the box
    box = plt.Rectangle((x - width / 2, y - height / 2), width, height, fill=None, edgecolor='black')
    ax.add_patch(box)
    # Add the text
    ax.text(x, y, text, ha='center', va='center', fontsize=10)

def draw_arrow(ax, start_x, start_y, end_x, end_y):
    # Draw the arrow
    ax.arrow(start_x, start_y - 0.75, 0, end_y - start_y + 1.5, head_width=0.1, head_length=0.2, fc='black', ec='black')

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 15))  # Adjusted figure size for wider boxes
ax.set_xlim(-8, 8)  # Adjusted limits to fit the wider boxes
ax.set_ylim(-16, 10)  # Adjusted limit for the "End" step box
ax.axis('off')

# List of steps with their positions
steps = [
    ("Start", 0, 8),
    ("Gather Ingredients", 0, 6),
    ("Determine Number of Batches", 0, 4),
    ("Multiply Ingredients by Number of Batches", 0, 2),
    ("Mix Ingredients", 0, 0),
    ("Preheat Oven to 350°F", 0, -2),
    ("Shape Cookies on Baking Sheet", 0, -4),
    ("Add Toppings to cookies", 0, -6),
    ("Bake for 10-12 Minutes", 0, -8),
    ("Cool Cookies", 0, -10),
    ("Serve and Enjoy", 0, -12),
    ("End", 0, -14),
]

# Draw the steps
for text, x, y in steps:
    draw_box(ax, text, x, y)

# Draw the arrows
for i in range(len(steps) - 1):
    draw_arrow(ax, steps[i][1], steps[i][2], steps[i + 1][1], steps[i + 1][2])

# Draw the box closure for "End"
draw_box(ax, "End", 0, -14, width=6, height=1.5)

# Save the plot as an image file
plt.savefig(r'C:\Users\e442532\Desktop\CSU_GRADUATE_CODE\csc_500_prin_of_prg\MODULE1\flowchart_with_end.png')
