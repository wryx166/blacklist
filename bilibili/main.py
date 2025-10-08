import pypinyin
import os
import stat

genshinList: list[str]
genshin: str

with open("genshin", "r", encoding="utf-8") as f:
    genshinList = [line for line in f.read().split("\n") if line.strip()]
with open("genshin", "w+", encoding="utf-8") as f:
    genshinList.sort(key=lambda x: ''.join(pypinyin.lazy_pinyin(x)))
    f.write('\n'.join(genshinList))
with open("output.txt", "w+", encoding="utf-8") as output:
    # genshin = '|'.join(genshinList)
    temp = ""
    tempList = []
    for item in genshinList:
        if len(temp + item + "|") < 62:
            if temp != "":
                temp += "|" + item
            else:
                temp = item
        else:
            tempList.append(temp)
            temp = item
    tempList.append(temp)

    for item in tempList:
        output.write(f"/{item}/\n")
        output.write(f"//{item}//\n")
        output.write("\n")
