from homework_1_sulaimanov_imran import Hero
from random import choice


class Warrior(Hero):

    def __init__(self, name, lvl, hp, strenght, stamina):
        super().__init__(name, lvl, hp, strenght)
        self.stamina = stamina

    def attack(self):
        print(f"Воин - {self.name} атакует мечом!\nсила упала на 1 единицу!")
        self.strenght -= 1


class Mage(Hero):

    def __init__(self, name, lvl, hp, strenght, mana):
        super().__init__(name, lvl, hp, strenght)
        self.mana = mana

    def attack(self):
        print(f"Маг - {self.name} кастует заклинание!\nсила упала на 1 единицу!")
        self.strenght -= 1


class Assassin(Hero):

    def __init__(self, name, lvl, hp, strenght, stealth):
        super().__init__(name, lvl, hp, strenght)
        self.stealth = stealth

    def attack(self):
        print(f"Ассасин - {self.name} атакует из-под тишка!\nсила упала на 1 единицу!")
        self.strenght -= 1


warior = Warrior("Galahad", 150, 1800, 400, 560)
mage = Mage("Merlin", 180, 1200, 200, 800)
assassin = Assassin("Ecio", 150, 1600, 300, 620)

rules = {"warrior": "assassin", "assassin": "mage", "mage": "warrior"}

menu = {"1": "warrior", "2": "assassin", "3": "mage", "0": "Выход"}

print("=== Игра ===")
print(f'"1": "warrior","2": "assassin","3": "mage","0": "Выход"')
while True:
    user_input = input("Выберите героя: ")

    if user_input == "0":
        print(f"\nВыход из игры...")
        break

    if user_input not in menu:
        print("Неверный ввод: Выберите 1,2,3 или 0.")
        continue

    comp_choice = choice(list(rules.keys()))
    user_choice = menu[user_input]

    print(f"Вы выбрали:{user_choice}\nПротивник:{comp_choice}")

    if user_choice == comp_choice:
        print("Ничья")
    elif rules[user_choice] == comp_choice:
        print(f"{user_choice} победил")
    else:
        print(f"{comp_choice} победил")
