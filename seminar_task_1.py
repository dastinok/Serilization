'''Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.'''
import json
import os
import pickle

exten = 'json'

def find_json(path):
    for file in (os.listdir()):
        if os.path.isfile(file):
            initial_name, initial_ext = os.path.join(file).split('.')
            if initial_ext == exten:
                with open(file, 'r', encoding='utf-8') as file:
                    new_dict = json.load(file)
                    initial_name = initial_name + '.pickle'
                    with open(initial_name, 'wb') as file:
                        pickle.dump(initial_name, file)


find_json(os.path.join(os.getcwd()))