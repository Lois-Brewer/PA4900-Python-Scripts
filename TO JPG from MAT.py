import numpy as np
import scipy.io as sio
from PIL import Image
import matplotlib.pyplot as plt

# Load the .mat file
data = sio.loadmat('demoData.mat')

# Loop through the variables in the .mat file
for var_name, var_content in data.items():
    if var_name == "preChangeImage" or var_name =="postChangeImage":
        var_content = var_content.astype(float)
        print(var_content.dtype)
        # Create a PIL image from the array
        img = Image.fromarray(var_content)
        # Display the image using matplotlib
        plt.imshow(img)
        plt.show()
        # Save the image using PIL
        img.save(f'data/{var_name}.jpg')