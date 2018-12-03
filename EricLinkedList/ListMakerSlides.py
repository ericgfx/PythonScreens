


class Node:
  def __init__(self, name, content, endDate=None, next_node = None):
    self.name = name
    self.content = content
    self.endDate = endDate
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_name(self):
    return self.name

  def get_content(self):
    return self.content

  def get_endDate(self):
    return self.endDate


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

  def remove_node(self):
    current_node = self.get_head_node()
    while current_node.get_endDate() == "today":
      self.head_node = current_node.get_next_node()
      current_node = self.get_head_node()
    while current_node:
      if current_node.get_next_node() != None:
        next_node = current_node.get_next_node()
        if next_node.get_endDate() == "today":
          current_node.set_next_node(next_node.get_next_node())
        elif next_node.get_name() != None:
          current_node = next_node
      else:
        current_node = None
        
a = Node("Slide1.png", "ACSC", "today")
b = Node("Slide2.png", "ACSC2", "tomorrow", a)
c = Node("Slide3.png", "ACSC3", "today", b)
d = Node("Slide4.png", "ACSC4", "tomorrow", c)
ll = LinkedList(55, "test", "tomorrow", d)
print("")
print(ll.stringify_list())
ll.remove_node()
print ("-------------")
ll.insert_beginning('Pop-pop','Pop-test')
print(ll.stringify_list())
print ("-------------")

