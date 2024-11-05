def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(len(strings)):
        position = file.tell()
        file.write(strings[i] + '\n')
        strings_positions[(i + 1, position)] = strings[i]
    return strings_positions
    file.close()


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
