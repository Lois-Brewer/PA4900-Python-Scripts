# Imports
import cv2
import numpy as np

# Reads image as a greyscale input, to read as a 1D numpy array
img = cv2.imread('Figure_12.png', cv2.IMREAD_GRAYSCALE)

# Calculates number of white pixels then divides by total number of pixels in image
n_white_pix = np.sum(img == 255)
print(n_white_pix/(img.size)*100)

