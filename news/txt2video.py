from gtts import gTTS
import cv2
import numpy as np
import os

def text_to_video(file_path, output_video_path):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Convert text to speech in Chinese
    tts = gTTS(text=text, lang='zh')
    audio_path = 'temp_audio.mp3'
    tts.save(audio_path)
    
    # Create a blank image for the video frame
    width, height = 1280, 720
    frame = np.zeros((height, width, 3), np.uint8)
    frame[:] = (0, 0, 0)  # Set background color to black
    
    # Set font and text properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (255, 255, 255)  # White color
    thickness = 2
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    
    # Calculate text position
    text_x = (frame.shape[1] - text_size[0]) // 2
    text_y = (frame.shape[0] + text_size[1]) // 2
    
    # Put text on the frame
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, font_color, thickness)
    
    # Create a video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, 1, (width, height))
    
    # Write the frame multiple times to match the audio length
    audio_duration = 10  # Set duration to match the audio length (in seconds)
    for _ in range(audio_duration):
        video_writer.write(frame)
    
    # Release the video writer
    video_writer.release()
    
    # Combine audio and video using ffmpeg
    os.system(f"ffmpeg -i {output_video_path} -i {audio_path} -c:v copy -c:a aac -strict experimental {output_video_path}")
    
    # Clean up temporary audio file
    os.remove(audio_path)
    print(f"Video file saved as {output_video_path}")

# Example usage
file_path = 'downloads/战力飙升!终结美国空优!空警3000上天! ｜ 同时试飞2款六代机!下一代空战规则中国定! ｜ 美国惊呆!中国AI公司DeepSeek细节全公开！ #沈逸观察.summary.txt'
output_video_path = 'downloads/战力飙升!终结美国空优!空警3000上天! ｜ 同时试飞2款六代机!下一代空战规则中国定! ｜ 美国惊呆!中国AI公司DeepSeek细节全公开！ #沈逸观察.summary.mp4'
text_to_video(file_path, output_video_path)