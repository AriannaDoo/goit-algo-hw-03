import sys
import shutil
from pathlib import Path


def copy_and_sort(src: Path, dest: Path) -> None:
    """
    Рекурсивно обходить директорію src,
    копіює файли у dest та сортує їх
    у піддиректорії за розширенням
    """
    try:
        for item in src.iterdir():
            if item.is_dir():
                # якщо елемент - директорія, викликаємо функцію рекурсивно
                copy_and_sort(item, dest)
            elif item.is_file():
                # отримуємо розширення файлу (без крапки)
                extension = item.suffix[1:] if item.suffix else "no_extension"

                # створюємо піддиректорію за розширенням
                target_dir = dest / extension
                target_dir.mkdir(parents=True, exist_ok=True)

                # копіюємо файл
                shutil.copy2(item, target_dir / item.name)

    except PermissionError:
        print(f"Немає доступу до: {src}")
    except FileNotFoundError:
        print(f"Шлях не знайдено: {src}")
    except Exception as e:
        print(f"Помилка при обробці {src}: {e}")


def main():
    # парсинг аргументів командного рядка
    if len(sys.argv) < 2:
        print("Використання: python task1.py <source_dir> [destination_dir]")
        return

    source_dir = Path(sys.argv[1])
    destination_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not source_dir.exists() or not source_dir.is_dir():
        print("Вихідна директорія не існує або це не директорія")
        return

    # створюємо директорію призначення
    destination_dir.mkdir(parents=True, exist_ok=True)

    # запускаємо рекурсивне копіювання
    copy_and_sort(source_dir, destination_dir)
    print("Копіювання та сортування завершено")


if __name__ == "__main__":
    main()
