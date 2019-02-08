class Node:
    def __init__(self, value, next_node):
      self.value = value
      self.next_node = next_node

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def Push(self, value):
        new_node = Node(value, None)
        if (self.head):
            new_node.next_node = self.head
        self.head = new_node
        self.length+= 1
        return None

    def Pop(self):
        if (self.head):
            tmp = self.head
            if (tmp.next_node):
                self.head = tmp.next_node
            else:
                self.head = None
            self.length-= 1
            return tmp.value
        else:
            raise ValueError('Stack has nothing to Pop!')

    def Length(self):
        return self.length

    def __len__ (self):
        return self.length

    def Peek(self):
        return self.head.value


def testStack():
    stack = Stack()
    stack.Push(3)
    stack.Push(5)
    stack.Push(7)

    print("Length is : " + str(stack.Length()))

    print("Head is : " + str(stack.Peek()))

    print(stack.Pop())
    print(stack.Pop())
    print(stack.Pop())




def reverseString(string):
    arr = Stack()
    for i in range(0, len(string)):
        arr.Push(string[i])

    string = ""
    for i in range(0, len(arr)):
        string+= arr.Pop()

    return string

def testReverse():
    sentence = "The cat sat on the mat"
    reversed = reverseString(sentence)
    print (reversed)


def testWords():
    print(reverseString('Stressed'))
    print(reverseString('Live'))
    print(reverseString('Stink'))
    print(reverseString('Strops'))
    print(reverseString('Lager'))
    print(reverseString('Smart'))
    print(reverseString('Snug'))
    print(reverseString('Lived'))
    print(reverseString('Reviled'))

def checkParenthesis(string):
    print(string)
    bracketStack = Stack()
    squigglyStack = Stack()
    failed = False
    for i in range(0, len(string)):
        if (string[i] == "{"):
            squigglyStack.Push("Yes")
        if (string[i] == "}"):
            try:
                squigglyStack.Pop()
            except:
                if (failed != True):
                    print("Squiggly Mismatch")
                    failed = True
        if (string[i] == "("):
            bracketStack.Push("Yes")
        if (string[i] == ")"):
            try:
                bracketStack.Pop()
            except:
                if (failed != True):
                    print("Bracket Mismatch")
                    failed = True

    if (len(bracketStack) != 0 and failed == False):
        print("Bracket Mismatch")
    elif (len(squigglyStack) != 0 and failed == False):
        print("Squiggly Mismatch")
    elif (failed == False):
            print("Success!")

def testParenthesis():
    checkParenthesis('(5+7) * (7+8) / (4+3)')
    checkParenthesis('((a)(b)(c))')
    checkParenthesis('((1)(((2))(3))))')
    checkParenthesis('({q)){w}})')
    checkParenthesis('{{{({q){w}}')



testParenthesis()
# testStack()
# testWords()
