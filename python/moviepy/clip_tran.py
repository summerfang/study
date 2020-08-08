from moviepy.editor import *

clip = (VideoFileClip("v1.mp4")
        .subclip(0,10)
        .fx(vfx.resize, width=360)
        .fx(vfx.speedx, 2)
        .fx(vfx.colorx, 0.5))

video = CompositeVideoClip([clip])
video.write_videofile("v1_tran.mp4")