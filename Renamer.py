# Imports
import os
import cv2

file_names = []

# Puts file names in directory in list
for file in os.listdir("test/time1"):
    if ".png" in file:
        file_names.append(file)

# Renames each file name stored in list
with open(r'file.txt', 'w') as fp:
    for item in file_names:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')