#import the necessary packages
import numpy as np
import argparse
import cv2

#construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to inout image")
ap.add_argument("-p", "--prototxt", required=True, help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True, help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.5, help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
#reads Model

# load the input image and construct an input blob for the image
# by resizing to a fixed 300x300 pixels and then normalizing it
image = cv2.imread(args["image"])
(h, w) = image.shape[:2] # returns (row,column,channel) here we take only row and column
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,(300, 300), (104.0, 177.0, 123.0))
#blobFromImage(Input image, scaleFactor,spatial size that the Convolutional Neural Network expects, mean value as RGB, swapRB = TRUE )
#swapRB swaps R and B. Mean values as RGB and OpenCV as BGR

# pass the blob through the network and obtain the detections and
# predictions
print("[INFO] computing object detections...")
net.setInput(blob) #Sets the new value for the layer output blob
detections = net.forward()#Runs forward pass to compute output of layer. Returns blob for first output of specified layer

print("Detection : \n{}".format(detections))
print("Detection Shape : \n{}".format(detections.shape))
print("Width & Height  : {} & {}".format(w,h))

# loop over the detections
for i in range(0, detections.shape[2]):
    # extract the confidence (i.e., probability) associated with the
    # prediction
    # print("Detections[0,0,{},2] : {}".format(i,detections[0,0,i,2]))

    confidence = detections[0, 0, i, 2]

    # filter out weak detections by ensuring the `confidence` is
    # greater than the minimum confidence
    if confidence > args["confidence"]:
        # compute the (x, y)-coordinates of the bounding box for the
        # object
        print("\n\nDetections[0,0,{},3:7] : {}".format(i,detections[0,0,i,3:7]))

        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        print("\n\nBox {}: {}".format(i,box))

        (startX, startY, endX, endY) = box.astype("int")

        print("\n\nBox {}: {}".format(i,box.astype("int")))
        
        # draw the bounding box of the face along with the associated
        # probability
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(image, (startX, startY), (endX, endY),(0, 0, 255), 2)
        cv2.putText(image, text, (startX, y),
        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

        # show the output image
        cv2.imshow("Output", image)
        cv2.waitKey(0)
