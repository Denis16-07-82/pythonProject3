if __name__ == '__main__':
    def division(a, b):
        if b == 0:
            try:
                n = 1 / b
            except ZeroDivisionError:
                return ('делить на ноль нельзя')
        else:
            n = a / b
            return (n)


    a = float(input('Введите делимое '))
    b = float(input(('Введите делитель ')))
    n = division(a, b)
    print(n)
