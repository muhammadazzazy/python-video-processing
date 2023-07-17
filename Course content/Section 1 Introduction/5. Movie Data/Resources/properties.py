# Import everything needed to edit video clips
from moviepy.editor import *

# Open movie
clip = VideoFileClip("/home/cat/Downloads/output.mp4")

# Show width
print(clip.w)

# Show height
print(clip.h)

# Size
print(clip.size)

# Show duration
print(clip.duration)

# Show framerate
print(clip.fps)

