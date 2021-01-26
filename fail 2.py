if __name__ == '__main__':
    def my_func(a, b, c):
        n = a + b + c
        p = min(a, b, c)
        n = n - p
        return (n)


    print('Введите 3 числа')
    a = float(input('Введите первое число '))
    b = float(input('Введите второе чило '))
    c = float(input('Введите третье число '))
n = my_func(a, b, c)
print(n)
