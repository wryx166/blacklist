with open("input.txt", "r", encoding="utf-8") as f:
    i = [line for line in f.read().split("\n") if line.strip()]
    output = "("+"|".join(i)+")"

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(f"/{output}/\n")
    f.write(f"//{output}//\n")