
import PySimpleGUI as sg
import subprocess
import re
import os
import io
import shutil
from functools import lru_cache
from shutil import copyfile, copy


def ontop_create():
    global return_data
    layout = [
        [sg.Text("Загрузить из папки на компьютере или из VCSM?")],
        [sg.Button('Папка', key='local', size=(15,1), pad=(14,5)), 
            sg.Button('VCSM', key='vcsm', size=(15,1), pad=(14,5))],
    ]

    window = sg.Window("EzSensor", layout, keep_on_top=True)

    while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return_data = 0
                break
            
            if event == 'local':
                window.close()
                return_data = 'local'
                break
            
            if event == 'vcsm':
                window.close()
                return_data = 'vcsm'
                break
    return(return_data)
            
