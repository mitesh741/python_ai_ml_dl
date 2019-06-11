import cv2
import numpy as np
import copy
import argparse
from imutils.video import VideoStream
from imutils.video import FPS
import time
import matplotlib.path as mpltPath
import imutils
import threading

# ==================================================================================================
#       Command line arguments
# ==================================================================================================
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True, help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True, help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2, help="minimum probability to filter weak detections")
ap.add_argument("-v", "--video",help="path to the (optional) video file")
args = vars(ap.parse_args())

# ==================================================================================================
#       Variables
# ==================================================================================================
flag = False
flag_is_centroid = False
counter = 0
(firstX, firstY) = (-1 , -1)
(startX, startY) = (-1 ,-1)
(endX, endY) = (-1,-1)
list_of_rects = [] 
rect = []
list_of_detections = []
empty_parking_spots = 0
num_of_cars_parked  = 0
num_of_cars_not_parked = 0
num_of_detections = 0
centroid_x  = 0 
centroid_y  = 0 
list_of_centroids = []
RED_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 255, 0)
text_available = ""
text_not_available = ""

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat","bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep","sofa", "train", "tvmonitor"]

COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# ==================================================================================================
#       Mouse call back function
# ==================================================================================================
def mouseCallback(event, x, y, flags, param):
    global endX, firstX ,firstY, endY, counter, startX, startY
    if event == cv2.EVENT_LBUTTONDOWN:
        endX = x
        endY = y

        if counter == 0:
            (startX,startY) = (x,y)
        counter = counter + 1


# ==================================================================================================
#       Find centroids of detections in each frames if any (detections)
# ==================================================================================================
def centroid_of_detections(coordinates):
    centroid_x = 0
    centroid_y = 0
    for j in range(len(coordinates)):
        for k in range(2):
            (x,y) = coordinates[j][k]
            centroid_x = centroid_x + x 
            centroid_y = centroid_y + y
        centroid = (centroid_x / 2, centroid_y / 2)
        list_of_centroids.insert(j, centroid)
        (centroid_x, centroid_y) = (0, 0)
    return list_of_centroids

cv2.namedWindow('frame')
cv2.setMouseCallback('frame',mouseCallback) # mouse callback has to be set only once

if not args.get("video", False):  # if a video path was not supplied, grab the reference to the webcam
    vs = VideoStream(src=0).start()
else:     # otherwise, grab a reference to the video file
    vs = cv2.VideoCapture(args["video"])
time.sleep(2.0) # allow the camera or video file to warm up

fps = FPS().start()

# ==================================================================================================
#       Keep taking frames from video source until last frame or 'q' key is pressed
# ==================================================================================================
while True:
    list_of_detections = []
    list_of_centroids = []
    img = vs.read()
    img = img[1] if args.get("video", False) else img # handle the frame from VideoCapture or VideoStream
    num_of_cars_parked = 0 
    num_of_cars_not_parked  = 0 
    if img is None: # If no frame is acquired then video ended
        break
# ==================================================================================================
#        Inference logic will go here
# ==================================================================================================
    img = imutils.resize(img, width=1080)
	# grab the frame dimensions and convert it to a blob
    (h, w) = img.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)),0.007843, (300, 300), 127.5)

    net.setInput(blob)
    detections = net.forward()

    # loop over the detections
    num_of_detections = detections.shape[2]
    for l in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, l, 2]
        if confidence > args["confidence"]:
           idx = int(detections[0, 0, l, 1])
           if idx == 7:
               detect_rects = []
               box = detections[0, 0, l, 3:7] * np.array([w, h, w, h])
               (rect_startX, rect_startY, rect_endX, rect_endY) = box.astype("int")
               centre =( (rect_startX+rect_endX)//2 , (rect_startY+rect_endY)//2 )
               cv2.circle(img, centre, 10, (255, 0, 0), -5)
               detect_rects.insert(0, (rect_startX, rect_startY)) # add Each coordinates
               detect_rects.insert(1, (rect_endX, rect_endY)) # add Each coordinates
               list_of_detections.append(copy.deepcopy(detect_rects))

# ==================================================================================================
#        Check If Centroid of detected object is inside drawn quadrilaterals
# ==================================================================================================
    if len(list_of_rects) > 0 :   # Only if User has drawn parking slots
        list_of_centroids = centroid_of_detections(list_of_detections)                
        for i in range(len(list_of_rects)):
            for m in range(len(list_of_centroids)):
                verts = list_of_rects[i][0]
                path = mpltPath.Path(verts)
                (x,y) = list_of_centroids[m]
                inside = path.contains_points([[x,y]])
                if True == inside:
                    tup = (list_of_rects[i][0] , RED_COLOR)
                    list_of_rects[i] = tup
                    num_of_cars_parked += 1
                    break
                else:
                    tup = (list_of_rects[i][0] , GREEN_COLOR)
                    list_of_rects[i] = tup
                    num_of_cars_not_parked += 1

# ==================================================================================================
#       Draw updated quadrilaterals and Text on each frame
# ==================================================================================================
    if num_of_detections > 0 :
        text_available = "Parking spots available: " + str(len(list_of_rects) - num_of_cars_parked)
        text_not_available = "Parking spots occupied: " + str(num_of_cars_parked)
        cv2.putText(img, text_available , (30, 30),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(img, text_not_available , (30, 60),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    for n in range(len(list_of_rects)):
        pts = np.array(list_of_rects[n][0], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True, color = list_of_rects[n][1],thickness = 2 ) # list_of_rects is list of tuple(rect, color)  

# ==================================================================================================
#       Draw new quadrilaterals and append in list
# ==================================================================================================
    if (counter != 0) and (counter != 1): 
        if counter == 2:
            point1 = (startX,startY)
            point2 = (endX,endY)
            if flag == False:
                rect.insert(0, point1)
                rect.insert(1, point2)
                (firstX,firstY) = (endX,endY) 
                flag = True
        if counter == 3:
            if flag == True:
                point3 = (endX,endY)
                rect.insert(2, point3)
                (firstX,firstY) = (endX,endY) 
                flag = False
        if counter == 4 :
            point4 = (endX,endY)
            if False == flag:
                rect.insert(3, point4)
                list_of_rects.append(copy.deepcopy(rect))
                tup = (list_of_rects[-1] , GREEN_COLOR)
                list_of_rects[-1] = tup
                rect.clear()
                counter = 0

# ==================================================================================================
#       Display each frame until Key 'q' is pressed
# ==================================================================================================

    cv2.imshow('frame', img)
    key = cv2.waitKey(40) & 0xFF
    if key == ord("q"):
        break
# ==================================================================================================
#       Destroy all opened windows
# ==================================================================================================
cv2.destroyAllWindows()
