"""Collage"""
import os
import cv2 as cv
import numpy as np

CANVAS = []
HEIGHTS = []
WIDTHS = []

f = ""
while f == "":
    f = input("""1 - PNG;
2 - JPG;
3 - BMP;
Choose the necessary image extension: """)
    if f == 1:
        FORMAT = ".png"
    elif f == 2:
        FORMAT = ".jpg"
    elif f == 3:
        FORMAT = ".bmp"

# Path to the working directory;
image_dir = os.getcwd() + "/Images"
collage_dir = os.getcwd() + "/Collage"

# The list of files in the directory;
files = os.listdir(image_dir)

# Get only the images from files list with FORMAT

images = [img for img in files if img.endswith(FORMAT)]

# Checking the existence of necessary files;
if len(images) == 0:
    print("No {0} files in {1}".format(FORMAT, directory))
    quit()
num_of_img = len(images)

# Get the shapes of images
for image in images:
    img = cv.imread(image)
    HEIGHTS.append(img.shape[0])
    WIDTHS.append(img.shape[1])

width = max(WIDTHS)
height = max(HEIGHTS)

# Create an a blank canvas
CANVAS = np.zeros((height * num_of_img, width, 3), np.uint8)
CANVAS[::] = (255,255,255)
for image in images:
    img = cv.imread(image)
    h_img = img.shape[0]
    w_img = img.shape[1]
    for h in range(height, height * num_of_img, height):
        CANVAS[h:h + h_img, :w_img] = img[:, :]
collage = CANVAS[:]
cv.imwrite(collage_dir + "/1.png", collage)

