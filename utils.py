import math

def dur(vid):
    return vid.duration

def durHoursMins(dur):
    return list(map(math.floor, divmod(dur / 60, 60)))

def durHours(dur):
    return durHoursMins(dur)[0]

def durPretty(dur):
    h, m = durHoursMins(dur)
    return '{:d} h {:02d} m'.format(int(h), int(m))

class Video:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class colour:
    # Formatting for film titles
    FILM0 = '\033[95m'
    FILM1 = '\033[92m'
    FILM2 = '\033[93m'
    FILM3 = '\033[91m'
    DEFAULT = '\033[94m'
    # Formatting for other elements in list
    SEP = '\033[96m'
    TIME = '\033[1m'
    # Formatting removal
    CLEAR = '\033[0m'