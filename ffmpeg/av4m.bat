REM "ffmpeg send a stream to server and recieve it back and send to server again."
ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream
ffmpeg -f rtsp -rtsp_transport tcp -i rtsp://www.summerfang.me:8554/mystream -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream1
ffplay -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream1


REM "ffmpeg send a stream to server and recieve it back. Put a picture and send to server again."
ffmpeg -f dshow -i video="Integrated Camera":audio="Internal Microphone (Conexant SmartAudio HD)" -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream
ffmpeg -f rtsp -rtsp_transport tcp -i rtsp://www.summerfang.me:8554/mystream -i powerbylogo.png -filter_complex "[1:v] scale=-1:100 [png];[0:v][png] overlay=25:25 [out]" -map "[out]" -vcodec libx264 -acodec aac -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream1
ffmpeg -f rtsp -rtsp_transport tcp -i rtsp://www.summerfang.me:8554/mystream -i powerbylogo.png -filter_complex "[1:v] scale=-1:100 [png];[0:v][png] overlay=25:25:enable='between(t,0,20)' [out] " -map "[out]" -vcodec libx264 -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream1
ffplay -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream1

REM "Merge bird"
ffmpeg -f rtsp -rtsp_transport tcp -i rtsp://www.summerfang.me:8554/mystream -i bird.mov -filter_complex "[1:v] scale=-1:100 [png];[0:v][png] overlay=25:25 [out]" -map "[out]" -vcodec libx264 -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream2
ffplay -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream2


ffmpeg -i fox.mp4 -vf "movie=bird.mov,scale=250:-1 [inner];[in][inner] overlay=10:10[out]" _win_av_with_bird.mp4



-f rtsp -rtsp_transport tcp -i rtsp://www.summerfang.me:8554/mystream -filter_complex "nullsrc=size=1280*720 [base];[0:v]crop=293:466:37:62 [speaker1];[1:v]crop=293:466:341:62 [speaker2];[base][speaker1] overlay=x=37:y=62 [step0];[step0][speaker2] overlay=x=341:y=62 [step1]" -map "[step1]" -map 1:a:0 -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/livestream1

ffplay -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream1
