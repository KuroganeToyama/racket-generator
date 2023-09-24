import random
from funcs import *

# Generates n random pairs of input - output for function func that takes in a list of params numbers
def generate_random_IO_pairs(n, func, params):
    io_pairs = []
    for _ in range(n):
        arg_list = []
        for _ in range(params):
            x = random.randint(-10000, 10000)
            arg_list.append(x)
        result = func(arg_list)
        io_pairs.append((arg_list, result))
    return io_pairs

# Generate check-expects for func_name
def generate_check_expect(func_name, arg_lists, expected_results):
    check_expects = []
    for args, result in zip(arg_lists, expected_results):
        check_expect = f'(check-expect ({func_name} {" ".join(map(str, args))}) {result})'
        check_expects.append(check_expect)
    return '\n'.join(check_expects)

random_pairs = generate_random_IO_pairs(1000, median, 3)

arg_lists, expected_results = zip(*random_pairs)

check_expects = generate_check_expect('median', arg_lists, expected_results)

# print(check_expects)     

# Put the check-expects in check-expect.txt
with open('check-expect.txt', 'w') as file:
    file.write(check_expects)