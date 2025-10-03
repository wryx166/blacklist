import pypinyin

genshinList: list[str]
genshin: str
with open("genshin", "r", encoding="utf-8") as f:
    genshinList = [line for line in f.read().split("\n") if line.strip()]
with open("genshin", "w+", encoding="utf-8") as f:
    genshinList.sort(key=lambda x: ''.join(pypinyin.lazy_pinyin(x)))
    f.write('\n'.join(genshinList))
with open("output.txt", "w+", encoding="utf-8") as output:
    genshin = '|'.join(genshinList)
    output.write(f"/{genshin}/\n")
    output.write(f"//{genshin}//\n")
