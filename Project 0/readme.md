# [Проект 0. Угадай число](https://github.com/Ursekov/MIPT_SF_DATA_SCIENCE/tree/main/Project%200)

## Оглавление  
[1. Описание проекта](https://github.com/Ursekov/MIPT_SF_DATA_SCIENCE/tree/main/Project%200#%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Какой кейс решаем?](https://github.com/Ursekov/MIPT_SF_DATA_SCIENCE/tree/main/Project%200#%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)  
[3. Краткая информация о данных](https://github.com/Ursekov/MIPT_SF_DATA_SCIENCE/tree/main/Project%200#%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/Ursekov/MIPT_SF_DATA_SCIENCE/tree/main/Project%200#%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результат](https://github.com/Ursekov/MIPT_SF_DATA_SCIENCE/tree/main/Project%200#%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)    
[6. Выводы](https://github.com/Ursekov/MIPT_SF_DATA_SCIENCE/tree/main/Project%200#%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B) 

**Файлы 'main.py' и 'main2.ipynb' идентичны по содержанию, но разные по формату.**

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](https://github.com/Ursekov/MIPT_SF_DATA_SCIENCE/tree/main/Project%200#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python

:arrow_up:[к оглавлению](https://github.com/Ursekov/MIPT_SF_DATA_SCIENCE/tree/main/Project%200#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Краткая информация о данных
Материалы, представленные МФТИ, лежат в облаке на [Google Диск](https://drive.google.com/drive/folders/1CnZIvDAE6x4eSsFkjbovUrECZmj4qjD1?usp=sharing).
Среди представленных материалов есть два готовых решения для поиска числа и функция(score_game), которая создает список загадываемых чисел через функцию(np.random.randint(1, 101, size=(1000))) и вычисляет среднее количество попыток, которое нужно программе.
  
:arrow_up:[к оглавлению](https://github.com/Ursekov/MIPT_SF_DATA_SCIENCE/tree/main/Project%200#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Этапы работы над проектом  
1. Формулирование алгоритма решения задач. (Использование техники бинарного поиска)
2. Реализация алгоритма.
3. Сохранение программы на платформе GitHub.

:arrow_up:[к оглавлению](https://github.com/Ursekov/MIPT_SF_DATA_SCIENCE/tree/main/Project%200#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Результаты:  
Алгоритм "угадывает" число в среднем за 5 попыток при 1000 повторений.

:arrow_up:[к оглавлению](https://github.com/Ursekov/MIPT_SF_DATA_SCIENCE/tree/main/Project%200#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Выводы:  
Предложенный алгоритм бинарного поиска является оптимальным для поиска загаданного числа и он работает в соответствии с условиями.

:arrow_up:[к оглавлению](https://github.com/Ursekov/MIPT_SF_DATA_SCIENCE/tree/main/Project%200#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами