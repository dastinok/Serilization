'''Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.'''
import csv
import os
import pickle

exten = 'pickle'

def get_picle(path):
    for file in (os.listdir()):
        if os.path.isfile(file):
            initial_name, initial_ext = os.path.join(file).split('.')
            if initial_ext == exten:
                with open(file, 'rb') as f:
                    new_dict = pickle.load(f)
                    #print(f'{new_dict = }')
                    initial_name = initial_name + '.csv'
                    with open(initial_name, 'w') as f:
                        csv_write = csv.DictWriter(f, fieldnames=[value for value in new_dict[0]],
                                                   dialect='excel',
                                                   quoting=csv.QUOTE_ALL)
                        csv_write.writeheader()
                        all_data = []
                        for i, dict_row in new_dict:
                        #    if i != 0:
                                all_data.append(new_dict)
                        csv_write.writerows(all_data)


get_picle(os.path.join(os.getcwd()))