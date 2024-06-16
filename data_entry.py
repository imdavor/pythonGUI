import PySimpleGUI as sG

# Add so me color to the window
sG.theme('DarkTeal9')

layout = [
    [sG.Text('Please fill out the following fields:')],
    [sG.Text('Name', size=(15, 1)), sG.InputText(key='Name')],
    [sG.Submit(), sG.Exit()]
]
window = sG.Window('Simple data entry form', layout)

# Check what is clicked
while True:
    event, values = window.read()
    if event == sG.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        print(event, values)
window.close()
