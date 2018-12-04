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