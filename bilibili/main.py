import pypinyin
import os
import stat
import unicodedata

genshinList: list[str]
genshin: str


def strip_symbols(s: str) -> str:
    # 删除 Unicode 分类为 P(标点) 或 S(符号) 的字符
    return ''.join(ch for ch in s if unicodedata.category(ch)[0] not in ("P", "S"))


with open("genshin", "r", encoding="utf-8") as f:
    genshinList = [line for line in f.read().split("\n") if line.strip()]
# 按拼音排序，先去掉符号并转小写
genshinList.sort(key=lambda x: "".join(pypinyin.lazy_pinyin(strip_symbols(x).lower())))
with open("genshin", "w+", encoding="utf-8") as f:
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
