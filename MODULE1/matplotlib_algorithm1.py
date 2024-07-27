import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def draw_box(ax, text, x, y, width=3, height=1):
    box = plt.Rectangle((x - width / 2, y - height / 2), width, height, fill=None, edgecolor='black')
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=8)

def draw_arrow(ax, start_x, start_y, end_x, end_y):
    ax.annotate(
        '',
        xy=(end_x, end_y + 0.5),
        xytext=(start_x, start_y - 0.5),
        arrowprops=dict(facecolor='black', shrink=0.05)
    )

fig, ax = plt.subplots(figsize=(12, 18))
ax.set_xlim(-10, 10)
ax.set_ylim(-24, 10)
ax.axis('off')

# List of steps with their positions
steps = [
    ("Start", 0, 8),
    ("Determine Number of Batches", 0, 6),
    ("Get 4 cups of flour per batch", 0, 4),
    ("Get 1/3 cup of sugar per batch", 0, 2),
    ("Get 1/5 cup of butter per batch", 0, 0),
    ("Get 1/4 Teaspoon baking powder per batch", 0, -2),
    ("Get 1 egg per batch", 0, -4),
    ("Get 2 Teaspoons of milk per batch", 0, -6),
    ("More Batches?", 0, -8),
    ("Mix Ingredients", 0, -10),
    ("Preheat Oven to 350°F", 0, -12),
    ("Shape Cookies on Baking Sheet", 0, -14),
    ("Bake for 10-12 Minutes", 0, -16),
    ("Cool Cookies", 0, -18),
    ("Serve and Enjoy", 0, -20),
    ("End", 0, -22),
]

# Draw the steps
for text, x, y in steps:
    draw_box(ax, text, x, y)

# Draw the arrows
for i in range(len(steps) - 1):
    draw_arrow(ax, steps[i][1], steps[i][2], steps[i + 1][1], steps[i + 1][2])

# Add special arrow from "More Batches?" to "Determine Number of Batches"
draw_arrow(ax, steps[8][1], steps[8][2], steps[1][1], steps[1][2])

# Save the plot as an image file
plt.savefig('flowchart_matplotlib.png')
