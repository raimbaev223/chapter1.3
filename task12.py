def factorial(num):
    if num == 0 or num == 1:
        return 1
    return factorial(num - 1) * num
print(1 * 2 * 3 * 4 )
print(factorial(4))