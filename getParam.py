import urllib.parse

def extract_params(url):
    # 解析URL
    parsed_url = urllib.parse.urlparse(url)
    # 解析查询参数
    params = urllib.parse.parse_qs(parsed_url.query)
    # 遍历并打印每个参数及其值
    for param, values in params.items():
        for value in values:
            print(f"{param}={value}")

    print("=====================================")
    for param, values in params.items():
        for value in values:
            print(f"{param}")

# 示例用法
url = r"https://www.bing.com/search?pglt=2083&q=%E5%8D%B8%E8%BD%BDedge&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEDSAQgzMzQ2ajBqMagCALACAA&FORM=ANSPA1&PC=U531&mkt=zh-CN&rdr=1&rdrig=8923C68117594E7BB64E2570DE4BBDF1"
extract_params(url)
