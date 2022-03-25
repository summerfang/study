ffmpeg -i bg.jpg -i obama.mp4 -i logo.jpg ^
-filter_complex "[0]scale=1280:-1[bg];[1]scale=1024:-1[obama];[bg][obama]overlay=128:36[obamawithbg];[1:a]volume=-3dB[a];[obamawithbg][2]overlay=main_w-overlay_w-10:18[obamawithbglogo]" ^
 -map "[obamawithbglogo]" -map "[a]" -preset ultrafast ^
obama_speech.mp4