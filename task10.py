a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))

for i in range(a, b+1, c):
    print(i, end=' ')
print()