# Load moviepy
from moviepy.editor import VideoFileClip, clips_array

# Define clips
clip1 = VideoFileClip("read.mp4")
clip2 = VideoFileClip("boat.mp4")
clip3 = VideoFileClip("face.mp4")
clip4 = VideoFileClip("coffee.mp4")

# Create combined clip
result = clips_array([[clip1,clip2],
                      [clip3,clip4]])

# Write output video
result.write_videofile("result.mp4")
 
