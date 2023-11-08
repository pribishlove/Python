import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

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

@memoize
@validate_args
@timer
def fibonacci_with_memoize(n):
    if n < 2:
        return n
    return fibonacci_with_memoize(n-1) + fibonacci_with_memoize(n-2)

@validate_args
@timer
def fibonacci_without_memoize(n):
    if n < 2:
        return n
    return fibonacci_without_memoize(n-1) + fibonacci_without_memoize(n-2)

result_with_memoize = fibonacci_with_memoize(5)
print(f"Result: {result_with_memoize}")
result_without_memoize = fibonacci_without_memoize(5)
print(f"Result: {result_without_memoize}")
