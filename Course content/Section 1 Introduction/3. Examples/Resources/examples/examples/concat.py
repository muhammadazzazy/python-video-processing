# Load moviepy
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Define clips
clip1 = VideoFileClip("boat.mp4")
clip2 = VideoFileClip("face.mp4")

# Create combined clip
result = concatenate_videoclips([clip1,clip2])

# Write output video
result.write_videofile("result.mp4")
 
