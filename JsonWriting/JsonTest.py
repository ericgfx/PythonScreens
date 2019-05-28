# -*- coding: utf-8 -*-
import json

# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Define data
datum = {'slide1': {'name': 'Chicken Coq-Au-Vin',
                   'main': 'Chicken',
                      'ingredients':
                        {
                          "chicken": 
                            {
                              'qty':1, 
                              'item_measure':'lb',
                              'item':'chicken'
                            },
                          "butter": 
                            {
                              'qty':0.5,
                              'item_measure':'oz',
                              'item':'butter'}
                        },
                   'endDate': 'Mar. 3'},
        'slide2': {'name': 'Slide2.PNG',
                   'content': 'key_dates',
                   'endDate': 'Mar. 3'}
                   }

#test I know what I'm doing with objects
print datum['slide1']['name']
print datum
# Write JSON file
with io.open('datum.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(datum,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Read JSON file
with open('datum.json') as data_file:
    data_loaded = json.load(data_file)

print(datum == data_loaded)


numIngredients = data_loaded['slide1']['ingredients'].items() #creates a view
print data_loaded['slide1']['ingredients'][1]['item'],": ", data_loaded['slide1']['ingredients'][1]['qty'], data_loaded['slide1']['ingredients'][1]['item_measure']
print len(numIngredients)