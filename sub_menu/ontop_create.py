
import PySimpleGUI as sg
import subprocess
import re
import os
import io
import shutil
from functools import lru_cache
from shutil import copyfile, copy


def ontop_create():
    layout = [
        [sg.Text("Загрузить из папки на компьютере или из VCSM?")],
        [sg.Button('Папка', key='local', size=(15,1), pad=(14,5)), 
            sg.Button('VCSM', key='vcsm', size=(15,1), pad=(14,5))],
    ]

    window = sg.Window("EzSensor", layout)

    while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                break
            
            if event == 'local':
                window.close()
                return('local')
            
            if event == 'vcsm':
                window.close()
                return('vcsm')
