import math

import object_detector
import cv2
import Detection_profiles


def RecognitionObject(self, frame, frame1, frame2):
    while True:
        nbobjects = []
        coordObjectsx = []
        coordObjectsy = []
        coordObjects = []
        count = 0

        # the coordinate that we use for the servo mapping
        xservo = 0
        yservo = 0

        data = object_detector.object_detector(frame)

        diff = cv2.absdiff(frame1, frame2)
        diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(diff_gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for d in data:
            x, y = d[2]

            if Detection_profiles.objectischecked[d[0]] == True:
                x, y = d[2]

                count += 1
                nbobjects.append(count)
                coordObjects.append(d[2])
                coordObjectsx.append(x)
                coordObjectsy.append(y)
                # Here we calculate the midpoint if there is more than one object
                if max(nbobjects) > 1:
                    xm = sum(coordObjectsx) / len(coordObjectsx)
                    ym = sum(coordObjectsy) / len(coordObjectsy)
                    xservo = math.ceil(xm)
                    yservo = math.ceil(ym)
                    print(xservo, yservo)
                else:
                    xservo = x
                    yservo = y

                self.mapServoPosition(xservo, yservo)

            for contour in contours:

                (x, y, w, h) = cv2.boundingRect(contour)
                if cv2.contourArea(contour) < 900:
                    continue
                # cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0),
                            3)



        return frame


