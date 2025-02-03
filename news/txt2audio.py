from gtts import gTTS
import os
# from playsound import playsound

def text_to_audio(file_path, output_audio_path):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Convert text to speech in Chinese
    tts = gTTS(text=text, lang='zh')
    
    # Save the audio file
    tts.save(output_audio_path)
    print(f"Audio file saved as {output_audio_path}")

# Example usage
file_path = './downloads/战力飙升!终结美国空优!空警3000上天! ｜ 同时试飞2款六代机!下一代空战规则中国定! ｜ 美国惊呆!中国AI公司DeepSeek细节全公开！ #沈逸观察.summary.txt'
output_audio_path = './downloads/战力飙升!终结美国空优!空警3000上天! ｜ 同时试飞2款六代机!下一代空战规则中国定! ｜ 美国惊呆!中国AI公司DeepSeek细节全公开！ #沈逸观察.summary.mp3'
text_to_audio(file_path, output_audio_path)