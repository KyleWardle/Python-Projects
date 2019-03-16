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

class UnlimitedPriorityQueue:
    def __init__(self):
        self.queues = {}

    def Push(self, value, priority = 1):
        if priority not in self.queues:
            self.queues[priority] = Queue()
        self.queues[priority].Push(value)


    def Pop(self, highest_priority = 1):
        for i in range(0, len(self.queues)):
            i = i + 1
            if ((len(self.queues[i]) > 0) and (highest_priority <= i)):
                return self.queues[i].Pop()


    def __len__ (self):
        length = 0
        for i in range(0, len(self.queues)):
            length += len(self.queues[i+1])

        return length


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
    pqueue.Push(2, 2) #Medium priority ,will be displayed second
    pqueue.Push(1, 1) #Top Priority, will be displayed first

    print("Length is : " + str(len(pqueue)))

    print(pqueue.Pop())
    print(pqueue.Pop())
    print(pqueue.Pop())


def testUnlimitedPriorityQueue():

    upqueue = UnlimitedPriorityQueue()
    upqueue.Push(3, 3)
    upqueue.Push(2, 2)
    upqueue.Push(1, 1)

    # print("Length is : " + str(len(upqueue)))

    print(upqueue.Pop())
    print(upqueue.Pop())
    print(upqueue.Pop())

testUnlimitedPriorityQueue()
