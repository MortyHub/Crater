import random

#################################
# Command Detection
#################################

TOKENS = ['help()', ' ', 'import', 'multiline()', 'contri()', 'dice()', 'createfile()', 'stop()']
IMPORTS = ['imp']
MULTITOK = []
MULTITOKENS = ['import random', 'log[', ']', 'import imp', 'depend()']
VARIABLES = []
VALUES = []
y = False
used = False
rand = False
imp = False
rand = 0.0
rand1 = 0.0


def write(r):

	if r == ' ':
		error('Invalid Arguments')
	if r not in TOKENS:
		error('Invalid Resource')
	if r == TOKENS[0]:
		print('This Feature Is Not Yet Available')
	if r == TOKENS[2]:
		importt = input('>> ')
		if importt not in IMPORTS:
			error('Invalid Import')
		else:
			importfun(IMPORTS[IMPORTS.index(importt)])
			print('Importing ' + importt)
	if r == TOKENS[3]:
		line = 1
		y = True
		print('Type: end When You Finish The Script')
		while(y == True):
			mult = input(str(line) + ' >> ')
			line += 1
			if mult == 'end':
				y = False
				runc(MULTITOK)
			else:
				MULTITOK.append(mult)
	if r == TOKENS[5]:
		rand = int(input('>> '))
		rand1 = int(input('>> '))
		print(random.randrange(rand, rand1))
	if r == TOKENS[6]:
		if imp == True:
			f = open("Crater.cra", "a+")
			for i in range(1):
				Ex =  '\n'.join([str(elem) for elem in MULTITOK]) 
				f.write(str(Ex) + "%d\r\n" % (i+1))
		else:
			error('port() function not specified')		
	if r == TOKENS[7]:
		exit()


		
def runc(c):
	result = ' '
	on = ' '
	current = 0
	for i in range(len(c)):
		if c[current] == 'import imp':
			importfun('imp')
		elif c[current] == 'import random':
			importfun('random')
		if c[current] == 'log[':
			on = 'log'
		if on == 'log':
			on = 'text'
		if on == 'text':
			if c[current] == ']':
				on = ' '
				result = result.split("log[")
				print(result[1])
			elif on == 'text':
				result += c[current]		
		current += 1
		if c[current] == 'port(':
			if imp == True:
				on = 'PORT'
			else:
				error('port() function not specified')
		
used = True

"""
def run(c, a):
	on = ' '
	current = 1
	STRFUN = []
	for i in range(a):
		print('dud')
		if c[current] == 'mb -b':
			leng = len(c)
			print(leng)
		elif c[current] == 'def str() {':
			on = '{'
		if on == '{':
			STRFUN.append(c[current])
		if c[current] == '}':
			print('in')
			if 'log[' in STRFUN:
				runc(c)
			on = ''
"""




#################################
# Errors
#################################

def error(er):
	print('Error: ' + er)

#################################
# Imports
#################################

def importfun(lib):
	if lib == 'imp':
		imp()

def imp():
	imp = True
	print('Successfully Imported IMP')
