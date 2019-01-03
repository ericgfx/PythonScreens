import os
from LinkedList import LinkedList
from os.path import join, isfile
#Bugger this took forever to get correct. Learned to search using error message.
from datetime import datetime, date
import json
import cPickle as pickle

# Testing Variables

Directory = '.'

# Global Variables
today = str(date.today()) # ie '2017-12-26'



############   Input Date   ######
def InputDate():
  userDate = raw_input("Please enter date in the format mm-dd-yyyy: ")
  month,day,year = userDate.split('-')
  date1 = date(int(year),int(month),int(day))
  return date1


############   Node from Node   ######

class Node:
  def __init__(self, name, content, endDate=None, startDate=None):
    self.name = name
    self.content = content
    self.endDate = endDate
    self.startDate = startDate
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
  def __init__(self,listName):
    self.listName = listName
    self.head_node = None

  def get_head_node(self):
    return self.head_node

  def archive(self):
    print "Archive function not ready yet."

  def inputSlide(self):
    print "Create New Slide not ready yet."

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


  def displayList(self):
    print""
    print "Today's Date: "+today+""
    string_list = str("-"*54) +"\n"
    current_node = self.get_head_node()

    while current_node:
      if current_node.get_name() != None:
        string_list += str(current_node.get_name())+"" + " "*(13 - len(str(current_node.get_name()))) + str(current_node.get_content()) + " "*(20 - len(str(current_node.get_content()))) + " End Date: "
        if current_node.get_endDate() != None:
          string_list += str(current_node.get_endDate())
      string_list += "\n"
      current_node = current_node.get_next_node()
    string_list += str("-"*54) +"\n"
    return string_list

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




############   Global Functions   ######
def changeList():
  print "Function not ready yet."

def joinDirectoryAndName(Filename):
  joint = os.path.join(Directory,Filename)
  return joint

def changeName(OldFilename, NewFilename):
  os.rename(OldFilename, NewFilename)
  print "Success! Go have a spot o' tea."


def changeFilename(OldFilename, NewFilename):
  OldFilename += ".png"
  print "Preparing to rename", OldFilename + " to " + str(NewFilename)+".png"
  OldFilename = joinDirectoryAndName(OldFilename)
  existsOld = os.path.isfile(OldFilename)
  i = 1
  while True:
    if NewFilename == 'expired':
      tempFilename = NewFilename + str(i) +".png"
    else:
      tempFilename = NewFilename +".png"
    i += 1
#    testFilename = joinDirectoryAndName(tempFilename)
    existsNew = os.path.isfile(joinDirectoryAndName(tempFilename))
    if existsOld and not existsNew:
      changeName(OldFilename,joinDirectoryAndName(tempFilename))
      break
    elif not existsOld:
      print "File named ", OldFilename ," does not exist"
      break
    elif existsNew:
      print "File", tempFilename," already exists."




############   User Functions   ######
def executeUserChoice(argument):
  switcher = {
    1: ll.remove_expired(today),
    2: ll.archive(),
    3: ll.inputSlide(),
    4: changeList()
  }
  #Get the function from switcher
  func = switcher.get(argument, lambda: "invalid")
  #Execute the function
  return func()

def whatNow():
  userChoice = 0
  print "---Make a selection---"
  print " 1 Remove Expired Slides"
  print " 2 Archive a Current Slide"
  print " 3 Add a new slide"
  print " 4 Change List Current List is: " + str(ll.listName) + "."
  while (userChoice > 4 or userChoice < 1):
    userChoice = int(raw_input("What would you like to do next? (1 - 4):"))
    print(userChoice)
  executeUserChoice(userChoice)


        
ll = LinkedList('CPMC')
ll.addNode("Slide1", "Key Dates", '2019-3-04')
ll.addNode("Slide10", "Declutter", '2019-1-04')
ll.addNode("Slide2", "Facility Specialists", '2019-3-03')
ll.addNode("Slide3", "Training", '2019-2-01')
ll.addNode("Slide4", "Download your Guides", '2019-5-04')
ll.addNode("Slide5", "Electric W2", '2019-01-04')
ll.addNode("Slide6", "Colleagues Campaign", '2018-12-30')
ll.addNode("Slide7", "Block Party", '2019-02-02')
ll.addNode("Slide8", "Diabetes", '2019-06-30')
ll.addNode("Slide9", "Diabetes 2", '2019-06-25')
print(ll.displayList())
whatNow()
'''pickle.dump(ll, open('cpmc.pkl', 'wb'))
x = pickle.load(open('cpmc.pkl'))
print str(x)
'''
#print(x.displayList())
