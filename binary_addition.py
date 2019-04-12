from tqdm import tqdm


class MaximumValueException(Exception):
    pass


class MinimumValueException(Exception):
    pass


class Binary:
    def __init__(self, application, integer: int = None):
        self.app = application
        self.binary_value = self.convert_int_to_binary(integer) if integer is not None else None

    def from_binary(self, binary: str):  # init from binary as opposed to an integer
        self.binary_value = self.allocate_bits(binary[::-1])[::-1]
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

        return Binary(self.app).from_binary(final_added[::-1])

    def __sub__(self, other):
        return self + (- other)

    def __mul__(self, other):
        other_value_reversed = list(other.binary_value[::-1])
        total = Binary(self.app, 0)
        for i in tqdm(range(1, len(other_value_reversed) + 1)):
            binary_val = int(self.binary_value) * int(other_value_reversed[i - 1]) * int(10 ** (i - 1))
            total = total + Binary(self.app).from_binary(str(binary_val))
        return total

    def __ge__(self, other):
        return self.denary() >= other.denary()  # I know this isn't ideal but will come back around to it.

    def __le__(self, other):
        return self.denary() <= other.denary()

    def __truediv__(self, divisor):
        dividend = self.binary_value
        cur_div = ""
        answer = ""

        for i in range(0, len(dividend)):
            cur_div = cur_div + dividend[i]
            if divisor <= Binary(self.app).from_binary(cur_div):
                answer = answer + "1"
                take_away = divisor * Binary(self.app).from_binary(answer)
                # print(take_away)
                # print(Binary(self.app).from_binary(cur_div))
                cur_div = (Binary(self.app).from_binary(cur_div) - take_away).binary_value

            else:
                if 0 < len(answer):  # If the first digit has been placed
                    answer = answer + "0"

        return Binary(self.app).from_binary(answer)

    def __neg__(self):
        return self.change_state()

    def denary(self):
        binary = list(self.binary_value)  # flips string
        value = 0
        if binary[0] == "1":
            binary = list(self.change_state().binary_value[::-1])
            for i in range(0, len(binary) - 1):
                value += ((2 ** i) * int(binary[i]))
            return -int(value)
        elif binary[0] == "0":
            binary = list(self.binary_value[::-1])
            for i in range(0, len(binary) - 1):
                value += ((2 ** i) * int(binary[i]))
            return int(value)

    def convert_int_to_binary(self, number):
        neg = False
        if number < 0:
            neg = True
        binary = self.positive_binary_convert(abs(number))
        if neg:
            binary = binary.change_state()
        return binary.binary_value

    def positive_binary_convert(self, integer):  # Converts a positive denary number to binary
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
        return Binary(self.app).from_binary(binary)

    def change_state(self, binary=None):  # Change from negative to positive
        if binary is not None:
            flipped = Binary(self.app).from_binary(binary).flip_bits()
        else:
            flipped = self.flip_bits()

        return flipped + Binary(self.app, 1)

    def allocate_bits(self, value):
        length = len(value)
        rem = self.app.bits - length

        if rem > 0:
            for i in range(0, rem):
                value = value + "0"

        if rem < 0:
            for i in range(0, abs(rem)):
                value = value[:-1]
        return value

    def flip_bits(self):
        binary_list = list(self.binary_value)

        for i in range(0, len(self.binary_value)):
            binary_list[i] = "1" if binary_list[i] == "0" else "0"
        binary = "".join(binary_list)
        return Binary(self.app).from_binary(binary)


class Application:
    def __init__(self, bits=8):
        self.bits = bits
        self.max_bound = (2 ** (self.bits - 1)) - 1
        self.min_bound = self.max_bound * -1

    def welcome_message(self):
        print("Welcome to the Binary Calculator!")
        print("---------------------------------")
        print("This Calculator is currently set to " + str(self.bits) + " bits.")
        print("The Maximum Bound of the calculator is " + str(self.max_bound))
        print("The Minimum Bound of the calculator is " + str(self.min_bound))

    def input_number(self, message):
        while True:
            try:
                user_input = int(input(message))
                if user_input > self.max_bound:
                    raise MaximumValueException()
                if user_input < self.min_bound:
                    raise MinimumValueException()

            except ValueError:
                print("Not an integer! Try again.")
                continue
            except MaximumValueException:
                print('Value above maximum bound of ' + str(self.max_bound))
            except MinimumValueException:
                print('Value below minimum bound of ' + str(self.min_bound))

            else:
                return user_input

    @staticmethod
    def input_sum_type():
        return str(input("What do you want to do (add, take, divide, multiply)? "))

    def input_integer(self, message):
        denary = self.input_number(message)
        binary = Binary(self, denary)
        print(binary)
        return binary

    @staticmethod
    def output_spacer():
        print("--------")

    @staticmethod
    def calculate(sum_type, first_binary, second_binary):
        if sum_type in ["add", "+"]:
            return first_binary + second_binary
        elif sum_type in ['take', '-']:
            return first_binary - second_binary
        elif sum_type in ['multiply', 'times', 'x', '*']:
            return first_binary * second_binary
        else:
            return None

    def output_calculated(self, calculated):
        print(calculated)
        self.output_spacer()
        print(calculated.denary())

    def retry(self):
        try_again = str(input("Do you want to try again? "))
        if try_again.lower() in ["yes", "y", "yea"]:
            self.main()
        else:
            print("Thanks.")

    def test(self):
        print("Passed" if (Binary(self, 5) + Binary(self, 10)).denary() == 15 else "Failed")
        print("Passed" if (Binary(self, 125) + Binary(self, 125)).denary() == 250 else "Failed")
        print("Passed" if (Binary(self, 5) - Binary(self, 10)).denary() == -5 else "Failed")
        print("Passed" if (Binary(self, 255) - Binary(self, 120)).denary() == 135 else "Failed")
        print("Passed" if (Binary(self, 4) * Binary(self, 5)).denary() == 20 else "Failed")
        print("Passed" if (Binary(self, 125) * Binary(self, 1000)).denary() == 125000 else "Failed")
        print("Passed" if (Binary(self, 10) / Binary(self, 2)).denary() == 5 else "Failed")
        print("Passed" if (Binary(self, 28788718) / Binary(self, 23198)).denary() == 1241 else "Failed")
        print((Binary(self, 13680) / Binary(self, 912)).denary())

    def start(self):
        self.welcome_message()
        self.main()

    def main(self):
        sum_type = self.input_sum_type()
        first_binary = self.input_integer("Enter your first Integer: ")
        second_binary = self.input_integer("Enter your Second Integer: ")
        self.output_spacer()
        calculated = self.calculate(sum_type, first_binary, second_binary)
        if calculated is not None:
            self.output_calculated(calculated)
        self.retry()


Application(1028).start()
