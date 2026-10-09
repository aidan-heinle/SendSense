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
        v = cv2.VideoCapture(video.file_path)

        if not v.isOpened():
            v.release()
            return None
        
        v.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

        success, frame = v.read()
        v.release()

        if success:
            return frame

        return None

            