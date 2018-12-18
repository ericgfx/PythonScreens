import os
from LinkedList import LinkedList
from os.path import join, isfile
#Bugger this took forever to get correct. Learned to search using error message.
from datetime import datetime, date


# Testing Variables

Directory = '.'
OldFilename = 'Slide1.png'

# Global Variables
today = str(date.today()) # '2017-12-26'



############   Input Date   ######
def InputDate():
  userDate = raw_input("Please enter date in the format mm-dd-yyyy: ")
  month,day,year = userDate.split('-')
  date1 = date(int(year),int(month),int(day))
  return date1


############   Node from Node   ######

class Node:
  def __init__(self, name, content, endDate=None):
    self.name = name
    self.content = content
    self.endDate = endDate
    self.next_node = None
    
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

############   Linked List   ######
# For how to sort a linked list, check out: https://stackoverflow.com/questions/19217647/sorted-linked-list-in-python

class LinkedList:
  def __init__(self):
    self.head_node = None

  def get_head_node(self):
    return self.head_node

  def addNode(self, name, content, endDate=None):
    curr = self.get_head_node()
    if curr is None:
      n = Node(name, content, endDate)
      n.next_node = None
      self.head_node = n
      return
    
    if curr.name > name:
      n = Node(name, content, endDate)
      n.set_next_node(curr)
      self.head_node = n
      return
     
    while curr.next_node is not None:
      if curr.next_node.name > name:
        break
      curr = curr.next_node
    n = Node(name, content, endDate)
    n.next_node = curr.next_node
    curr.next_node = n
    return


  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()

    while current_node:
      if current_node.get_name() != None:
        string_list += str(current_node.get_name()) + " "*(13 - len(str(current_node.get_name()))) + str(current_node.get_content()) + " "*(20 - len(str(current_node.get_content()))) + " End Date: "
        if current_node.get_endDate() != None:
          string_list += str(current_node.get_endDate())
      string_list += "\n"
      current_node = current_node.get_next_node()

    return string_list #not sure I need this

  def remove_expired(self, endDate):
    current_node = self.get_head_node()

    while current_node.get_endDate() <= endDate:
      oldFilename = str(current_node.get_name())
      changeFilename(oldFilename, "expired")
      self.head_node = current_node.get_next_node()
      current_node = self.get_head_node() 

    while current_node:
      if current_node.get_next_node() != None:
        next_node = current_node.get_next_node()
        if next_node.get_endDate() <= endDate:
          oldFilename = str(next_node.get_name())
          changeFilename(oldFilename, "expired")
          current_node.set_next_node(next_node.get_next_node())
        elif next_node.get_name() != None:
          current_node = next_node
      else:
        current_node = None



def joinDirectoryAndName(Filename):
  joint = os.path.join(Directory,Filename)
  return joint

def changeName(OldFilename, NewFilename):
  os.rename(OldFilename, NewFilename)
  print "Success! Go have a spot o' tea."


def changeFilename(OldFilename, NewFilename):
  OldFilename = joinDirectoryAndName(OldFilename)
  existsOld = os.path.isfile(OldFilename)
  while True:
    i = 1
    NewFilename = NewFilename + str(i) +".png"
    testFilename = joinDirectoryAndName(NewFilename)
    existsNew = os.path.isfile(testFilename)
    if existsOld and not existsNew:
      print "Preparing to rename", OldFilename
      changeName(OldFilename,testFilename)
      break
    elif not existsOld:
      print "File named ", OldFilename ," does not exist"
      break



#changeFilename(OldFilename, "remove")

        
ll = LinkedList()
ll.addNode("Slide1.png", "Key Dates", '2019-3-04')
ll.addNode("Slide2.png", "Facility Specialists", '2019-3-03')
ll.addNode("Slide3.png", "Training", '2019-2-01')
ll.addNode("Slide4.png", "Download your Guides", '2019-5-04')
ll.addNode("Slide5.png", "Electric W2", '2019-01-04')
ll.addNode("Slide8.png", "Diabetes", '2018-12-30')
ll.addNode("Slide9.png", "Holiday Sale", '2018-12-25')
ll.addNode("Slide10.png", "Declutter", '2019-1-04')
ll.addNode("Slide6.png", "Colleagues Campaign", '2018-12-30')
ll.addNode("Slide7.png", "Holiday Parties", '2018-12-13')
ll.addNode("Slide11.png", "Test", '2018-12-03')
ll.addNode("Slide12.png", "test", '2018-12-13')
ll.addNode("Slide13.png", "Test Remove", '2018-11-30')

#print(ll.stringify_list())
ll.remove_expired(today)
print ("-"*54)
print(ll.stringify_list())
print ("-"*54)

