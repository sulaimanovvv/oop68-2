import time
import colorama

# Эта библиотека нужна для окрашивания текста в консоли.
# Она используется для визуального выделения важных сообщений, ошибок или успехов при выводе данных.


def speed_test(func):

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        total_time = end - start

        if total_time < 0.05:
            color = colorama.Fore.GREEN
        else:
            color = colorama.Fore.YELLOW

        print(
            f"Задача [{func.__name__}] выполнена за: {color}{total_time:.4f} сек{colorama.Style.RESET_ALL}"
        )
        return result

    return wrapper


@speed_test
def create_huge_list(size):
    return [x**2 for x in range(size)]


print(
    colorama.Fore.CYAN
    + "=== ДОБРО ПОЖАЛОВАТЬ В ТЕСТ СКОРОСТИ ПРОЦЕССОРА ==="
    + colorama.Style.RESET_ALL
)
print("Сейчас мы нагрузим ваше устройство математическими вычислениями...\n")

print("Этап 1: Обработка 50 000 чисел")
create_huge_list(50000)

print("\nЭтап 2: Обработка 500 000 чисел")
create_huge_list(500000)

print("\nЭтап 3: Обработка 5 000 000 чисел")
create_huge_list(5000000)

print(
    colorama.Fore.MAGENTA
    + "\nТестирование успешно завершено!"
    + colorama.Style.RESET_ALL
)
