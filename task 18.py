# Задача 18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:

# 5
# 1 2 3 4 5
# 6
# -> 5

# col = int(input('Введите длинну массива: '))

# array = list()
# from random import randint 
# for _ in range(col):
#     array.append(randint(0, col))

# print(array)

# numb = int(input('Введите число которое необходимо найти: '))

# ar= sorted(array)
# print(ar)
# a=list()
# for i in range(len(ar)):
#     res = ar[i]-numb
#     a.append(res)
# sorted(a)
# print(a)
    
l = [5, 78, 45, 12, 56, 9999]

def nearest(lst, target):
  return min(lst, key=lambda x: abs(x-target))

print(nearest(l, 2))