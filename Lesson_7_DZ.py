# Задача 1. Создайте пользовательский аналог метода map().

def my_map(func, iterable):
    return [func(item) for item in iterable]

# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.
# Эту задачу честно стырил у Антона, т.к. хочу успеть вовремя сдать всю домашку
# Но в коде я разобрался

from time import time

def benchmark(amt):
    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            total = 0
            for i in range(amt):
                start_time = time()
                func(*args, **kwargs)
                total += time() - start_time
            average_time = total / amt
            print(f"среднее время выполнения функции = {average_time}\nкол-во тестов = {amt}")
        return wrapper2
    return wrapper1

