import PySimpleGUI as sg
from helpers import show_table
sg.theme('DarkAmber')

layout = [  
            [sg.Text("Welcome to Excel Simple Display")],
            [sg.Text('Enter the name of excel file'), sg.InputText(), sg.Text(".xls or .xlsx")],
            [sg.Button('Ok', disabled_button_color="black"), sg.Button('Exit',size =(10,1),)]
         ]


window = sg.Window('ESD', layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit': 

        break

    if event == "Ok":
        print(type(values))
        print(values)
        show_table(values[0])

window.close()