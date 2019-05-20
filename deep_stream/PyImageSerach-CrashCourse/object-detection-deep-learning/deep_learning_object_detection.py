# USAGE
# python deep_learning_object_detection.py --images_path images/ \
#	--prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel

# import the necessary packages
import xml.etree.ElementTree as ET
import numpy as np
import argparse
import cv2
from imutils import paths
import shutil
import copy
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images_path", required=True,
	help="path to input images")
ap.add_argument("-p", "--prototxt", required=True,
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
	help="minimum probability to filter weak detections")
ap.add_argument("-s", "--show_image", default="n",
	help="show image with detected boxes, give 'y' to enable")
ap.add_argument("--sample_xml", required=True,
	help="Sample XML file")
args = vars(ap.parse_args())

# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

sample_xml = args["sample_xml"]
# load the input image and construct an input blob for the image
# by resizing to a fixed 300x300 pixels and then normalizing it
# (note: normalization is done via the authors of the MobileNet SSD
# implementation)

for imagePath in paths.list_images(args["images_path"]):
	print("Filepath : {}".format(imagePath))
	image = cv2.imread(imagePath)
	(h, w) = image.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
	# pass the blob through the network and obtain the detections and
	# predictions
	print("[INFO] computing object detections...")
	net.setInput(blob)
	detections = net.forward()
	number_of_detections = 0
	first_object_index = 5
	# loop over the detections
	root = None
	et = None
	new_xml = ""
	is_object_detected = False
	for i in np.arange(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with the
		# prediction
		confidence = detections[0, 0, i, 2]

		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
		if confidence > args["confidence"]:
			# extract the index of the class label from the `detections`,
			# then compute the (x, y)-coordinates of the bounding box for
			# the object
			idx = int(detections[0, 0, i, 1])
			if idx == 14:
				is_object_detected = True
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")
				# display the prediction
				label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
				new_xml = imagePath.split(".")[0] + ".xml"
				number_of_detections += 1
				first_object_index += 1
				
				if number_of_detections == 1:
					
					shutil.copy2(sample_xml,new_xml)
					et = ET.parse(new_xml)
					root = et.getroot()
					
					root[2].text = imagePath 
					root[1].text = imagePath.split("/")[-1]
					root[0].text = imagePath.split("/")[-2]

				# To append Object in Root when multiple objects are detected in a single image
				new_tag = None

				if( number_of_detections > 1) :
					new_tag = copy.deepcopy(root[first_object_index -1])

				if new_tag != None :
					# ET.dump(root)		#To print XML format data on console
					new_tag[4][0].text = str(startX)
					new_tag[4][1].text = str(startY)
					new_tag[4][2].text = str(endX)
					new_tag[4][3].text = str(endY)
					root.insert(first_object_index, new_tag)
				else :
					root[first_object_index][4][0].text = str(startX)
					root[first_object_index][4][1].text = str(startY)
					root[first_object_index][4][2].text = str(endX)
					root[first_object_index][4][3].text = str(endY)

				cv2.rectangle(image, (startX, startY), (endX, endY),COLORS[idx], 2)
				y = startY - 15 if startY - 15 > 15 else startY + 15
				cv2.putText(image, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
	if is_object_detected == True:
		print("Writing XML file : {}".format(new_xml))
		et.write(new_xml)
	else: 
		print("Deleting file: {}".format(imagePath))
		if os.path.exists(imagePath):
   			os.remove(imagePath)
		else:
			print("The file does not exist")



	# show the output image
	if args["show_image"] != "n":
		cv2.imshow("Output", image)
		cv2.waitKey(0)
		