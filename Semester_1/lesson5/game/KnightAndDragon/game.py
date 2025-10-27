from .characters import CharacterFactory, Dragon, DragonManager

from .utils import custom_output, print_health_bar


def choose_character():
    print("[!] Выберите героя:")
    print("[1] Рыцарь")
    print("[2] Дровосек")
    print("[3] Маг")
    print("[4] Убийца")
    print("[5] Лучник")
    print("[6] Арбалетчик")
    print("[7] Копейщик")

    while (choice := input("[SELECT] Ваш выбор (1-7): ").strip()) not in [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
    ]:
        print("[!] Неверный выбор. Повторите ввод.")

    return choice


def start():
    choice = choose_character()
    factory = CharacterFactory(custom_print=custom_output)
    hero = factory.create_character(choice)

    # Создаём дракона
    dragon = Dragon(
        name="Пласидусакс",
        max_health=200,
        health=200,
        shield=20,
        claw_damage=18,
        tail_damage=22,
        fire_breath_damage=28,
        ability_chance=0.25,
    )
    dragon_manager = DragonManager(dragon, custom_print=custom_output)

    battle_loop(hero, dragon, dragon_manager)


def show_status(hero, dragon):
    """Показывает полосы здоровья и маны."""
    print("=" * 70)
    print_health_bar(str(hero), hero.health, hero.max_health, hero.shield)
    if hasattr(hero, "mana"):
        print(f"Мана: {hero.mana}")
    print_health_bar(str(dragon), dragon.health, dragon.max_health, dragon.shield)
    print("=" * 70)


def get_available_weapons(hero):
    """Возвращает список имён оружий героя."""
    return list(hero._weapons_manager._weapons.keys())


def player_turn(hero):
    """Ход игрока: выбор действия."""
    while True:
        print("[SELECT] Ваш ход! Выберите действие:")
        print("[1] Атаковать")
        print("[2] Сменить оружие")
        print("[3] Использовать способность")
        print("[4] Использовать зелье")

        choice = input("[SELECT] Ваш выбор (1-4): ").strip()
        print("=" * 70)

        if choice == "1":
            return "attack"

        elif choice == "2":
            weapons = get_available_weapons(hero)
            if len(weapons) <= 1:
                print("*У вас только одно оружие!*")
                continue
            print("Доступные оружия:")
            for i, w in enumerate(weapons, 1):
                print(f"{i}. {w}")
            try:
                w_choice = int(input("Выберите оружие: ")) - 1
                if 0 <= w_choice < len(weapons):
                    print("✍️Story tailing:")
                    hero.switch_weapon(weapons[w_choice])
                else:
                    print("*Неверный выбор.*")
            except ValueError:
                print("*Введите число.*")
            continue  # остаёмся в меню

        elif choice == "3":
            if hero.can_use_ability():
                return "ability"
            continue

        elif choice == "4":
            print("[🍼] Зелья:")
            print("[1] Лечебное зелье")
            if hasattr(hero, "mana"):
                print("[2] Зелье маны")
            potion_choice = input(
                "[SELECT] Выберите зелье (1"
                + (", 2" if hasattr(hero, "mana") else "")
                + "): "
            ).strip()
            print("=" * 70)
            if potion_choice == "1":
                print("✍️Story tailing:")
                hero.use_potion("Лечебное зелье")
                print("=" * 70)
            elif potion_choice == "2" and hasattr(hero, "mana"):
                print("✍️Story tailing:")
                hero.use_potion("Эликсир маны")
                print("=" * 70)
            else:
                print("*Неверный выбор.*")
            continue  # остаёмся в меню

        else:
            print("*Введите 1, 2, 3 или 4.*")


def ending_heroic_victory(hero, dragon):
    custom_output(f"\n🌟{str(hero)} стоит над поверженным {str(dragon)}!")
    custom_output("Его клинок не дрогнул, а сердце — не сжалось.")
    custom_output("Деревня спасена. Песни о подвиге будут петься веками!")
    custom_output("\n🎖️КОНЕЦ: НЕПОБЕДИМЫЙ ГЕРОЙ")


def ending_pyrhic_victory(hero, dragon):
    custom_output(f"\n🩸{str(hero)} падает на колени рядом с телом {str(dragon)}!")
    custom_output("Рана на боку кровоточит, доспехи в пыли и крови...")
    custom_output("Деревня спасена... но сможет ли герой дойти домой?")
    custom_output("\n⚰️КОНЕЦ: ПОБЕДА ЦЕНОЙ ЖИЗНИ")


def ending_tragic_defeat(hero, dragon):
    custom_output(f"\n🔥{str(dragon)} взмахивает крыльями над бездыханным телом {str(hero)}.")
    custom_output("Пламя пожирает последние следы боя.")
    custom_output("Деревня обречена... Никто не осмелится бросить вызов дракону снова.")
    custom_output("\n🌑КОНЕЦ: ПЛАМЯ ПОБЕДИЛО")





def battle_loop(hero, dragon, enemy_manager):
    """Основной цикл боя."""
    print("⚔️ Бой начался!\n")
    while hero.is_alive() and dragon.is_alive():
        show_status(hero, dragon)

        # Ход игрока
        action = player_turn(hero)
        print("✍️Story tailing:")
        if action == "attack":
            hero.attack(dragon)
        elif action == "ability":
            hero.use_ability(dragon)

        # Обработка эффектов после хода игрока
        hero.process_effect()
        dragon.process_effect(hero)

        if not dragon.is_alive():
            if hero.health <= 50:
                ending_pyrhic_victory(hero, dragon)
            else:
                ending_heroic_victory(hero, dragon)
            break

        # Ход дракона
        enemy_manager.next_turn(hero)

        # Обработка эффектов после хода дракона
        hero.process_effect()
        dragon.process_effect()

        if not hero.is_alive():
            ending_tragic_defeat(hero, dragon)
            break

    print("\n🔚Бой завершён.")
