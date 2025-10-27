__all__ = ["print_health_bar", "custom_output"]

import time


def custom_output(msg):
    for ch in msg:
        print(ch, end="", flush=True)
        time.sleep(0.05)
    print(flush=True)


def print_health_bar(
        name: str,
        current_health: int,
        max_health: int,
        shield: int = 0,
        total_width: int = 30,
        use_colors: bool = True,
) -> None:
    """
    Печатает красивый прогресс-бар здоровья и щита для персонажа.
    """
    # Защита от деления на ноль и некорректных значений
    current_health = max(0, min(current_health, max_health))
    shield = max(0, shield)

    # Рассчитываем доли
    health_ratio = current_health / max_health if max_health > 0 else 0
    health_width = int(total_width * health_ratio)
    shield_width = min(shield, total_width - health_width)

    # Цвета
    GREEN = "\033[92m" if use_colors else ""
    BLUE = "\033[94m" if use_colors else ""
    RESET = "\033[0m" if use_colors else ""

    # Собираем полосу
    bar = ""
    # Здоровье
    bar += GREEN + "█" * health_width + RESET
    # Щит
    bar += BLUE + "█" * shield_width + RESET
    # Пустота
    empty_width = total_width - health_width - shield_width
    bar += "░" * empty_width

    # Форматируем текст
    health_text = f"{current_health}/{max_health}"
    shield_text = f" (🛡️ {shield})" if shield > 0 else ""

    print(f"'{name}': ❤️ [{bar}] {health_text}{shield_text}")
