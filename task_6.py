# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
# программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.


import chardet


file_name = 'test_file.txt'


# f = open(file_name, '+w')
# f.write('сетевое программирование\n')
# f.write('сокет\n')
# f.write('декоратор\n')
# f.close()


f = open(file_name, 'rb')
content = f.read()
print(chardet.detect(content))
content_en = content.decode('windows-1251').encode('utf-8')
print(chardet.detect(content_en))

