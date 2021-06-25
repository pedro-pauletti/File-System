import PySimpleGUI as sg
sg.theme('Dark Grey 1')

menu = [['&File', ['&New File']], ['&Application', ['&Restart','&Quit']],
        ['&Help', ['&About']] ]


layout_choice = [
                [sg.Radio('Record', "RadioDemo", default=True, size=(10,1), k='record'), sg.Radio('Text', "RadioDemo", default=True, size=(10,1), k='text')],
                [sg.Button('Launch', key='Launch')],
        ]

left_col_text = [
                [sg.Multiline(default_text= '', key='body', size=(70,30))],
                [sg.Button('Save', key='Save')],
        ]

right_col_text = [
                [sg.Text('Search Word:',size = (5,1)), sg.InputText(size=(50, 1), key='word'),sg.Button('Search', key='SearchTxt')],
                [sg.Text('Search Word Output')],
                [sg.Multiline(default_text= '', key='output', size=(70,25))]
        ]        

layout_text = [
                [sg.Menu(menu, key='-MENU-')],
                [sg.Text('Choose a name or a file path:', size = (25,1)), sg.InputText(size=(50, 1), key='file'), sg.FileBrowse(key = 'Browse'), sg.Button('Load File', key='LoadTxt')],
                [sg.Text('Current File:', size = (15,1)), sg.Text('', key='input')],
                [sg.Text('Last Modification:',size = (15,1)), sg.Text('', key='lastMod')],
                [sg.HorizontalSeparator()],
                [sg.Column(left_col_text, element_justification='c'), sg.VSeperator(),sg.Column(right_col_text, element_justification='c')]
        ]

left_col_record = [
                [sg.Text('Student Registration')],
                [sg.Text('ID:',size = (5,1)),  sg.InputText(size=(30, 1), key='ID')],
                [sg.Text('Name:',size = (5,1)),  sg.InputText(size=(30, 1), key='Name')],
                [sg.Text('Age:',size = (5,1)),  sg.InputText(size=(30, 1), key='Age')],
                [sg.Text('Class:',size = (5,1)),  sg.InputText(size=(30, 1), key='Class')],
                [sg.Button('ADD', key='ADD')],
        ]

right_col_record = [
                [sg.Text('Search Record By:',size = (15,1)), sg.Combo(values=('ID', 'Name', 'Age', 'Class'), default_value='ID', readonly=True, k='combo', size = (5,1)), sg.InputText(size=(50, 1), key='attribute'),sg.Button('Search', key='SearchRecord')],
                [sg.Text('Record Output')],
                [sg.Multiline(default_text= '', key='output', size=(50,30))]
        ]


layout_record = [
                [sg.Menu(menu, key='-MENU-')],
                [sg.Text('Choose a name or a file path:'), sg.InputText(size=(50, 1), key='file'), sg.FileBrowse(key = 'Browse'), sg.Button('Load File', key='LoadRecord')],
                [sg.Text('Current File:'), sg.Text('', key='input')],
                [sg.Text('Last Modification:',size = (15,1)), sg.Text('', key='lastMod')],
                [sg.HorizontalSeparator()],
                [sg.Column(left_col_record, element_justification='c'), sg.VSeperator(),sg.Column(right_col_record, element_justification='c')]
        ]

layout_newFile = [
                [sg.Text('Name of File:'),  sg.InputText(size=(30, 1), key='nameFile')],
                [sg.Button('Create File', key='Create')],
        ]