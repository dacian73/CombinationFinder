import PySimpleGUIWeb as sg

myLayout = [
    [sg.Text("Insert list of values (one per row)")],
    [sg.Multiline(key='VALUES')],
    [sg.Text("Insert the sum")],
    [sg.Input(key='SUM')],
    [sg.Button("Find Combinations")],
    [sg.Output(size=(80, 20))],
    [sg.Button("Close")],
]

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print("%s = %s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])


myWindow = sg.Window(title="Combination finder", layout=myLayout, web_port=2222, web_start_browser=False)

while True:
    event, values = myWindow.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    if event == "Find Combinations":
        print('All the possible combinations:')
        subset_sum(list(map(float, values['VALUES'].splitlines())),
                   float(values['SUM']))
myWindow.close()




