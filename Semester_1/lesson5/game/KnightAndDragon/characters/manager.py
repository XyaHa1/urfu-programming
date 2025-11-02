from .heroes.heroes import Knight, Lumberjack, Wizard, Assassin, Archer, Spearman
from ..consumables import AbilityManager, PotionManager
from ..consumables.abilities import (
    Shielding,
    StrikeEnhancement,
    Burning,
    Bleeding,
    HeavyBolt,
    SpearThrow,
    ArrowStorm,
)
from ..consumables.messages.messages_abilities import (
    NARRATOR_SHIELD_PHRASES,
    NARRATOR_HEAVY_BOLT_PHRASES,
    NARRATOR_BLEED_PHRASES,
    NARRATOR_FIREBALL_PHRASES,
    NARRATOR_SPEAR_THROW_PHRASES,
    NARRATOR_ARROW_STORM_PHRASES,
    NARRATOR_EMPOWERED_STRIKE_PHRASES,
)
from ..consumables.potions import HealingPotion, ManaPotion
from ..weapons import (
    Sword,
    Axe,
    MeleeStaff,
    Knife,
    Bow,
    RangedStaff,
    Crossbow,
    Spear,
    WeaponManager,
)


class CharacterFactory:
    def __init__(self, custom_print):
        self._custom_print = custom_print

    def create_character(self, choice: str):

        if choice == "1":  # Рыцарь
            weapons = {"Меч": Sword("Меч", damage=20, crit_chance=0.3)}
            weapon_manager = WeaponManager(
                name_user="Рыцарь", weapons=weapons, custom_print=self._custom_print
            )
            ability = AbilityManager(
                Shielding("Щит", max_cost=3, cost=3),
                NARRATOR_SHIELD_PHRASES,
                custom_print=self._custom_print,
            )
            potions = {
                "Лечебное зелье": HealingPotion(
                    "Лечебное зелье", max_count=3, healing_amount=25
                )
            }
            potion_manager = PotionManager(
                "Рыцарь", potions, custom_print=self._custom_print
            )

            return Knight(
                "Рыцарь", 120, 120, 40, weapon_manager, ability, potion_manager
            )

        elif choice == "2":  # Дровосек
            weapons = {"Топор": Axe("Топор", damage=26, crit_chance=0.35)}
            weapon_manager = WeaponManager(
                name_user="Дровосек", weapons=weapons, custom_print=self._custom_print
            )
            ability = AbilityManager(
                StrikeEnhancement("Усиленный удар", max_cost=2, cost=2, damage=15),
                NARRATOR_EMPOWERED_STRIKE_PHRASES,
                custom_print=self._custom_print,
            )
            potions = {
                "Лечебное зелье": HealingPotion(
                    "Лечебное зелье", max_count=3, healing_amount=20
                )
            }
            potion_manager = PotionManager(
                "Дровосек", potions, custom_print=self._custom_print
            )

            return Lumberjack(
                "Дровосек",
                110,
                135,
                30,
                weapon_manager,
                ability,
                potion_manager,
            )

        elif choice == "3":  # Маг
            weapons = {
                "Посох": RangedStaff("Посох", damage=17, crit_chance=0.2),
                "Посох(вблизи)": MeleeStaff(
                    "Посох(вблизи)", damage=14, crit_chance=0.2
                ),
            }
            weapon_manager = WeaponManager(
                name_user="Колдун", weapons=weapons, custom_print=self._custom_print
            )
            ability = AbilityManager(
                Burning("Огненный шар", max_cost=3, cost=3, damage=30),
                NARRATOR_FIREBALL_PHRASES,
                custom_print=self._custom_print,
            )
            potions = {
                "Лечебное зелье": HealingPotion(
                    "Лечебное зелье", max_count=2, healing_amount=20
                ),
                "Эликсир маны": ManaPotion("Эликсир маны", max_count=3, mana_amount=20),
            }
            potion_manager = PotionManager(
                "Колдун", potions, custom_print=self._custom_print
            )

            wizard = Wizard(
                "Колдун",
                90,
                110,
                50,
                20,
                weapon_manager,
                ability,
                potion_manager,
            )
            return wizard

        elif choice == "4":  # Ассасин
            weapons = {"Нож": Knife("Нож", damage=22, crit_chance=0.55)}
            weapon_manager = WeaponManager(
                name_user="Убийца", weapons=weapons, custom_print=self._custom_print
            )
            ability = AbilityManager(
                Bleeding("Кровотечение", max_cost=2, cost=2, damage=10),
                NARRATOR_BLEED_PHRASES,
                custom_print=self._custom_print,
            )
            potions = {
                "Лечебное зелье": HealingPotion(
                    "Лечебное зелье", max_count=3, healing_amount=15
                )
            }
            potion_manager = PotionManager(
                "Убийца", potions, custom_print=self._custom_print
            )

            return Assassin(
                "Убийца",
                100,
                130,
                20,
                weapon_manager,
                ability,
                potion_manager,
            )

        elif choice == "5":  # Лучник
            weapons = {
                "Лук": Bow("Лук", damage=18, crit_chance=0.3),
                "Кинжал": Knife("Кинжал", damage=16, crit_chance=0.4),
            }
            weapon_manager = WeaponManager(
                name_user="Лучник", weapons=weapons, custom_print=self._custom_print
            )
            ability = AbilityManager(
                ArrowStorm("Град стрел", max_cost=2, cost=2, damage=20),
                NARRATOR_ARROW_STORM_PHRASES,
                custom_print=self._custom_print,
            )
            potions = {
                "Лечебное зелье": HealingPotion(
                    "Лечебное зелье", max_count=3, healing_amount=20
                )
            }
            potion_manager = PotionManager(
                "Лучник", potions, custom_print=self._custom_print
            )

            return Archer(
                "Лучник",
                100,
                130,
                20,
                weapon_manager,
                ability,
                potion_manager,
            )

        elif choice == "6":  # Арбалетчик
            weapons = {
                "Арбалет": Crossbow("Арбалет", damage=24, crit_chance=0.25),
                "Кинжал": Knife("Кинжал", damage=16, crit_chance=0.4),
            }
            weapon_manager = WeaponManager(
                name_user="Арбалетчик", weapons=weapons, custom_print=self._custom_print
            )
            # Для простоты — одна способность (можно расширить)
            ability = AbilityManager(
                HeavyBolt("Тяжелый болт", max_cost=2, cost=2, damage=20),
                NARRATOR_HEAVY_BOLT_PHRASES,
                custom_print=self._custom_print,
            )
            potions = {
                "Лечебное зелье": HealingPotion(
                    "Лечебное зелье", max_count=3, healing_amount=20
                )
            }
            potion_manager = PotionManager(
                "Арбалетчик", potions, custom_print=self._custom_print
            )

            return Archer(
                "Арбалетчик",
                100,
                100,
                20,
                weapon_manager,
                ability,
                potion_manager,
            )

        elif choice == "7":  # Копейщик
            weapons = {"Копьё": Spear("Копьё", damage=22, crit_chance=0.3)}
            weapon_manager = WeaponManager(
                name_user="Копейщик", weapons=weapons, custom_print=self._custom_print
            )
            ability = AbilityManager(
                SpearThrow("Метательное копьё", max_cost=2, cost=2, damage=30),
                NARRATOR_SPEAR_THROW_PHRASES,
                custom_print=self._custom_print,
            )
            potions = {
                "Лечебное зелье": HealingPotion(
                    "Лечебное зелье", max_count=3, healing_amount=20
                )
            }
            potion_manager = PotionManager(
                "Копейщик", potions, custom_print=self._custom_print
            )

            return Spearman(
                "Копейщик",
                110,
                110,
                25,
                weapon_manager,
                ability,
                potion_manager,
            )

        else:
            raise ValueError("Неверный выбор персонажа")
