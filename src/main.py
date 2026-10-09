from model.classes import *
from model.videoProcessor import VideoProcessor
from model.HoldDetector import HoldDetector
import cv2

athlete = Athlete(1, "Aidan")

session = Session(1, "09/29/2026")
athlete.add_session(session)

problem = Problem(
    problem_id=1,
    wall_angle=30,
    style="overhang"
)
"""
hold1 = Hold(1, color=(255, 0, 0), pos=(300, 400))
hold2 = Hold(2, color=(255, 0, 0), pos=(450, 300))

problem.add_hold(hold1)
problem.add_hold(hold2)
"""

video = Video(1, "videos/yellow_logo.mp4")

attempt = Attempt(1, problem)
attempt.set_video(video)

session.add_attempt(attempt)
"""
pose = Pose(timestamp=1.5)
pose.left_shoulder = (400, 250)
pose.right_shoulder = (450, 250)
pose.left_wrist = (350, 350)
pose.right_wrist = (500, 300)


movement = Movement(
    start_time=1.5,
    end_time=2.2
)
"""
print(athlete.name)
print(athlete.get_session(1).date)
print(session.attempts[0].problem.style)
print(attempt.video.file_path)
print(len(problem.holds))


vProcessor = VideoProcessor()
vProcessor.process_video(video)

hDetector = HoldDetector()

print(f"FPS: {video.fps}")
print(f"Height: {video.height}")
print(f"Width: {video.width}")
print(f"Duration: {video.duration}")
print(f"Frame Count: {video.frame_count}")

frame = vProcessor.get_frame(video, 0)


if frame is not None:
    f, holds = hDetector.fast_detect(frame)

    print(f"holds detected: {len(holds)}")

    for h in holds:
        problem.add_hold(h)

    for h in problem.holds:
        print(f"hold id: {h.hold_id}, pos: {h.pos}")

    cv2.namedWindow("Hold Detection", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Hold Detection", 500, 800)

    cv2.imshow("Hold Detection", f)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

