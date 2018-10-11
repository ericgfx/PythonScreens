import json

filename = 'slideList.txt'

with open('slideList.txt', 'r') as my_file:
    testObjects = my_file.read()

testList = [
    {"filename": "Test1.png",
    "content": 'TestContent1',
    "startDate":'01/01/2018',
    "endDate": '03/03/2019',
    "Filler Status": False 
    },
    {
    "filename": "Test2.png",
    "content": 'TestContent2',
	"startDate":'01/01/2018',
    "endDate": '01/01/2018',
    "Filler Status": False }
]

# readFile()
print(testObjects[0]['content'])

# my_list = [i ** 2 for i in range(1, 11)]

# my_file = open("output.txt", "r+")

# # Add your code below!
# for i in my_list:
#   my_file.write(str(i) + "\n")
  
# my_file.close()