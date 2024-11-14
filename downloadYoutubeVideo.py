import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': '18',
        'outtmpl': 'C:/Users/medme/Downloads/Vidoes' + '/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__" :
    video_url = input("URL : ")
    try:
        download_video(video_url)
    except Exception as e :
        print(f"Error : {e}")