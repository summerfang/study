from moviepy.editor import *

clip1 = VideoFileClip("v1.mp4")
crop1 = (clip1.subclip(0,5)
        .crop(x1=200, x2=-200))


video = CompositeVideoClip([crop1])

video.write_videofile("crop.mp4")