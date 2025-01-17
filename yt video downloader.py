import yt_dlp
import os

DOWNLOAD_PATH = r'E:\yt video downloader'  # Fixed download path

def download_youtube_video(url):
    """
    Downloads the highest quality video available for the given YouTube URL.
    """
    if not os.path.exists(DOWNLOAD_PATH):
        os.makedirs(DOWNLOAD_PATH)
        
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Prioritize highest resolution MP4
        'merge_output_format': 'mp4',         # Merge video and audio as MP4 format
        'outtmpl': os.path.join(DOWNLOAD_PATH, '%(title)s.%(ext)s'),  
        'progress_hooks': [progress_hook],   
        'noplaylist': True,                   # Download a single video, not entire playlists
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def progress_hook(d):
    """
    Displays download progress in the console.
    """
    if d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} - {d['_speed_str']} - {d['eta']} seconds remaining")
    elif d['status'] == 'finished':
        print("✅ Download complete!")

if __name__ == '__main__':
    while True:  # Infinite loop for continuous downloads
        youtube_url = input("🎥 Enter the YouTube video URL (or type 'exit' to quit): ")
        if youtube_url.lower() == 'exit':
            print("👋 Exiting the downloader. Goodbye!")
            break
        download_youtube_video(youtube_url)
        print("\n🎯 Ready for the next download!\n")
