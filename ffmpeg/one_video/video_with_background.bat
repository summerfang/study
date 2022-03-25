ffmpeg -i bg.jpg -i obama.mp4 ^
-filter_complex "[0]scale=1280:-1[bg];[1]scale=1024:-1[obama];[bg][obama]overlay=128:36[obamawithbg];[1:a]volume=-3dB[a]" ^
 -map "[obamawithbg]" -map "[a]" -preset ultrafast ^
obama_speech_bg.mp4