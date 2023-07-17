# Load moviepy
from moviepy.editor import VideoFileClip, vfx

# Define clips
clip1 = VideoFileClip("horse.mp4")

# Apply effects
clip1 = clip1.fx( vfx.resize, width=100)

# Write output video
clip1.write_videofile("result.mp4")
 
