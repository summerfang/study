from moviepy.editor import VideoFileClip

def get_audio_codec(input_video):
    video_clip = VideoFileClip(input_video)
    
    # Access the audioclip attribute to get the audio stream
    audio_clip = video_clip.audio
    
    # Check if the audio clip exists
    if audio_clip:
        audio_codec = audio_clip.fps
        
        return audio_codec
    
    return None

# Replace 'input_video.mp4' with your actual file name
input_video = 'input_video.mp4'

audio_codec = get_audio_codec(input_video)

if audio_codec:
    print(f"The audio codec of {input_video} is: {audio_codec}")
else:
    print(f"{input_video} does not have an audio stream.")
