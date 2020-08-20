REM "Capture default to file, it is 640*480"
ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" default_av.avi

REM "Capture 480p to file"
ffmpeg -f dshow -video_size 640*480 -rtbufsize 1702000k -framerate 30 -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" win_av_480p.mpg

REM "Capture 720p to file"
ffmpeg -f dshow -video_size 1280*720 -rtbufsize 702000k -framerate 30 -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" win_av_720p.mpg

REM "Camera to file with video only"
ffmpeg -f dshow -i video="Integrated Camera" v.mp4