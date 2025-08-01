import eel
import LinkWebData as LWD
from datetime import datetime


@eel.expose #用decorator的方式，將JS要呼叫的PY function暴露給eel, 讓eel當作一個library  去給JS使用
def Reloadsetting(judge):
    result = None
    if(judge == "url"):
        result = LWD.OF_Url()     
    elif(judge == "startRow"):
        result = LWD.OF_StartRow()
    return result

@eel.expose #用decorator的方式，將JS要呼叫的PY function暴露給eel, 讓eel當作一個library  去給JS使用
def Upsetting(content):
    url, startRow = content
    LWD.UpUrl(url)
    LWD.UpStartRow(startRow)
    LWD.GetUrl()
    LWD.GetData()
    reselt = "Python函式(Upsetting)執行完畢"
    return reselt

@eel.expose
def initSentence():
    return LWD.ChooseSentence()

@eel.expose
def UpSentence():
    print(datetime.now() , ":已更新句子", sep="")
    return LWD.ChooseSentence()


def WebUI():
    eel.init('WebUI') # eel.init(網頁的資料夾)
    eel.start('main.html', mode='chrome-app', port=8080, cmdline_args=['--start-maximized']) 
