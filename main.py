from Crater.src.program import write

version = '0.2.3'
Crater = 'Crater >> '

print('Crater ' + version + ' (default, Nov 16 2021, 20:56:28) For Help Please Type In command: help()')
while True:
	instr = input(Crater)
	write(instr)