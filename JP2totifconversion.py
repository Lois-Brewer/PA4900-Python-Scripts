# Imports
from PIL import Image, ImageOps
import os

min_size = 1830

# define the directory containing the images
dir_path = 'img1'

for image in os.listdir(dir_path):
    # define the path to the JP2 file and open it with Pillow
    jp2_path = f'img1/{image}'
    with Image.open(jp2_path) as jp2:
        # convert the JP2 image to TIFF format
        tif = jp2.convert('RGB')

        # save the compressed TIFF image to a new file
        tif.save(f'converted/img1/{name}.tif')
