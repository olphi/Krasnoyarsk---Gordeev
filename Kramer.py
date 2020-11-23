import copy
import numpy as np

def Kramer(a,b):
    res = []
    for i in range(len(A)):
        a = copy.deepcopy(A)
        for j in range(len(b)):
            a[i][j] = b[j]
        det = round(np.linalg.det(a))
        print('Определитель матрицы A' + str(i + 1) + ': ' + str(det))
        res.append(det / Det) 
    return res

A = []
n = int(input('Введите количество переменных:'))
print('Введите матрицу А:')
for i in range(n):
    A.append(list(map(int, input().split())))
print('Введите b:')
b = list(map(int, input().split()))
Det = round(np.linalg.det(A))
print('Определитель матрицы A:', Det)

ans = Kramer(A, b)
for i in range(1, len(ans) + 1):
    print('x' + str(i) + ' = ' + str(ans[i - 1]))
    
# Схема №3 - Гордеев, Пустовойтова, Анастасов
# А
# 0 1 -1 0 0 2
# -1 1 0 0 4 -4
# -1 0 0 5 -5 0
# 1 0 -1 5 0 -5
# 0 0 1 3 0 0
# 0 1 0 0 -4 0
# 
# b
# 0 0 0 -10 18 -16
