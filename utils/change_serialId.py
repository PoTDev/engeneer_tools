import PySimpleGUI as sg
import subprocess
import re
import os
import io
import shutil
from functools import lru_cache
from shutil import copyfile, copy

from PySimpleGUI.PySimpleGUI import theme_text_color


def change_serialId():

    #Обнаружение папки
    new_vis_folder = sg.popup_get_folder('Please enter a folder name')
    print(new_vis_folder)

    #_________Удаление из EzSendor_________#

    if sg.popup_yes_no('Старые файлы удалятся. Продолжить? ') == 'Yes':
        #deleting CAL

        try:
            os.mkdir(r'C:\EzSensor\CAL')
        except OSError:
            print ("Директория уже существует. Создать директорию не удалось.")
        else:
            print ("Успешно создана директория")

        folder = r'C:\EzSensor\CAL'
        for i in os.listdir(folder):
            file_path = os.path.join(folder, i)
            print(file_path)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

        #deleting EzSensor.ini in main folder
        folder = r'C:\EzSensor\EzSensor.ini'
        try:
            if os.path.isfile(folder) or os.path.islink(folder):
                os.unlink(folder)

        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (folder, e))



        #_________Копирование в папку_________#
        new_list= []
        for i in os.listdir(new_vis_folder):
            file_path = os.path.join(new_vis_folder, i)
            new_list.append(file_path)
            print(file_path)

        len_of_list = len(new_list)
        print(len_of_list)


        #если первая папка, переместится во вторую
        if len_of_list == 1:
            print(new_list[0])
            new_vis_folder = new_list[0]

            new_list= []
            for i in os.listdir(new_vis_folder):
                file_path = os.path.join(new_vis_folder, i)
                new_list.append(file_path)
                print(file_path)
            len_of_list = len(new_list)
            print(len_of_list)


        for i in range(len_of_list):
            copy(new_list[i], r'C:\EzSensor\CAL') 
        
        copy(*filter(lambda x: 'EzSensor.ini' in x, new_list), r'C:\EzSensor\CAL') 
        copy(*filter(lambda x: 'EzSensor.ini' in x, new_list), r'C:\EzSensor')

    else:
        sg.popup("Отменено", custom_text = ("OK"))