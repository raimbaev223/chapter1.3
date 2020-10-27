user = int(input('Введите число: '))
user2 = int(input('Введите еще число: '))

for i in range(user, user2):
    if i**2 < user2:
        print(i**2)
