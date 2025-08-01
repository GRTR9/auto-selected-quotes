import requests as req
from bs4 import BeautifulSoup
import random
import ResourcePath
import os

Data = []
url = ""

def UpUrl(new):
    with open(ResourcePath.resource_path(os.path.join("Data","data.txt")), "w") as file:
        file.write(new)

def UpStartRow(new):
    with open(ResourcePath.resource_path(os.path.join("Data","StartRow.txt")), "w") as file:
        file.write(new)

def OF_Url():
    with open(ResourcePath.resource_path(os.path.join("Data","data.txt")), "r") as file:
        return file.read()

def OF_StartRow():
    with open(ResourcePath.resource_path(os.path.join("Data","StartRow.txt")), "r") as file:
        return int(file.read())

def GetUrl():
    global url
    url = OF_Url()

def GetData():
    global Data
    #設立http請求時需要的headers，避免伺服器被判定為爬蟲而擋住
    upheaders = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    #向http請求獲取網頁原始碼
    r = req.get(url, headers=upheaders)
    #利用BeautifulSoup整理網頁
    soup = BeautifulSoup(r.text, "html.parser")
    #尋找<span>標籤的所有節點
    results = soup.find_all("span")

    if len(results) == 0:
        Data = ["Invalid URL"]
        return
    
    #獲取起始行數
    startRow = OF_StartRow()-1

    #加工節點，以「•」為切分點，利用暫存，將屬於同一個「•」的文字存入list的同一格
    temp = ""
    for resultone in results[startRow:]:
        nowSentence = (resultone.getText())
        if(nowSentence == ""):
            temp+= "\n" + nowSentence
        elif(nowSentence[0] == "•"):
            Data.append(temp)
            temp = nowSentence[2:]
        else:
            temp+= "\n" + nowSentence
    Data.append(temp)
    del Data[0]

def ChooseSentence():
    end = len(Data) - 1
    sentence = Data[random.randint(0,end)]
    return sentence

# GetUrl()
# GetData()
# print(Data)