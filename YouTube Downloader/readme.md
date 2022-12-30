# YouTube Downloader

This code uses the pytube library to download a YouTube video specified by the user. It first prompts the user to enter the YouTube URL, and then creates a YouTube object using that URL.

Next, it gets the video and audio streams from the YouTube object, and downloads the audio stream to the directory specified by output_dir. The video stream is then converted to MP3 format using the ffmpeg command-line tool, and the temporary MP4 file is deleted.

This code will download the specified YouTube video, extract the audio, and save it in MP3 format to the specified directory. It's worth noting that downloading content from YouTube is generally against the site's terms of service, and you should only do so if you have the necessary rights to the content.
