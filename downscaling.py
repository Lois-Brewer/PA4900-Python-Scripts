# Imports
from PIL import Image
import os

# Load the image
im_repo = "B"

# For image in directory resize to 650x650 pixels
for im in os.listdir(im_repo):
    image = Image.open(f"{im_repo}/" + f"{im}")
    downscaled_image = image.resize((650, 650))
    downscaled_image.save(f"{im_repo}/" + f"{im}")

