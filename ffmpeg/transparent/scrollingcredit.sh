ffplay -f lavfi -i color=white@0.0:s=1280x720:rate=60,format=rgba -ss 00:00:00 -t 00:01:30 -vf "drawtext=fontfile=/System/Library/Fonts/Supplemental/Impact.ttf:fontsize=60:fontcolor=green:x=(w-text_w)/2+20:y=h-40*t:line_spacing=80:textfile='names.txt'"