
import cv2
import glob
import os


for filename in glob.iglob('*.jpg'):
    print(filename)
    image = cv2.imread(filename)
    resized = cv2.resize(image, (300, 300))
    cv2.imwrite( filename, resized)
