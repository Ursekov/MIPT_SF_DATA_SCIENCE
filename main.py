import numpy as np

def score_game(random_predict) -> int:
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
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    low, high = 0, 100 # начальные значения поиска
    count = 0
    predict = (low + high) // 2 # предполагаемое число
    while True:
        count += 1
        if predict < number: # в случае, если предполагаемое число меньше загаданного, 
            low = predict + 1 # нижняя граница смещается, убрав половину чисел из диапазона 
        elif predict > number: # в случае, если предполагаемое число больше загаданного,
            high = predict # верхняя граница смещается, убрав половину чисел из диапазона 
        else:
            break
        predict = (low + high) // 2 # вычисляется новое предполагаемое число 

    return count

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
