from functools import lru_cache
import time


@lru_cache(maxsize=4)
def slow_sqr(i):
    print(f'Calculating sqr for {i}...')
    time.sleep(0.5)  # задумаемся...
    return i ** 2


for i in [1, 2, 3, 1, 3, 15, 8, 1, 4, 4, 1]:
    print(f'i = {i}  => i ** 2 = {slow_sqr(i)}')

print(slow_sqr.cache_info())
