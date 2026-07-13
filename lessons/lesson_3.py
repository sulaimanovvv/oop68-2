class BankAccount:

    def __init__(self, fio, balance, login, password):
        self.fio = fio
        self._balance = balance
        self.__password = password
        self.login = login

    def __get_balance(self, password):
        if password == self.__password:
            return self._balance
        return "Не верный пароль !!"

    def __get_random_pass(self):
        pass

    def reset_pass(self):
        return self.__get_random_pass()


ardager = BankAccount("Ardager Kartanbekov", 1000, "ardage_dev", "Def123")

# print(dir(ardager))
# # print(ardager._BankAccount__password)
# # print(ardager.login)
# print(ardager._BankAccount__get_balance("Def123"))
# print(ardager._balance)

from abc import ABC, abstractmethod


# Абстрактный класс
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "MAy may"

    def move(self):
        return "Step"


class Dog(Animal):
    def move(self):
        return "Step"

    def make_sound(self):
        return "Gaf Gaf"


# tuzik = Dog()
# garfild = Cat()
