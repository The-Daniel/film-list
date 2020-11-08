import os
import sys
import math

from moviepy.video.io.VideoFileClip import VideoFileClip

class colour:
    SEP = '\033[96m' # GREEN
    TIME = '\033[1m'

    FILM0 = '\033[95m'
    FILM1 = '\033[92m'
    FILM2 = '\033[93m'
    FILM3 = '\033[91m'
    DEFAULT = '\033[94m'

    CLEAR = '\033[0m'

class Video:
    def __init__(self, name, age):
        self.name = name
        self.duration = duration

def dur(vid):
    return vid.duration

def durHoursMins(dur):
    return list(map(math.floor, divmod(dur / 60, 60)))

def durHours(dur):
    return durHoursMins(dur)[0]

def durPretty(dur):
    h, m = durHoursMins(dur)
    return '{:d} h {:02d} m'.format(int(h), int(m))

VID_FILES = ['.mp4', '.avi', '.mkv']
JUNK_FILES = ['.srt', '.jpg', '.jpeg', '.png', '.txt', '.nfo', '.ini']

JUNK_WORDS = VID_FILES + [ '1080p', '720p', '480p', 'x264', 'BluRay', 'BrRip', 'BRRip', 'BRrip', 'Bluray', 'HDRip', 'HDTV', 'Rip', 'DUAL AUDIO',
    'YIFY', 'XviD', 'PRiSTiNE', 'anoXmous_', 'BOKUTOX', 'anoXmous', 'Sujaidr', 'ShAaNiG', 'ExYuSubs', '-VLiS', '-FTP', 'GAZ' ]

def prettyTitle(tit):
    for WORD in JUNK_WORDS:
        tit = tit.replace(WORD, '')
    return tit.replace('.', ' ')

filmDir = str(sys.argv[-1]) # '/run/media/dandan/9CA5-30ED/Movies/'
fileList = list()

for dp, dn, filenames in os.walk(filmDir):
    for f in filenames:
        ext = os.path.splitext(f)[1]
        if ext in VID_FILES:
            filepath = os.path.join(dp, f)
            duration = VideoFileClip(filepath).duration
            fileList += [ Video(f, duration)]
        elif (ext not in JUNK_FILES):
            print('Unhandled file extension:', os.path.splitext(f)[1], '({})'.format(f))


fileList.sort(key = dur)

for f in fileList:
    def titColour(x):
        return {
            0: colour.FILM0,
            1: colour.FILM1,
            2: colour.FILM2,
            3: colour.FILM3,
            'default': colour.DEFAULT,
        }.get(x, colour.FILM1) 

    print( colour.TIME + durPretty(f.duration) + colour.CLEAR, 
        colour.SEP + '||',
        titColour(durHours(dur(f))) + prettyTitle(f.name) + colour.CLEAR)
