import json, io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
    
slideList = []
def slide(name, content, endDate = None, startDate = None):
	slide= {
	  'name': name,
	  'content': content,
	  'endDate': endDate,
	  'startDate': startDate }
	return slide

#Create slides and add to Slide List
slideList.append(slide("Slide1", "Key Dates", '2019-03-04'))
slideList.append(slide("Slide10", "Declutter", '2019-01-04'))
slideList.append(slide("Slide2", "Facility Specialists", '2019-03-03'))
slideList.append(slide("Slide3", "Training", '2019-02-01'))
slideList.append(slide("Slide4", "Download your Guides", '2019-05-04'))
slideList.append(slide("Slide5", "Electric W2", '2019-01-04'))
slideList.append(slide("Slide6", "Colleagues Campaign", '2018-12-30'))
slideList.append(slide("Slide7", "Block Parties", '2019-02-02'))
slideList.append(slide("Slide8", "Diabetes", '2019-06-25'))
slideList.append(slide("Slide9", "Diabetes2", '2019-06-25'))

with io.open('cpmc.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(slideList,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

with open('cpmc.json') as data_file:
    data_loaded = json.load(data_file)

#This tests the original vs the json'd list
print(slideList == data_loaded)
print data_loaded[0]['content']
print slideList[0]['content']
