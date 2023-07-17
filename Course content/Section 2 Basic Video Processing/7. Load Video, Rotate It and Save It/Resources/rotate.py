# load moviepy
from moviepy.editor import *

# load video and edit it
video = VideoFileClip("river.mp4")

# rotate
video.rotate(180)

# write video
video.write_videofile("output.mp4")
