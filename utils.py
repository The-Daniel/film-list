import math

def get_duration(vid):
    return vid.duration

def get_mins_hours(dur):
    return list(map(math.floor, divmod(dur / 60, 60)))

def get_hours(dur):
    return get_mins_hours(dur)[0]

def get_duration_pretty(dur):
    h, m = get_mins_hours(dur)
    return '{:d} h {:02d} m'.format(int(h), int(m))

class Video:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class Colour:
    # Formatting for film titles
    FILM0 = '\033[95m'
    FILM1 = '\033[92m'
    FILM2 = '\033[93m'
    FILM3 = '\033[91m'
    FILM4 = '\033[94m'
    DEFAULT = '\033[90m'
    # Formatting for other elements in list
    SEP = '\033[96m'
    TIME = '\033[1m'
    # Formatting removal
    CLEAR = '\033[0m'