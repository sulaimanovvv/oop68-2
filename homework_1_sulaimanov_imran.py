class Hero:
    def __init__(self, name: str, lvl: int, hp: int, strenght: int):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.strenght = strenght

    def get_status(self):
        print(
            f"Характеристики героя: {self.name}\nУровень - {self.lvl}\nЗдоровье - {self.hp}\nСила - {self.strenght}"
        )

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.lvl}")

    def attack(self):
        print(f"{self.name} наносит удар!\nсила упала на 1 единицу!")
        self.strenght -= 1

    def rest(self):
        print(f"{self.name} отдыхает..\nЗдоровье восстановилось на 1 единицу")
        self.hp += 1


kirito = Hero("Kirito", 89, 1200, 230)
asuna = Hero("Asuna", 94, 1350, 290)

kirito.get_status()
kirito.greet()
kirito.attack()
kirito.rest()
kirito.get_status()

asuna.get_status()
asuna.greet()
asuna.attack()
asuna.rest()
asuna.get_status()
