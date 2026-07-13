from abc import ABC, abstractmethod


class Hero(ABC):

    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def great(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        self.__health += 1
        print(f"{self.name} отдыхает")

    @abstractmethod
    def attack(self):
        print(f"Герой атакует")


class Warrior(Hero):
    def attack(self):
        print(f"Воин атакаует мечом")


class Mage(Hero):
    def attack(self):
        print(f"Маг использует магию")


class Assassin(Hero):
    def attack(self):
        print(f"Ассасин атакует из-под тишка")


galahad = Warrior("Galahad", 150, 1800, 400)
merlin = Mage("Merlin", 180, 1200, 200)
ecio = Assassin("Ecio", 150, 1600, 300)

galahad.great()
galahad.rest()
galahad.attack()

merlin.great()
merlin.rest()
merlin.attack()

ecio.great()
ecio.rest()
ecio.attack()
