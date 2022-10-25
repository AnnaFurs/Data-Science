"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0

    # Предполагаемое число predict_number = 50 в середине диапазона 1..100, 
    # вводим переменную shift для следующих смещений дипазона
    predict_number = shift = 50

    while True:
        # каждую итерацию уменьшаем смещение на 2
        shift = int(shift / 2)
        # если получили 0, возвращаем значение 1, чтобы не вызвать бесконкечный цикл 
        shift = 1 if shift == 0 else shift
        count += 1
        if number == predict_number:
            break
        # если число меньше предполагаемого, уменьшаем диапазон поиска
        # на величину shift, в случае если больше - увеличиваем
        predict_number = predict_number - shift if number < predict_number \
            else predict_number + shift
    return count


def score_game(func) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    