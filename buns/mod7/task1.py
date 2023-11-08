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
def example_function(x):
    return f"The argument is {x}"

print(example_function(5))
print(example_function("string"))
print(example_function(-2))
print(example_function(1, 2))
print(example_function())
