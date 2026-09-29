class Athlete:
    def __init__(self, athlete_id, name):
        self.athlete_id = athlete_id
        self.name = name
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)


class Session:
    def __init__(self, session_id, date):
        self.session_id = session_id
        self.date = date
        self.attempts = []


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


class Hold:
    def __init__(self, hold_id, color=(0,0,0), pos=(0,0)):
        self.hold_id = hold_id
        self.color = color
        self.pos = pos

    


class Video:
    pass


class Pose:
    pass


class Movement:
    pass