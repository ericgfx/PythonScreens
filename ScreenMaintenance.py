# -*- coding: utf-8 -*-
import json
from datetime import date

# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Define data
class MySlide:
    def __init__(self,fileName,content,endDate,fillerStatus):
        self.fileName = fileName
        self.content = content
        self.endDate = endDate
        self.fillerStatus = fillerStatus
        

data = {'slide1' : {'fileName': 'Slide1.PNG',
                   'content': 'key_dates',
                   'end': [2019, 3, 2]},
        'slide2' : {'fileName': 'Slide2.PNG',
                   'content': 'key_dates',
                   'end': 'Mar. 3'}
                   }
print data['slide1']['end']

# Create a JSON file which saves the data
with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Read JSON file
with open('data.json') as data_file:
    data_loaded = json.load(data_file)

print(data == data_loaded)

print data_loaded['slide1']['end']

AddASlide = True
while AddASlide:
  TestSlide = MySlide('Slide3.PNG','Eric Test Slide','Mar. 3',True)
  print(TestSlide)
  print("Converting AddASlide")
  AddASlide = False

# New Concept is to create as a string, then read back using JSON, that way you can create named objects. There is bound to be a better way.