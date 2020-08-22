REM "Capture default to file, it is 640*480"
ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" _480.avi
ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" _480.mpg
ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" _480.mp4
ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" _480.mkv

REM "Capture 480p to file"
ffmpeg -f dshow -video_size 640*480 -rtbufsize 702000k -framerate 30 -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" _480p.mpg

REM "Capture 720p to file"
ffmpeg -f dshow -video_size 1280*720 -rtbufsize 702000k -framerate 30 -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" _720p.mpg

REM "Camera to file with video only"
ffmpeg -f dshow -i video="Integrated Camera" _480p_v_only.mp4

REM "Record audio"
ffmpeg -f dshow -i audio="Internal Microphone (Conexant SmartAudio HD)" _a_only.mp4