REM "Crop part of video from specific area and start and end time"
REM "The rectange is 293*466, p1(37,62), p2(341,62), p3(645,62), p4(948,62)"
ffmpeg -i fox.mp4 -ss 00:02:10.000 -to 00:03:05.000 -filter:v "crop=293:466:37:62" _speaker1.mp4
ffmpeg -i fox.mp4 -ss 00:02:10.000 -to 00:03:05.000 -filter:v "crop=293:466:341:62" _speaker2.mp4
ffmpeg -i fox.mp4 -ss 00:02:10.000 -to 00:03:05.000 -filter:v "crop=293:466:645:62" _speaker3.mp4
ffmpeg -i fox.mp4 -ss 00:02:10.000 -to 00:03:05.000 -filter:v "crop=293:466:948:62" _speaker4.mp4

REM "Crop part of video"
ffmpeg -i fox.mp4 -ss 00:02:10.000 -to 00:03:05.000 _4speakers.mp4
ffmpeg -i fox.mp4 -ss 00:02:10.000 -to 00:02:30.000 _4speakers_10s.mp4

REM "Generate 4 speakers with mask"
ffmpeg -i _4speakers_10s.mp4 -i fox.png -filter_complex "[0:v][1:v] overlay" -pix_fmt yuv420p -c:a copy _fox_4speakers_720p.mp4
ffmpeg -i _4speakers_10s.mp4  -i _4speakers_10s.mp4 -i _4speakers_10s.mp4 -i _4speakers_10s.mp4 -i fox.png -filter_complex "nullsrc=size=1280*720 [base]; [0:v]setpts=PTS-STARTPTS,crop=293:466:37:62 [speaker1];[1:v]setpts=PTS-STARTPTS, crop=293:466:341:62 [speaker2];[2:v]setpts=PTS-STARTPTS, crop=293:466:645:62 [speaker3];[3:v]setpts=PTS-STARTPTS, crop=293:466:948:62 [speaker4];[base][speaker1] overlay=x=37:y=62 [step0];[step0][speaker2] overlay=x=341:y=62 [step1];[step1][speaker3] overlay=x=645:y=62 [step2];[step2][speaker4] overlay=x=948:y=62 [step3];[step3][4:v] overlay [step4]" -map "[step4]" -map 1:a:0 _fox_10s.mp4

REM "Generate 4 speakers and stream out. The loop doesn't work"
ffmpeg -re -i _4speakers_10s.mp4  -i _4speakers_10s.mp4 -i _4speakers_10s.mp4 -i _4speakers_10s.mp4 -i fox.png -filter_complex "nullsrc=size=1280*720 [base]; [0:v]setpts=PTS-STARTPTS,crop=293:466:37:62 [speaker1];[1:v]setpts=PTS-STARTPTS, crop=293:466:341:62 [speaker2];[2:v]setpts=PTS-STARTPTS, crop=293:466:645:62 [speaker3];[3:v]setpts=PTS-STARTPTS, crop=293:466:948:62 [speaker4];[base][speaker1] overlay=x=37:y=62 [step0];[step0][speaker2] overlay=x=341:y=62 [step1];[step1][speaker3] overlay=x=645:y=62 [step2];[step2][speaker4] overlay=x=948:y=62 [step3];[step3][4:v] overlay [step4]" -map "[step4]" -map 1:a:0  -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/livestream
ffmpeg -threads 2 -re -fflags +genpts -stream_loop -1 -i _4speakers_10s.mp4  -i _4speakers_10s.mp4 -i _4speakers_10s.mp4 -i _4speakers_10s.mp4 -i fox.png -filter_complex "nullsrc=size=1280*720 [base]; [0:v]setpts=PTS-STARTPTS,crop=293:466:37:62 [speaker1];[1:v]setpts=PTS-STARTPTS, crop=293:466:341:62 [speaker2];[2:v]setpts=PTS-STARTPTS, crop=293:466:645:62 [speaker3];[3:v]setpts=PTS-STARTPTS, crop=293:466:948:62 [speaker4];[base][speaker1] overlay=x=37:y=62 [step0];[step0][speaker2] overlay=x=341:y=62 [step1];[step1][speaker3] overlay=x=645:y=62 [step2];[step2][speaker4] overlay=x=948:y=62 [step3];[step3][4:v] overlay [step4]" -map "[step4]" -map 1:a:0  -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/livestream

REM "Loop play one video. it look it need a long video to make loop work"
ffmpeg -threads 2 -re -fflags +genpts -stream_loop -1 -i fox.mp4 -c copy -f mpegts -mpegts_service_id 102 -metadata service_name=My_channel -metadata service_provider=My_Self -max_interleave_delta 0 -use_wallclock_as_timestamps 1 -flush_packets 1 -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/livestream

REM "Play back the stream"
ffplay -f rtsp -rtsp_transport tcp rtsp://www.summerfang.me:8554/livestream1


ffmpeg -f rtsp -rtsp_transport tcp - i rtsp://www.summerfang.me:8554/livestream -f rtsp -rtsp_transport tcp - i rtsp://www.summerfang.me:8554/livestream -filter_complex "nullsrc=size=1280*720 [base];[0:v]crop=293:466:37:62 [speaker1];[1:v]crop=293:466:341:62 [speaker2];[base][speaker1] overlay=x=37:y=62 [step0];[step0][speaker2] overlay=x=341:y=62 [step1]" -map "[step2]" -map 1:a:0 _fox_10s.mp4