import shutil
import subprocess
import logging
import os
import sys
import time
import argparse
import platform
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_valid_url(url):
    """
    Validate the URL format.

    Args:
        url (str): The URL to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

def get_executable_path():
    """
    Retrieve the path to the dt_ylp executable from environment variables.

    Returns:
        str: Path to the dt_ylp executable if found, else None.
    """
    system = platform.system()
    dt_ylp_path = os.getenv("DT_YLP_PATH")

    if system == "Windows" and not dt_ylp_path.endswith(".exe"):
        dt_ylp_path += ".exe"
    
    return dt_ylp_path

def download_video(url, output_path='downloads/', retries=3, delay=5):
    """
    Download video by calling dt_ylp.exe with the specified output filename format.
    Clears the download directory before downloading. After downloading, returns the absolute path of the downloaded file.

    Args:
        url (str): The URL of the video to download.
        output_path (str): Path to save the downloaded video.
        retries (int): Number of retries if download fails.
        delay (int): Delay between retries in seconds.

    Returns:
        str: Absolute path to the downloaded video file if successful, else None.
    """
    if not is_valid_url(url):
        print("Error: Invalid URL format.")
        return None

    # Clear the download directory by deleting all existing files
    if os.path.exists(output_path):
        try:
            for filename in os.listdir(output_path):
                file_path = os.path.join(output_path, filename)
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            logging.info(f"Cleared the download directory: {output_path}")
        except Exception as e:
            logging.error(f"Failed to clear the download directory: {e}")
            return None
    else:
        try:
            os.makedirs(output_path)
            logging.info(f"Created the download directory: {output_path}")
        except Exception as e:
            logging.error(f"Failed to create the download directory: {e}")
            return None

    dt_ylp_path = get_executable_path()
    if not dt_ylp_path:
        logging.error("DT_YLP_PATH not found in environment variables.")
        return None

    for attempt in range(1, retries + 1):
        try:
            # Set the output filename format to %(title)s.%(ext)s
            output_template = os.path.join(output_path, '%(title)s.%(ext)s')

            # Execute the dt_ylp.exe command with the specified output template
            subprocess.run([dt_ylp_path, '-o', output_template, url], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            logging.info(f"Video downloaded successfully to: {output_template}")

            # After download, check the download directory for the file
            downloaded_files = [os.path.join(output_path, f) for f in os.listdir(output_path) if os.path.isfile(os.path.join(output_path, f))]
            if downloaded_files:
                downloaded_file = os.path.abspath(downloaded_files[0])
                logging.info(f"Downloaded file path: {downloaded_file}")
                return downloaded_file
            else:
                logging.error("Download failed: No files found in the download directory.")
                return None

        except subprocess.CalledProcessError as e:
            logging.error(f"Attempt {attempt}: Error downloading video: {e.stderr.decode().strip()}")
            if attempt < retries:
                logging.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                logging.error("Max retries reached. Failed to download video.")
        except FileNotFoundError:
            logging.error(f"dt_ylp.exe not found at '{dt_ylp_path}'. Please verify the path in the .env file.")
            break  # Exit loop if executable is not found
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            break  # Exit loop on unexpected errors
    return None

def main():
    parser = argparse.ArgumentParser(
        description="Download videos using dt_ylp.exe",
        epilog="Ensure that DT_YLP_PATH is set in the .env file."
    )
    parser.add_argument("url", type=str, help="URL of the video to download")
    parser.add_argument("-o", "--output", type=str, default="downloads/", help="Output directory for downloaded videos")
    parser.add_argument("-r", "--retries", type=int, default=3, help="Number of retry attempts for failed downloads")
    parser.add_argument("-d", "--delay", type=int, default=5, help="Delay in seconds between retries")
    args = parser.parse_args()

    download_video(args.url, args.output, retries=args.retries, delay=args.delay)

if __name__ == "__main__":
    main()