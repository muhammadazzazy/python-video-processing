# Load moviepy
from moviepy.editor import VideoFileClip, vfx

# Define clips
clip1 = VideoFileClip("horse.mp4")

# Speed up clip
clip1 = clip1.fx( vfx.speedx, 4)

# Write output video
clip1.write_videofile("result.mp4")
 
