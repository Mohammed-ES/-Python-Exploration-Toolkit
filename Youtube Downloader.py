import yt_dlp

def download_yt_video(url):
    yt_opts = {
        'format': 'bestvideo[height<=1080]',  # Sélectionne la meilleure qualité vidéo jusqu'à 1080p
        'noplaylist': True,  # Ne télécharge pas les playlists
    }
    
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download([url])  # Télécharge la vidéo à partir de l'URL fournie
        
if __name__ == "__main__":
    video_url = input("Enter the Youtube Video URL: ")  # Demande à l'utilisateur de saisir l'URL de la vidéo
    download_yt_video(video_url)  # Télécharge la vidéo
