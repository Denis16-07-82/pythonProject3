if __name__ == '__main__':
    def my_fanc(my_str):
        my_str=my_str.rstrip('$')
        my_newstr = my_str.split()
        i = 0
        sum_newstr = 0
        while i < len(my_newstr):
            sum_newstr += float(my_newstr[i])
            i += 1
        return (sum_newstr)


    my_str = ''
    sum_newstr_1=0
    while my_str.count('$') == 0:
        my_str = input('Введите числа через пробел,для остановки программы введите символ $ и нажмите Enter: ')
        sum_newstr = my_fanc(my_str)
        sum_newstr_1+=sum_newstr
        print(sum_newstr_1)
    print('вы вышли из программы')
