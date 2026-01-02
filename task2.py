import turtle


def koch_segment(t: turtle.Turtle, order: int, size: float) -> None:
    """
    Рекурсивно малює один відрізок кривої Коха.
    """
    # Базовий випадок: просто малюємо пряму
    if order == 0:
        t.forward(size)
        return

    # Рекурсивний випадок: ділимо відрізок на 4 частини з поворотами
    koch_segment(t, order - 1, size / 3)
    t.left(60)
    koch_segment(t, order - 1, size / 3)
    t.right(120)
    koch_segment(t, order - 1, size / 3)
    t.left(60)
    koch_segment(t, order - 1, size / 3)


def draw_koch_snowflake(order: int, size: float = 300.0) -> None:
    """
    Малює сніжинку Коха: 3 сторони рівностороннього трикутника,
    на кожній стороні застосовуємо рекурсивну криву Коха.
    """
    screen = turtle.Screen()
    screen.title("Koch Snowflake (Recursion)")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # Розташовуємо "черепаху" так, щоб фігура була приблизно по центру
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Малюємо 3 сторони сніжинки
    for _ in range(3):
        koch_segment(t, order, size)
        t.right(120)

    screen.mainloop()


def get_int(prompt: str, min_value: int = 0, max_value: int = 8) -> int:
    """
    Зчитує ціле число з консолі та перевіряє діапазон.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value < min_value or value > max_value:
                print(f"Please enter an integer between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")


def get_float(prompt: str, min_value: float = 50.0, max_value: float = 800.0) -> float:
    """
    Зчитує число з плаваючою крапкою та перевіряє діапазон.
    """
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            value = float(raw)
            if value < min_value or value > max_value:
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    print("Koch Snowflake Generator (Recursion)")
    order = get_int("Enter recursion level (0-8): ", 0, 8)
    size = get_float("Enter size in pixels (50-800): ", 50.0, 800.0)
    draw_koch_snowflake(order, size)


if __name__ == "__main__":
    main()
