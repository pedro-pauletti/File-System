import PySimpleGUI as sg
import interface as vs
import os
from collections import Counter
import pickle
import datetime
import sys
import subprocess
import webbrowser

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


window =  sg.Window('File System', vs.layout_choice, default_element_size=(50, 1), auto_size_text=False, finalize=True, resizable=True, icon = 'assets\logo.ico')


record = 0

class Student:

    def __init__(self, id, name, age, turma):
        self.id = id
        self.name = name
        self.age = age
        self.turma = turma

    def __str__(self):
        return "ID = " + str(self.id) + "\nName = " + self.name + "\nAge = " + str(self.age) + "\nClass = " + self.turma + "\n"


def searchWords (text, words):
    text = text.lower().split()
    words = words.lower().replace(',', '').split() 

    listWords = []

    for w in words:
        for t in text:
            if w == t:
                listWords.append(t)

    return Counter(listWords) 


def loadRecord(file):
    record = []
    with open(file, "r+b") as mypicklefile:
        while True:
            try: 
                record.append(pickle.load(mypicklefile))
            except EOFError:
                break
    return record

def createFileRecord(nameFile):
    open(nameFile, "wb")
    window['input'].update(value= nameFile)
    window['output'].update(value = '')
    window['lastMod'].update(value= modification_date(window['input'].get()))
    loadRecord(nameFile)

def createFileTxt(nameFile):
    nameFile = nameFile + ".txt"
    open(nameFile, "w")
    window['body'].update(value = '')
    window['output'].update(value = '')
    window['input'].update(value= nameFile)
    window['lastMod'].update(value= modification_date(window['input'].get()))
    with open(nameFile,'a+', encoding='utf-8') as arq:
        file = arq.read()
    with open(nameFile,'r+', encoding='utf-8') as arq:
        file = arq.read()
    window['body'].update(value= file)

def writeRecord(id, name, age, sclass, file):
    with open(file, "a+b") as mypicklefile:
        pickle.dump(Student(id, name, age, sclass), mypicklefile)

def searchRecord(combo, attribute, file):
    with open(file, "rb") as mypicklefile:
        while True:
            try: 
                aux = pickle.load(mypicklefile)
                if combo == 'ID':
                    if aux.id == attribute:
                        window['output'].print(aux)
                elif combo == 'Name':
                    if aux.name == attribute:
                        window['output'].print(aux)
                elif combo == 'Age':
                    if aux.age == attribute:
                        window['output'].print(aux)
                else:
                    if aux.turma == attribute:
                        window['output'].print(aux)
            except EOFError:
                break
    return 'Record Not Found'
        


while True:

    event, values = window.read()

    if event == 'Launch':
        if window['record'].get() == True:
            window = sg.Window('File System', vs.layout_record, default_element_size=(50, 1), auto_size_text=False, finalize=True, resizable=True, icon = 'assets\logo.ico')
            record = 1
        else:
            window = sg.Window('File System', vs.layout_text, default_element_size=(50, 1), auto_size_text=False, finalize=True, resizable=True, icon = 'assets\logo.ico')

    if event == 'Restart':
        window.close()
        subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    if event == 'About':
        webbrowser.open('https://github.com/pedro-pauletti/File-System')

    if event == 'New File':
        nameFile = sg.popup_get_text('Name of File:', title= 'Create File')
        if record == 1:
            createFileRecord(nameFile)
        else:
            createFileTxt(nameFile)

    if event == 'LoadTxt':
        window['input'].update(value= window['file'].get())
        window['lastMod'].update(value= modification_date(window['input'].get()))
        with open(window['file'].get(),'a+', encoding='utf-8') as arq:
            file = arq.read()
        with open(window['file'].get(),'r+', encoding='utf-8') as arq:
            file = arq.read()
        window['body'].update(value= file)

    if event == 'LoadRecord':
        window['output'].update(value= '')
        window['input'].update(value= window['file'].get())
        window['lastMod'].update(value= modification_date(window['input'].get()))
        records = loadRecord(window['file'].get())
        for i in range(len(records)):
            window['output'].print(records[i])


    if event == 'Save':
        with open(window['input'].get(),'r+', encoding='utf-8') as arq:       
            arq.write(window['body'].get())
            arq.truncate()
        window['lastMod'].update(value= modification_date(window['input'].get()))


    if event == 'ADD':
        writeRecord(window['ID'].get(), window['Name'].get(), window['Age'].get(), window['Class'].get(), window['input'].get())
        window['ID'].update(value= '')
        window['Name'].update(value= '')
        window['Age'].update(value= '')
        window['Class'].update(value= '')
        window['lastMod'].update(value= modification_date(window['input'].get()))

        window['output'].update(value= '')
        records = loadRecord(window['input'].get())
        for i in range(len(records)):
            window['output'].print(records[i])
            

    if event == 'SearchTxt':
        window['output'].update(value = '')
        words = window['word'].get().lower().replace(',', '').split() 
        print(words)
        numLine = 1
          
        for i in range(len(words)):
            with open(window['input'].get(),'r') as arq: 
                for line in arq:
                    if words[i] in line.lower():
                        window['output'].print(words[i] + ' found in line ' + str(numLine) + '\n')
                    numLine += 1
            arq.close()
            numLine = 1

        window['output'].print(searchWords(window['body'].get(), window['word'].get()))

    if event == 'SearchRecord':
        window['output'].update(value = '')
        searchRecord(window['combo'].get(), window['attribute'].get(), window['file'].get())


    
