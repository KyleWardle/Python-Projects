import re
import time


def get_input():
    num_regex = re.compile(r"^\d+(?:\.\d{,30})?$")
    input_str = input("Input a decimal: ")
    while num_regex.match(input_str) is None:
        input_str = input("Nope, not valid. Give me another: ")
    return input_str


def allocate_bits(binary):
    length = len(binary)
    if length < 4:
        rem = 4 - length
    else:
        rem = length % 4
    for i in range(0, rem):
        binary = binary + "0"
    return binary


def calculate_first_half(input_str):
    num_array = str(float(input_str)).split('.')  # Split the float as string on decimal place
    integer = num_array[0]
    before = ""
    finished = False
    while not finished:
        divided = int(int(integer) / 2)
        remainder = int(integer) % 2
        before = before + str(remainder)
        integer = divided
        if divided == 0:
            finished = True
    before = allocate_bits(before)
    first_half = before[::-1]  # Flips the string
    return first_half


def calculate_second_half(input_str):
    num_array = str(float(input_str)).split('.')  # Split the float as string on decimal place
    decimal = float(input_str) - int(num_array[0])
    after = ""
    finished = False
    while not finished:
        times_by_2 = decimal * 2
        halves = str(float(times_by_2)).split('.')
        decimal = times_by_2 - int(halves[0])
        after = after + halves[0]
        if float(decimal) == 0.0:
            finished = True
    after = allocate_bits(after)
    return after


def covert_decimal_to_binary(input_val):
    first_half = calculate_first_half(input_val)
    second_half = calculate_second_half(input_val)

    return first_half + "." + second_half


def main():
    decimal = get_input()  # Float Returned as string
    start = time.time()
    binary = covert_decimal_to_binary(decimal)
    print(binary)

    print(time.time() - start)


main()
