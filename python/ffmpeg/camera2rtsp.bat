REM "Push streaming to server. It works but frame drops"
ffmpeg -stream_loop -1 -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/win


REM "Another works from camera to rstp stream"
ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream

