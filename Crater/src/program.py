#################################
# Command Detection
#################################

TOKENS = ['command: help', 'command:']

def write(r):
	if r == 'command:':
		error('Invalid Arguments')
	if r not in TOKENS:
		error('Invalid Resource')
	if r == TOKENS[0]:
		print('This Feature Is Not Yet Available')
	
#################################
# Errors
#################################

def error(er):
	print(er)