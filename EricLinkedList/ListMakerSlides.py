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

############   Testing Variables #####
Directory = '.'

############   Global Variables ######
today = str(date.today()) # ie '2017-12-26'
dashCount = 69


############   Global Functions ######
def alertBlock(message):
  if message != "":
    print "\n" + str("-"*dashCount) + "\n" + message + "\n" + str("-"*dashCount) +"\n"
  else:
    print "\n" + str("-"*dashCount) + "\n" + str("-"*dashCount) + "\n"*2

def slideForArray(name, content, endDate = None, startDate = None):
  slide= {
    'name': name,
    'content': content,
    'endDate': endDate,
    'startDate': startDate }
  return slide

############   Input Date   ##########
def inputDate():
  userDate = raw_input("Please enter date in the format yyyy-mm-dd: ")
  return userDate


############   OS Functions   ########
def joinDirectoryAndName(OsFilename):
  joint = os.path.join(Directory,OsFilename)
  return joint

def changeOsFilename(oldOsFilename, newOsFilename):
  oldOsFilename += ".png"
  oldOsFilename = joinDirectoryAndName(oldOsFilename)
  existsOld = os.path.isfile(oldOsFilename)
  i = 1
  while True:
    tempOsFilename = newOsFilename + str(i) +".png"
    i += 1
    existsNew = os.path.isfile(joinDirectoryAndName(tempOsFilename))
    if existsOld and not existsNew:
      os.rename(oldOsFilename,joinDirectoryAndName(tempOsFilename))
      print "Renaming", oldOsFilename + " to " + str(newOsFilename)+".png"
      print "Success! Go have a spot o' tea."
      break
    elif not existsOld:
      print "File named ", oldOsFilename ," does not exist."
      break
    elif existsNew:
      print "File", tempOsFilename," already exists."


############   Node from Node   ######

class Node:
  def __init__(self, name, content, endDate=None, startDate=None):
    self.name = name
    self.content = content
    if (endDate == 'nult' or endDate == " " or endDate == None):
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

  def get_startDate(self):
    return self.startDate

  def printSlide(self):
    string_list = str(self.get_name() + " " * (13 - len(str(self.get_name()))) + str(self.get_content()) + " "*(20 - len(str(self.get_content()))) + " End Date: ")
    if self.get_endDate() != None:
      string_list += str(self.get_endDate()) + " "
    if self.get_startDate() != None:
      string_list += " Start Date: " + str(self.get_startDate())
    alertBlock(string_list)    

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
    print "Slide Count of " + self.listName.upper() + " is " + str(self.slideCount) + "."

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

  def executeUserChoice(self, argument):
    method_name = 'number_' + str(argument)
    # Get the method from the list. Default to a lambda. Returning 'method' executes it.
    method = getattr(self, method_name, lambda: self.invalidArg())
    return method()

  def invalidArg(self):
    alertBlock("Invalid Argument")

  def number_1(self): #Display List
    alertBlock("Displaying List")
    print(self.displayList())

  def number_2(self): #Remove Expired
    alertBlock("Removing Expired")
    self.remove_expired(today)

  def number_3(self): #Create New Slide
    self.createNewSlide()

  def number_4(self): #Remove Slide
    alertBlock("Removing Slide")    
    slideToRemove = "Slide" + str(raw_input("Slide to remove: "))
    self.removeSlide(slideToRemove)

  def number_E(self): #Archive Slide
    alertBlock("Edit a Slide")
    slideToEdit = "Slide" + str(raw_input("Slide number to edit: "))
    self.editSlide(slideToEdit)

  def number_S(self): #Archive Slide
    alertBlock("Archiving List" +self.listName)
    self.archiveList()

  def number_D(self): #Duplicate List
    duplicateListName = str(raw_input("Save list as: "))
    alertBlock("Saving "+ self.listName +" as " + duplicateListName + ".")
    self.archiveList(duplicateListName)
    changeList(duplicateListName)

  def number_L(self): #Load List
    changeList()

  def number_X(self): #Exit Program
    global runProgram 
    alertBlock('Exiting Program')
    runProgram = False
    return runProgram

  def editSlide(self, slideToEdit):
    current_node = self.get_head_node()
    beginningSlideCount = self.slideCount
    string_list =""
    while current_node:
#      if current_node.get_next_node() != None:
      if current_node.get_name() == slideToEdit:
        current_node.printSlide()
        whatToEdit = str(raw_input("What do you want to edit (content, end, start?) ")).lower()
        if whatToEdit[0:3] == 'con':
          current_node.content = str(raw_input("New Content: "))
        elif whatToEdit[0:3] == 'end':
          current_node.endDate = str(raw_input("New End Date (yyyy-mm-dd): "))
        elif whatToEdit[0:3] == 'sta':
          current_node.startDate = str(raw_input("New Start Date (yyyy-mm-dd): "))
        current_node = None
      else:
        current_node = current_node.get_next_node()
#      else:
#        current_node = None


  def archiveList(self, listFilename=None): 
    current_node = self.get_head_node()
    if listFilename == None:
      listFilename = self.listName
    slideList = []
    while current_node:
      slideList.append(slideForArray(current_node.get_name(), current_node.get_content(), current_node.get_endDate(), current_node.startDate))
      current_node = current_node.get_next_node()
    print slideList #test Archive
    with io.open(listFilename + '.json', 'w', encoding='utf8') as outfile:
      str_ = json.dumps(slideList,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
      outfile.write(to_unicode(str_))
    with open(listFilename + '.json') as data_file:
      data_loaded = json.load(data_file)

#This tests the original vs the json'd list
    if (slideList == data_loaded):
      if self.slideCount == 0:
        print '---> HMMM, empty list saved... what are you up to?'
      else:
        print '----> SUCCESS! ' + listFilename.upper() + ' created. Which is a ' + (str(type(slideList)).upper())[7:11] + ' of ' + (str(type(slideList[0])).upper()[7:11]) + "'s."
    else:
      print '----> UNSUCCESSFUL!!'

  def displayList(self):
    print "Today's Date: "+today
    self.print_slideCount()
    string_list = str("-"*dashCount) +"\n"
    current_node = self.get_head_node()

    while current_node:
      if current_node.get_name() != None:
        string_list += str(current_node.get_name())+"" + " "*(13 - len(str(current_node.get_name()))) + str(current_node.get_content()) + " "*(20 - len(str(current_node.get_content()))) + " End: "
        if current_node.get_endDate() != None:
          string_list += str(current_node.get_endDate())
        else:
          string_list += " "*10
        if current_node.get_startDate() != None:
          string_list += "   Start: " + str(current_node.get_startDate())
      string_list += "\n"
      current_node = current_node.get_next_node()
    string_list += str("-"*dashCount) +"\n"
    return string_list

  def remove_expired(self, endDate):
    current_node = self.get_head_node()
    beginningSlideCount = self.slideCount
    #to remove a slide I first check the head node
    while current_node.get_endDate() <= endDate:
      oldOsFilename = str(current_node.get_name())
      changeOsFilename(oldOsFilename, "expired")
      self.head_node = current_node.get_next_node()
      current_node = self.get_head_node()
      self.slideCount -= 1 
    #then onto the rest of the list  
    while current_node:
      if current_node.get_next_node() != None:
        next_node = current_node.get_next_node()
        if next_node.get_endDate() <= endDate:
          self.slideCount -= 1
          oldOsFilename = str(next_node.get_name())
          changeOsFilename(oldOsFilename, "expired")
          current_node.set_next_node(next_node.get_next_node())
        elif next_node.get_name() != None:
          current_node = next_node
      else:
        current_node = None
    alertBlock('Slides removed: ' + str(beginningSlideCount - self.slideCount))

  def get_unusedSlidename(self):
    slideNames = ['Slide1','Slide2','Slide3','Slide4','Slide5','Slide6','Slide7','Slide8','Slide9','Slide10']    
    current_node = self.get_head_node()
    beginningSlideCount = self.slideCount
    emptyFound = False
    while not emptyFound and current_node:
      for name in slideNames:
        if current_node.get_name() == name:
          slideNames.remove(str(name))
      current_node = current_node.get_next_node()
    return slideNames[0]

  def createNewSlide(self,newSlideName = "Slide1"):
    if self.slideCount > 9:
      alertBlock("Remove a slide first")
      return
    alertBlock("Create New Slide")
    newSlideName = self.get_unusedSlidename()
    content = str(raw_input("What is the content? "))
    yesNo = str(raw_input("Is there an End Date? (Y/N) ")).upper()
    if yesNo == "Y":
      endDate = inputDate()
    else:
      endDate = None
    yesNo = str(raw_input("Is there an Starting Date? (Y/N) ")).upper()
    if yesNo == "Y":
      startDate = inputDate()
    else:
      startDate = None
    self.addNode(newSlideName, content, endDate, startDate)
    print("New Slide wilt be named: " + newSlideName)

  def removeSlide(self, slideNameToRemove):
    current_node = self.get_head_node()
    beginningSlideCount = self.slideCount
    #to remove a slide I first check the head node
    if current_node.get_name() == slideNameToRemove:
      oldOsFilename = str(current_node.get_name())
      changeOsFilename(oldOsFilename, "deleteMe")
      self.head_node = current_node.get_next_node()
      self.slideCount -= 1 
      current_node = None
    #next loop through list
    while current_node:
      if current_node.get_next_node() != None:
        next_node = current_node.get_next_node()
        if next_node.get_name() == slideNameToRemove:
          self.slideCount -= 1
          oldOsFilename = str(next_node.get_name())
          changeOsFilename(oldOsFilename, "deleteMe")
          current_node.set_next_node(next_node.get_next_node())
        elif next_node.get_name() != None:
          current_node = next_node
      else:
        current_node = None
    alertBlock('Slides removed: ' + (str(beginningSlideCount-self.slideCount)))





############   User Functions   ######
def changeList(activeList = None):
  if activeList == None:
    activeList = str(raw_input("What list would you like to work on? (cpmc,WOW): "))
  global workingList
  workingList = LinkedList(activeList)
  activeList += '.json'
  with open(activeList) as data_file:
    slideList = json.load(data_file)
  for x in slideList:
    workingList.addNode(x['name'],x['content'],x['endDate'],x['startDate'])
  alertBlock('New list ' + workingList.listName.upper() + ' loaded.')



def whatNow():
  if (workingList.listName):
    print "Current List is: " + workingList.listName.upper() + "."
  print "---Make a selection---"
  print "  1   Display List"
  print "  2   Remove Expired Slides"
  print "  3   Add a new Slide"
  print "  4   Remove a Slide"
  print "  E   Edit a Slide"
  print "  S   Save List"
  print "  D   Duplicate List"
  print "  L   Load different List"
  userChoice = raw_input("What would you like to do next? (1 - 6, eXit):").upper()
  workingList.executeUserChoice(userChoice)


###### Program ######
runProgram = True
workingList = ""
futureList = LinkedList("future")
with open("future.json") as data_file:
  slideList = json.load(data_file)
for x in slideList:
  futureList.addNode(x['name'],x['content'],x['endDate'],x['startDate'])
futureList.print_slideCount()
while runProgram:
  if workingList:
    whatNow()
  else:
    changeList()
