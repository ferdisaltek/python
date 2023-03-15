from pytube import YouTube

url = "https://www.youtube.com/watch?v=CHSnz0bCaUk"
yt = YouTube(url)

print("Title:", yt.title)
print("Length:", yt.length, "seconds")

stream = yt.streams.get_highest_resolution()
stream.download()
