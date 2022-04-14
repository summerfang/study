ffmpeg -stream_loop -1 -i background.mp4 -i obama.mp4 -stream_loop -1 -i speaker.mp4 -stream_loop -1 -i logo.mp4 \
-filter_complex "[0]scale=1280:-1,loop=-1[bg];[1]scale=512:-1[obama];[bg][obama]overlay=64:210[obamawithbg];[2]scale=512:-1[speaker];[obamawithbg][speaker]overlay=main_w/2+64:210[obamawithspeaker];[3]scale=180:-1[logo];[obamawithspeaker][logo]overlay=main_w-overlay_w-10:18[obamawithbglogo];[1:a]volume=-3dB[a]" \
-map "[obamawithbglogo]" -map "[a]" -preset ultrafast \
-tune zerolatency -crf 28 -g 60 \
-c:a aac -f matroska - | ffplay -


ffmpeg -stream_loop -1 -i background.mp4 -i obama.mp4 -stream_loop -1 -i speaker.mp4 -stream_loop -1 -i logo.mp4 \
-filter_complex "[0]scale=1280:-1,loop=-1[bg];[1]scale=512:-1[obama];[bg][obama]overlay=64:210[obamawithbg];[2]scale=512:-1[speaker];[obamawithbg][speaker]overlay=main_w/2+64:210[obamawithspeaker];[3]scale=180:-1[logo];[obamawithspeaker][logo]overlay=main_w-overlay_w-10:18[obamawithbglogo];[1:a]volume=-3dB[a]" \
-map "[obamawithbglogo]" -map "[a]" -preset ultrafast \
-tune zerolatency -crf 28 -g 60 \
-c:a aac -f matroska - | ffplay -