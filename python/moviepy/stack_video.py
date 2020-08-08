from moviepy.editor import *

clip1 = VideoFileClip("v1.mp4").subclip(0,10)
clip2 = clip1.fx(vfx.mirror_x)
clip3 = clip1.fx(vfx.mirror_y)
clip4 = clip1.resize(0.60)

final_clip = clips_array([[clip1,clip2],[clip3,clip4]])
final_clip.resize(width=480).write_videofile("stack.mp4")