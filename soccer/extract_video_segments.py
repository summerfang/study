import os
import subprocess
import shutil

def extract_video_segments(file_path):
    # Path to the input video file
    input_video = file_path

    # Duration of each segment (in seconds)
    segment_duration = 15

    # Path to the text file with start times
    start_times_file = 'start_times.txt'

    # Directory to save the extracted clips
    output_directory = 'extracted_clips'

    # Create the output directory if it doesn't exist
    shutil.rmtree(output_directory, ignore_errors=True)
    os.makedirs(output_directory, exist_ok=True)

    # Read the start times from the file
    with open(start_times_file, 'r') as file:
        start_times = file.readlines()

    # Process each start time
    for i, start_time in enumerate(start_times):
        start_time = start_time.strip()

        # Construct the output file name
        output_video = os.path.join(output_directory, f'output_segment_{i + 1}.mp4')

        # Construct the FFmpeg command with re-encoding to ensure clean cuts
        ffmpeg_command = [
            'ffmpeg',
            '-ss', start_time,  # Seek to the start time
            '-i', input_video,  # Input file
            '-t', str(segment_duration),  # Duration of segment
            '-c:v', 'libx264',  # Re-encode video using h264
            '-preset', 'fast',  # Encoding preset for speed/quality balance
            '-c:a', 'aac',      # Re-encode audio using AAC
            '-b:a', '128k',     # Audio bitrate
            output_video
        ]

        print(f"Extracting segment {i+1}/{len(start_times)} starting at {start_time}...")
        # Run the FFmpeg command
        subprocess.run(ffmpeg_command)

    print("Video segments extraction completed.")
