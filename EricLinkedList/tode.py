class Tode:
  def __init__(self, value, content, endDate = None, next_node = None):
    self.value = value
    self.content = content
    self.endDate = endDate
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_value(self):
    return self.value

  def get_details(self):
  	details=[self.value, self.content, self.endDate]
  	return details

