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
    np.random.seed(99) # фиксирует сид чисел 
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
    """Функция (игра) "угадай число" где сам компьютер загадывает случайное число и сам отгадывает его за минимальное 
    количество попыток по написанному алгоритму

    Args:
        number (int, optional): заданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    # Вначале компьютер будет загадывать сразу срединное число 50
    predict_number = 50
    while True:
        # Количество попыток
        count+=1
        # Условие выхода из цикла, когда число угадано
        if predict_number == number: break
        
        # Примерная иллюстрация нашего отрезка от 1 до 100
        # левая сторона [1] --- (25) --- (50) --- (75) --- [100] правая сторона
        # Если загаданное число (number) больше чем 50 (середина) идем вправо
        elif number > predict_number:
            if predict_number == 50:
                # Ставим ставим середину между 50 --- (75) --- 100
                predict_number = 75
            else:
                # Отсчитываем от 75 к 100
                predict_number += 1
        # Если загаданное число (number) меньше чем 50 (середина) идем влево
        elif number < predict_number:
            if predict_number == 50:
                # Ставим ставим середину между 50 --- (25) --- 1
                predict_number = 25
            else:
                # Отсчитываем от 25 к 1
                predict_number -= 1

    return(count)

score_game(predict_number_game)