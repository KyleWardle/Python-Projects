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
            self.next_node.print_all(string)
        else:
            string = string[:-1]
            string += "]"
            print(string)


class LinkedList:
    def __init__(self, value = None):
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
        while(True):
            count += 1
            if node.next_node:
                node = node.next_node
            else:
                return count


    def append(self, value):
        new_node = Node(value, None)
        if self.first_node.value == None:
            self.first_node.value = value
        else:
            if self.last_node:
                self.last_node.next_node = new_node
            else:
                self.first_node.next_node = new_node
            self.length += 1
            self.last_node = new_node

    def output(self):
        self.first_node.print_all()

    def get(self, index):
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
        from_value = self.get(from_index)
        to_value = self.get(to_index)
        self.set(from_index, to_value)
        self.set(to_index, from_value)
        return True

    def delete(self, index):
        node = self.first_node
        prev_node = None
        next_node = None

        if (index == 0):
            self.first_node = node.next_node
        else:
            for i in range(0, index + 1):
                if i == (index - 1):
                    prev_node = node
                if i == index:
                    prev_node.next_node = node.next_node
                    return True
                if node.next_node:
                    node = node.next_node
                else:
                    raise ArrayOverrunException('Array Overrun!')

    def bubble_sort(self):
        for a in range(0, len(self)):
            for b in range(0, len(self)):
                if self.get(b) > self.get(b + 1):
                    self.swap(b, b + 1)
        return True

    def merge(self, other):
        both_count = len(self) + len(other)
        merged = LinkedList()

        for i in range(0, both_count):
            if (self.get(0) < other.get(0)):
                merged.append(self.get(0))
                self.delete(0)
            else:
                merged.append(other.get(0))
                other.delete(0)

        if len(self) < len(other):
            merged.append(other.get(0))
        else:
            merged.append(self.get(0))

        self = merged

    def split(self):
        node = self.first_node
        index = (len(self) // 2)
        print("index" + str(index))
        first_half = LinkedList()
        second_half = LinkedList()
        # print(index)
        for i in range(0, index + 1):
            print(i)
            if i == index:
                second_half.first_node = node.next_node
                second_half.last_node = self.last_node
                second_half.length = second_half.re_calculate_length()

                first_half.last_node = node
                first_half.last_node.next_node = None
                # print(first_half.last_node.next_node)
                first_half.first_node = self.first_node
                first_half.length = first_half.re_calculate_length()

                return {
                    'first_half': first_half,
                    'second_half': second_half
                }
            if node.next_node:
                node = node.next_node
            else:
                raise ArrayOverrunException('Array Overrun!')


    def merge_sort(self):
        print(len(self))
        if len(self) == 1:
            return self
        else:
            print("BeforeSPlit")
            self.output()
            split = self.split()
            print("First")
            split['first_half'].output()
            print("second")
            split['second_half'].output()

            a = split['first_half'].merge_sort()
            b = split['second_half'].merge_sort()

            return a.merge(b)



linked_list = LinkedList()
linked_list.append(3)
linked_list.append(5)
# linked_list.append(7)
linked_list.append(2)
linked_list.append(1)
linked_list.append(4)

# split = linked_list.split()


#
# for i in range(1, 5):
#     linked_list.append(randint(0, 100))

linked_list.output()
#
# split = linked_list.split()
#
# split['first_half'].output()
# split['second_half'].output()

# print(linked_list.re_calculate_length())
#
# split = linked_list.split()

#
# split['first_half'].output()
# print(len(split['first_half']))
# split['second_half'].output()
# print(len(split['second_half']))
#
# split_first = split['first_half'].split()
# split_first['first_half'].output()
# print(len(split_first['first_half']))
# split_first['second_half'].output()
# print(len(split_first['second_half']))
#
# split_second = split['second_half'].split()
# split_second['first_half'].output()
# print(len(split_second['first_half']))
# split_second['second_half'].output()
# print(len(split_second['second_half']))


sorted = linked_list.merge_sort()

sorted.output()
