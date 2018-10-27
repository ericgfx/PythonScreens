# -*- coding: utf-8 -*-
import json

# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Define data
data = {'slide1': {'filename': 'Slide1.PNG',
                   'content': 'key_dates',
                   'end': 'Mar. 3'},
        'slide2': {'filename': 'Slide1.PNG',
                   'content': 'key_dates',
                   'end': 'Mar. 3'}
                   }

print data['slide1']['filename']

# Write JSON file
with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Read JSON file
with open('data.json') as data_file:
    data_loaded = json.load(data_file)

print(data == data_loaded)

print data_loaded['slide1']['filename']
