import numpy as np
def score_game(predict_number_game) -> int:
    """Вывод среднего значения угаданного числа из списка на 1000 подходов

    Args:
        predict_number_game (_type_): функция по угадыванию чисел

    Returns:
        int: среднее значение угаданных попыток
    """
    # Количество попыток
    count_lst = []
    np.random.seed(3) # фиксирует сид чисел 
    random_arr = np.random.randint(1, 100, size=1000) # задаем список чисел
    
    for number in random_arr:
        count = predict_number_game(number)
        count_lst.append(count)
    
    # среднее значение
    score = int(np.mean(count_lst))
    print(f"Ваш алгоритм угадывает число в среднем: {score} попыток")
    return(score)

print('-' * 40)
def predict_number_game(number:int=1) -> int:
    """Функция (игра) "угадай число" где сам компьютер загадывает случайное число и сам отгадывает его за минимальное (V1 - почти бинарный поиск)
    количество попыток по написанному алгоритму

    Args:
        number (int, optional): заданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    # Вначале компьютер будет загадывать
    predict_number = 0
    min = 1
    max = 100
    
    while True:
        # Количество попыток
        count+=1
        # Угадываем число, задаем сначала отрезок от 1 до 100
        predict_number = np.random.randint(min, max)
        
        # Условие выхода из цикла, когда число угадано
        if predict_number == number: break
        # Если загаданное число (number) больше нашего числа, то начинаем считать от этого числа
        elif number > predict_number:
            min = predict_number
        # Если загаданное число (number) меньше нашего числа, то начинаем считать от этого числа
        elif number < predict_number:
            max = predict_number
            
    return(count)

score_game(predict_number_game)