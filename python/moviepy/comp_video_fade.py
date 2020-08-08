from moviepy.editor import *

clip1 = VideoFileClip("v1.mp4").subclip(0,5)
clip2 = clip1.fx(vfx.mirror_x)
clip3 = clip1.fx(vfx.mirror_y)

video = CompositeVideoClip([clip1,clip2.set_start(5).crossfadein(1), clip3.set_start(10).crossfadein(1.5)])
video.write_videofile("v1_video_fade.mp4")