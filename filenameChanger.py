import os
from os.path import join, isfile

# Global Variables for testing only.
Directory = '.'
OldFilename = 'Slide1.png'
NewFilename = 'Filler1.png'


def joinDirectoryAndName(Directory,Filename):
	joint = os.path.join(Directory,Filename)
	return joint

def changeName(OldFilename,NewFilename):
	os.rename(OldFilename, NewFilename)
	print "Success! Go have a spot o' tea."


def runTest(OldFilename,NewFilename,Directory):
	OldFilename = joinDirectoryAndName(Directory,OldFilename)
	NewFilename = joinDirectoryAndName(Directory,NewFilename)
	existsOld = os.path.isfile(OldFilename)
	existsNew = os.path.isfile(NewFilename)
	if existsOld and not existsNew:
		print "Preparing to rename"
		changeName(OldFilename,NewFilename)
	elif not existsOld:
		print "File named",OldFilename,"does not exist"
	elif existsNew:
		print "File already exists"


runTest(OldFilename,NewFilename,Directory)



# Results:
#// Successfully changes the name of the file.
#// OSError: [Errno 2] No such file or directory
