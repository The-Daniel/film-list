import os
import sys

from utils import *

from moviepy.video.io.VideoFileClip import VideoFileClip

VID_FILES = ['.mp4', '.avi', '.mkv']
JUNK_FILES = ['.srt', '.jpg', '.jpeg', '.png', '.txt', '.nfo', '.ini']

JUNK_WORDS = VID_FILES + [ '1080p', '720p', '480p', 'x264', 'BluRay', 'BrRip', 'BRRip', 'BRrip', 'Bluray', 'HDRip', 'HDTV', 'Rip', 'DUAL AUDIO',
    'YIFY', 'XviD', 'PRiSTiNE', 'anoXmous_', 'BOKUTOX', 'anoXmous', 'Sujaidr', 'ShAaNiG', 'ExYuSubs', '-VLiS', '-FTP', 'GAZ' ]

def prettyTitle(tit):
    for WORD in JUNK_WORDS:
        tit = tit.replace(WORD, '')
    return tit.replace('.', ' ')


def main(argv):
    filmDir = str(argv[-1])
    if not os.path.exists(filmDir): raise FileNotFoundError(filmDir)
            
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

if __name__ == "__main__":
   main(sys.argv[1:])