import os
from LinkedList import LinkedList
from os.path import join, isfile
#Bugger this took forever to get correct. Learned to search using error message.
from datetime import datetime, date
import json, io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Testing Variables
Directory = '.'

# Global Variables
today = str(date.today()) # ie '2017-12-26'


############   Global Functions #####
def alertBlock(message):
  if message != "":
    print "\n" + str("-"*54) + "\n" + message + "\n" + str("-"*54)
  else:
    print "\n" + str("-"*54) + "\n" + str("-"*54) + "\n"




############   Input Date   ######
def InputDate():
  userDate = raw_input("Please enter date in the format mm-dd-yyyy: ")
  month,day,year = userDate.split('-')
  date1 = date(int(year),int(month),int(day))
  return date1


############   OS Functions   ######
def joinDirectoryAndName(OsFilename):
  joint = os.path.join(Directory,OsFilename)
  return joint


def changeOsName(oldOsFilename, newOsFilename):
  os.rename(oldOsFilename, newOsFilename)
  print "Success! Go have a spot o' tea."


def changeOsFilename(oldOsFilename, newOsFilename):
  oldOsFilename += ".png"
  print "Preparing to rename", oldOsFilename + " to " + str(newOsFilename)+".png"
  oldOsFilename = joinDirectoryAndName(oldOsFilename)
  existsOld = os.path.isfile(oldOsFilename)
  i = 1
  while True:
    if newOsFilename == 'expired':
      tempOsFilename = newOsFilename + str(i) +".png"
    else:
      tempOsFilename = newOsFilename +".png"
    i += 1
    existsNew = os.path.isfile(joinDirectoryAndName(tempOsFilename))
    if existsOld and not existsNew:
      os.rename(oldOsFilename,joinDirectoryAndName(tempOsFilename))
      print "Success! Go have a spot o' tea."
      break #here was changeOSName
    elif not existsOld:
      print "File named ", oldOsFilename ," does not exist"
      break
    elif existsNew:
      print "File", tempOsFilename," already exists."


############   Node from Node   ######

class Node:
  def __init__(self, name, content, endDate=None, startDate=None):
    self.name = name
    self.content = content
    if (endDate == 'null' or endDate == " " or endDate == None):
      self.endDate = '9999-12-31'
    else:
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
    self.slideCount = 0
    self.head_node = None

  def get_head_node(self):
    return self.head_node

  def print_slideCount(self):
    print "Slide Count is " + str(self.slideCount) + ""

  def addNode(self, name, content, endDate=None, startDate=None):
    curr = self.get_head_node()
    if curr is None:
      n = Node(name, content, endDate, startDate)
      n.next_node = None
      self.head_node = n
      self.slideCount += 1
      return
    
    if curr.name > name:
      n = Node(name, content, endDate, startDate)
      n.set_next_node(curr)
      self.head_node = n
      self.slideCount += 1
      return
     
    while curr.next_node is not None:
      if curr.next_node.name > name:
        break
      curr = curr.next_node
    n = Node(name, content, endDate, startDate)
    self.slideCount += 1
    n.next_node = curr.next_node
    curr.next_node = n
    return

  def displayList(self):
    print "Today's Date: "+today
    self.print_slideCount()
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
#to remove a slide I first check the head node
    while current_node.get_endDate() <= endDate:
      oldOsFilename = str(current_node.get_name())
      changeOsFilename(oldOsFilename, "expired")
      self.head_node = current_node.get_next_node()
      current_node = self.get_head_node() 

    while current_node:
      if current_node.get_next_node() != None:
        next_node = current_node.get_next_node()
        if next_node.get_endDate() <= endDate:
          oldOsFilename = str(next_node.get_name())
          changeOsFilename(oldOsFilename, "expired")
          current_node.set_next_node(next_node.get_next_node())
        elif next_node.get_name() != None:
          current_node = next_node
      else:
        current_node = None
  
  def archiveList(self):
    alertBlock("Archive function not ready yet.")

  def searchName(self, slideName):
    pass
    
  def inputSlide(self):
    slideNames = ['Slide1','Slide2','Slide3','Slide4','Slide5','Slide6','Slide7','Slide8','Slide9','Slide10']
    pass

  def removeSlide(self):
    pass

  def executeUserChoice(self, argument):
      method_name = 'number_' + str(argument)
      # Get the method from the list. Default to a lambda. Returning 'method' executes it.
      method = getattr(self, method_name, lambda: self.invalidArg())
      return method()

  def invalidArg(self):
    alertBlock("Invalid Argument")

  def number_1(self):
    alertBlock("Displaying List")
    print(self.displayList())

  def number_2(self):
    alertBlock("Removing Expired")
    self.remove_expired(today)
    alertBlock("")

  def number_3(self):
    alertBlock("Input New Slide")
    self.inputSlide()

  def number_4(self):
    alertBlock("Removing Slide")    
    slideToRemove = "slide" + str(raw_input("What slide number do you want to remove? "))
    print slideToRemove
    self.removeSlide()
    alertBlock("")

  def number_5(self):
    alertBlock("Archiving List" +self.listName)
    self.archiveList()
    alertBlock("")

  def number_6(self):
    changeList()

  def number_X(self):
    global runProgram 
    alertBlock('Exiting Program')
    runProgram = False
    return runProgram




############   User Functions   ######
def changeList():
  activeList = str(raw_input("What list would you like to work on? (cpmc,WOW): "
))
  global ll
  ll = LinkedList(activeList)
  activeList += '.json'
  with open(activeList) as data_file:
    slideList = json.load(data_file)
  for x in slideList:
    ll.addNode(x['name'],x['content'],x['endDate'],x['startDate'])


def whatNow():
  if (ll.listName):
    print "Current List is: " + str(ll.listName) + "."
  print "---Make a selection---"
  print "  1   Display List"
  print "  2   Remove Expired Slides"
  print "  3   Add a new slide"
  print "  4   Remove a slide"
  print "  5   Save a list"
  print "  6   Load a list"
  userChoice = (raw_input("What would you like to do next? (1 - 6, eXit):"))
  ll.executeUserChoice(userChoice)


###### Program ######
runProgram = True
ll = ""
while runProgram:
  if ll:
    whatNow()
  else:
    changeList()
