10

#  Первый способ
from __future__ import division
import math
x = input()  # длина ряда
def fib(n):
    SQRT5 = math.sqrt(5)
    PHI = (SQRT5 + 1) / 2
    return int(PHI ** n / SQRT5 + 0.5)
for i in range(1, int(x)):
    print(fib(i))


  # Второй способ
x = input()  # длина ряда
def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a
for i in range(1, int(x)):
    print(fib(i))

