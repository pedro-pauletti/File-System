<p align="center">
    <img src="https://img.shields.io/github/repo-size/pedro-pauletti/File-System-Simulator">
    <img src="https://img.shields.io/github/downloads/pedro-pauletti/File-System-Simulator/total">
    <img src="https://img.shields.io/github/contributors/pedro-pauletti/File-System-Simulator">
</p>

<p>
<h1 align="center">
    <img title="File-System-Simulator" src="https://user-images.githubusercontent.com/57163905/122691294-29082080-d205-11eb-9fe4-8518f95589d4.png" width = "250px"/>
    <h1 align="center">File-System-Simulator</h1>
</h1>
</p>


## 🇺🇸 File System Simulator for educational and didactic purposes, developed for the discipline: Operating Systems l
## 🇧🇷 Simulador de Sistemas de Arquivos com propósito educacional e didático, desenvolvido para a disciplina de Sistemas Operacionais l

<p>
<h1 align="center">
    <img title="Tela Inicial" src="https://user-images.githubusercontent.com/57163905/123202095-5b767f80-d48a-11eb-9c5f-903d7bb13556.gif" width = "900px"/>
</h1>
</p>


<a align="center" href="https://drive.google.com/file/d/11CljHm4zd4VsnoGVodOWI1Cn0g-kw78O/view?usp=sharing"><img src="https://user-images.githubusercontent.com/57163905/122691481-4be70480-d206-11eb-9a95-08755f4a58fe.png" width = "400px"></a>



Get to know the project:
=================
<!--ts-->
   * [About](#About)
   * [How to use?](#How-to-Use)
   * [Text FileSystem](#Text-FileSystem)
   * [Record FileSystem](#Record-FileSystem)
   * [Tools Used](#Tools-Used)
   * [References](#References)
   * [Author](#Author)
<!--te-->

## About 💬

In computing, filesystem  controls how data is stored and retrieved. Without a file system, data placed in a storage medium would be one large body of data with no way to tell where one piece of data stops and the next begins. By separating the data into pieces and giving each piece a name, the data is easily isolated and identified. The structure and logic rules used to manage the groups of data and their names is called a "file system."

The idea of creating a simulator that students and interested parties can understand and analyze the operation of a file system that allows the recording of files in blocks (record) or text, the simulator allows visual and didactic way, to perform searches and edit the file, adding or removing data. The entire system was developed in Python. An interface was designed using a PySimpleGUI graphical library. 


## How to use?💡
### Choosing the File System
<p>
<h1 align="center">
    <img src="https://user-images.githubusercontent.com/57163905/123370628-80d0bf80-d556-11eb-97fe-3bfd4ab28446.png" width = "300px"/>
</h1>
</p>


### Create a file
<p>
<h1 align="center">
    <img src="https://user-images.githubusercontent.com/57163905/123202830-bceb1e00-d48b-11eb-9f3b-5ca66e443ea7.gif" width = "900px"/>
</h1>
</p>


# Text FileSystem
System does not control file size in bytes, the end of a text file is indicated by placing one or more special characters, known as end-of-file marker, as padding after the last line in a text file.

- Opening a file
<p>
<h1 align="center">
    <img src="https://user-images.githubusercontent.com/57163905/123202653-61b92b80-d48b-11eb-80cd-dbbc33eaa74c.gif" width = "900px"/>
</h1>
</p>

- Searching Words
<p>
<h1 align="center">
    <img src="https://user-images.githubusercontent.com/57163905/123203431-ba3cf880-d48c-11eb-85d8-f30cabbdf352.gif" width = "900px"/>
</h1>
</p>


# Record FileSystem
 File system where data is stored as collections of records. Each record is given a unique identifier. Different access methods for records may be provided, for example records may be retrieved in sequential order, by key, or by record number.

- Opening a file
<p>
<h1 align="center">
    <img src="https://user-images.githubusercontent.com/57163905/123202690-74336500-d48b-11eb-876e-d5b036a5380f.gif" width = "900px"/>
</h1>
</p>

- Searching Records
<p>
<h1 align="center">
    <img src="https://user-images.githubusercontent.com/57163905/123203482-d6409a00-d48c-11eb-8c7b-ad8e9d52f4ba.gif" width = "900px"/>
</h1>
</p>

- Add Records
<p>
<h1 align="center">
    <img src="https://user-images.githubusercontent.com/57163905/123203605-038d4800-d48d-11eb-8bd8-4bc09be40141.gif" width = "900px"/>
</h1>
</p>

### Buttons:
- ***Launch*** – Initializes the file system selected by the user
- ***Browse*** – Search files
- ***Load File*** – Loads the selected file into the simulator
- ***Save*** – Saves the changes made to the file (Text File System)
- ***ADD*** – Adds a record to the file (Record File System)
- ***Search*** - Performs a search in the file, words for the Text File System and records, from the search key, in the Record File System<br>
- ***File:***<br>
– ***New File:*** Opens the window for creating a new file<br>
- ***Application:***<br>
– ***Restart:*** Restart the application returning to the choice page<br>
– ***Quit:*** Close the application<br>
- ***Help:***<br>
– ***About:*** Redirects user to application's GitHub page<br>


## 🛠 Tools Used

- 🔗[Python](https://www.python.org/)
- 🔗[PySimpleGUI](https://pypi.org/project/PySimpleGUI/)

## References ✔
- 🔗 [File System](https://en.wikipedia.org/wiki/File_system)
- 🔗 [Armazenamento de arquivos, em blocos ou de objetos?](https://www.redhat.com/pt-br/topics/data-storage/file-block-object-storage)
- 🔗 [Text file](https://en.wikipedia.org/wiki/Record-oriented_filesystem) 
- 🔗 [Record-oriented filesystem](https://en.wikipedia.org/wiki/Text_file)


## Author👨🏼‍💻

<p align="center">
    <a align="center" href="https://pedro-pauletti.github.io/pedropauletti.github.io/"><img src="https://user-images.githubusercontent.com/57163905/116717987-e0c04500-a9af-11eb-835f-81939e7c8bf1.jpeg" width = "150px"></a>
    <h3 align="center">Pedro Pauletti</h3>
</p>
