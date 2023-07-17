# Load moviepy
from moviepy.editor import VideoFileClip, vfx

# Define clips
clip1 = VideoFileClip("/home/cat/Downloads/example/horse.mp4")

# Speed up clip
clip1 = clip1.fx( vfx.speedx, 4)

# Write output video
clip1.write_videofile("/home/cat/Downloads/example/result.mp4")
 
