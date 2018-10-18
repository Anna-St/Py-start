# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.

import random
 
max_n = 2500

spisok = [random.randint(0,9) for _ in range(max_n)]
spisok = ''.join(list(map(lambda x: str(x), spisok)))
print(spisok)

path = 'D:\GeekBrains\Phyton\Start\Lesson4\\' + 'script' + '.txt'
with open(path, 'w', encoding='UTF-8') as file:
    file.write(str(spisok))




