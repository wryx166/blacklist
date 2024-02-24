# 原始字符串  
original_string = "github.com##.Box-sc-g0xbh4-0.bDcVHV:has-text(%s)" 
  
# 复制base_blacklist.txt的内容到blacklist.txt 
with open("base_list.txt", "r") as source_file:  
    with open("blacklist.txt", "w") as target_file:  
        target_file.writelines(source_file)
  
# 读取github/blacklist_github.txt文件中的每一行，并插入到指定的字符串中，然后追加到blacklist.txt  
with open("github/blacklist_github.txt", "r") as file:  
    lines = file.readlines()  
  
# 在blacklist.txt文件末尾追加新内容  
with open("blacklist.txt", "a") as file:  
    file.write("\n")
    file.write("\n")
    for line in lines:  
        # 去除每行末尾的换行符并插入到原始字符串中  
        new_string = original_string % line.strip()
        file.write(new_string + "\n")  
  
print("新内容已追加到blacklist.txt文件中！")