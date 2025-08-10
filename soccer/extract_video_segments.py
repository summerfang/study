import os
import subprocess
import shutil

def extract_video_segments(file_path):
    # Path to the input video file
    input_video = file_path

    # Duration of each segment (in seconds)
    segment_duration = 20

    

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

        # Construct the FFmpeg command to cut at the nearest previous keyframe
        ffmpeg_command = [
            'ffmpeg',
            '-ss', start_time,  # First seek to the approximate position
            '-i', input_video,  # Input file
            '-c:v', 'libx264',  # Video codec
            '-preset', 'fast',  # Encoding preset
            '-c:a', 'aac',      # Audio codec
            '-b:a', '128k',     # Audio bitrate
            '-t', str(segment_duration),  # Duration of segment
            '-avoid_negative_ts', 'make_zero',  # Avoid negative timestamps
            '-async', '1',      # Audio sync
            output_video
        ]

        print(f"Extracting segment {i+1}/{len(start_times)} starting at {start_time}...")
        # Run the FFmpeg command
        subprocess.run(ffmpeg_command)

    print("Video segments extraction completed.")
