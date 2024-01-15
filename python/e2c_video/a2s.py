from google.cloud import speech_v1p1beta1 as speech
from google.cloud import translate_v2 as translate
from moviepy.editor import VideoFileClip, TextClip

def transcribe_audio(audio_file, language='en-US'):
    client = speech.SpeechClient()

    with open(audio_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=language,
        enable_word_time_offsets=True,  # Enable timestamps
    )

    response = client.recognize(config=config, audio=audio)

    results = []
    for result in response.results:
        alternative = result.alternatives[0]
        start_time = alternative.words[0].start_time.total_seconds()
        end_time = alternative.words[-1].end_time.total_seconds()
        transcribed_text = ' '.join(word.word for word in alternative.words)
        results.append({
            'start_time': start_time,
            'end_time': end_time,
            'transcribed_text': transcribed_text,
        })

    return results

def translate_text(text, target_language='zh-CN'):
    client = translate.Client()

    translation = client.translate(text, target_language=target_language)

    return translation['input'], translation['translatedText']

def merge_video_with_stt(video_file, stt_results):
    video_clip = VideoFileClip(video_file)

    # Create text clips with STT results
    text_clips = []
    for result in stt_results:
        start_time = result['start_time']
        end_time = result['end_time']
        translated_text = result['translated_text']
        text_clip = TextClip(translated_text, fontsize=24, color='white', bg_color='black', size=(640, 100))
        text_clip = text_clip.set_start(start_time).set_end(end_time)
        text_clips.append(text_clip)

    # Overlay text clips on the video
    final_clip = video_clip.set_audio(None).set_duration(max(end_time for end_time in [clip.end for clip in text_clips] + [video_clip.end]))
    for text_clip in text_clips:
        final_clip = final_clip.overlay(text_clip, position=(0, 0))

    # Write the final video
    final_clip.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac")

# Replace 'input_video.mp4' and 'input_audio.wav' with your actual file names
video_file = 'input_video.mp4'
audio_file = 'input_audio.wav'

# Transcribe audio to text with timestamps
stt_results = transcribe_audio(audio_file)

# Translate each segment of text to Chinese
for result in stt_results:
    original_text, translated_text = translate_text(result['transcribed_text'])
    result['original_text'] = original_text
    result['translated_text'] = translated_text

# Merge video with STT results
merge_video_with_stt(video_file, stt_results)
