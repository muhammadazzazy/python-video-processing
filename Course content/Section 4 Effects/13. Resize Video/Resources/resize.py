# Load moviepy
from moviepy.editor import VideoFileClip, vfx

# Define clips
clip1 = VideoFileClip("/home/cat/Downloads/example/horse.mp4")

# Apply effects
clip1 = clip1.fx( vfx.resize, width=100)

# Write output video
clip1.write_videofile("/home/cat/Downloads/example/result.mp4")
 
