'''Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.'''
import csv
import json


def csv_to_json(csv_file, json_file):
    result_dict = {}
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file, dialect='excel')
        for i, line in enumerate(csv_reader):
            if i != 0:
                name = line[0].title()
                uid = f'{line[2]:0>10}'
                lvl = line[2]
                key = hash(uid + name)
                result_dict[key] = (name, uid, lvl)
    with open(json_file, 'w', encoding='utf-8') as res_file:
        json.dump(result_dict, res_file, ensure_ascii=False, indent=4)

csv_to_json('csv_file.csv', 'new_json_file.json')