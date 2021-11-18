import random

#################################
# Command Detection
#################################

TOKENS = ['help()', ' ', 'import', 'multiline()', 'contri()', 'dice()']
IMPORTS = ['imp']
MULTITOK = []
MULTITOKENS = ['import random', 'log[', ']', 'import imp']
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
used = True




#################################
# Errors
#################################

def error(er):
	print(er)

#################################
# Imports
#################################

def importfun(lib):
	if lib == 'imp':
		imp()

def imp():
	imp = True
	print('Successfully Imported IMP')