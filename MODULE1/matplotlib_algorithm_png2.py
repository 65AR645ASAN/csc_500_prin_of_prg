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
    # Adjust the start and end points to be outside the boxes
    arrow_start_y = start_y - 1.5 / 2  # Adjust based on box height
    arrow_end_y = end_y + 1.5 / 2  # Adjust based on box height
    ax.annotate('', xy=(end_x, arrow_end_y), xytext=(start_x, arrow_start_y),
                arrowprops=dict(facecolor='black', shrink=0.05, width=0.5, headwidth=5, headlength=10))

fig, ax = plt.subplots(figsize=(8, 20))  # Adjusted figure size for wider boxes
ax.set_xlim(-8, 8)  # Adjusted limits to fit the wider boxes
ax.set_ylim(-22, 10)  # Adjusted limit for the "End" step box
ax.axis('off')

# Draw the first five steps and arrows
draw_box(ax, "Start", 0, 8)
draw_box(ax, "Gather Ingredients", 0, 6)
draw_box(ax, "Determine Number of Batches", 0, 4)
draw_box(ax, "Multiply Ingredients by Number of Batches", 0, 2, width=8)  # Increased width for this step
draw_box(ax, "Mix Ingredients", 0, 0)
draw_arrow(ax, 0, 8, 0, 6)
draw_arrow(ax, 0, 6, 0, 4)
draw_arrow(ax, 0, 4, 0, 2)
draw_arrow(ax, 0, 2, 0, 0)

# Save the plot as an image file
plt.savefig(r'C:\Users\e442532\Desktop\CSU_GRADUATE_CODE\csc_500_prin_of_prg\MODULE1\flowchart_partial.png')
