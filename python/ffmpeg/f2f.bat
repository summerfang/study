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