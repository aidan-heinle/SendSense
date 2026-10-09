import cv2

class VideoProcessor:
    def process_video(self, video):
        v = cv2.VideoCapture(video.file_path)

        if v.isOpened():
            fps = v.get(cv2.CAP_PROP_FPS)
            frame_count = v.get(cv2.CAP_PROP_FRAME_COUNT)
            width = v.get(cv2.CAP_PROP_FRAME_WIDTH)
            height = v.get(cv2.CAP_PROP_FRAME_HEIGHT)
            duration = frame_count / fps 

            video.duration = duration
            video.fps = fps
            video.width = width
            video.height = height
            video.frame_count = frame_count

        else:
            return None


    def get_frame(self, video, frame_number):

        # make this faster later

        if frame_number > (video.frame_count-1) or frame_number < 0:
            return None

        v = cv2.VideoCapture(video.file_path)

        if v.isOpened():
            current_frame = 0
            while True:
                success, frame = v.read()

                if not success:
                    v.release()
                    return None

                if current_frame == frame_number:
                    v.release()
                    return frame

                current_frame += 1
        else:
            v.release()
            return None
            