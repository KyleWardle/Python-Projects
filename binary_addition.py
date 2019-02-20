def input_number(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput


class Binary:
    def __init__(self, integer: int = None):
        self.binary_value = self.convert_int_to_binary(integer) if integer is not None else None

    def from_binary(self, binary):
        self.binary_value = binary
        return self

    def __str__(self):
        return self.binary_value

    def __len__(self):
        return len(self.binary_value)

    def __add__(self, other):
        first = list(self.binary_value[::-1])  # flips both around to work with left to right rather than opposite
        second = list(other.binary_value[::-1])

        final_added = ""
        carry = False

        for i in range(0, len(first)):
            added_val = int(first[i]) + int(second[i])
            if carry:
                added_val = added_val + 1

            if added_val == 0 or added_val == 1:
                final_added = final_added + str(added_val)
                carry = False
            else:
                final_added = final_added + str(added_val - 2)
                carry = True

        return Binary().from_binary(final_added[::-1])

    def denary(self):
        binary = list(self.binary_value[::-1])  # flips string
        value = 0
        for i in range(0, len(binary)):
            value += ((2 ** i) * int(binary[i]))
        return value

    def convert_int_to_binary(self, number):
        print(number)
        neg = False
        if number < 0:
            neg = True
        binary = self.positive_binary_convert(abs(number))
        if neg:
            binary = self.make_binary_negative(binary)
        return binary

    def positive_binary_convert(self, integer):
        before = ""
        finished = False
        while not finished:
            divided = int(int(integer) / 2)
            remainder = int(integer) % 2
            before = before + str(remainder)
            integer = divided
            if divided == 0:
                finished = True
        before = self.allocate_bits(before)
        binary = before[::-1]  # Flips the string
        return binary

    def make_binary_negative(self, binary):
        flipped = Binary().from_binary(self.flip_bits(binary))
        return str(flipped + Binary().from_binary("00000001"))

    @staticmethod
    def allocate_bits(value):
        length = len(value)
        if length < 8:
            rem = 8 - length
        else:
            rem = length % 8
        for i in range(0, rem):
            value = value + "0"
        return value

    @staticmethod
    def flip_bits(binary):
        binary_list = list(binary)
        for i in range(0, len(binary)):
            binary_list[i] = "1" if binary_list[i] == "0" else "0"
        binary = "".join(binary_list)
        return binary


def main():
    first_denary = input_number("Enter your first Integer to add: ")
    first_binary = Binary(first_denary)
    print(first_binary)

    second_denary = input_number("Enter your second Integer to add: ")
    second_binary = Binary(second_denary)
    print(second_binary)

    added = first_binary + second_binary
    print("--------")
    print(added)
    print("--------")

    print(added.denary())

    try_again = str(input("Do you want to try again? "))
    if try_again.lower() in ["yes", "y", "yea"]:
        main()
    else:
        print("Thanks.")


main()
