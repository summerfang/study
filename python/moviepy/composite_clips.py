from moviepy.editor import *

clip1 = VideoFileClip("v.mp4").subclip(0,5)
clip2 = VideoFileClip("v1.mp4").subclip(0,5)
clip3 = clip2.fx(vfx.mirror_y)

video = CompositeVideoClip([clip1,clip2,clip3])
video.write_videofile('v1_composite.mp4')

