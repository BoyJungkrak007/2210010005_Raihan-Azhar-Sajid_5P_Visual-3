import PySimpleGUI as sg
sg.theme("LightGreen8")
sg.theme_text_color("#00ffff")
Window = sg.Window('Profile Berwarna', 
    [[sg.Text('NPM :2210010005'),],
        [sg.Text('Nama :Raiahan Azhar Sajid')], 
        [sg.Text('kelas :5P reguler Banjarmasin')],
        [sg.Text('matkul : pempgraman Visual')],
    ],size=(500,200)).read(close=True)
event, values=Window.read()
Window.close()