import ffmpeg

in_file = ffmpeg.input("../../ffmpeg/fox.mp4")
overlay_file = ffmpeg.input("../../ffmpeg/fox.png")

(
    ffmpeg
    .concat(in_file.trim(start_frame=10, end_frame=20), in_file.trim(start_frame=10000, end_frame=10010))
    .drawbox(50,50,120,120, color="red", thickness=5)
    .output("_fox_redbox.mp4")
    .run()
)