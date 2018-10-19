# 3. Определить, какие из слов «attribute», «класс», «функция»,
# «type» невозможно записать в байтовом типе.


bytes_s_1 = b'attribute'
bytes_s_2 = 'класс'
bytes_s_3 = 'функция'
bytes_s_4 = b'type'
bytes_s_2_en = bytes_s_2.encode('ascii', 'replace')
bytes_s_3_en = bytes_s_3.encode('ascii', 'replace')


print(bytes_s_1)
print(bytes_s_2_en)
print(bytes_s_3_en)
print(bytes_s_4)
