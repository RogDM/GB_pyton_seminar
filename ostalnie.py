# **Задачи:**

# 1. Напишите программу, которая будет на вход принимать 
# число N и выводить числа от -N до N
#     *Примеры:* 
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# num = int(input("Введите число: "))

# for i in range(-num,num+1):
#     print(i)


# 2. Напишите программу, которая будет принимать на 
# вход дробь и показывать первую цифру дробной части числа.
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# num = input("Введите число: ")
# count = 0
# not_num = 0
# for i in num:
#     count += 1
#     if i == "," or i == ".":
#         not_num = 1
#         print(num[count])
# if not_num == 0:
#      print("Нет")


# 3. Напишите программу, которая принимает на вход число и п
# роверяет, кратно ли оно 5 и 10 или 15, но не 30.

# num = int(input("Введите число: "))

# if (num % 5 == 0 or num % 10 == 0 or num % 15 == 0) and  num % 30 != 0:
#     print(True)
# else:
#     print(False)
