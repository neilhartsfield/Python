import os
import pytube

# Prompt the user for the YouTube URL
url = input("Enter the YouTube URL: ")

# Create a YouTube object
yt = pytube.YouTube(url)

# Get the video and audio stream
video_stream = yt.streams.filter(file_extension='mp4', resolution='720p').first()
audio_stream = yt.streams.filter(only_audio=True).first()

# Download the audio to the C:\my\mp3 directory
output_dir = r"C:\my\mp3"
output_file_mp4 = video_stream.title + ".mp4" # Use the original video name with a .mp4 extension
output_file_mp3 = video_stream.title + ".mp3"  # Use the original video name with a .mp3 extension
audio_stream.download(output_path=output_dir)

# Set the input & output paths for ffmpeg conversion
ffmpeg_input_path = os.path.join(output_dir, output_file_mp4)
ffmpeg_output_path = os.path.join(output_dir, output_file_mp3)

# Use ffmpeg to convert the audio to MP3 format
# Enclose the file name in quotes to properly handle spaces and special characters
os.system(f'ffmpeg -i "{ffmpeg_input_path}" -vn -ar 44100 -ac 2 -ab 192k -f mp3 "{ffmpeg_output_path}"')

# Delete the temporary file
os.remove(ffmpeg_input_path)

# Sample URL for testing
# https://www.youtube.com/watch?v=dQw4w9WgXcQ
