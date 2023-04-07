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
    min = 1
    max = 101
    predict_current = np.random.randint(1, 101)
    while True:
        count += 1

        if predict_current == number: break 
        elif predict_current > number:  
            max = predict_current  
            predict_current -= int((max - min) // 2)
        else:
            min = predict_current
            predict_current += int((max - min) // 2)
    return count

def score_game(random_predict, size=20) -> int:
    count_ls = []
    random_array = np.random.randint(1, 101, size) 
    for number in random_array:
        count_ls.append(random_predict(number))
 

    print(f'Ваша программа угадывает число за {max(count_ls)} попыток') 
  
        
if __name__ == "__main__":
    # RUN
    score_game(random_predict)