import requests
import ddddocr

if __name__ == '__main__':
    # 利用ddddocr进行简单的验证码识别
    ocr = ddddocr.DdddOcr()
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    img_url = "https://img-blog.csdnimg.cn/img_convert/3d98a624abfeecbc05fbb8d720e69b10.png"
    img = requests.get(img_url, headers=headers).content
    result = ocr.classification(img)
    print(result)
