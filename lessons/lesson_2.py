class User:

    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

    def user_login(self, password):
        if password == self.password:
            return "Ok"
        return "fail"


imran = User("imran", "sulaimanoff.imran@yandex.com", "qwerty123")
print(imran.user_login("qwerty123"))


class UserVIP(User):

    def __init__(self, name, login, password, last_name):
        super().__init__(name, login, password)
        self.last_name = last_name

    def vip_login(self, name):
        if name == self.name:
            return "ok"
        return "fail"

    def user_login(self, login):
        if login == self.login:
            return "выполнено"
        return "не выполнено"


john = UserVIP("john", "john_doe@gmail.com", "asdf123")


class Fly:
    def fly(self):
        print("fly")


class Swim:
    def swim(self):
        print("swim")


class Animal(Fly, Swim):
    pass


donald_duck = Animal()


class A:
    def action(self):
        print("A")


class B(A):
    def action(self):
        print("B")


class C(A):
    def action(self):
        print()
