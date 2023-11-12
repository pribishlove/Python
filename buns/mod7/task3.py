import time

class Timer:
    def __init__(self, func):
        self.func = func
        self.start_time = None
        self.end_time = None
    def __call__(self, *args, **kwargs):
        if self.start_time is None:
            self.start_time = time.time()
            result = self.func(*args, **kwargs)
            self.end_time = time.time()
            print(f"Функция {self.func.__name__} выполнялась {self.end_time - self.start_time} секунд")
            self.start_time = None
            self.end_time = None
        else:
            result = self.func(*args, **kwargs)
        return result
def memoize(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

def validate_args(func):
    def wrapper(*args, **kwargs):
        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 else "Too many arguments"
        arg = args[0]
        if not isinstance(arg, int):
            return "Wrong types"
        if arg < 0:
            return "Negative argument"
        return func(*args, **kwargs)
    return wrapper

@validate_args
@Timer
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

result_without_memoize = fibonacci(30)
print(f"Result: {result_without_memoize}")

fibonacci = memoize(fibonacci)

result_with_memoize = fibonacci(30)
print(f"Result: {result_with_memoize}")
