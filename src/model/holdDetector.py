import cv2
import numpy as np
from model.classes import Hold


class HoldDetector:
    def detect(self, frame):
        # yellow pixels (for now)

        yellow = (
            (frame[:, :, 2] > 150) &
            (frame[:, :, 1] > 150) &
            (frame[:, :, 0] < 100)
        ).astype(np.uint8) * 255

        contours, _ = cv2.findContours(
            yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE

        )

        for contour in contours:
            if cv2.contourArea(contour) < 100:
                continue

            x, y, width, height = cv2.boundingRect(contour)
            cv2.rectangle(
                frame,
                (x, y),
                (x + width, y + height), 
                (0, 255, 0),
                2
            )

        return frame


    def fast_detect(self, frame):

        lower_yellow = np.array([20, 80, 80])
        upper_yellow = np.array([40, 255, 255])

        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, k)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, k)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        hold_id = 0 # better method for this later
        holds = []

        for c in contours:
            area = cv2.contourArea(c)
            if area < 50:
                continue

            x, y, width, height = cv2.boundingRect(c)

            holds.append(Hold(hold_id, (0, 255, 55), (x, y)))
            hold_id += 1

            cv2.rectangle(
                frame,
                (x, y),
                (x + width, y + height),
                (0, 255, 255),
                2
            )

            label_yel = max(y - 10, 20)

            cv2.putText(
                frame,
                "Yellow Hold",
                (x, label_yel),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 255),
                2
            )

        return (frame, holds)
   
