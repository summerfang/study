REM "Load a local file to hls"
ffmpeg -re -i win_av_480p.mp4 -vcodec libx264 -g 30 -acodec aac -strict -2 -f flv rtmp://www.summerfang.me/show/stream

REM "Repeatly load a local file to hls"
ffmpeg -re -stream_loop -1 -i win_av_480p.mp4 -vcodec libx264 -g 30 -acodec aac -strict -2 -f flv rtmp://www.summerfang.me/show/stream

