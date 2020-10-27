n = int(input('Введите число: '))
fib = fib2 = 1
if n < 2:
    quit()
    print(fib, end=' ')
    print(fib2, end=' ')
for i in range(2, n):
    fib, fib2 = fib2, fib + fib2
    print(fib2, end=' ')
print()