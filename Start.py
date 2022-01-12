import PySimpleGUI as sg
import subprocess
import re
import os
import io
import shutil
from functools import lru_cache
from shutil import copyfile, copy

from PySimpleGUI.PySimpleGUI import theme_text_color

#______________GLOBAL_ENV____________#
win_ezsensor = False
win_ezdent = False
win_database = False
need_to_close_main = False
#_________________END________________#


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
    else:
        sg.popup("Отменено", custom_text = ("OK"))



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




#-------------EZSENSOR---------------#
def open_ezsensor():
    global win_ezsensor
    global need_to_close_main

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
        [sg.Button('Диангостика', key='Diagn', pad=(5,5))], 
        [sg.Button('Смена SN', key='change_id', pad=(5,1))],
        [sg.Button('Назад', key='Back', pad=(5,20))]]

        window = sg.Window("EzSensor", layout, modal=True)
        choice = None
        while True:
            event, values = window.read()

            if event == "Diagn":
                os.startfile(r"C:\EzSensor\_EzSensor")
                continue

            if event == 'change_id':
                change_serialId()
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

            if event == "Сохранить":
                print('kek')



#---------------MAIN-----------------#
def main():

    global win_ezsensor
    global win_ezdent
    global win_database
    global need_to_close_main

    layout = [
        [sg.Button('EzSensor', key='open_ezsensor', size=(15,1), pad=(80,5))],
        [sg.Button('EzDent', key='open_ezdent', size=(15,1), pad=(80,5))],
        [sg.Button('Data Base', key='open_database', size=(15,1), pad=(80,5))],
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
            open_ezsensor()

            if need_to_close_main == True:
                window.close()
            else: 
                window.UnHide()
    
        if event == "open_ezdent":
            print("2")
        if event == "open_database":
            print("3")

    window.close()

if __name__ == "__main__":
    main()