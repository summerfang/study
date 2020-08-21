REM "Make two video side by side. One is 1280*720 and another is 640*480"
ffmpeg -i win_av_720p.mp4 -i win_av_480p.mp4 -filter_complex "[0:v]pad=1920:720:0:[a]; [a][1:v]overlay=1281:0[b]" -map "[b]" -pix_fmt yuv420p win_av_composite.mp4

REM "Make two videos side by side and push to stream service"
ffmpeg -i win_av_720p.mp4 -i win_av_480p.mp4 -filter_complex "[0:v]pad=1920:720:0:[a]; [a][1:v]overlay=1281:0[b]" -map "[b]" -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream
ffplay  -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream

ffmpeg -i aoc-meets-garbage-disposal.mp4 -i garbage.mp3 -codec copy aoc-meets-garbage-disposal-mix.mp4

ffmpeg -i win_av_720p.mp4 -i powerbylogo.png -filter_complex "[0:v][1:v] overlay=25:25:enable='between(t,0,20)'" -pix_fmt yuv420p -c:a copy win_av_720p_powerby.mp4

ffmpeg -i win_av_720p.mp4 -i bird.mov -filter_complex "[1:v]setpts=PTS-10/TB[a]; [0:v][a]overlay=enable=gte(t\,5):shortest=1[out]" -map [out] -map 0:a -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a copy win_av_with_bird.mp4

REM "Put a bird in the video"
ffmpeg -i win_av_720p.mp4 -vf "movie=bird.mov,scale=250:-1 [inner];[in][inner] overlay=10:10[out]" win_av_with_bird.mp4

REM "Mask a picture to video with 4 rectangle available for people"
ffmpeg -i win_av_720p.mp4 -i mask_4_pillar.png -filter_complex "[0:v][1:v] overlay=25:25:enable='between(t,0,20)'" -pix_fmt yuv420p -c:a copy win_av_720p_4_pillar.mp4

ffmpeg -i win_av_720p.mp4 -i fox4speaker.png -filter_complex "[0][1] overlay" fox4speaker_test.mp4


ffmpeg -i win_av_720p.mp4 -i mask_4_pillar.png 
-filter_complex "[0:v][1:v] overlay=25:25:enable='between(t,0,20)'" -pix_fmt yuv420p -c:a copy 
win_av_720p_4_pillar.mp4

ffmpeg -i video -i image1 -i image2 -i image3
 -filter_complex
    "[0][1]overlay=x=X:y=Y:enable='between(t,23,27)'[v1];
     [v1][2]overlay=x=X:y=Y:enable='between(t,44,61)'[v2];
     [v2][3]overlay=x=X:y=Y:enable='gt(t,112)'[v3]"
-map "[v3]" -map 0:a  out.mp4

ffmpeg -i win_av_720p.mp4 -vf "movie=bird.mov,scale=250:-1 [inner];[in][inner] overlay=10:10[out]" 
-i mask_4_pillar.png -filter_complex "[0:v][1:v] overlay=25:25:enable='between(t,0,20)'" 
-pix_fmt yuv420p -c:a copy win_av_with_pillar_bird.mp4

REM "Add a tranparent png and a tranparent video"
ffmpeg -i win_av_720p.mp4 -i mask_4_pillar.png -i bird_small.mov -filter_complex "[0][1] overlay=enable='between(t,0,1)'[v1]; [v1][2]overlay=enable='between(t,1,2):x=100'[v2]" -map "[v2]" -map 0:a pillar_bird.mp4

