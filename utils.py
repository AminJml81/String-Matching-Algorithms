import time
from functools import wraps



def time_elapsed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()   
        duration = end_time - start_time
        print(f"Function '{func.__name__}' executed in {duration:.2f} seconds.")
        
        return result
    
    return wrapper