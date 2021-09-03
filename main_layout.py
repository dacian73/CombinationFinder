import PySimpleGUI as sg

myLayout = [
    [sg.Text("Insert list of values (one per row)")],
    [sg.Multiline(key='VALUES')],
    [sg.Text("Insert the sum")],
    [sg.Input(key='SUM')],
    [sg.Button("Find Combinations")],
    [sg.Output(size=(80, 20))],
    [sg.Button("Close")],
]
