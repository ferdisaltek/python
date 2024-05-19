from youtube_transcript_api import YouTubeTranscriptApi

# YouTube video ID'sini girin
video_id = "ybkkiGtJmkM&t=9s"

# Transkripti alın
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Transkripti bir metin dosyasına yazdırın
with open("transcript.txt", "w", encoding="utf-8") as f:
    for entry in transcript:
        f.write(f"{entry['start']}: {entry['text']}\n")

print("Transkript başarıyla alındı ve transcript.txt dosyasına kaydedildi.")
