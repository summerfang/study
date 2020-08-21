REM "The rectange is 293*466, p1(37,62), p2(341,62), p3(645,62), p4(948,62)"

ffmpeg -i fox.mp4 -ss 00:02:10.000 -to 00:03:05.000 -filter:v "crop=293:466:37:62" first_speaker.mp4
ffmpeg -i fox.mp4 -ss 00:02:10.000 -to 00:03:05.000 -filter:v "crop=293:466:341:62" second_speaker.mp4
ffmpeg -i fox.mp4 -ss 00:02:10.000 -to 00:03:05.000 -filter:v "crop=293:466:645:62" third_speaker.mp4
ffmpeg -i fox.mp4 -ss 00:02:10.000 -to 00:03:05.000 -filter:v "crop=293:466:948:62" forth_speaker.mp4

ffmpeg -i fox.mp4 -ss 00:02:10.000 -to 00:03:05.000 fox_4speakers.mp4
ffmpeg -i fox.mp4 -ss 00:02:10.000 -to 00:02:20.000 fox_4speakers_10s.mp4

ffmpeg -i fox_4speakers.mp4 -i fox4speaker.png -filter_complex "[0:v][1:v] overlay=" -pix_fmt yuv420p -c:a copy new_fox_4speakerwin_av_720p_4_pillar.mp4
ffmpeg -i fox_4speakers_10s.mp4  -i fox_4speakers_10s.mp4 -i fox_4speakers_10s.mp4 -i fox_4speakers_10s.mp4 -i fox4speaker.png -filter_complex "nullsrc=size=1280*720 [base]; [0:v]setpts=PTS-STARTPTS,crop=293:466:37:62 [first_speaker];[1:v]setpts=PTS-STARTPTS, crop=293:466:341:62 [second_speaker];[2:v]setpts=PTS-STARTPTS, crop=293:466:645:62 [third_speaker];[3:v]setpts=PTS-STARTPTS, crop=293:466:948:62 [forth_speaker];[base][first_speaker] overlay=x=37:y=62 [step0];[step0][second_speaker] overlay=x=341:y=62 [step1];[step1][third_speaker] overlay=x=645:y=62 [step2];[step2][forth_speaker] overlay=x=948:y=62 [step3];[step3][4:v] overlay [step4]" -map "[step4]"  -map 1:a:0 fox4speaker_step3.mp4
ffmpeg -re -stream_loop -1 -i fox_4speakers_10s.mp4  -i fox_4speakers_10s.mp4 -i fox_4speakers_10s.mp4 -i fox_4speakers_10s.mp4 -i fox4speaker.png -filter_complex "nullsrc=size=1280*720 [base]; [0:v]setpts=PTS-STARTPTS,crop=293:466:37:62 [first_speaker];[1:v]setpts=PTS-STARTPTS, crop=293:466:341:62 [second_speaker];[2:v]setpts=PTS-STARTPTS, crop=293:466:645:62 [third_speaker];[3:v]setpts=PTS-STARTPTS, crop=293:466:948:62 [forth_speaker];[base][first_speaker] overlay=x=37:y=62 [step0];[step0][second_speaker] overlay=x=341:y=62 [step1];[step1][third_speaker] overlay=x=645:y=62 [step2];[step2][forth_speaker] overlay=x=948:y=62 [step3];[step3][4:v] overlay [step4]" -map "[step4]" -map 1:a:0 -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/livestream
ffmpeg -re -i fox_4speakers.mp4  -i fox_4speakers.mp4 -i fox_4speakers.mp4 -i fox_4speakers.mp4 -i fox4speaker.png -filter_complex "nullsrc=size=1280*720 [base]; [0:v]setpts=PTS-STARTPTS,crop=293:466:37:62 [first_speaker];[1:v]setpts=PTS-STARTPTS, crop=293:466:341:62 [second_speaker];[2:v]setpts=PTS-STARTPTS, crop=293:466:645:62 [third_speaker];[3:v]setpts=PTS-STARTPTS, crop=293:466:948:62 [forth_speaker];[base][first_speaker] overlay=x=37:y=62 [step0];[step0][second_speaker] overlay=x=341:y=62 [step1];[step1][third_speaker] overlay=x=645:y=62 [step2];[step2][forth_speaker] overlay=x=948:y=62 [step3];[step3][4:v] overlay [step4]" -map "[step4]" -map 1:a:0 -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/livestream

ffmpeg -i "C:/01/test-%02d.JPG"  -filter_complex "\
  [0:v]crop=3300:3300,scale=900:900[vid]; \
  [0:v]crop=3300:3300,scale=900:900,reverse[r]; \
  [vid][r]concat,loop=2:80,setpts=N/13/TB[out]" \
  -map "[out"] \
  -vcodec libx264 -pix_fmt yuv420p -crf 23 -an \
  "C:/01/test.mp4"
