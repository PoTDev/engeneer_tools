import PySimpleGUI as sg
import subprocess
import re
import os
import io
import shutil
from functools import lru_cache
from shutil import copyfile, copy

from PySimpleGUI.PySimpleGUI import theme_text_color

from utils.change_serialId import change_serialId
from utils.get_ezsensorid import get_ezsensorId
from sub_menu.ontop_create import ontop_create


#-------------EZSENSOR---------------#
def open_ezsensor(win_ezsensor, need_to_close_main):

    if not os.path.isdir(r"C:\EzSensor"):
        layout = [[sg.Text("Папки EzSensor не существует")], 
        [sg.Text("Возможно EzSensor не установлен")],
        [sg.Button('Назад', key='Back')]]

        window = sg.Window("EzSensor", layout, modal=True)
        choice = None
        while True:
            event, values = window.read()

            if event == "Back":
                window.close()
                win_ezsensor = False
                need_to_close_main = False
                break

            if event == sg.WIN_CLOSED:
                window.close()
                win_ezsensor = False
                need_to_close_main = True
                break
    else:
        layout = [[sg.Text("SN: "), sg.Multiline(default_text=str(get_ezsensorId()), auto_size_text=True, size=(30,1), disabled=True)],
        [sg.Button('Диагностика', key='Diagn', pad=(5,2))], 
        [sg.Button('Замена Calibration Data', key='change_cd', pad=(5,2))],
        [sg.Button('Cоздать флешку', key='create_flash', pad=(5,2))],
        [sg.Button('Назад', key='Back', pad=(5,20))]]

        window = sg.Window("EzSensor", layout)
        choice = None
        while True:
            event, values = window.read()

            if event == "Diagn":
                os.startfile(r"C:\EzSensor\_EzSensor")
                continue

            if event == 'change_cd':
                change_result = ontop_create()
                if change_result == 'local':
                    change_serialId()
                    continue
                elif change_result == 'vcsm':
                    print('2')
                    continue
                elif change_result == 0:
                    continue
            
            if event == "create_flash":
                ontop_result = ontop_create()
                if ontop_result == 'local':
                    print('1')
                    continue
                elif ontop_result == 'vcsm':
                    print('2')
                    continue
                elif ontop_result == 0:
                    continue



            if event == "Back":
                window.close()
                win_ezsensor = False
                need_to_close_main = False
                break

            if event == sg.WIN_CLOSED:
                window.close()
                win_ezsensor = False
                need_to_close_main = True
                break

                
    return(win_ezsensor, need_to_close_main)
