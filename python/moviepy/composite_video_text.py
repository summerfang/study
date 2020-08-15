from moviepy.editor import *

clip = VideoFileClip("v1.mp4").subclip(50,60)
clip = clip.volumex(0.8)

txt_clip = TextClip("This is a test text", fontsize=70, color='white')
txt_clip = txt_clip.set_pos('center').set_duration(10)

video = CompositeVideoClip([clip, txt_clip])
video.write_videofile("v1_out.webm")