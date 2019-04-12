from random import randint
import copy


class ArrayOverrunException(Exception):
    pass


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

    def print_all(self, string="["):
        string += str(self.value) + ","
        if self.next_node:
            return self.next_node.print_all(string)
        else:
            string = string[:-1]
            string += "]"
            return string


class LinkedList:
    def __init__(self, value=None):
        self.first_node = Node(value, None)
        self.last_node = None
        self.length = 0

    def __len__(self):
        return self.length

    def re_calculate_length(self):
        node = self.first_node
        count = 0
        if node.value == None:
            return count
        while (True):
            count += 1
            if node.next_node:
                node = node.next_node
            else:
                return count

    def re_calculate_last_node(self):
        node = self.first_node
        while True:
            if node.next_node:
                node = node.next_node
            else:
                return node

    def append(self, value):
        new_node = Node(value, None)
        if self.first_node.value == None:
            self.first_node.value = value
            self.length += 1
        else:
            if self.last_node:
                self.last_node.next_node = new_node
            else:
                self.first_node.next_node = new_node
            self.length += 1
            self.last_node = new_node

    def __str__(self):
        return self.first_node.print_all()

    def __getitem__(self, index):
        node = self.first_node
        for i in range(0, index + 1):
            if i == index:
                return node.value
            if node.next_node:
                node = node.next_node
            else:
                raise ArrayOverrunException('Array Overrun!')

    def set(self, index, value):
        node = self.first_node
        for i in range(0, index + 1):
            if i == index:
                node.value = value
                return True
            if node.next_node:
                node = node.next_node
            else:
                raise ArrayOverrunException('Array Overrun!')

    def swap(self, from_index, to_index):
        from_value = self[from_index]
        to_value = self[to_index]
        self.set(from_index, to_value)
        self.set(to_index, from_value)
        return True

    def delete(self, index):
        node = self.first_node
        prev_node = None

        if index == 0:
            self.first_node = node.next_node
            self.length -= 1
        else:
            for i in range(0, index + 1):
                if i == (index - 1):
                    prev_node = node
                if i == index:
                    prev_node.next_node = node.next_node
                    self.length -= 1
                    return True
                if node.next_node:
                    node = node.next_node
                else:
                    raise ArrayOverrunException('Array Overrun!')

    def bubble_sort(self):
        print(len(self))
        for a in range(0, len(self) - 1):
            for b in range(0, len(self) - 1):
                if self[b] > self[b + 1]:
                    self.swap(b, b + 1)
        return True

    def merge(self, other):
        merged = LinkedList()

        while len(self) > 0 and len(other) > 0:
            if self[0] < other[0]:
                merged.append(self[0])
                self.delete(0)
            else:
                merged.append(other[0])
                other.delete(0)

        if len(self) < len(other):
            for i in range(0, len(other)):
                merged.append(other[0])
                other.delete(0)
        else:
            for i in range(0, len(self)):
                merged.append(self[0])
                self.delete(0)
        # print(merged)
        return merged

    def split(self):
        # print(self)
        slow = self.first_node
        fast = self.first_node

        while fast and fast.next_node:
            fast = fast.next_node
            if fast.next_node:
                fast = fast.next_node
                slow = slow.next_node

        first_half = LinkedList()
        second_half = LinkedList()

        second_half.first_node = slow.next_node
        second_half.last_node = second_half.re_calculate_last_node()
        second_half.length = second_half.re_calculate_length()

        first_half.first_node = self.first_node
        slow.next_node = None
        first_half.last_node = first_half.re_calculate_last_node()
        first_half.length = first_half.re_calculate_length()

        return {
            'first_half': first_half,
            'second_half': second_half
        }

    def merge_sort(self):
        if len(self) == 1:
            return self
        else:
            split = self.split()
            a = split['first_half'].merge_sort()
            b = split['second_half'].merge_sort()

            return a.merge(b)


linked_list = LinkedList()

for i in range(1, 100):
    linked_list.append(randint(0, 100))

print(linked_list)

sorted = linked_list.merge_sort()

print(sorted)
