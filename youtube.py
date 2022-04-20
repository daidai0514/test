# Original Problem：https://stackoverflow.com/questions/68945080/pytube-exceptions-regexmatcherror-get-throttling-function-name-could-not-find
from pytube import YouTube
import os

yt = YouTube(input("輸入Youtube影片網址："))
print(f"開始下載{yt.title}")

path = os.getcwd()+"\\music\\"
# OSError: [Errno 22] Invalid argument：此錯誤為youtube片名有其他符號所導致，與output_path無關
yt.streams.get_audio_only().download(output_path=path)
print("下載成功")