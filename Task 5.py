# k - клад
# n - изначальное кол-во монет
# k = (5/6)^6 * n - sum( (5/6)^i, i=1..6)
# a = (5/6)^6 = 15625/46656
# b = sum( (5/6)^i, i=1..6) = 155155/46656
# n = (k + b)/a: k, n: целые

import math


k = 1
a = 15625/46656
b = 155155/46656
n = (k+b)/a
print('start: {} {}'.format(k, n))

while math.modf(n)[0] != 0.0:  # пока n - не целое
    k += 1
    n = (k+b)/a
    print('{} {}'.format(k, n))

print('Найденное число: {}'.format(n))
print('Проверка:-------------')

for i in range(6):
    print('остаток:{}'.format(n % 6))
    n -= 1
    n -= n//6
    print(n)

print('Ответ: {}'.format(k))
