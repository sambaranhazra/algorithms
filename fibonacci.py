def fib(n):
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
        i = i + 1
    return a


if __name__ == '__main__':
    number = int(input('Enter the number: '))
    print(fib(number))
