import tkinter as tk
import LinkWebData as LWD
import os
import ResourcePath

KidWindow = {"Zero" : 1} #用於避免重複子視窗
ms_sentence = None

def UI():
    global ms_sentence
    global window
    #建立主視窗
    window = tk.Tk()
    window.title("名言佳句")
    #大小&置中
    windowwidth = 800
    windowheight = 500
    CenterWindow(window, windowwidth, windowheight)
    window.minsize(width=windowwidth, height=windowheight)
    #禁止拉動大小
    #window.resizable(False,False)
    #ICON
    window.iconbitmap(ResourcePath.resource_path("Base.ico"))
    #置頂
    window.attributes("-topmost", True)

    #Img
    img_settings = tk.PhotoImage(file=ResourcePath.resource_path(os.path.join("img","gear_settings.png")))
    img_refresh = tk.PhotoImage(file=ResourcePath.resource_path(os.path.join("img","refresh.png")))
    #btn_settings
    btn_settings = tk.Button(text="設定", font="微軟正黑體",bd=0.5)
    btn_settings.config(image=img_settings)
    btn_settings.config(command=BuildSettingsWindow)
    btn_settings.place(x=0, y=0, anchor="nw")
    btn_refresh = tk.Button(text="刷新", font="微軟正黑體",bd=0.5)
    btn_refresh.config(image=img_refresh)
    btn_refresh.config(command= UpLb_sentence)
    btn_refresh.place(x=17, y=0, anchor="nw")
    #label
    ms_sentence = tk.Message(text="句子", font="標楷體 18", justify="left", width=700)
    ms_sentence.place(anchor="center", relx=0.5, rely=0.5)
    ms_sentence.config(text= LWD.ChooseSentence())








    #常駐主視窗，否則會一閃即逝
    window.mainloop()


def CenterWindow(root, width, height):
    screenwidth = root.winfo_screenwidth()    # 取得螢幕寬度
    screenheight = root.winfo_screenheight()  # 取得螢幕高度
    root.geometry(f'{width}x{height}+{int((screenwidth - width)/2)}+{int((screenheight - height)/2) }') #寬*高+x+y

def UpSettings():
    #獲取值
    url = en_url.get()
    startRow = en_startRow.get()
    LWD.UpUrl(url)
    LWD.UpStartRow(startRow)
    LWD.GetUrl()
    LWD.GetData()
    CloseSettingsWindow()
    

def UpLb_sentence():
    ms_sentence.config(text= LWD.ChooseSentence())


def BuildSettingsWindow():
    global settingsWindow
    global en_startRow, en_url
    if(KidWindow["Zero"]):
        KidWindow["Zero"] = 0
        window.attributes("-topmost", False) #取消主視窗的置頂，好讓子視窗好找
        #子視窗建立
        settingsWindow = tk.Toplevel()
        settingsWindow.title("設定")
        settingsWindow.attributes("-toolwindow", 1)
        CenterWindow(settingsWindow, 400, 300)
        #按鈕
        btn_check = tk.Button(settingsWindow, text="確認", font="微軟正黑體", bd=0.5)
        btn_check.grid(row=2, column=1, columnspan=2)
        #Label
        lb_url = tk.Label(settingsWindow, text="url", font="微軟正黑體")
        lb_url.grid(row=0, column=0, sticky="w")
        lb_startRow = tk.Label(settingsWindow, text="起始行", font="微軟正黑體")
        lb_startRow.grid(row=1, column=0, sticky="w")
        #輸入框
        en_url = tk.Entry(settingsWindow, font="微軟正黑體")
        en_url.insert(0, LWD.OF_Url())
        en_url.grid(row=0, column=1)
        en_startRow = tk.Entry(settingsWindow, font="微軟正黑體")
        en_startRow.insert(0, LWD.OF_StartRow())
        en_startRow.grid(row=1, column=1)
        

        #按鈕事件
        btn_check.config(command= UpSettings) #command必須為無括弧函式，所以用lambda將其包成函式回傳
        #自定義刪除
        settingsWindow.protocol("WM_DELETE_WINDOW", CloseSettingsWindow)
    else:
        #將settingsWindow視窗移上來
        settingsWindow.lift()
        # settingsWindow.deiconify() #解除最小化

def CloseSettingsWindow():
    KidWindow["Zero"] = 1
    window.attributes("-topmost", True)
    settingsWindow.destroy()


# UI()