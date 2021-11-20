import random
import os

#################################
# Command Detection
#################################

TOKENS = [
    'help()', ' ', 'import', 'multiline()', 'contri()', 'dice()',
    'imp.createfile()', 'stop()', 'imp.port()', 'imp.grab()', 'c -mb project file'
]
IMPORTS = ['imp', 'lib']
MULTITOKENS = [
	'log[', ']', 'import imp', 'depend()', 'import lib'
	]
LOADER = ['###################','=##################', '==#################', '===###############', '====###############', '=====#############', '======#############', '=======############', '========###########', '=========##########', '==========#########', '===========########', '============#######', '=============######', '==============#####', '===============####', '================###', '=================##', '==================#', '===================']
VARIABLES = []
VALUES = []
V = []
y = False
used = False
rand = False
rand = 0.0
rand1 = 0.0
global MULTITOK


def write(r):
    MULTITOK = ['']
    if r == ' ':
        error('Invalid Arguments')
    if r not in TOKENS:
        error('Invalid Resource')
    if r == TOKENS[0]:
        print('import\nmultiline\nlog\ndice\nhelp\nstop')
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
        while (y == True):
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
                 Ex = '\n'.join([str(elem) for elem in MULTITOK])
                 f.write(str(Ex) + "%d\r\n" % (i + 1))
        else:
            error('imp() not defined')
    if r == TOKENS[7]:
        exit()
    if r == TOKENS[8]:
        if imp == True:
            fl = input('>> ')
            file_extension = os.path.splitext(fl)
            if file_extension[1] == '.cra':
                with open(fl) as f:
                    lines = f.readlines()
                MULTITOK = lines[1::1]
                print(colored(0, 153, 0, lines))
            else:
                error('File Type Invalid')
        else:
            error('imp() not defined')
    if r == TOKENS[10]:
        preset()

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
    print(colored(235, 94, 94, 'Error: ' + er))


#################################
# Imports
#################################


def importfun(lib):
    if lib == 'imp':
        global imp
        imp = True
    if lib == 'lib':
        global libr
        libr = True

#################################
# File Loader
#################################

def preset():
	os.mkdir('Crater-Library')
	os.mkdir('Crater-Library/src')
	os.mkdir('Crater-Library/src/scripts')
	os.mkdir('Crater-Library/src/items')
	os.mkdir('Crater-Library/src/assets')
	f = open('Crater-Library/src/scripts/main.cra', 'a+')

#################################
# Others
#################################


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

