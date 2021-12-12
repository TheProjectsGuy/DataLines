# View images and ground truth
"""
    View the images and ground truth information for BSDS500 
    dataloader

    Creator: TheProjectsGuy
"""

# %% Import everything
import numpy as np
from matplotlib import pyplot as plt
# Load data through function call
from datalines.dataloaders.BSDS500 import load_data

# %% Load data
data = load_data()  # Download and load everything as dict
# Data segment to visualize
vset = "training"   # "training", "test", or "validation"
viz_data = data[vset]

# %% Pick a random sample from set
# Random point
n = np.random.randint(0, len(viz_data['images']))
# Fetch image, annotator segmentation and border list
img_data = viz_data['images'][n]
segs_data = viz_data['groundTruth']['segmentation'][n]
bdrs_data = viz_data['groundTruth']['boundaries'][n]
print(f"Visualizing {vset} set's sample {n}")
num_anns = viz_data['groundTruth']['na'][n]
print(f"Sample has {num_anns} annotators")
print(f"Image can be found at '{viz_data['paths']['img'][n]}'")
print(f"Annotations can be found at '{viz_data['paths']['gt'][n]}'")

# %% Visualize the data-point using matplotlib
fig = plt.figure("BSDS500 Random Sample", figsize=(12, 6.5))
fig.suptitle(f"Image: {viz_data['paths']['img'][n]}\n"
    f"Annotations: {viz_data['paths']['gt'][n]}") # Title
gs = fig.add_gridspec(2, num_anns+1)    # Grid
ax = fig.add_subplot(gs[:, 0])  # First column
ax.imshow(img_data)
ax.set_axis_off()
ax.set_title(f"Image {n}")
# For each annotator
for i in range(num_anns):
    # Segmentation
    ax = fig.add_subplot(gs[0, i+1])
    ax.imshow(segs_data[i])
    ax.set_title(f"Seg {i}")
    ax.set_axis_off()
    # Boundaries
    ax = fig.add_subplot(gs[1, i+1])
    ax.imshow(bdrs_data[i], cmap='gray')
    ax.set_title(f"Bdr {i}")
    ax.set_axis_off()
fig.tight_layout()
plt.show()

# %%
