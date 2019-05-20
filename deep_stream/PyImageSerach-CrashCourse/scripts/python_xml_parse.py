"""
Usage : image_xml_dir = absolute path of images folder
python python_xml_parse.py --image_xml_dir /home/Project/ankit/DL/cars_dataset/cars_300x300/train
"""
import xml.etree.ElementTree 
import os
#from imutils import paths
import glob
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image_xml_dir", required=True,
	help="path of directory where xml and images are stored")

args = vars(ap.parse_args())

for filepath in glob.iglob(args["image_xml_dir"] + '/*.xml'):

    et = xml.etree.ElementTree.parse(filepath)

    root = et.getroot()

    new_path = os.path.abspath(args["image_xml_dir"])+ "/"  + root[1].text
    print("new_path: " + new_path )
    
    root[2].text = new_path
    root[0].text = new_path.rsplit('/')[-2]

    # et.write(root[1].text.rsplit('.',1)[0] + ".xml")
    et.write(args["image_xml_dir"] + "/" + root[1].text.rsplit('.',1)[0]  + ".xml")