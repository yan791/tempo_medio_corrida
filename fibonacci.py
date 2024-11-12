import os
os.system("cls")
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = int(input("digite o numero que deseja ver: "))
print(fibonacci(n))
