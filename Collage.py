"""Collage"""
import os
import cv2 as cv
import numpy as np

CANVAS = []
HEIGHTS = []
WIDTHS = []

FORMAT = str(input("Enter the images format: "))

if os.uname()[0] == "Linux":
    # Path to work directory;
    directory = os.getcwd()
    # The list of files in the directory;
    files = os.listdir(directory)
    # Get only the images from files list with FORMAT
    images = [img for img in files if img.endswith(FORMAT)]
    l_img = len(images)
    # Get the shapes of images 

    for image in images:
        img = cv.imread(image)
        HEIGHTS.append(img.shape[:1])
        WIDTHS.append(img.shape[1:2])

    width = max(WIDTHS)[0]
    height = max(HEIGHTS)[0]

    # Create an a blank canvas
    CANVAS = np.zeros((height * l_img, width, 3), np.uint8)
    CANVAS[::] = (255,255,255)  
    for image in images:
        img = cv.imread(image)
        for h in range(0, height * l_img , height):
            CANVAS[h:h + height] = img[:]
    collage = CANVAS[:]
    cv.imwrite("Collage.bmp", collage)
