import re
count = 0

expr = input('Enter a regular expression: ')
fhand = open('mbox.txt')

for line in fhand:
    line = line.rstrip()
    if re.search(expr, line):
        count = count + 1
print('mbox.txt had', count, 'lines that matched', expr)

_________________________________________


import re

numlist = list()

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
	print('File doesn\'t exsist:', fname)
	quit()

for line in fhand:
    line = line.rstrip()
    stuff = re.findall('New Revision: ([0-9]+)', line)
    if len(stuff) < 1: continue
    num = int(stuff[0])
    numlist.append(num)
print(sum(numlist) // len(numlist))
