import numpy as np


def random_predict(number: int = 1) -> int:
    
    count = 0
    min1 = 1
    max1 = 101
    predict_current = np.random.randint(1, 101)
    while True:
        count += 1

        if predict_current == number: break 
        elif predict_current > number:  
            max1 = predict_current  
            predict_current -= int((max1 - min1) // 2)
        else:
            min1 = predict_current
            predict_current += int((max1 - min1) // 2)
    return count


def score_game(random_predict, size=20) -> int:
    count_ls = []
    random_array = np.random.randint(1, 101, size) 
    for number in random_array:
        count_ls.append(random_predict(number))
 

    print(f'Ваш  {max(count_ls)}') 
  
    
    
if __name__ == "__main__":
    # RUN
    score_game(random_predict)