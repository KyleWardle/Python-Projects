class Node:
  def __init__(self, value, next_node):
    self.value = value
    self.next_node = next_node

  def print_all(self, string = "["):
    string += str(self.value) + ","
    if (self.next_node):
      self.next_node.print_all(string)
    else:
      string = string[:-1]
      string += "]"
      print(string)

class NewArray:
  def __init__(self, value):
    self.first_node = Node(value, None)
    self.last_node = None

  def append(self, value):
    new_node = Node(value, None)
    if (self.last_node):
      self.last_node.next_node = new_node
    else:
      self.first_node.next_node = new_node

    self.last_node = new_node

  def output(self):
    self.first_node.print_all()

# Node4 = Node(82, None)
# Node3 = Node(52, Node4)
# Node2 = Node(11, Node3)
# Node1 = Node(15, Node2)

# Node1.print_all()

new_arr = NewArray(1)
new_arr.append(2)
new_arr.append(3)
new_arr.append(4)
new_arr.append(5)

new_arr.output()
