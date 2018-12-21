import os
from LinkedList import LinkedList
from os.path import join, isfile
#Bugger this took forever to get correct. Learned to search using error message.
from datetime import datetime, date
import json
import cPickle as pickle

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
    return string_list #not sure I need this

  def remove_expired(self, endDate=today):
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




#changeFilename(OldFilename, "remove")

        
x = pickle.load(open('cpmc.pkl'))
x.remove_expired(today)
print(x.displayList())
