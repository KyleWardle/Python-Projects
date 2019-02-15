class Node:
    def __init__(self, value, next_node, previous_node):
      self.value = value
      self.next_node = next_node
      self.previous_node = previous_node

class Queue:
    def __init__(self):
        self.head = None
        self.bottom = None
        self.length = 0

    def Push(self, value):
        new_node = Node(value, None, None)
        if (self.head):
            new_node.next_node = self.head
            self.head.previous_node = new_node
        if (self.bottom == None):
            self.bottom = new_node
        self.head = new_node
        self.length+= 1
        return None

    def Pop(self):
        if (self.bottom):
            tmp = self.bottom
            if (tmp.previous_node):
                self.bottom = tmp.previous_node
            else:
                self.bottom = None
            self.length-= 1
            return tmp.value
        else:
            raise ValueError('Queue has nothing to Pop!')

    def Length(self):
        return self.length

    def __len__ (self):
        return self.length

    def Peek(self):
        return self.head.value

class PriorityQueue:
    def __init__(self):
        self.low_priority = Queue()
        self.med_priority = Queue()
        self.high_priority = Queue()

    def Push(self, value, priority = 3):
        if (priority == 3):
            self.low_priority.Push(value)
        if (priority == 2):
            self.med_priority.Push(value)
        if (priority == 1):
            self.high_priority.Push(value)

    def Pop(self, highest_priority = 1):
        if ((len(self.high_priority) > 0) and (highest_priority <= 1)):
            return self.high_priority.Pop()
        if ((len(self.med_priority) > 0) and (highest_priority <= 2)):
            return self.med_priority.Pop()
        if ((len(self.low_priority) > 0) and (highest_priority <= 3)):
            return self.low_priority.Pop()

    def __len__ (self):
        return len(self.low_priority) + len(self.med_priority) + len(self.high_priority)

def testQueue():
    queue = Queue()
    queue.Push(3)
    queue.Push(5)
    queue.Push(7)

    print("Length is : " + str(queue.Length()))


    print(queue.Pop())
    print(queue.Pop())
    print(queue.Pop())

def testPriorityQueue():
    pqueue = PriorityQueue()
    pqueue.Push(3)
    pqueue.Push(2, 2)
    pqueue.Push(1, 1)

    print(pqueue.Pop(2))
    print(pqueue.Pop())
    print(pqueue.Pop())


testPriorityQueue()
