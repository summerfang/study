from moviepy.editor import *

clip1 = VideoFileClip("v.mp4")
clip2 = VideoFileClip("v1.mp4")
clip3 = VideoFileClip("v1.mp4").subclip(4,10)

video = CompositeVideoClip([clip1, clip2.set_start(5), clip3.set_start(10)])

video.write_videofile("v1_time.mp4")
