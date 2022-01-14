import PySimpleGUI as sg
import subprocess
import re
import os
import io
import shutil
from functools import lru_cache
from shutil import copyfile, copy


# def create_flash():

#Обнаружение папки
# cal_data = sg.popup_get_folder('Введите путь до Calibration Data')

# fresh_folder = sg.popup_get_folder('Введите путь до оригинала флешки')

# install_folder = sg.popup_get_folder('Введите папку для сохранения')

cal_data = r'C:\Users\ПотаповИА\Downloads\E15OHFD621-33639'
fresh_folder = r'C:\Users\ПотаповИА\Desktop\VATECH\Шаблоны флешок Визиограф\универсальная (win7)'
install_folder = r'C:\Users\ПотаповИА\Desktop\VATECH\тест'



#Копирование оринала флешки в папку назначения
new_list= []
for i in os.listdir(fresh_folder):
    file_path = os.path.join(fresh_folder, i)
    new_list.append(file_path)
    print(file_path)

len_of_list = len(new_list)
print(len_of_list)

#присоединение серийного номера визика и создание папки
# sn_number = get_sn_number()


sn_number = os.path.basename(cal_data)
print('Серийный номер: '+ sn_number)

final_install_folder = os.path.join(install_folder, 'flash_'+ sn_number)
print('Куда сохранится флешка: '+ final_install_folder)

if os.path.isdir(final_install_folder):
    


#итоговое копирование папки
for i in range(len_of_list):
    shutil.copytree(new_list[i], final_install_folder, dirs_exist_ok=True) 


#копирование калибровочных в флешку
#_________Копирование в папку_________#

#ДЛЯ НОВОЙ-----------------------------------------------------
if os.path.basename(fresh_folder) == r'20 версия последняя с vcsm':
    new_cal_for_copy = os.path.join(final_install_folder, 'Setup', 'EzSensor', 'Console', 'CAL')
    new_list= []
    for i in os.listdir(cal_data):
        file_path = os.path.join(cal_data, i)
        new_list.append(file_path)
        print('Папки внутри: '+ file_path)

    len_of_list = len(new_list)
    print(len_of_list)


    #если первая папка, переместится во вторую
    if len_of_list == 1:
        print('new_list[0] '+ new_list[0])
        cal_data = new_list[0]

        new_list= []
        for i in os.listdir(cal_data):
            file_path = os.path.join(cal_data, i)
            new_list.append(file_path)
            print(file_path)
        len_of_list = len(new_list)
        print(len_of_list)


    for i in range(len_of_list):
        copy(new_list[i], new_cal_for_copy) 

    copy(*filter(lambda x: 'EzSensor.ini' in x, new_list), os.path.join(final_install_folder, 'Setup', 'EzSensor', 'Console'))



#ДЛЯ УНИВЕРСАЛЬНОЙ----------------------------------------------
elif os.path.basename(fresh_folder) == r'универсальная (win7)':
    new_cal_for_copy = os.path.join(final_install_folder, 'CAL')

    new_list= []
    for i in os.listdir(cal_data):
        file_path = os.path.join(cal_data, i)
        new_list.append(file_path)
        print('Папки внутри: '+ file_path)

    len_of_list = len(new_list)
    print(len_of_list)


    #если первая папка, переместится во вторую
    if len_of_list == 1:
        print('new_list[0] '+ new_list[0])
        cal_data = new_list[0]

        new_list= []
        for i in os.listdir(cal_data):
            file_path = os.path.join(cal_data, i)
            new_list.append(file_path)
            print(file_path)
        len_of_list = len(new_list)
        print(len_of_list)


    for i in range(len_of_list):
        copy(new_list[i], new_cal_for_copy) 

    copy(*filter(lambda x: 'EzSensor.ini' in x, new_list), final_install_folder)


