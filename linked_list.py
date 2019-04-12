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


class NewArray:
    def __init__(self, value):
        self.first_node = Node(value, None)
        self.last_node = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        new_node = Node(value, None)
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

    def bubble_sort(self):
        for a in range(0, len(self)):
            for b in range(0, len(self)):
                if self.get(b) > self.get(b + 1):
                    self.swap(b, b + 1)
        return True



def init_test_array():
    new_arr = NewArray(2)
    new_arr.append(4)
    new_arr.append(1)
    new_arr.append(3)
    return new_arr


def test_swap():
    new_arr = init_test_array()
    new_arr.swap(0, 1)
    new_arr.output()

    new_arr = init_test_array()
    new_arr.swap(2, 3)
    new_arr.output()

    new_arr = init_test_array()
    new_arr.swap(0, 3)
    new_arr.output()

def main():
    input_val = ""
    new_arr = None
    while input_val != "sort":
        input_val = input("Please enter a number, enter 'sort' to stop entering and sort the array : ")
        if input_val != "sort":
            if new_arr != None:
                new_arr.append(int(input_val))
            else:
                new_arr = NewArray(int(input_val))

    new_arr.output()
    new_arr.bubble_sort()
    new_arr.output()


if __name__ == "__main__":
    main()
