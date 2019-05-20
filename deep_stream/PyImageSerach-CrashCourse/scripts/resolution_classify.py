import cv2
import glob
import os
import imutils
import glob

hd_dir = "hd_single_object"
# Create target Directory if don't exist
if not os.path.exists(hd_dir):
    os.mkdir(hd_dir)
    print("HD Directory " , hd_dir ,  " Created \n")
else:    
    print("HD Directory " , hd_dir ,  " already exists\n")


sd_dir = "sd_single_object"
# Create target Directory if don't exist
if not os.path.exists(sd_dir):
    os.mkdir(sd_dir)
    print("SD Directory " , sd_dir ,  " Created\n ")
else:    
    print("SD Directory " , sd_dir ,  " already exists\n")

for filename in glob.iglob('*.jpg'):
    print(filename )
    image = cv2.imread(filename)
    (h, w, d) = image.shape
    print("width={}, height={} ".format(w, h))
   
    if (w <= 500) or (h <= 500) :
        os.rename(filename , os.getcwd() + "/" + sd_dir + "/" + filename.split(os.path.sep)[-1] )
        print("moved to SD\n")
    elif (w >= 800) or (h >= 600) :
        os.rename(filename , os.getcwd() + "/" + hd_dir + "/" + filename.split(os.path.sep)[-1] )
        print("moved to HD\n")
    else:
        print("NOT MOVED\n")

