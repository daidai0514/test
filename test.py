import json
import random

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