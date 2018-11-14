# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    tic_list=str(ticket_number)
    if len(tic_list) != 6: return False
    first = 0
    last = 0
    for i in range(3):
        first += int(tic_list[i])
        last += int(tic_list[-i-1])
    return first == last


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))




