//這邊必須要async funciton 因為python返回需要時間，而JS 又不會block，
//所以需要用async function 加上await去呼叫PY function
async function js_Reloadsetting()
{ 
    
    //呼叫的方式，就是加上eel.加上剛剛被expose PY function的名稱然後多加()輸入參數，最後加()取值
    var url = await eel.Reloadsetting("url")()  //py回傳string
    var startRow = await eel.Reloadsetting("startRow")()    //py回傳int
    
    //更改input的value
    document.getElementById("url").value = url
    document.getElementById("startRow").value = String(startRow)
}

async function js_Upsetting()
{ //help me to solve Uncaught (in promise) TypeError: eel.Upsetting is not a function

    var url = document.getElementById("url").value
    var startRow = document.getElementById("startRow").value
    var result = await eel.Upsetting([url, startRow])()
    console.log(result)
    alert("已更改")
}

async function js_Upsentence()
{
    var p_sentence = document.getElementById("sentence")
    p_sentence.innerText = await eel.UpSentence()()
}

async function js_initSentence()
{
	var p_sentence = document.getElementById("sentence")
	p_sentence.innerText = await eel.initSentence()()
}

window.onload = js_initSentence()