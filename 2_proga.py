# 2. Напишите программу, которая на вход принимает 
# 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# 1 вариант
# A = 5
# Array = []
# for i in range(A):
#     z = int(input("Введите число "))
#     Array.append(z)
    
# print(Array)

# num = 0
# for i in Array:
#     if Array[i] > num:
#         num = Array[i]
# print(num)
    
# 2 вариант
# from    random  import randint
# count=5
# nums = [randint(1, 20) for i in range(count)]
# print (nums)
# mymax = nums[0]
# mymin = nums[0]
# for i in range(count):
#     if nums[i] > mymax : myMax=nums[i]
#     if nums[i] < mymin : myMin=nums[i]
# print ('Max:', mymax, 'Min:', mymin)



