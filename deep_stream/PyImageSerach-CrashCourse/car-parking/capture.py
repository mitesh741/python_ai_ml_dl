import threading
import cv2
import time

class VideoCaptureTreading:
    def __init__(self, src=0, width=1280, height=720):
        # self.src = "./car_parking_1.mp4"
        self.src = src
        self.cap = cv2.VideoCapture(self.src)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.grabbed, self.frame = self.cap.read()
        # self.frame = self.frame[1]
        self.started = False
        self.read_lock = threading.Lock()

    def set(self, var1, var2):
        self.cap.set(var1, var2)

    def start(self):
        if self.started:
            print('[!] Threaded video capturing has already been started.')
            return None
        self.started = True
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.start()
        return self

    def update(self):
        while self.started:
            grabbed, frame = self.cap.read()
            if frame is None:
                print("Child Thread: End of Video File...............")
                self.started = False
                break
            with self.read_lock:
                self.grabbed = grabbed
                self.frame = frame
                time.sleep(1/(self.fps)) 

    def read(self):
        with self.read_lock:
            frame = self.frame.copy()
            grabbed = self.grabbed
        return grabbed, frame

    def stop(self):
        self.started = False
        self.thread.join()

    def __exit__(self, exec_type, exc_value, traceback):
        self.cap.release()
