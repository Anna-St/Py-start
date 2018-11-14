# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

import re

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

#с помощью re
line_2_str = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2)
print(line_2_str)


#без re
sym_1 = list(map(lambda x: chr(x), list(range(65, 91))))
sym_2 = list(map(lambda x: chr(x), list(range(97, 123))))
line_new = list(line_2)
 
lst = []
i = len(line_new) - 1
#Поиск символа в верхнем регистре после которого стоят еще два символа в верхнем регистре
while i >= 0:
    if line_new[i] in sym_2:
         lst.append(line_new[i])
    elif line_new[i] in sym_1 and i <= len(line_new) - 3 and line_new[i+1] in sym_1 and line_new[i+2] in sym_1:
        lst.append(line_new[i])
    else:
        lst.append(' ')
    i -= 1
lst.reverse() 
 
i = 0
lst_2 = []
registr = True

while i <= len(lst)-1:
    if lst[i] in sym_2:
        registr = True
    if lst[i] in sym_1 and lst[i-1] in sym_2 and lst[i-2] in sym_2:
        lst_2.append(lst[i])
        registr = False
    elif lst[i] in sym_1 and registr == False:
        lst_2.append(lst[i])
    else:
        lst_2.append(' ')
    i += 1
st=''.join(lst_2).split(' ') 
 
line_str_3 = [i for i in st if i != '']
print(line_str_3)
