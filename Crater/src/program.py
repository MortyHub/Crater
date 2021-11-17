import random

#################################
# Command Detection
#################################

TOKENS = ['help()', ' ', 'import', 'multiline()']
IMPORTS = ['random', 'imp']
MULTITOK = []
MULTITOKENS = ['import', 'log[', ']', 'random[']
PACKAGES = []
y = False
used = False

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
			if importt == 'random':
				importfun('random')
			elif importt == 'imp':
				importfun('imp')
			print('Imported ' + importt)
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
		
def runc(c):

	result = ' '
	res = []
	on = ' '
	current = 0
	for i in range(len(c)):
		if c[current] == 'import':
			on = 'import'
		if on == 'import':
			importfun(c[current])
		
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
				res.append(on)
		if c[current] == 'random':
			if 'random' in PACKAGES:
				on = 'rand['
			if on == 'rand':
				on = 'Num'
			if on == 'rand':
				if c[current] == ']':
					on = ' '
					res = res.split("random[")
					print(random.randrange(result[0], result[1]))
				elif on == 'Num':
					result += c[current] 
			else:
				error('Error, Package Not Imported')

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
	if lib == 'random':
		rand()
	elif lib == 'imp':
		imp()

def rand():
	PACKAGES.append('random')
	rand = True

def imp():
	PACKAGES.append('imp')
	imp = True