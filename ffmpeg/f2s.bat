REM "Load a local file to hls"
ffmpeg -re -i win_av_480p.mp4 -vcodec libx264 -g 30 -acodec aac -strict -2 -f flv rtmp://www.summerfang.me/show/stream

REM "Repeatly load a local file to hls"
ffmpeg -re -stream_loop -1 -i win_av_480p.mp4 -vcodec libx264 -g 30 -acodec aac -strict -2 -f flv rtmp://www.summerfang.me/show/stream

REM This works well
ffmpeg -re -stream_loop -1 -i av.mp4 -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/livestream

ffmpeg -re -i v.mp4 -pix_fmt yuv420p -vsync 1 -threads 0 -vcodec libx264 -r 30 -g 60 -sc_threshold 0 -b:v 512k -bufsize 640k -maxrate 640k -preset veryfast -profile:v baseline -tune film -acodec aac -b:a 128k -ac 2 -ar 48000 -af "aresample=async=1:min_hard_comp=0.100000:first_pts=0" -bsf:v h264_mp4toannexb -f mpegts udp://www.summerfang.me:8000?pkt_size=1316
ffmpeg -re -i "%WMSAPP_HOME%/content/sample.mp4" -pix_fmt yuv420p -vsync 1 -threads 0 -vcodec libx264 -r 30 -g 60 -sc_threshold 0 -b:v 640k -bufsize 768k -maxrate 800k -preset veryfast -profile:v baseline -tune film -acodec aac -b:a 128k -ac 2 -ar 48000 -af "aresample=async=1:min_hard_comp=0.100000:first_pts=0" -bsf:v h264_mp4toannexb -f mpegts udp://www.summerfang.me:8000?pkt_size=1316

ffmpeg -re -stream_loop -1 -i win_av_720p.mp4 -i mask_4_pillar.png -i bird_small.mov -filter_complex "[0][1] overlay=enable='between(t,0,1)'[v1]; [v1][2]overlay=enable='between(t,1):x=100'[v2]" -map "[v2]" -map 0:a -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/livestream

ffplay -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/livestream


REM "Steam 4 speakers with background, logo, banner and flying bird to server"
ffmpeg -re -i _4speakers.mp4 -i background.jpg -i bird.mov -i powerbylogo.png -i banner.png -filter_complex "[0:v]crop=293:466:37:62[spk1];[0:v]crop=293:466:341:62[spk2];[0:v]crop=293:466:645:62[spk3];[0:v]crop=293:466:948:62[spk4];[2:v]scale=150:-1[bird];[3:v]scale=150:-1[logo];[4:v]scale=-1:-1[banner];[1:v][spk1]overlay=37:62[step1];[step1][spk2]overlay=341:62[step2];[step2][spk3]overlay=645:62[step3];[step3][spk4]overlay=948:62[step4];[step4][banner]overlay=60:540[step5];[step5][logo]overlay[step6];[step6][bird]overlay=1100:650[step7]" -map "[step7]" -c:v libx264 -map 0:a -c:a aac -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/livestream

REM Looply Steam 4 speakers with background, logo, banner and flying bird to server
ffmpeg -stream_loop -1 -re -i _4speakers.mp4 -i background.jpg -i bird.mov -i powerbylogo.png -i banner.png -filter_complex "[0:v]crop=293:466:37:62[spk1];[0:v]crop=293:466:341:62[spk2];[0:v]crop=293:466:645:62[spk3];[0:v]crop=293:466:948:62[spk4];[2:v]scale=150:-1[bird];[3:v]scale=150:-1[logo];[4:v]scale=-1:-1[banner];[1:v][spk1]overlay=37:62[step1];[step1][spk2]overlay=341:62[step2];[step2][spk3]overlay=645:62[step3];[step3][spk4]overlay=948:62[step4];[step4][banner]overlay=60:540[step5];[step5][logo]overlay[step6];[step6][bird]overlay=1100:650[step7]" -map "[step7]" -c:v libx264 -map 0:a -c:a aac -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/livestream