ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" -f rtsp rtsp://www.summerfang.me:8554/mystream

ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" -vcodec mpeg4 -r 30 -q 12 -f rtsp rtsp://www.summerfang.me:8554/mystream