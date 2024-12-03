# "Сложные моменты и исключения в стеке вызовов функции"
# "План перехват"

def personal_sum(numbers):                  # принимает коллекцию numbers
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number                # Подсчитываут сумму чисел в numbers путём перебора
        except TypeError:
            incorrect_data += 1             # считает ошибки в типе данных
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
    return (result, incorrect_data)         # выводит сумму и количество ошибок


# ищет среднее арифметическое корректных данных
def calculate_average(numbers):
    try:
        result = personal_sum(numbers)
        return result[0] / (len(numbers) - result[1])
    except ZeroDivisionError:
        return 0                            # если корректных данных на входе нет
    except TypeError:
        return print(f'В numbers записан некорректный тип данных {numbers}')


# Строка перебирается, но каждый символ - строковый тип
print(f'Результат 1: {calculate_average("1, 2, 3")}')
# Учитываются только 1 и 3
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
# Передана не коллекция
print(f'Результат 3: {calculate_average(567)}')
# Всё должно работать
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
