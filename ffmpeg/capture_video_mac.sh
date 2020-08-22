# This can record 720p video with 30fps. But it could lost some fame in old mac
ffmpeg -f avfoundation -r 30 -s "1280x720" -i "0:0" mac_av.mp4

# Record Mac desktop
ffmpeg -f avfoundation -i "1:none" mac_desk.mp4