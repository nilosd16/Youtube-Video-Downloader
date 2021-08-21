#make sure you have pytube installed, if not run the following:
#pip install pytube

from pytube import YouTube 
link = "url of the video you want to download"
video = YouTube(link)

#video download
video = video.streams.get_highest_resolution()
video.download()