import PySimpleGUI as sg
import subprocess
import re
import os
import io
import shutil
from functools import lru_cache
from shutil import copyfile, copy

from PySimpleGUI.PySimpleGUI import theme_text_color

from sub_menu.ezsensor_main import open_ezsensor

#______________GLOBAL_ENV____________#
win_ezsensor = False
win_ezdent = False
win_database = False
need_to_close_main = False
#_________________END________________#



#---------------MAIN-----------------#
def main():

    global win_ezsensor
    global win_ezdent
    global win_database
    global need_to_close_main

    layout = [
        [sg.Button('EzSensor', key='open_ezsensor', size=(15,1), pad=(80,5))],
        #[sg.Button('EzDent', key='open_ezdent', size=(15,1), pad=(80,5))],
        #[sg.Button('Data Base', key='open_database', size=(15,1), pad=(80,5))],
        [sg.Text(key='-OUTPUT-')],
        [sg.Button('Выйти', key='Exit')]
    ]
    window = sg.Window('Engeneer Tools', layout, 
    auto_size_text=True,
    auto_size_buttons=True,
    resizable=False,
    grab_anywhere=False,
    border_depth=5,
    #default_element_size=(15, 1),
    finalize=True,
    size=(290, 200)
    
    )

    while True:      
    #################----LOGIC----#################
        event, values = window.read()
        # print(event, values) #debug
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "open_ezsensor":
            win_ezsensor = True
            window.Hide()
            open_ezsensor(win_ezsensor, need_to_close_main)

            if need_to_close_main == True:
                window.close()
            else: 
                window.UnHide()
    
        # if event == "open_ezdent":
        #     print("2")
        # if event == "open_database":
        #     print("3")

    window.close()