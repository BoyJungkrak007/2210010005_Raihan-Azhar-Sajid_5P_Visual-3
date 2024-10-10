import PySimpleGUI as sg
window = sg.Window('Selamat Datang Di Kelas', 
    [[sg.Text("Selamat datang di kelas", font=("Arial",25,"italic","bold","underline",))],
        [sg.Text('NPM       : 2210010005'),],
        [sg.Text('Nama      : Raihan Azhar Sajid')], 
        [sg.Text('kelas     : 5P reguler Banjarmasin')],
        [sg.Text('matkul    : pempgraman Visual')],
    ],size=(500,200))
event, values=window.read()
window.close()
