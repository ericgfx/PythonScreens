from node import Node
from LinkedList import LinkedList
#import datetime  #Bugger this took forever to get correct.
from datetime import datetime, date
today = str(date.today()) # '2017-12-26'

def InputDate():
  userDate = raw_input("Please enter date in the format mm-dd-yyyy: ")
  month,day,year = userDate.split('-')
  date1 = date(int(year),int(month),int(day))
  return date1


class LinkedList:
  def __init__(self, name, content, endDate=None, next_node=None):
    self.head_node = Node(name, content, endDate, next_node)

  def get_head_node(self):
    return self.head_node

  def insert_beginning(self, new_name, new_content, new_endDate=None):
    new_node = Node(new_name, new_content, new_endDate)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node


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
        if next_node.get_endDate() <= endDate:
          current_node.set_next_node(next_node.get_next_node())
        elif next_node.get_name() != None:
          current_node = next_node
      else:
        current_node = None


# For how to sort a linked list, check out: https://stackoverflow.com/questions/19217647/sorted-linked-list-in-python




        
a = Node("Slide1.png", "Key Dates", '2019-3-04')
b = Node("Slide2.png", "Facility Specialists", '2019-3-03', a)
c = Node("Slide3.png", "Training", '2019-2-01', b)
d = Node("Slide4.png", "Download your Guides", '2019-5-04', c)
ll = LinkedList("Slide5.png", "Electric W2", '2019-01-04', d)
ll.insert_beginning("Slide6.png", "Colleagues Campaign", '2018-12-30')
ll.insert_beginning("Slide7.png", "Holiday Parties", '2018-12-13')
ll.insert_beginning("Slide8.png", "Diabetes", '2018-12-30')
ll.insert_beginning("Slide9.png", "Holiday Sale", '2018-12-25')
ll.insert_beginning("Slide10.png", "Declutter", '2019-1-04')


'''endDate=InputDate()
print("You entered: " + str(endDate))
print("")
print("Today is " + today)
print(ll.stringify_list2())'''
ll.remove_node(today)
print ("-"*54)
print(ll.stringify_list2())
print ("-"*54)

