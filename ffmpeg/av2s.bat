ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" -f rtsp rtsp://www.summerfang.me:8554/mystream

ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" -vcodec mpeg4 -r 30 -q 12 -f rtsp rtsp://www.summerfang.me:8554/mystream

REM "Push streaming to server. It works but frame drops, 2s delay"
ffmpeg -stream_loop -1 -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/win
ffplay -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/win

REM "Another works from camera to rstp stream"
ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream
ffplay -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream

REM "Delay 2-4s"
ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" -vcodec libx264 -g 30 -acodec aac -strict -2 -f flv rtmp://www.summerfang.me/show/stream
ffplay rtmp://www.summerfang.me/show/stream


