import cv2
from threading import Thread
from Object_Recognition import RecognitionObject


class Main(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(Self):
        cap = cv2.VideoCapture("http://192.168.137.188:8080/?action=stream")
        ret, frame = cap.read()
        ret, frame1 = cap.read()
        ret, frame2 = cap.read()
        while True:
            RecognitionObject(frame, frame1, frame2)
            cv2.imshow('berry', RecognitionObject())
        cap.release()
        cv.destroyAllWindows()


thread1 = Main()

thread1.start()

thread1.join()
