REM "Stream to file"

REM "ffmpeg send a stream to server and recieve it back and save it to file."
ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream
ffmpeg -y -f rtsp -rtsp_transport tcp -i rtsp://www.summerfang.me:8554/mystream -acodec copy -vcodec copy _s2f.mp4


REM "ffmpeg send a stream to server and recieve it back. Then ffmpeg mix the stream with a photo and save it to file."
ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream
ffmpeg -y -f rtsp -rtsp_transport tcp -i rtsp://www.summerfang.me:8554/mystream -i powerbylogo.png -filter_complex "[1:v] scale=-1:100 [png];[0:v][png] overlay=25:25:enable='between(t,0,20)'" _s2f.mp4

REM "ffmpeg send a stream to server and recieve it back. Then ffmpeg mix the stream with a photo and save it to file."
ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream
ffmpeg -f rtsp -rtsp_transport tcp -i rtsp://www.summerfang.me:8554/mystream -i powerbylogo.png -filter_complex "[1:v] scale=-1:100 [png];[0:v][png] overlay=25:25:enable='between(t,0,20)' [out] " -map "[out]" -vcodec libx264 -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream1
ffplay -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream4
