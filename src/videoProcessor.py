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

        else:
            print(f"Video ID:{video.video_id} path: {video.file_path} failed to open!")\


    def get_frame(self, video, frame_number):
        pass
        # to do