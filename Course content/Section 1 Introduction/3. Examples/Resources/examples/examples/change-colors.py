# Load moviepy
from moviepy.editor import VideoFileClip, vfx

# Define clips
clip1 = VideoFileClip("face.mp4")

# Apply effects
clip1 = clip1.fx( vfx.colorx, 0.5)

# Write output video
clip1.write_videofile("result.mp4")
 
