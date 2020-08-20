ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" -vcodec libx264 -g 30 -acodec aac -strict -2 -f flv rtmp://www.summerfang.me/show/stream
