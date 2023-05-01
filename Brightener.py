# Imports
from PIL import Image, ImageEnhance
import os

# Iterates through images in a directory and brightens them up significantly
for image in os.listdir(""):
    img = Image.open(f"{image}.png").convert("RGB")
    img_enhancer = ImageEnhance.Brightness(img)
    enhanced_output = img_enhancer.enhance(500)
    enhanced_output.save("bright_output/{image}.png")
