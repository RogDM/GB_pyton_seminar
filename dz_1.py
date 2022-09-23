# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# Решение:

# day = int(input("Введите день недели: "))
# while day not in range(1,8):
#     day = int(input("Введите корректный день: "))
# if  0 < day < 6:
#     print("нет")
# elif 6 <= day <= 7:
#     print("да")


# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ = not ⋁ = or ⋀ = and

# Решение:

# print("Для проверки утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z \nВведите Х ", end=" ")
# х = int(input(""))
# y = int(input("Введите y: "))
# z = int(input("Введите z: "))
# print(not(х or y or Z) == (not х and not y and not z))


# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# Решение:


# coordinate_x = int(input("Введите координату x: "))
# coordinate_y = int(input("Введите координату y: "))

# if coordinate_x == 0 or coordinate_y == 0:
#     print("Не корректный ввод")
#     if coordinate_x == 0:
#         while coordinate_x == 0:
#             coordinate_x = int(input("Введите корректную координату x (не 0): "))
#     if coordinate_y == 0:
#         while coordinate_y == 0:
#             coordinate_y = int(input("Введите корректную координату y (не 0): "))

# if coordinate_x > 0 and coordinate_y > 0:
#     print("x =", coordinate_x, "y =", coordinate_y, "-> 1")

# elif coordinate_x < 0 and coordinate_y > 0:
#     print("x =", coordinate_x, "y =", coordinate_y,  "-> 2")

# elif coordinate_x < 0 and coordinate_y < 0:
#     print("x =", coordinate_x, "y =", coordinate_y,  "-> 3")

# elif coordinate_x > 0 and coordinate_y < 0:
#     print("x =", coordinate_x, "y =", coordinate_y,  "-> 4")

# переделанный elif (вставил elif вместо else во имя паранои - "вдург через цикл какая-то фигня пройдёт?")
# ну и такое вариант мне кажется более громоздким.
# elif coordinate_x > 0:
#     if coordinate_y > 0:
#         print("x =", coordinate_x, "y =", coordinate_y, "-> 1")
#     elif coordinate_y < 0:
#         print("x =", coordinate_x, "y =", coordinate_y,  "-> 4")

# elif coordinate_x < 0:
#     if coordinate_y > 0:
#         print("x =", coordinate_x, "y =", coordinate_y,  "-> 2")
#     elif coordinate_y < 0:
#         print("x =", coordinate_x, "y =", coordinate_y,  "-> 3")




# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# Решение:
# quarter = int(input("Введите номер четверти: "))

# while quarter not in range(1,5):
#     print("Не верный ввод")
#     quarter = int(input("Введите корректный номер четверти (1-4): "))

# if quarter == 1:
#     print("x > 0; y > 0")

# elif  quarter == 2:
#     print("x < 0; y > 0")

# elif quarter == 3:
#     print("x < 0; y < 0")

# elif quarter == 4:
#     print("x > 0; y < 0")



# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# Решение:

# x1 = int(input("Введите x1: "))
# x2 = int(input("Введите x2: "))
# y1 = int(input("Введите y1: "))
# y2 = int(input("Введите y2: "))

# rezult = round(((y1 - x1) ** 2 + (y2 - x2) ** 2) ** 0.5, 2)

# print(f"A ({x1},{y1}); B ({x2},{y2}) -> {rezult}")

