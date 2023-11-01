def is_armstrong_number(num):
    num_str = str(num)
    n = len(num_str)
    return num == sum(int(digit) ** n for digit in num_str)
def armstrong_numbers_generator():
    num = 10
    while True:
        if is_armstrong_number(num):
            yield num
        num += 1
def get_armstrong_numbers():
    return next(generator)
generator = armstrong_numbers_generator()

for i in range(8):
    print(get_armstrong_numbers(),  end=' ')
