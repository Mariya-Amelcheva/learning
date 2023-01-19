fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
	print('File doesn\'t exsist:', fname)
	quit()

for line in fhand:
    line = line.rstrip()
    LINE = line.upper()
    print(LINE)

_________________________________________


fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
	print('File doesn\'t exsist:', fname)
	quit()

count = 0
sum = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        x = line
        y = x.find(':')
        number = float(line[y+1:])
        count = count + 1
        sum = sum + number
print('Average spam confidence:', sum/count)

_________________________________________

fname = input('Enter a file name: ')
if fname == 'na na boo boo':
    print(fname.upper(), '- You have been punk\'d!!!')
    quit()
try:
    fhand = open(fname)
except:
	print('File doesn\'t exsist:', fname)
	quit()

count = 0
sum = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        x = line
        y = x.find(':')
        number = float(line[y+1:])
        count = count + 1
        sum = sum + number
print('Average spam confidence:', sum/count)
