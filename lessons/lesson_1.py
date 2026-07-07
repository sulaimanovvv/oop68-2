class Hero:
    # Конструктор класса
    def __init__(self, name, hp, lvl):
        # Атрибуты экземпляра класса
        self.hero_name = name
        self.hero_hp = hp
        self.hero_lvl = lvl

    # Метод класса
    def base_action(self):
        return f"this base action {self.hero_name}"


# Обьект(Экземпляр класса)
kirito = Hero("Кирито", 1000, 100)
asuna = Hero("Asuna", 1200, 110)
straiker = Hero("Straiker", 1500, 143)

print(kirito.hero_name)
print(asuna.hero_name)
print(kirito.base_action())
