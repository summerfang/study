from moviepy.editor import *

clip1 = VideoFileClip("v.mp4").subclip(0,5)
clip2 = VideoFileClip("v1.mp4").subclip(0,5)
clip3 = clip2.fx(vfx.mirror_x)
clip4 = clip2.fx(vfx.mirror_y)

video = CompositeVideoClip([clip1, clip2.set_position((10,10)), clip3.set_position(("center")), clip4.set_position(("left", "bottom"))])
video.write_videofile("v1_comp.mp4")