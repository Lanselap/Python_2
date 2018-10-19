# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
# из строкового представления в байтовое и выполнить обратное преобразование
# (используя методы encode и decode).


w1 = 'разработка'
w2 = 'администрирование'
w3 = 'protocol'
w4 = 'standard'


enc_w1 = w1.encode('utf-8')
enc_w2 = w2.encode('utf-8')
enc_w3 = w3.encode('utf-8')
enc_w4 = w4.encode('utf-8')


print(enc_w1)
print(enc_w2)
print(enc_w3)
print(enc_w4)


dec_enc_w1 = enc_w1.decode('utf-8')
dec_enc_w2 = enc_w2.decode('utf-8')
dec_enc_w3 = enc_w3.decode('utf-8')
dec_enc_w4 = enc_w4.decode('utf-8')


print(dec_enc_w1)
print(dec_enc_w2)
print(dec_enc_w3)
print(dec_enc_w4)
