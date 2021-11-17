#################################
# Command Detection
#################################

TOKENS = ['command: help', 'command:', 'command: import']
IMPORTS = ['math', 'random', 'imp']

def write(r):
	if r == 'command:':
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
			importfun(IMPORTS[importt])
			print('Importing ' + importt)

#################################
# Errors
#################################

def error(er):
	print(er)

#################################
# Imports
#################################

def importfun(lib):
	if lib == 'math':
		math()
	elif lib == 'random':
		rand()
	elif lib == 'imp':
		