import io
from pprint import pprint

def custom_write(file_name, strings):
    file = open(file_name, "a", encoding= "utf-8")
    string_positions = {}
    nos_ = 0
    for i in strings:
        ns_ = file.tell()
        file.write(f"{i}\n")
        nos_ += 1
        string_positions[(nos_, ns_)] = i
    file.close()
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
