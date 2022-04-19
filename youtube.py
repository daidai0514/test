# Original Problem：https://stackoverflow.com/questions/68945080/pytube-exceptions-regexmatcherror-get-throttling-function-name-could-not-find
from pytube import YouTube
import os

yt = YouTube(input("輸入Youtube影片網址："))
print(f"開始下載{yt.title}")

path = os.getcwd()+"\\music\\"
yt.streams.get_audio_only().download(filename=yt.title+".mp3", output_path=path)
print("下載成功")