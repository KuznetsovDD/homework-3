# Задача 18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:

# 5
# 1 2 3 4 5
# 6
# -> 5

col = int(input('Введите длинну массива: '))

array = list()
from random import randint 
for _ in range(col):
    array.append(randint(0, col))

print(array)

numb = int(input('Введите число которое необходимо найти: '))



s = min(array, key= lambda x: abs(x-numb) ) # переебирает весь массив и из 
# каждого элемента массива вычитает заданное число, сравнивает по модулю и показывает минимальное 

print(s)  

# from random import randint
# n = int(input('Введите количество элементов: '))
# lst = [randint(1, n) for i in range(n)]
# print(lst)

# input_set = set(lst)

# num = int(input('Введите искомое число: '))
# dif = 0
# if num > max(input_set):
#     print(max(input_set))
# elif num < min(input_set):
#     print(min(input_set))
# else:
#     while True: # Есть возможность запускать бесконечный цикл
#         if num - dif in input_set and num + dif in input_set and num - dif != num + dif: # Конструкция сравнивает значение выражения сo значениями во множестве 
#             print(num - dif, num + dif)
#             break
#         elif num - dif in input_set:
#             print(num - dif)
#             break
#         elif num + dif in input_set:
#             print(num + dif)
#             break
#         else:
#             dif += 1