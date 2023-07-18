# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
n = int(input("Введите число: "))
numF = -1
fa = 0
fb = 1
if (n == fa):
    numF = 1
elif (n == fb):
    numF = 2
else:
    f = fb
    i = 2
    while f < n:
        i += 1
        f = fa + fb
        fa = fb
        fb = f
        print(f, " = Fibonacci(", i, ")")
    if f == n:
        numF = i
if numF > 0:
    print(n, " is Fib(", numF, ")")
else:
    print(numF)
    print(n, " is not Fib-num, but lays between ", fa, fb)
