#!/usr/bin/env python3
#coding=utf-8

# 12306抢票软件
# 实际上就是个爬虫，

import requests,base64,json
# import matplot
from PIL import Image

def loginByQrCode(session,data):    
    qrcodeUrl = data["qrcode"]["Url"]
    headers = data["qrcode"]["headers"]
    postData = data["qrcode"]["data"]
    requests.post
    response = session.post(qrcodeUrl,data=postData,headers=headers)
    resData = json.loads(response.text)
    if resData["result_message"] == "生成二维码成功":        
        showQrCode(resData["image"])
        statuscode = int(checkQR(session,resData["uuid"],data["checkUrl"]))        
        while statuscode != 2:
            statuscode = int(checkQR(session,resData["uuid"],data["checkUrl"]))
        print("登录成功")
        return True
    return False

def showQrCode(base64Str):
    imageData = base64.b64decode(base64Str)
    with open("qrcode.jpg","wb") as f:
        f.write(imageData)
    
    img = Image.open("qrcode.jpg")
    img.show()

def checkQR(session,uuid,checkUrl):
    checkData = {
        "uuid":uuid,
        "appid":"otn"
    }
        
    checkResponse = session.post(checkUrl,checkData)
    checkRes = json.loads(checkResponse.text)
    statusCode = checkRes["result_code"]        
    return statusCode

if __name__ == "__main__":
    with open("data","r",encoding="utf-8") as f:
        data = json.loads(f.read())
    s = requests.session()    
    loginRes = loginByQrCode(s,data)
    if loginRes:
        pass


