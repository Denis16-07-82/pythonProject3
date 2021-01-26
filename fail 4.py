if __name__ == '__main__':
    def my_func(name, last_name, year, city, email, phone):
        print('Имя: ' + name + ', Фамилия: ' + last_name +
              ', Год рождения: ' + year + ', Город проживания: ' + city + ', email: ' +
              email + ', Номер телефона: ' + phone)


    name=input('Ваше имя: ')
    last_name=input('Ваша фамилия: ')
    year=input('Год рождения: ')
    city=input('Город проживания: ')
    email=input('email: ')
    phone=input('телефон: ')
    my_func(name,last_name,year,city,email,phone)