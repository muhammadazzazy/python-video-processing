# Load moviepy
from moviepy.editor import VideoFileClip, vfx

# Define clips
clip1 = VideoFileClip("faceshort.mp4")

# Apply effects
clip1 = clip1.fx( vfx.mirror_x )

# Write output video
clip1.write_videofile("result.mp4")
 
