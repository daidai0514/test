# Original Problem：https://stackoverflow.com/questions/68945080/pytube-exceptions-regexmatcherror-get-throttling-function-name-could-not-find
from pytube import YouTube
from pytube import Playlist
import os,re

# 基本參數
mp3_path = os.getcwd()+"\\MP3\\"
mp4_path = os.getcwd()+"\\MP4\\"
error_word = "\n下載錯誤！ 請重新輸入\n"+\
             "重新選擇請輸入\"back\""
input_word = "\n輸入Youtube影片網址："

def del_title(title):      
    return re.sub('[\/:*?"<>|]', '-', title) # 去掉非法字元  

while True:
    choose = input("選擇下載類型\n"+
                   "---------------A:下載單部影片-mp3\n"+
                   "---------------B:下載單部影片-mp4\n"+
                   "---------------C:下載多部影片-mp3\n"+
                   "---------------D:下載多部影片-mp4\n"+
                   "---------------END:結束程式\n"+
                   "---------------註1:私人播放清單需轉公開或不公開\n"+
                   "---------------註2:Youtube合輯需先儲存成私人播放清單\n"
                   "輸入選項：")

    # 下載單部影片-mp3
    if choose == "A":
        while True:
            url = input(input_word)
            if url == "back":
                break
            try:
                yt = YouTube(url)
                print(f"\n開始下載 --> {yt.title}")

                yt.streams.get_audio_only().download(filename=del_title(yt.title)+".mp3", output_path=mp3_path)
                print("下載成功", end="\n\n")
                break
            except:
                print(error_word)

    # 下載單部影片-mp4
    elif choose == "B":
        while True:
            url = input(input_word)
            if url == "back":
                break
            try:
                yt = YouTube(url)
                print(f"\n開始下載 --> {yt.title}")
                
                yt.streams.get_highest_resolution().download(filename=del_title(yt.title)+".mp4", output_path=mp4_path)
                print("下載成功", end="\n\n")
                break
            except:
                print(error_word)

    # 下載多部影片-mp3
    elif choose == "C":
        while True:
            url = input(input_word)
            if url == "back":
                break

            failed = []
            try:
                yt = Playlist(url)
                print(f"\n開始下載 --> {yt.title}")

                for url in yt.video_urls:
                    try:
                        yt = YouTube(url)
                        print(f'下載中影片 --> {yt.title}')
                        yt.streams.get_audio_only().download(filename=del_title(yt.title)+".mp3", output_path=mp3_path)
                    except:
                        print(f'影片: {yt.title} 無法下載，跳過繼續下載下一部。', end='\n\n')
                        failed.append(yt.title)
                    else:
                        print("影片下載完成", end='\n\n')

                if len(failed) != 0:
                    error_yt = '\n'.join(failed)
                    print("下載失敗列表：\n")
                    print(error_yt, end='\n\n')
                break
            except:
                print(error_word)

    # 下載多部影片-mp4
    elif choose == "D":
        while True:
            url = input(input_word)
            if url == "back":
                break

            failed = []
            try:
                yt = Playlist(url)
                print(f"\n開始下載 --> {yt.title}")

                for url in yt.video_urls:
                    try:
                        yt = YouTube(url)
                        print(f'下載中影片 --> {yt.title}')
                        yt.streams.get_highest_resolution().download(filename=del_title(yt.title)+".mp4", output_path=mp4_path)
                    except:
                        print(f'影片: {yt.title} 無法下載，跳過繼續下載下一部。', end='\n\n')
                        failed.append(yt.title)
                    else:
                        print("影片下載完成", end='\n\n')

                if len(failed) != 0:
                    error_yt = '\n'.join(failed)
                    print("下載失敗列表：\n")
                    print(error_yt, end='\n\n')
                break
            except:
                print(error_word)

    # 結束程式
    elif choose == "END":
        break

    else:
        print("\n無效選項！\n")