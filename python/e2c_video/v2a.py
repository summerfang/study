import subprocess

def extract_audio(input_file, output_file):
    command = ['ffmpeg', '-i', input_file, '-vn', '-acodec', 'copy', output_file]
    subprocess.run(command)

# Replace 'input_video.mp4' and 'output_audio.mp3' with your actual file names
extract_audio('input_video.mp4', 'output_audio.mp3')
