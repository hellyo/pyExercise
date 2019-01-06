#!/usr/bin/env python3
#coding=utf-8

# 12306抢票软件
# 实际上就是个爬虫，

import requests,base64,json
# import matplot
from PIL import Image

def loginByQrCode(session,data): 
    '''
    @description: 通过扫描二维码登陆12306
    @param {type} 
    @return: True:登陆成功，False:登陆失败
    '''   
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
    '''
    @description:根据base64字符串显示图片
    @param {type} 
    @return: 
    '''
    imageData = base64.b64decode(base64Str)
    with open("qrcode.jpg","wb") as f:
        f.write(imageData)
    
    img = Image.open("qrcode.jpg")
    img.show()

def checkQR(session,uuid,checkUrl):
    '''
    @description: 扫码后检查是否登录成功
    @param {type} 
    @return: 
    '''
    checkData = {
        "uuid":uuid,
        "appid":"otn"
    }
        
    checkResponse = session.post(checkUrl,checkData)
    checkRes = json.loads(checkResponse.text)
    statusCode = checkRes["result_code"]        
    return statusCode

def searchForTicket(s,queryData,**kwargs):
    '''
    @description: 余票查询
    @param s：requests.sessionc对象，当前和12306的连接对象 
    @param queryData:dict = { 
                formW：str 出发站
                toW:str 到达站
                date:str 出发日期，格式：yyyy-mm-dd
                ticketType:str 票的类型，成人票（ADULT）还是学生票(0x00)
            }
    @return: tuple(bool:是否有余票)
    '''
    searchData = {
        "leftTicketDTO.train_date":queryData["date"],
        "leftTicketDTO.from_station":queryData["fromW"],
        "leftTicketDTO.to_station":queryData["toW"],
        "purpose_codes":queryData["ticketType"]
    }    
    url = queryData["url"]
    url += "?"
    for item in searchData:
        url += (item + "=" + searchData[item] + "&")

    res = s.get(url[:-1])
    print(res.text)


def orderTicket():
    pass

def sendmail():
    pass

if __name__ == "__main__":
    with open("12306/data","r",encoding="utf-8") as f:
        data = json.loads(f.read())
    s = requests.session()    
    loginRes = loginByQrCode(s,data)
    if loginRes:
        searchForTicket(s,data["queryData"])
        # orderTicket()



