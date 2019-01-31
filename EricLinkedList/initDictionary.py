import json, io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
    
listFilename = 'wow'
slideList = []
def slide(name, content, endDate = None, startDate = None):
	slide= {
	  'name': name,
	  'content': content,
	  'endDate': endDate,
	  'startDate': startDate }
	return slide

#Create slides and add to Slide List
slideList.append(slide("Slide0", "EXPIRED!", '2018-03-04'))
slideList.append(slide("Slide1", "Key Dates", '2019-03-04'))
slideList.append(slide("Slide2", "Facility Specialists", '2019-03-03'))
slideList.append(slide("Slide3", "Training", '2019-02-01'))
slideList.append(slide("Slide4", "Download your Guides", '2019-05-04'))
slideList.append(slide("Slide5", "Moving Sale", '2019-01-18'))
slideList.append(slide("Slide6", "Farewell", '2019-02-23'))
slideList.append(slide("Slide7", "Open House Parties", '2019-02-02'))
slideList.append(slide("Slide8", "Diabetes", '2019-06-25'))
slideList.append(slide("Slide9", "Diabetes2", '2019-06-25'))
slideList.append(slide("Slide10", "STD_See the Future", '2019-02-07'))

with io.open(listFilename + '.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(slideList,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

with open(listFilename + '.json') as data_file:
    data_loaded = json.load(data_file)

#This tests the original vs the json'd list
if (slideList == data_loaded):
  print '----> SUCCESS! ' + listFilename.upper() + ' created. Which is a ' + (str(type(slideList)).upper())[7:11] + ' of ' + (str(type(slideList[0])).upper()[7:11]) + "'s."
else:
  print '----> UNSUCCESSFUL!!'

print listFilename

'''
#Test to specifically verify the last dictionary item's key of content's value
print data_loaded[len(data_loaded)-1]['content']
print slideList[len(slideList)-1]['content']
'''