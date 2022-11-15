# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя,
# объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса.

user_data = ['Марка автомобиля: ', 'Год выпуска: ', 'Объем двигателя: ',
                 'Цвет кузова: ', 'Цена в рублях: ']
print('Вас приветствует конфигуратор автомобиля')
def my_new_car():
    new_car = []
    for i in range(5):
        my_set = input(user_data[i])
        if type(user_data[i]) == int:
            new_car.append(int(my_set))
        elif type(user_data[i]) == float:
            new_car.append(float(my_set))
        else:
            new_car.append(my_set)
    return new_car

x = my_new_car()

class Car:
    def __init__(self, full):
        self.__name = full[0]
        self.__year = full[1]
        self.__motor = full[2]
        self.__color = full[3]
        self.__price = full[4]

    def get_prise(self):
        return self.__price

    def set_prise(self, new_price):
        if type(new_price) in (float, int):
            self.__price = new_price

    def get_year(self):
        return self.__year

    def set_year(self, new_year):
        if type(new_year) in (float, int):
            self.__year = new_year

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if type(new_name) == str:
            self.__name = new_name

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        if type(new_color) == str:
            self.__color = new_color

    def get_motor(self):
        return self.__motor

    def set_motor(self, new_motor):
        if type(new_motor) in (float, int):
            self.__motor = new_motor

    def __str__(self):
        result = '''Ваш автомобиль: %(n)s
Год выпуска: %(y)s
Объем двигателя: %(m)sл.
Цвет кузова: %(c)s
Цена автомобиля: %(p)s рублей ''' % {
            'n': self.__name,
            'y': self.__year,
            'm': self.__motor,
            'c': self.__color,
            'p': self.__price}
        return result

def change_configuration():
    my_car = Car(x)
    print((my_car))
    user_says = input('Хотите что-нибудь изменить в автомобиле? ').lower()
    while user_says == 'да':
        print('''Что вы хотите изменить?
1 - Марка автомобиля
2 - Год выпуска
3 - Объем двигателя
4 - Цвет кузова
5 - Цену автомобиля''')
        user_say = int(input())
        if user_say == 1:
            car_name = input('Введите новую марку: ')
            my_car.set_name(car_name)

        elif user_say == 2:
            car_name = int(input('Введите новый год выпуска: '))
            my_car.set_year(car_name)

        elif user_say == 3:
            car_name = float(input('Введите новый объем двигателя: '))
            my_car.set_motor(car_name)

        elif user_say == 4:
            car_name = input('Введите новый цвет: ')
            my_car.set_color(car_name)

        elif user_say == 5:
            car_name = int(input('Введите новую цену: '))
            my_car.set_prise(car_name)

        user_says = input('Хотите еще что-нибудь изменить в автомобиле? ').lower()
    return my_car



print(change_configuration())