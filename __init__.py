import os
import sys

from utils import *

from moviepy.video.io.VideoFileClip import VideoFileClip as video_file_clip

VID_FILES = ['.mp4', '.avi', '.mkv']
JUNK_FILES = ['.srt', '.jpg', '.jpeg', '.png', '.txt', '.nfo', '.ini', '.rar', '.sub', '.idx']
JUNK_WORDS = VID_FILES + [ '1080p', '720p', '480p', 'x264', 'BluRay', 'BrRip', 'BRRip', 'BRrip', 'Bluray', 'HDRip', 'HDTV', 'Rip', 'DUAL AUDIO',
    'YIFY', 'XviD', 'PRiSTiNE', 'anoXmous_', 'BOKUTOX', 'anoXmous', 'Sujaidr', 'ShAaNiG', 'ExYuSubs', '-VLiS', '-FTP', 'GAZ' ]

def title_pretty(str):
    for word in JUNK_WORDS:
        str = str.replace(word, '')
    str = str.replace('.', ' ')
    return str

def main(argv):
    film_dir = str(argv[-1])
    if not os.path.exists(film_dir): raise FileNotFoundError(film_dir)
    
    film_list = list()

    for root, dirs, filenames in os.walk(film_dir):
        for f in filenames:
            ext = os.path.splitext(f)[1]
            if ext in VID_FILES:
                filepath = os.path.join(root, f)
                duration = video_file_clip(filepath).duration
                film_list += [ Video(f, duration)]
            elif (ext not in JUNK_FILES):
                print('Unhandled file extension:', os.path.splitext(f)[1], '({})'.format(f))

    film_list.sort(key = get_duration)
    for f in film_list:
        def title_colour(x):
            return {
                0: Colour.FILM0,
                1: Colour.FILM1,
                2: Colour.FILM2,
                3: Colour.FILM3,
                4: Colour.FILM4,
                'default': Colour.DEFAULT,
            }.get(x, Colour.DEFAULT) 

        print( Colour.TIME + get_duration_pretty(f.duration) + Colour.CLEAR, 
            Colour.SEP + '||',
            title_colour(get_hours(get_duration(f))) + title_pretty(f.name) + Colour.CLEAR)

if __name__ == "__main__":
   main(sys.argv[1:])