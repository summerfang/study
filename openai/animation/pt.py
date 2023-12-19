import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a perfect binary tree with 5 levels
tree = nx.balanced_tree(2, 4)

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(8, 8))

# Function to update the plot for each frame of the animation
def update(frame):
    ax.clear()
    pos = nx.nx_agraph.graphviz_layout(tree, prog='dot')
    nx.draw(tree, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=12, font_color='black', edge_color='gray')

# Create the animation
animation = FuncAnimation(fig, update, frames=range(10), interval=1000)

# Save the animation as a video file
animation.save('perfect_binary_tree.mp4', writer='ffmpeg')

# Show the plot
plt.show()