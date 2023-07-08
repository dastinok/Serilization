'''Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.'''
import json

with open('seminar_3.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

res_dict = {}
for line in lines:
    line = line.strip().split()
    res_dict[line[0].title()] = line[1]

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(res_dict, f, indent=4, ensure_ascii=False)
