import json
import os
def readData(path=None,name='history.json'):
    with open(name, 'r',encoding='utf-8') as fh: #открываем файл с данными о исполнителях на чтение
        history = json.load(fh)
    return(history)

def writeData(new,name='history.json'):
    history_old = readData(name=name)
    history_old.update(new)
    with open(name, "w") as write_file:
        json.dump(history_old, write_file,ensure_ascii=False)
    return ('ok')

def readHtml(nameHtml):
    with open(nameHtml, 'r',encoding='utf-8') as fh: #открываем файл с даннымина чтение
        codeHtml = fh.readline()
    return(codeHtml)

def writeHtml(new,name):
    with open("./templates/"+name, 'w', encoding='utf-8') as write_file:
        write_file.write(str(new))
    return('ok')