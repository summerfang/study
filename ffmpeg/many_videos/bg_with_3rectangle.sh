ffmpeg -stream_loop -1 -i background.mp4 -vf "drawbox=x=iw/25:y=ih/25:w=0.25*iw:h=0.75*ih:color=white@0.5:t=4:enable='between(t,0,10)',drawbox=x=14*iw/25:y=ih/25:w=0.4*iw:h=0.75*ih:color=white@0.5:t=4:enable='between(t,0,10)',,drawbox=x=14*iw/25:y=ih/25:w=0.4*iw:h=0.75*ih:color=white@0.5:t=4:enable='between(t,0,10)'[out]"  -f matroska - | ffplay -