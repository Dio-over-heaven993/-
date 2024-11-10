#1
# from random import randint
# arr = list()
# for i in range(3):
#     brr = list()
#     for j in range(3):
#         brr.append(randint(-15, 15))
#     arr.append(brr)
# print(arr)
# print(max(arr[0][2], arr[1][2], arr[2][2]), max(arr[1]))
#2
from random import randint
n = int(input())
m = int(input())
arr = list()
for i in range(m):
    brr = list()
    for j in range(n):
        brr.append(randint(-15, 15))
    arr.append(brr)
print(arr)    
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] > 0: arr[i][j] = 1
        else: arr[i][j] = 0
print(arr)
#3
# array = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
# for i in array:
#   print(' '.join(list(map(str, i))))
# column = list()
# diag_1 = list()
# diag_2 = list()
# for i in range(0, len(array)):
#   flag_1 = 0
#   if sum(array[i]) == sum(array[0]):
#     flag_1 = 1
# for i in range(3):
#   for j in range(3):
#       if i == j:
#         print(j)
#         diag_1.append(array[i][j])
# if sum(diag_1) == sum(array[0]) == sum(diag_2):
#   flag_2 = 1
# print('Это магический квадрат!') if flag_1 and flag_2 and flag_3 else print('Это не магический квадрат!')
