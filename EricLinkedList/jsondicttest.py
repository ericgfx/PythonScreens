import json, io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
    
slideList = []
def slide(name, content, endDate = None, startDate = None):
	slide=[]
	slide.append(name)
	slide.append(content)
	slide.append(endDate)
	slide.append(startDate)
	return slide

slideList.append(slide("Slide1", "Key Dates", '2019-3-04'))
slideList.append(slide("Slide2", "Facility Specialists", '2019-3-03'))
slideList.append(slide("Slide3", "Training", '2019-2-01'))
slideList.append(slide("Slide4", "Download your Guides", '2019-5-04'))
slideList.append(slide("Slide5", "Electric W2", '2019-01-04'))
slideList.append(slide("Slide8", "Diabetes", '2018-12-30'))
slideList.append(slide("Slide9", "Holiday Sale", '2018-12-25'))
slideList.append(slide("Slide10", "Declutter", '2019-1-04'))
slideList.append(slide("Slide6", "Colleagues Campaign", '2018-12-30'))
slideList.append(slide("Slide7", "Holiday Parties", '2018-12-13'))
'''print slideList

print(json.dumps(slideList, default=lambda o: o.__dict__))
'''
#json.dump(slideList, open('cpmc.json', 'wb'))
with io.open('cpmc.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(slideList,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

'''d_json = json.dumps(slideList)
print d_json
d_loaded = json.loads(d_json)
print d_loaded
'''
