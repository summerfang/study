REM This works well
ffmpeg -re -stream_loop -1 -i av.mp4 -f rtsp -rtsp_transport tcp rtsp://www.happymeet.me:8554/livestream