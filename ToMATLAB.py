import numpy as np
from scipy import io as sio
import imageio

# Load the images as numpy arrays
img1 = imageio.v2.imread('before.png')
img2 = imageio.v2.imread('after.png')



# Save the data in a MATLAB file
sio.savemat('images.mat', mdict={'preChangeImage': img1, "postChangeImage":img2})
