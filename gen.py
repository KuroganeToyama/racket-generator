import random
import argparse
from funcs import *
from mapping import *

# Generates tests random IO pairs for function func that takes in a list of params numbers
def generate_random_IO_pairs(func, params, tests):
    io_pairs = []
    for _ in range(tests):
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

# Create parser object to read command line arguments
parser = argparse.ArgumentParser(description = "Racket Check-expect Generator")

# Add command line arguments
parser.add_argument("func", nargs = 1, metavar = "func [str]", type = str, help = "Function to generate check-expects for")
parser.add_argument("params", nargs = 1, metavar = "params [int]", type = int, help = "Number of parameters of the function")
parser.add_argument("tests", nargs = 1, metavar = "tests [int]", type = int, help = "Number of check-expects to be generated")

# Parse the command line arguments
cmd_line_args = parser.parse_args()
func_name = cmd_line_args.func[0]
func = function_mappings[cmd_line_args.func[0]]
params = cmd_line_args.params[0]
tests = cmd_line_args.tests[0]

# Generate random IO pairs
random_pairs = generate_random_IO_pairs(func, params, tests)

# Generate argument lists and expected results
arg_lists, expected_results = zip(*random_pairs)

# Generate list of check-expects
check_expects = generate_check_expect(func_name, arg_lists, expected_results)

# Put the check-expects in check-expect.txt
with open('check-expect.txt', 'w') as file:
    file.write(check_expects)