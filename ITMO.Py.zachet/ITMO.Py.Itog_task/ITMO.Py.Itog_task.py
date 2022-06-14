#Алгоритм 8. Вычисление минимакса для последовательности хранящейся в массиве
import random
M = random.sample([i for i in range(10)],10)
Max = M[1]
Min = M[1]
i = 2
n = 1
for i in range(1, 1+n):
    if M[i] > Max:
        Max = M[i]; IndMax = i
        if M[i] < Min:
            Min = M[i]; IndMin = i
            i = i+1