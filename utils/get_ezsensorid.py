import PySimpleGUI as sg
import subprocess
import re
import os
import io
import shutil
from functools import lru_cache
from shutil import copyfile, copy

from PySimpleGUI.PySimpleGUI import theme_text_color


def get_ezsensorId():
    full_serial_number = []
    word = u'SerialId='

    if not os.path.isfile(r"C:\EzSensor\EzSensor.ini"):
        return("Данные отсутсвуют")
    else:
        with io.open(r"C:\EzSensor\EzSensor.ini", encoding='utf-8') as file:
            for line in file:
                if word in line:
                    full_serial_number = line

        serial_number = []
        for i in range(9, len(full_serial_number)):
            serial_number.append(full_serial_number[i])
            i+=1

        result_serial_number = "".join(serial_number)
        
    return(result_serial_number)