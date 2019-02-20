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

    def push(self, value):
        new_node = Node(value, None, None)
        if self.head:
            new_node.next_node = self.head
            self.head.previous_node = new_node
        if self.bottom is None:
            self.bottom = new_node
        self.head = new_node
        self.length += 1
        return None

    def pop(self):
        if self.bottom:
            tmp = self.bottom
            if tmp.previous_node:
                self.bottom = tmp.previous_node
            else:
                self.bottom = None
            self.length -= 1
            return tmp.value
        else:
            raise ValueError('Queue has nothing to Pop!')

    def length(self):
        return self.length

    def __len__(self):
        return self.length

    def Peek(self):
        return self.head.value


class PriorityQueue:
    def __init__(self):
        self.low_priority = Queue()
        self.med_priority = Queue()
        self.high_priority = Queue()

    def push(self, value, priority=3):
        if priority == 3:
            self.low_priority.push(value)
        if priority == 2:
            self.med_priority.push(value)
        if priority == 1:
            self.high_priority.push(value)

    def pop(self, highest_priority=1):
        if (len(self.high_priority) > 0) and (highest_priority <= 1):
            return self.high_priority.pop()
        if (len(self.med_priority) > 0) and (highest_priority <= 2):
            return self.med_priority.pop()
        if (len(self.low_priority) > 0) and (highest_priority <= 3):
            return self.low_priority.pop()

    def __len__(self):
        return len(self.low_priority) + len(self.med_priority) + len(self.high_priority)


def test_queue():
    queue = Queue()
    queue.push(3)
    queue.push(5)
    queue.push(7)

    print("Length is : " + str(queue.length()))

    print(queue.pop())
    print(queue.pop())
    print(queue.pop())


def test_priority_queue():
    pqueue = PriorityQueue()
    pqueue.push(3)
    pqueue.push(2, 2)
    pqueue.push(1, 1)

    print(pqueue.pop(2))
    print(pqueue.pop())
    print(pqueue.pop())


test_priority_queue()
