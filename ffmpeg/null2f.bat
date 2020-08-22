REM "Generate 5s white noise video with size 1280*720"
ffmpeg -filter_complex "nullsrc=s=1280*720:duration=5, geq=random(1)*255:128:128" 1280by720_white_noise.mp4

REM "Generate 15s test av signal"
ffmpeg -filter_complex "testsrc=duration=15:size=qcif:rate=10" qcif.mp4

REM "Generate red color video"
ffmpeg -filter_complex "color=c=red@0.2:duration=5:s=qcif:r=10" redcolor.mp4

REM "Column bar video"
ffmpeg -filter_complex "pal100bars=duration=5:size=640*480:rate=10" pal100bars.mp4

