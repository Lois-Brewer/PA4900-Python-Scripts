# Imports
import numpy as np
from PIL import Image, ImageChops

# Load the images
img1 = Image.open("img1.jpeg")
img2 = Image.open("img2.jpg")

# Convert pmg1 and img2 to numpy array
arr1 = np.array(img1)
arr2 = np.array(img2)

# Calculate the image colour difference
diff = np.abs(arr1 - arr2).sum(axis=2)
print(diff)

# Can set and adjust the threshold here
threshold = 400

# Create a mask in black and white
mask = (diff > threshold).astype(np.uint8) * 255

# Covert to image (jpg) format
result = Image.fromarray(mask, mode="L")
inv_img = ImageChops.invert(result)

# Save the image
inv_img.save("result.png")
