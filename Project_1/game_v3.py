"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number: int=np.random.randint(1, 101)) -> int:
    """Рандомно угадываем число
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    
    Returns:
        int: Число попыток
    """
    min = 1
    max = 100
    predict_number = int(np.random.randint(min, max + 1))  #  программа начинает отгадывать число
    count = 0  # подсчет количества попыток на отгадывание числа

    while predict_number != number:
        count += 1

        if predict_number > number:
            max = predict_number
            predict_number = (min + max) // 2

        elif predict_number < number:
            min = predict_number
            predict_number = (min + max) // 2

        else:
            break  # конец игры и выход из цикла
    
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов
    программа угадывает число 
    
    Args:
        random_predict ([type]): функция угадывания
    
    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    
    np.random.seed(np.random.randint(1, 10)) # не фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(100))  # загадали список рандомных чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f"Ваша программа угадывает число за: {score} попытки.")
    return score

score_game(random_predict)

if __name__ == "__main__":
    # RUN
    score_game(random_predict)