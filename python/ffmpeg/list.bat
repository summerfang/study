REM "-f dshow is used in Windows presenting directshow"
ffmpeg -list_devices true -f dshow -i dummy

REM "List resolution of camera in windows"
ffmpeg -f dshow -list_options true -i video="Integrated Camera"