import ffmpeg

stream = ffmpeg.input("_fox_20s.mp4")
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, "_fox_hflip_20s.mp4")
ffmpeg.run(stream)

