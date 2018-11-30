
import re
import time

def getInput():
    NUM_REGEX = re.compile(r"^\d+(?:\.\d{,30})?$")
    input_str = input("Input a decimal: ")
    while NUM_REGEX.match(input_str) is None:
        input_str = input("Nope, not valid. Give me another: ")
    return input_str

def allocateBits(object):
    length = len(object)
    if (length < 4):
        rem = 4 - length
    else:
        rem = length % 4
    for i in range(0, rem):
        object = object + "0"
    return object

def calculateFirstHalf(input_str):
    numArray = str(float(input_str)).split('.') # Split the float as string on decimal place
    integer = numArray[0]
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
    firstHalf = before[::-1] # Flips the string
    return firstHalf

def calculateSecondHalf(input_str):
    numArray = str(float(input_str)).split('.') # Split the float as string on decimal place
    decimal = float(input_str) - int(numArray[0])
    after = ""
    finished = False
    while finished != True:
        timesBy2 = decimal * 2
        halves = str(float(timesBy2)).split('.')
        decimal =  timesBy2 - int(halves[0])
        after = after + halves[0]
        if float(decimal) == 0.0:
            finished = True
    after = allocateBits(after)
    return after

def convertDecimalToBinary(input):
    firstHalf = calculateFirstHalf(input)
    secondHalf = calculateSecondHalf(input)

    return firstHalf + "." + secondHalf

def main():
    decimal = getInput() # Float Returned as string
    start = time.time()
    binary = convertDecimalToBinary(decimal)
    print(binary)

    print(time.time() - start)

main();
