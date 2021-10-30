#coding=utf-8

import requests
import base64


def get_file_content(filePath):   #读取截图方法
  with open(filePath, 'rb') as fp:
    return fp.read()


def ocr(img_name):
    img = get_file_content(img_name)
    bi = base64.b64encode(img)
    data = {
        "tutu":"zxmasdogk",
        "img":bi
        }
    url = "http://82.156.106.10:8888?API_ID=tutu"

    img_req = requests.post(url=url,data=data)
    return(img_req.text)

