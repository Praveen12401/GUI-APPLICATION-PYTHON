from pytube import YouTube
# only single video downlode now
link="https://youtu.be/PS70tOQNN_E"
youtube_1=YouTube(link)
# print(youtube_1.title)
# print(youtube_1.thumbnail_url)
videos=youtube_1.streams.all()
vid=list(enumerate(videos))
for i in vid:
    print(i)
print()
strm=int(input("Enter a number :  "))
videos[strm].download()
print("succesfully download")