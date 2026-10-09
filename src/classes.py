class Athlete:
    def __init__(self, athlete_id, name):
        self.athlete_id = athlete_id
        self.name = name
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

    def get_session(self, session_id):
        a = [s for s in self.sessions if s.session_id == session_id]
        return a[0]


class Session:
    def __init__(self, session_id, date):
        self.session_id = session_id
        self.date = date
        self.attempts = []

    def add_attempt(self, attempt):
        self.attempts.append(attempt)

    def get_attempt(self, attempt_id):
        a = [s for s in self.attemtps if s.attempt_id == attempt_id]
        return a[0]


class Attempt:
    def __init__(self, attempt_id, problem):
            self.attempt_id = attempt_id
            self.problem = problem
            self.video = None
            self.result = None

    def set_video(self, video):
        self.video = video


class Problem:
    def __init__(self, problem_id, wall_angle=None, style=None):
        self.problem_id = problem_id
        self.wall_angle = wall_angle
        self.style = style
        self.holds = []

    def add_hold(self, hold):
        self.holds.append(hold)

    


class Hold:
    def __init__(self, hold_id, color=(0,0,0), pos=(0,0)):
        self.hold_id = hold_id
        self.color = color
        self.pos = pos # center



class Video:
    def __init__(self, video_id, file_path):
        self.video_id = video_id
        self.file_path = file_path

        self.duration = None
        self.fps = None
        self.width = None
        self.height = None

class Pose:
    def __init__(self, timestamp):
        self.timestamp = timestamp

        self.left_shoulder = None
        self.right_shoulder = None
        self.left_elbow = None
        self.right_elbow = None

        self.left_wrist = None
        self.right_wrist = None

        self.left_hip = None
        self.right_hip = None

        self.left_knee = None
        self.right_knee = None

        self.left_ankle = None
        self.right_ankle = None

class Movement:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time