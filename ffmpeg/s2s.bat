 ffmpeg -i rtmp://example.com/appname/streamname -vcodec libx264 -vprofile baseline -acodec aac -strict -2 -f flv rtmp://www.summerfang/show/stream

ffmpeg -re -stream_loop -1 -i fox.mp4 -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/livestream
ffmpeg -f rtsp -rtsp_transport tcp -i rtsp://www.summerfang.me:8554/livestream -f rtsp -rtsp_transport tcp -i rtsp://www.summerfang.me:8554/livestream -filter_complex "nullsrc=size=1280*720 [base];[0:v]crop=293:466:37:62 [speaker1];[1:v]crop=293:466:341:62 [speaker2];[base][speaker1] overlay=x=37:y=62 [step0];[step0][speaker2] overlay=x=341:y=62 [step1]" -map "[step1]" -map 1:a:0 -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/livestream1
-f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/livestream1
