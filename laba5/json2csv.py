#В командной строке написать: python json2csv.py example.json

import json
import os
import sys
import csv

# Чтение файла JSON
with open('example.json', 'r') as file:
    json_data = json.load(file)
#print(json_data['article'])

json_file = sys.argv[1]
root_name = os.path.splitext(os.path.basename(json_file))[0]
csv_file = f'{root_name}.csv'


# Запись данных в CSV
with open(csv_file, 'w+', newline='') as file:
    fieldnames = ['edition', 'id', 'author', 'language']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(json_data['article'])
