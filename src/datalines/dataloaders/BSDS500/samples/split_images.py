# Split images
"""
    Demonstrate splitting images into BSDS68 + 432

    Creator: TheProjectsGuy
"""

# %% Import everything
import numpy as np
from matplotlib import pyplot as plt
from datalines.dataloaders.BSDS500 import load_data, load_imgs

# %% Load data
data = load_data()

# %% Split
train_imgs, test_imgs = load_imgs(data)
print(f"Split has {len(test_imgs)} test and {len(train_imgs)} "
    "training samples")
all_images = load_imgs(data, split_data=False)  # Return all images
print(f"There are a total of {len(all_images)} images")

# %%
