from node import Node
from LinkedList import LinkedList
from datetime import date
today = str(date.today()) # '2017-12-26'


def type(name, content, endDate):
  table = name + ' ' + content.ljust(20) + endDate
  return table


class LinkedList:
  def __init__(self, name, content, endDate=None, next_node=None):
    self.head_node = Node(name, content, endDate, next_node)

  def get_head_node(self):
    return self.head_node

  def insert_beginning(self, new_name, new_content, new_endDate=None):
    new_node = Node(new_name, new_content, new_endDate)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_name() != None:
        string_list += str(current_node.get_name()) + "-" + str(current_node.get_content())
        if current_node.get_endDate() != None:
          string_list += " End Date: " + str(current_node.get_endDate())
      string_list += "\n"
      current_node = current_node.get_next_node()
    return string_list

  def stringify_list2(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_name() != None:
        string_list += str(current_node.get_name()) + " "*(13 - len(str(current_node.get_name()))) + str(current_node.get_content()) + " "*(20 - len(str(current_node.get_content()))) + " End Date: "
        if current_node.get_endDate() != None:
          string_list += str(current_node.get_endDate())
      string_list += "\n"
      current_node = current_node.get_next_node()
    return string_list

  def remove_node(self, endDate):
    current_node = self.get_head_node()
    while current_node.get_endDate() == endDate:
      self.head_node = current_node.get_next_node()
      current_node = self.get_head_node()
    while current_node:
      if current_node.get_next_node() != None:
        next_node = current_node.get_next_node()
        if next_node.get_endDate() == endDate:
          current_node.set_next_node(next_node.get_next_node())
        elif next_node.get_name() != None:
          current_node = next_node
      else:
        current_node = None







        
a = Node("Slide1.png", "ACSC", '2018-12-04')
b = Node("Slide2.png", "ACSC2", '2018-12-03', a)
c = Node("Slide3.png", "ACSC3", '2018-12-04', b)
d = Node("Slide4.png", "ACSC4", '2018-12-04', c)
ll = LinkedList(55, "test", '2018-12-04', d)
print("")
print("Today is " + today)
print(ll.stringify_list2())
ll.remove_node(today)
print ("-"*54)
ll.insert_beginning('Pop-pop','Pop-test')
print(ll.stringify_list2())
print ("-"*54)

