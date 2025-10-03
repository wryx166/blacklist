with open("genshin", encoding="utf-8") as f:
    genshin = f.read().replace("\n", "|")
    with open("output.txt", "w+", encoding="utf-8") as output:
        output.write(f"/{genshin}/\n")
        output.write(f"//{genshin}//\n")
