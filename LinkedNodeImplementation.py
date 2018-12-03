#from node import Node
class Node:
  def __init__(self, value, val2=None, next_node=None):
    self.value = value
    self.val2 = val2
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_value(self):
    return self.value

  def get_val2(self):
    return self.val2


class LinkedList:
  def __init__(self, value=None, val2=None, next_node=None):
    self.head_node = Node(value, val2, next_node)
  def get_head_node(self):
    return self.head_node
  def insert_beginning(self, new_value, val2=None):
    new_node = Node(new_value, val2)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + ": " + str(current_node.get_val2())
        if current_node.get_next_node() != None:
          string_list += ", "
      current_node = current_node.get_next_node()
    return string_list
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    while current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
      current_node = self.get_head_node()
    while current_node:
      if current_node.get_next_node() != None:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
        elif next_node.get_value() != None:
          current_node = next_node
      else:
        current_node = None
        
#'''
a = Node("Slide1.png", "a")
b = Node(70, "a", a)
c = Node(5675, "b", b)
d = Node(90, "c", c)
ll = LinkedList("Eric", "d", d)
print(ll.stringify_list())
ll.remove_node(5675)
print ("-------------")
ll.insert_beginning('Pop-pop')
print(ll.stringify_list())
print ("-------------")

'''
ll = LinkedList('c')
ll.insert_beginning('b')
ll.insert_beginning('b')
ll.insert_beginning('b')
ll.insert_beginning('a')
print(ll.stringify_list())
ll.remove_node('b')
print ("-------------")
print(ll.stringify_list())
print ("-------------")
'''