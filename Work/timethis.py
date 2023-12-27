

import time
def time_taken(func):
    def timer(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__module__}.{func.__name__}: {end - start}')
        return r
    return timer
