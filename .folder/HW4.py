# Задача 22.
# n1 = int(input('Введите количество элементов первого набора чисел: '))
# n2 = int(input('Введите количество элементов второго набора чисел: '))
# arr1 = []
# arr2 = []
# for i in range(n1):
#     arr1.append(int(input('Введите элемент первого массива: ')))
# for j in range(n2):
#     arr2.append(int(input('Введите элемент второго массива: ')))
# arr3 = []
# for i in arr1:
#     if i in arr2 and i not in arr3:
#             arr3.append(i)
# arr3.sort()
# print(arr3)

# Задача 24.
# import random
# kust = int(input("введите количество кустов: "))
# berryes = list(random.randint(0, 10) for i in range(kust))
# result = []
# i = 0
# sum = 0

# print(berryes)

# while (i < kust):
#     if (i == kust - 1):
#         sum = berryes[i] + berryes[i - 1] + berryes[0]
#     else:
#         sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
#         result.append(sum)
#         result.sort()
#     i += 1

# print(f"максимальное число ягод за одну итерацию {result[-1]}")