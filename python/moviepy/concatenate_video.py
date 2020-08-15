from moviepy.editor import *

clip1 = VideoFileClip("v1.mp4").subclip(0,3)
clip2 = VideoFileClip("v.mp4").subclip(0,4)
clip3 = VideoFileClip("v1.mp4").subclip(10,14)
final_clip = concatenate_videoclips([clip2,clip1,clip3])
final_clip.write_videofile("v1_concatenate.mp4")