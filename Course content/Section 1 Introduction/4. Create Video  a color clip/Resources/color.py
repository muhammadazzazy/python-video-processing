# Import everything needed to edit video clips
from moviepy.editor import *

# Create a color image
clip = ColorClip(size =(320, 200), color =[64, 90, 16])

# Set duration of the video
clip = clip.set_duration(5)

# Set the screen speed
clip.fps = 24

# Save output
clip.write_videofile("test.mp4")
