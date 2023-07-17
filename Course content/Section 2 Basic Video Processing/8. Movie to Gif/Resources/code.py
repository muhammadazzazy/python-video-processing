# Import everything needed to edit video clips
from moviepy.editor import *

# Load video
clip = VideoFileClip("/home/cat/Downloads/read.mp4")

# Convert to gif
clip.write_gif("test.gif")
