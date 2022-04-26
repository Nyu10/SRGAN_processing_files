"""
num_channels.py
Find number of channels in your image.
Author: liuhh02 https://machinelearningtutorials.weebly.com/
"""

from PIL import Image
import numpy as np

# name of your image file
filename = './dataset/1000_raw/0AA9XP3MFSEX_0_1568.tiff'

# open image using PIL
img = Image.open(filename)

# convert to numpy array
img = np.array(img)

# find number of channels
if img.ndim == 2:
    channels = 1
    print("image has 1 channel")
else:
    channels = image.shape[-1]
    print("image has", channels, "channels")