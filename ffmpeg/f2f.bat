REM "mkv copy to mp4 is OK. It doesn't work reversely"
ffmpeg -i region.mkv -codec copy region.mp4

REM "PTS stands for Presentation TimeStamps."
REM "Here [0:v] refers to the first video stream in the first input file, which is linked to the first (main) input of the overlay filter."
REM "Similarly the first video stream in the second input is linked to the second (overlay) input of overlay."
REM ""shortest=1" here to specify that we want the output video to stop when the shortest input video stops. "
ffmpeg -i win_av_320_240p.mp4 -i win_av_320_240p.mp4 -i win_av_320_240p.mp4 -i win_av_320_240p.mp4 -i win_av_320_240p.mp4 -filter_complex "nullsrc=size=640*480 [base];[0:v] setpts=PTS-STARTPTS, scale=320*240 [upperleft];[1:v] setpts=STARTPTS, scale=320*240 [upright];[2:v] setpts=STARTPTS, scale=320*240 [bottomleft];[3:v] setpts=STARTPTS, scale=320*240 [bottomright];[base][upperleft] overlay=shortest=1 [tmp1];[tmp1][upright] overlay=shortest=1:x=320 [tmp2];[tmp2][bottomleft] overlay=shortest=1:y=240 [tmp3];[tmp3][bottomright] overlay=shortest=1:x=320:y=240" 2by2.mp4
ffmpeg -i win_av_320_240p.mp4 -i win_av_320_240p.mp4 -i win_av_320_240p.mp4 -i win_av_320_240p.mp4 -i win_av_320_240p.mp4 -filter_complex "nullsrc=size=640*480 [base];[0:v] setpts=PTS-STARTPTS, scale=320*240 [upperleft];[1:v] setpts=STARTPTS, scale=320*240 [upright];[2:v] setpts=STARTPTS, scale=320*240 [bottomleft];[3:v] setpts=STARTPTS, scale=320*240 [bottomright];[base][upperleft] overlay=shortest=1 [tmp1];[tmp1][upright] overlay=x=320 [tmp2];[tmp2][bottomleft] overlay=y=240 [tmp3];[tmp3][bottomright] overlay=x=320:y=240" 2by2.mp4

REM "Scale a video with x=320, y with same scale"
ffmpeg -i bird.mov -vf scale=320:-1 bird_small.mov

REM "Scale a video to x=320 and y=240"
ffmpeg -i win_av_720p.mp4 -vf scale=320:240 win_av_320_240p.mp4

REM "Scale a video to y=240 and x with the same scale"
ffmpeg -i win_av_720p.mp4 -vf scale=320:-1 win_av_168p.mp4

REM "Scale a video to x=320 and y with the same scale, it looks x has to be even number, or it will failed"
ffmpeg -i win_av_720p.mp4 -vf scale=430:240 win_av_240p.mp4

REM "Make two video side by side. One is 1280*720 and another is 640*480"
ffmpeg -i win_av_720p.mp4 -i win_av_480p.mp4 -filter_complex "[0:v]pad=1920:720:0:[a]; [a][1:v]overlay=1281:0[b]" -map "[b]" -pix_fmt yuv420p win_av_composite.mp4

REM "Make two videos side by side and push to stream service"
ffmpeg -i win_av_720p.mp4 -i win_av_480p.mp4 -filter_complex "[0:v]pad=1920:720:0:[a]; [a][1:v]overlay=1281:0[b]" -map "[b]" -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream
ffplay  -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/mystream

ffmpeg -i aoc-meets-garbage-disposal.mp4 -i garbage.mp3 -codec copy aoc-meets-garbage-disposal-mix.mp4

ffmpeg -i win_av_720p.mp4 -i powerbylogo.png -filter_complex "[0:v][1:v] overlay=25:25:enable='between(t,0,20)'" -pix_fmt yuv420p -c:a copy win_av_720p_powerby.mp4

ffmpeg -i win_av_720p.mp4 -i bird.mov -filter_complex "[1:v]setpts=PTS-10/TB[a]; [0:v][a]overlay=enable=gte(t\,5):shortest=1[out]" -map [out] -map 0:a -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a copy win_av_with_bird.mp4

REM "Put a bird in the video"
ffmpeg -i fox.mp4 -vf "movie=bird.mov,scale=250:-1 [inner];[in][inner] overlay=10:10[out]" _win_av_with_bird.mp4

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

REM "Using a image to generate a video"
ffmpeg -i fox.png -filter_complex "[0:v]crop=1280:720,scale=-1:360[vid];[0:v]crop=1280:720,scale=-1:360,reverse[r];[vid][r]concat,loop=2:80,setpts=N/13/TB[out]" -map "[out"] -vcodec libx264 -pix_fmt yuv420p -crf 23 -an _f2v.mp4

ffmpeg -y -i _4speakers.mp4 -i background.jpg -filter_complex "[0:v]crop=293:466:37:62[spk1];[0:v]crop=293:466:341:62[spk2];[0:v]crop=293:466:645:62[spk3];[0:v]crop=293:466:948:62[spk4];[1:v][spk1]overlay=37:62[step1]" -map "[step4]" -c:v libx264 -c:a aac _new_4speakers.mp4

REM "1 speaker with background"
ffmpeg -y -i _4speakers.mp4 -i background.jpg -filter_complex "[0:v]crop=293:466:37:62[spk1];[1:v][spk1]overlay=37:62[step1]" -map "[step1]" -c:v libx264 -map 0:a -c:a aac _new_4speakers.mp4

REM "2 speakers with background"
ffmpeg -y -i _4speakers.mp4 -i background.jpg -filter_complex "[0:v]crop=293:466:37:62[spk1];[0:v]crop=293:466:341:62[spk2];[1:v][spk1]overlay=37:62[step1];[step1][spk2]overlay=341:62[step2]" -map "[step2]" -c:v libx264 -map 0:a -c:a aac _new_4speakers.mp4

REM "3 speakers with background"
ffmpeg -y -i _4speakers.mp4 -i background.jpg -filter_complex "[0:v]crop=293:466:37:62[spk1];[0:v]crop=293:466:341:62[spk2];[0:v]crop=293:466:645:62[spk3];[1:v][spk1]overlay=37:62[step1];[step1][spk2]overlay=341:62[step2];[step2][spk3]overlay=645:62[step3]" -map "[step3]" -c:v libx264 -map 0:a -c:a aac _new_4speakers.mp4

REM "4 speakers with background"
ffmpeg -y -i _4speakers.mp4 -i background.jpg -filter_complex "[0:v]crop=293:466:37:62[spk1];[0:v]crop=293:466:341:62[spk2];[0:v]crop=293:466:645:62[spk3];[0:v]crop=293:466:948:62[spk4];[1:v][spk1]overlay=37:62[step1];[step1][spk2]overlay=341:62[step2];[step2][spk3]overlay=645:62[step3];[step3][spk4]overlay=948:62[step4]" -map "[step4]" -c:v libx264 -map 0:a -c:a aac _new_4speakers.mp4

REM "4 speakers with background and flying bird"
ffmpeg -y -i _4speakers.mp4 -i background.jpg -i bird.mov -filter_complex "[0:v]crop=293:466:37:62[spk1];[0:v]crop=293:466:341:62[spk2];[0:v]crop=293:466:645:62[spk3];[0:v]crop=293:466:948:62[spk4];[2:v]scale=150:-1[bird];[1:v][spk1]overlay=37:62[step1];[step1][spk2]overlay=341:62[step2];[step2][spk3]overlay=645:62[step3];[step3][spk4]overlay=948:62[step4];[step4][bird]overlay=5:5[step5]" -map "[step5]" -c:v libx264 -map 0:a -c:a aac _new_4speakers.mp4

REM "4 speakers with background, logo and flying bird"
ffmpeg -y -i _4speakers.mp4 -i background.jpg -i bird.mov -i powerbylogo.png -filter_complex "[0:v]crop=293:466:37:62[spk1];[0:v]crop=293:466:341:62[spk2];[0:v]crop=293:466:645:62[spk3];[0:v]crop=293:466:948:62[spk4];[2:v]scale=150:-1[bird];[3:v]scale=150:-1[logo];[1:v][spk1]overlay=37:62[step1];[step1][spk2]overlay=341:62[step2];[step2][spk3]overlay=645:62[step3];[step3][spk4]overlay=948:62[step4];[step4][bird]overlay=1100:600[step5];[step5][logo]overlay[step6]" -map "[step6]" -c:v libx264 -map 0:a -c:a aac _new_4speakers.mp4

REM "4 speakers with background, logo, banner and flying bird"
ffmpeg -y -i _4speakers.mp4 -i background.jpg -i bird.mov -i powerbylogo.png -i banner.png -filter_complex "[0:v]crop=293:466:37:62[spk1];[0:v]crop=293:466:341:62[spk2];[0:v]crop=293:466:645:62[spk3];[0:v]crop=293:466:948:62[spk4];[2:v]scale=150:-1[bird];[3:v]scale=150:-1[logo];[4:v]scale=-1:-1[banner];[1:v][spk1]overlay=37:62[step1];[step1][spk2]overlay=341:62[step2];[step2][spk3]overlay=645:62[step3];[step3][spk4]overlay=948:62[step4];[step4][banner]overlay=60:540[step5];[step5][logo]overlay[step6];[step6][bird]overlay=1100:650[step7]" -map "[step7]" -c:v libx264 -map 0:a -c:a aac _new_4speakers.mp4
