





#Get the function from switcher

def executeUserChoice(argument):
  switcher = {
    '1' : ll.remove_expired(today),
    '2' : ll.archive(),
    '3' : ll.inputSlide(),
    '4' : changeList(),
    'X' : runProgram = true
  }
  exitProgram = switcher.get[argument, "Error"]
  return exitProgram



#https://jaxenter.com/implement-switch-case-statement-python-138315.html
#https://www.pydanny.com/why-doesnt-python-have-switch-case.html
runProgram = True

def exitProgram():
	global runProgram 
	print 'Exiting Program'
	runProgram = False
	return runProgram

class Switcher(object):
    def numbers_to_methods_to_strings(self, argument):
        method_name = 'number_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: self.invalidArg())
        # Call the method as we return it
        return method()

    def invalidArg(self):
    	print "Invalid Argument"

    def number_0(self):
        print "zero"

    def number_1(self):
        print "one"

    def number_X(self):
        global runProgram 
        print 'Exiting Program'
        runProgram = False
        return runProgram

print runProgram
a=Switcher()
i = 0
while runProgram:
	a.numbers_to_methods_to_strings(i)
	i += 1
	if i == 3:
		a.numbers_to_methods_to_strings('X')
print "Success! Now go to Jumpity Bumpity."

'''
def zero():
    return "zero"

def one():
    return "one"

def numbers_to_functions_to_strings(argument):
    switcher = {
        0: zero,
        1: one,
        2: lambda: "two",
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "nothing")
    # Execute the function
    return func()'''