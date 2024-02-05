import subprocess

def extract_audio(input_file, output_file):
    # command = ['ffmpeg', '-i', input_file, '-c:a libmp3lame -y', output_file]
    command = ['ffmpeg', '-i', input_file, '-c:a pcm_s16le', '-ar 44100', output_file]
    result = subprocess.run(command)
    print("Command Line:", ' '.join(result.args))

# Replace 'input_video.mp4' and 'output_audio.mp3' with your actual file names
extract_audio('input_video.mp4', 'output_audio.wav')
