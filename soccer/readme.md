# Installation Instructions

## Precondition

1. **Install yt-dlp**
    - You can install `yt-dlp` using pip:
      ```sh
      pip install yt-dlp
      ```

2. **Install ffmpeg**
    - Follow the instructions on the [official FFmpeg website](https://ffmpeg.org/download.html) to download and install FFmpeg for your operating system.
    - Alternatively, you can use a package manager:
      - **Windows**: Use [winget](https://docs.microsoft.com/en-us/windows/package-manager/winget/):
         ```sh
         winget install "FFmpeg (Essentials Build)"
         ```
      - **macOS**: Use [Homebrew](https://brew.sh/):
         ```sh
         brew install ffmpeg
         ```
      - **Linux**: Use your distribution's package manager, for example:
         ```sh
         sudo apt-get install ffmpeg
         ```

3. ** Add an .env file in the folder which is used to  read parameter **
Example in .env

```
YT_DLP_PATH=C:\yt-dlp\yt-dlp
YOUTUBE_URL=https://www.youtube.com/watch?v=MaGxrNcnX7c&t=550s
```