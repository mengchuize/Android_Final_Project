import base64

def convert(picurl):
    with open(picurl, "rb") as f:  # 转为二进制格式
        base64_data = base64.b64encode(f.read())
    return base64_data.decode()

if __name__=='__main__':
    print(convert('F:\\WebServer\\AndroidWebServer\\userImages\\001.png'))