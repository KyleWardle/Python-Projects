
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput
       break

def allocateBits(object):
    length = len(object)
    if (length < 8):
        rem = 8 - length
    else:
        rem = length % 8
    # rem = 4 - rem
    for i in range(0, rem):
        object = object + "0"
    return object

def positiveBinaryConvert(integer):
    before = ""
    finished = False
    while finished != True:
        divided = int(int(integer) / 2)
        remainder = int(integer) % 2
        before = before + str(remainder)
        integer = divided
        if divided == 0:
            finished = True
    before = allocateBits(before)
    binary = before[::-1] # Flips the string
    return binary

def binary_add(first, second):
    first = list(first[::-1]) #flips both around to work with left to right rahter than opposite
    second = list(second[::-1])

    final_added = ""
    carry = False

    for i in range(0, len(first)):
        added = int(first[i]) + int(second[i])
        if (carry):
            added = added + 1

        if (added == 0 or added == 1):
            final_added = final_added + str(added)
            carry = False
        else:
            final_added = final_added + str(added - 2)
            carry = True

    return final_added[::-1]



def flipBits(binary):
    binary_list = list(binary)
    for i in range(0, len(binary)):
        binary_list[i] = "1" if binary_list[i] == "0" else "0"
    binary = "".join(binary_list)
    return binary

def makeBinaryNegative(binary):
    flipped = flipBits(binary)
    return binary_add(flipped, "00000001")

def convertIntToBinary(number):
    neg  = False;
    if (number < 0):
        neg = True

    binary = positiveBinaryConvert(abs(number))

    if (neg):
        binary = makeBinaryNegative(binary)

    return binary

def binaryToDenary(binary_str):
    binary = list(binary_str[::-1]) #flips string
    value = 0

    for i in range (0, len(binary)):
        value += ((2 ** i) * int(binary[i]))

    return value





first_denary = inputNumber("Enter your first Integer to add: ")
first_binary = convertIntToBinary(first_denary)
print(first_binary)

second_denary =  inputNumber("Enter your second Integer to add: ")
second_binary = convertIntToBinary(second_denary)
print(second_binary)

added = binary_add(first_binary, second_binary)
print("--------")
print(added)
print("--------")
denary = binaryToDenary(added)
print(denary)


# added = binary_add("00000111", "00000111")
# print(added)
