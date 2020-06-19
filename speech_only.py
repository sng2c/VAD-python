from moviepy.editor import *
import csv

data = None
video = VideoFileClip("../peng2clip.mp4")
clips = []
with open("out.csv") as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        a, b = row['speech_begin'], row['speech_end']
        print(f'{a} ~ {b}')
        clips.append(video.subclip(a, b))
video2 = concatenate_videoclips(clips)
video2.write_videofile("out.mp4")
video2.close()
