from __future__ import print_function
"""
Command: /home/ankit/.virtualenvs/cv/bin/python /home/Project/ankit/DL/demo/app/car_counter.py \
--input /home/ankit/Downloads/car_lanes_cctv_cam.mp4 --classes 1 --model \
/home/Project/ankit/DL/cars_training/colab/trained_ssd_mobilenet_colab/13259/frozen_inference_graph.pb --labels \
/home/Project/ankit/DL/cars_dataset/cars_300x300_data/label_map.pbtxt --skip-frames 2 --num-workers=1 --queue-size=128
"""

# import the necessary packages
from support.centroidtracker import CentroidTracker
from support.trackableobject import TrackableObject
from imutils.video import FPS
import numpy as np
import time
import dlib
import tensorflow as tf
import cv2

import argparse
import src.detect_with_tf as dtf
# from utils.app_utils import *
# from utils.objDet_utils import *
from multiprocessing import Queue, Pool, Lock
from queue import PriorityQueue
import matplotlib.path as mpltPath
import copy
import threading
from queue import Queue

# ==================================================================================================
#                       Construct the argument parser and parse the arguments
# ==================================================================================================

ap = argparse.ArgumentParser()
ap.add_argument("--input", required=True, type=str, help="path to input video file")
ap.add_argument("--output", type=str, help="path to optional output video file")
ap.add_argument("--confidence", type=float, default=0.4, help="minimum probability to filter weak detections")
ap.add_argument("--skip-frames", type=int, default=30, help="# of skip frames between detections")
ap.add_argument("--classes", required=True, type=int, help="number of classes for which model is trained")
ap.add_argument("--model", required=True, help="path to tensorflow pre-trained model file with .pb extension")
ap.add_argument("--labels", required=True, help="path to labels file with .pbtxt extension")
ap.add_argument("--display", type=int, default=1, help="Whether or not frames should be displayed")
ap.add_argument("--num-workers", dest='num_workers', type=int, default=1, help='Number of workers.')
ap.add_argument("--queue-size", dest='queue_size', type=int, default=128, help='Size of the queue.')
ap.add_argument("--logger-debug", dest='logger_debug', type=int, default=0, help='Print logger debug')
ap.add_argument("--fullscreen", dest='full_screen', type=int, default=0, help='enable full screen')
args = vars(ap.parse_args())

# ==================================================================================================
#                                       Global variables
# ==================================================================================================

PATH_TO_CKPT = args["model"]
PATH_TO_LABELS = args["labels"]
NUM_CLASSES = args["classes"]
TEST_VIDEO_PATH = args["input"]
DETECTION_GRAPH = None
OUTPUTS = []

# start the frames per second throughput estimator
fps = FPS().start()

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
# ==================================================================================================
#                                       Load the model and labels
# ==================================================================================================

# DETECTION_GRAPH = dtf.load_model(PATH_TO_CKPT)
dtf.load_labels(PATH_TO_LABELS, NUM_CLASSES)
dtf.set_confidence(args["confidence"])

# ==================================================================================================
#                                       Init video stream of video
# ==================================================================================================
vs = cv2.VideoCapture(TEST_VIDEO_PATH)
time.sleep(2.0)

# ==================================================================================================
#                                       Process tracking and detection on Frame
# ==================================================================================================


def process_frame(frame, detection_graph, sess, lock):
    global OUTPUTS,  fps, counter, firstX, firstY, flag, list_of_centroids, list_of_detections, num_of_cars_not_parked, num_of_cars_parked, num_of_detections

    list_of_detections.clear()
    list_of_centroids.clear()
    num_of_cars_parked = 0 
    num_of_cars_not_parked  = 0 

    # if we are viewing a video and we did not grab a frame, then we have reached the end of the video
    if frame is None:
        print("Video completed..!!")
        return None

    im_width = frame.shape[1]
    im_height = frame.shape[0]

    # convert the frame from BGR to RGB for dlib
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # check to see if we should run a more computationally expensive
    # object detection method to aid our tracker
    # set the status and initialize our new set of object trackers
    # status = "Detecting"

    num_detections, detection_classes, detection_boxes, detection_scores = dtf.run_inference_on_frame(frame, detection_graph, sess)

    # lock.acquire()
    for index in range(0, detection_boxes.shape[0]):
        if (detection_scores[index]*100) < (args["confidence"]*100):
            break
        OUTPUTS.append(tuple((detection_boxes[index], detection_classes[index], detection_scores[index]*100)))

    for OUTPUT in OUTPUTS:
        detect_rects = []
        (ymin, xmin, ymax, xmax) = OUTPUT[0]
        xmin = int(xmin*im_width)
        ymin = int(ymin*im_height)
        xmax = int(xmax*im_width)
        ymax = int(ymax*im_height)
        center_x = (xmin + xmax) // 2
        center_y = (ymin + ymax) // 2
        cv2.circle(frame, (center_x, center_y), 4, (0, 255, 0), -1)
        detect_rects.insert(0, (xmin, ymin)) # add Each coordinates
        detect_rects.insert(1, (xmax, ymax)) # add Each coordinates
        list_of_detections.append(copy.deepcopy(detect_rects))

    num_of_detections = len(OUTPUTS)

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
        cv2.putText(frame, text_available , (30, 30),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
        cv2.putText(frame, text_not_available , (30, 60),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

    for n in range(len(list_of_rects)):
        pts = np.array(list_of_rects[n][0], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(frame ,[pts],True, color = list_of_rects[n][1],thickness = 2 ) # list_of_rects is list of tuple(rect, color)     
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

    # increment the total number of frames processed thus far and
    # then update the FPS counter
    fps.update()

    OUTPUTS.clear()
    return frame


# Define worker thread (to be executed as multiple processes)
def worker(input_q, output_q, lock):
    global fps, vs

    # cv2.namedWindow('object_detection')
    # cv2.setMouseCallback('object_detection',mouseCallback)
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
        sess = tf.Session(graph=detection_graph)
    print("Print from worker..!!")
    while True:
        frame = input_q.get()
        if frame is None:
            break
        # Check frame object is a 2-D array (video) or 1-D (webcam)
        if len(frame) == 2:
            # frame_rgb = cv2.cvtColor(frame[1], cv2.COLOR_BGR2RGB)
            processed_frame = process_frame(frame[1], detection_graph, sess, lock)
            output_q.put((frame[0], processed_frame))
        else:
            # frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            processed_frame = process_frame(frame, detection_graph, sess, lock)
            output_q.put(processed_frame)
    # stop the timer and display FPS information
    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    vs.release()

    # close any open windows
    cv2.destroyAllWindows()



def start_app():
    # Multiprocessing: Init input and output Queue, output Priority Queue and pool of workers
    input_q = Queue(maxsize=args["queue_size"])
    output_q = Queue(maxsize=args["queue_size"])
    output_pq = PriorityQueue(maxsize=3 * args["queue_size"])
    lock = Lock()

    # pool = Pool(args["num_workers"], worker, (input_q, output_q, lock))
    for i in range(args["num_workers"]):
        t = threading.Thread(target=worker, args=(input_q,output_q, lock))
        t.daemon = True
        t.start()
        
    cv2.namedWindow('object_detection')
    cv2.setMouseCallback('object_detection',mouseCallback)

    
    # cv2.setMouseCallback('frame',mouseCallback)

    countReadFrame = 0
    countWriteFrame = 1
    nFrame = int(vs.get(cv2.CAP_PROP_FRAME_COUNT))
    firstReadFrame = True
    firstTreatedFrame = True
    firstUsedFrame = True
    while True:

        # Check input queue is not full
        if not input_q.full():
            # Read frame and store in input queue
            ret, frame = vs.read()
            if ret:
                input_q.put((int(vs.get(cv2.CAP_PROP_POS_FRAMES)), frame))
                countReadFrame += 1
                if firstReadFrame:
                    print(" --> Reading first frames from input file. Feeding input queue.\n")
                    firstReadFrame = False

        # Check output queue is not empty
        if not output_q.empty():
            # Recover treated frame in output queue and feed priority queue
            output_pq.put(output_q.get())
            if firstTreatedFrame:
                print(" --> Recovering the first treated frame.\n")
                firstTreatedFrame = False


        # Check output priority queue is not empty
        if not output_pq.empty():
            prior, output_frame = output_pq.get()
            if prior > countWriteFrame:
                output_pq.put((prior, output_frame))
            else:
                countWriteFrame = countWriteFrame + 1

                # Display the resulting frame
                if args["display"]:
                    cv2.imshow('object_detection', output_frame)
                    # fps.update()

                if firstUsedFrame:
                    print(" --> Start using recovered frame (displaying and/or writing).\n")
                    firstUsedFrame = False

        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

        print("Read frames: %-3i %% -- Write frame: %-3i %%" % (int(countReadFrame / nFrame * 100), int(countWriteFrame / nFrame * 100)),
              end='\r')
        if (not ret) & input_q.empty() & output_q.empty() & output_pq.empty():
            break

    print("\nFile have been successfully read and treated:\n  --> {}/{} read frames \n  --> {}/{} write frames \n".format(
        countReadFrame, nFrame, countWriteFrame - 1, nFrame))

    # When everything done, release the capture
    fps.stop()
    print("FPS =", fps.fps())
    # pool.terminate()
    # pool.join()
    vs.release()
    cv2.destroyAllWindows()


start_app()
# for OUTPUT in OUTPUTS:
#       print("OUTPUT : {}".format(OUTPUT))
# NOTE 1:-
# OUTPUTS[0] = detection_boxes
# OUTPUTS[1] = detection_classes
# OUTPUTS[2] = detection_scores

# NOTE 2:-
# To draw box from normalized coordinates, below is the format to get the points
# im_width = frame.shape[1], im_height = frame.shape[0]
# ymin, xmin, ymax, xmax = box
# (xmin * im_width, xmax * im_width, ymin * im_height, ymax * im_height)
