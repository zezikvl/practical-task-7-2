from pprint import pprint

def custom_write(file_name, strings):
    strings_positions = {}
    num_line = 1
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        file.tell()
        file.write(f'{i}\n')
        strings_positions[(num_line, file.tell())] = i
        num_line += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)