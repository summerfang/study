import os
import shutil
import importlib.util
import platform

def check_yt_dlp():
    print("Checking if yt-dlp is installed as a Python library...")
    # Check if yt-dlp is installed as a Python library
    yt_dlp_spec = importlib.util.find_spec("yt_dlp")
    if yt_dlp_spec is not None:
        print("yt-dlp is installed as a Python library.")
        return "lib"

    print("Checking if yt-dlp is installed as an executable...")
    # Check if yt-dlp is installed as an executable
    yt_dlp_path = os.getenv("YT_DLP_PATH", "yt-dlp")
    yt_dlp_executable = shutil.which(yt_dlp_path)
    if yt_dlp_executable:
        print(f"yt-dlp executable found at {yt_dlp_executable}.")
        return "executable"

    print("yt-dlp is not installed.")
    return None

def check_ffmpeg():
    print("Checking if ffmpeg is installed...")
    ffmpeg_executable = shutil.which("ffmpeg")
    if ffmpeg_executable is None:
        print("ffmpeg is not installed or not found in PATH.")
        os_name = platform.system()
        if os_name == "Windows" and int(platform.version().split('.')[2]) >= 1809:
            print("You can install ffmpeg using winget:")
            print("  winget install ffmpeg")
        elif os_name == "Darwin":
            print("You can install ffmpeg using Homebrew:")
            print("  brew install ffmpeg")
        elif os_name == "Linux":
            print("You can install ffmpeg using your package manager, for example:")
            print("  sudo apt-get install ffmpeg")
        else:
            print("Please install ffmpeg from https://ffmpeg.org/download.html and add it to your PATH.")
        exit(1)
    else:
        print(f"ffmpeg is installed at {ffmpeg_executable}.")

def print_yt_dlp_install_guide():
    os_name = platform.system()
    print("yt-dlp is not installed.")
    print("You can install yt-dlp as a Python library using pip:")
    print("  pip install yt-dlp")
    print("Or you can download the yt-dlp executable and set the YT_DLP_PATH environment variable:")
    if os_name == "Windows":
        print("  set YT_DLP_PATH=C:\\path\\to\\yt-dlp")
    elif os_name == "Darwin" or os_name == "Linux":
        print("  export YT_DLP_PATH=/path/to/yt-dlp")
    print("Alternatively, you can add the full path of yt-dlp to the .env file:")
    print("  YT_DLP_PATH=/path/to/yt-dlp")

def ensure_preconditions():
    print("Starting preconditions check...")
    yt_dlp_status = check_yt_dlp()
    if yt_dlp_status is None:
        print_yt_dlp_install_guide()
        exit(1)
    check_ffmpeg()
    print("All preconditions are met.")
    return yt_dlp_status

if __name__ == "__main__":
    preconditions_status = ensure_preconditions()
    if preconditions_status == "lib":
        print("yt-dlp is installed as a Python library.")
    elif preconditions_status == "executable":
        print("yt-dlp is installed as an executable.")