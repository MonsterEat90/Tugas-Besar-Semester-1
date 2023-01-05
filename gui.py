import PySimpleGUI as sg

sg.theme('LightGrey4')

layout = [[sg.Text('Database Motor')],
          [sg.Text('Masukkan Pilihan = '), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Aplikasi Input', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
