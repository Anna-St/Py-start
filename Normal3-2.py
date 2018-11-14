# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    def min_num(ls): #функция определения наименьшего элемента в списке
        min_el = float('inf')
        for el in ls:
            if el < min_el:
                min_el = el
        return min_el
    med_list = [x for x in origin_list] #промежуточный (рабочий) список
    sorted_list = []
    while len(med_list):
        for el in med_list:
            if el == min_num(med_list):
                sorted_list.append(el)
                med_list.remove(el)
    print('Список %s преобразован:\n%s' % (origin_list, sorted_list))
    return sorted_list


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
