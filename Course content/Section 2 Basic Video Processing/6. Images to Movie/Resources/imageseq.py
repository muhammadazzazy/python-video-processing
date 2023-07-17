# Import everything needed to edit video clips
from moviepy.editor import *

# Create a image sequence
clip = ImageSequenceClip(['~/Downloads/frame1.jpg',
                          '~/Downloads/frame2.jpg',
                          '~/Downloads/frame3.jpg',
                          '~/Downloads/frame4.jpg'],
                         fps=1)
# Save output
clip.write_videofile("test.mp4")
