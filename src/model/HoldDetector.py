import cv2
import numpy as np


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
        return frame