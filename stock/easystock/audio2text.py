import os
import sys
import argparse
import logging
import whisper

def transcribe_audio(audio_path, model_size='base', language=None):
    """
    Transcribe an audio file to text using OpenAI's Whisper model.

    Args:
        audio_path (str): Full path to the audio file (e.g., .mp3).
        model_size (str): Size of the Whisper model to use ('tiny', 'base', 'small', 'medium', 'large').
        language (str, optional): Language of the audio (e.g., 'en' for English, 'zh' for Chinese). 
                                  If not specified, the model will attempt to detect the language.

    Returns:
        str: Transcribed text or None if transcription fails.
    """
    if not os.path.isfile(audio_path):
        logging.error(f"Audio file not found: {audio_path}")
        return None

    try:
        logging.info(f"Loading Whisper model ({model_size})...")
        model = whisper.load_model(model_size)
        logging.info("Transcribing audio...")
        result = model.transcribe(audio_path, language=language)
        logging.info("Transcription successful.")
        return result['text']
    except Exception as e:
        logging.error(f"An error occurred during transcription: {e}")
        return None

def save_transcription(text, output_path):
    """
    Save the transcribed text to a file.

    Args:
        text (str): The transcribed text.
        output_path (str): Path to save the text file.
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        logging.info(f"Transcription saved to: {output_path}")
    except Exception as e:
        logging.error(f"Failed to save transcription: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert MP3 audio to text using Whisper.")
    parser.add_argument('path', type=str, help='Full path to the audio file (e.g., .mp3, .webm).')
    parser.add_argument('-m', '--model', type=str, default='base',
                        choices=['tiny', 'base', 'small', 'medium', 'large'],
                        help='Whisper model size to use (default: base).')
    parser.add_argument('-l', '--language', type=str, default=None,
                        help='Language of the audio (e.g., "en" for English, "zh" for Chinese). '
                             'If not specified, the model will attempt to detect the language.')
    parser.add_argument('-o', '--output', type=str, default=None,
                        help='Path to save the transcribed text. Defaults to <audio_filename>.txt')
    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    if not os.path.isfile(args.path):
        logging.error(f"File does not exist: {args.path}")
        sys.exit(1)

    transcription = transcribe_audio(args.path, args.model, args.language)
    if transcription:
        if args.output:
            save_transcription(transcription, args.output)
        else:
            base, _ = os.path.splitext(args.path)
            output_path = f"{base}.txt"
            save_transcription(transcription, output_path)
        print("Transcription completed successfully.")
    else:
        print("Transcription failed.")

if __name__ == "__main__":
    main()