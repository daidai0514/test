import json
import random
import os

#-------------------------------------------------------------------------------------
# 若目錄不存在，則建立單階層目錄
music_path = './music'
if not os.path.isdir(music_path):
    os.mkdir(music_path)

# os.path.abspath(__file__)：__file__可為相對路徑(或檔案?)
print(os.path.abspath("./music"))
# os.getcwd()：取得目前工作目錄
print(os.getcwd()+"\\music\\")
# "c:\\Users\\andyc\\Desktop\\test\\music\\"

#-------------------------------------------------------------------------------------
with open('config.json',mode='r+',encoding='utf8') as jfile:
    jdata = json.load(jfile)

    jdata["dinner"].append("new")
    # seek() 方法用於移動文件讀取指針到指定位置。
    jfile.seek(0)
    jfile.write(json.dumps(jdata))
    # truncate() 方法用於截斷文件，如果指定了可選參數 size，則表示截斷文件為 size 個字符。
    # 如果沒有指定 size，則從當前位置起截斷；截斷之後 size 後面的所有字符被刪除。
    jfile.truncate()

print(jdata["dinner"])

print(random.choice(jdata["dinner"]))

#-------------------------------------------------------------------------------------