"""Collage"""
import os
import cv2 as cv
import numpy as np

CANVAS = []
HEIGHTS = []
WIDTHS = []

collage_dir = os.getcwd() + "/Collages"

# Choosing the format;
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
print("Working format is *{0}".format(FORMAT))

for i in range(1, 64):
    # Path to the working directory;
    image_dir = "{0}/{1}".format(os.getcwd(), i)        

    # The list of files in the directory;
    try:
        files = os.listdir(image_dir)
    except OSError as e:
        print(e)
        continue
        
    # Get only the images from files list with FORMAT;
    images = [img for img in files if img.endswith(FORMAT)]
        
    # Checking the existence of necessary files;
    if len(images) == 0:
        print("No *{0} files in {1}".format(FORMAT, image_dir))
        continue

    # Print files in image directory;
    print("\nThe list of *{0} files in \n'{1}'".format(FORMAT, image_dir))
    for img in sorted(images):
        print(img)

    num_of_img = len(images)

    # Get the shapes of images
    for image in images:
        image = "{0}/{1}".format(image_dir, image)
        img = cv.imread(image)
        HEIGHTS.append(img.shape[0])
        WIDTHS.append(img.shape[1])

    width = max(WIDTHS)
    height = max(HEIGHTS)

    # Create an a blank canvas
    CANVAS = np.zeros((height * num_of_img, width, 3), np.uint8)
    CANVAS[::] = (255,255,255)
    h = 0
    for image in sorted(images):
        image = "/{0}/{1}".format(image_dir, image)
        print(image)
        img = cv.imread(image)
        h_img = img.shape[0]
        w_img = img.shape[1]
        CANVAS[h:h + h_img, :w_img] = img[:, :]
        h += height
    collage = CANVAS[:]
    cv.imwrite(collage_dir + "/1.png", collage)
    print("Succesfully created!")
print("Collages saved in:\n{0}".format(collage_dir))


