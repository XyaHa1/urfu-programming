from .character import Character


class Dragon(Character):
    def __init__(self, name, health, damage, shild):
        super().__init__(name, health, damage, shild)

    def attack(self, enemy: Character):
        pass
