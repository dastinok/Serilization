'''Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.'''
import csv

import random

def user_input():
    user_list = []
    while True:
        name = input('Name: ')
        if not name:
            return user_list
        while True:
            user_id = random.randint(10_000, 100_000)
            if user_id not in [uid[2] for uid in user_list]:
                break
        while True:
            id = input('Id: ')
            if id.isdigit() and 0 < int(id) < 8:
                user_list.append((name, id, user_id))
                break

def csv_write():
    user_list = user_input()
    result_dict = []
    for user in user_list:
        if user[1] in result_dict:
            result_dict[user[1]].update({user[2]:user[0]})
        else:
            result_dict[user[1]] = {user[2]:user[0]}
    with open('result.csv', 'w', encoding='utf-8') as f:
        csv_write = csv.DictWriter(f, dialect='excel', quoting=csv.QUOTE_ALL)
        csv_write.writerow('name', 'id', 'acces_level')

        for user in user_list:
            csv_write.writerow(user)
            #csv_write.writerow(user[1])
            #csv_write.writerow(user[2])


csv_write()