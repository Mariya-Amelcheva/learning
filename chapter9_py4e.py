d = dict()

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
	print('File doesn\'t exsist:', fname)
	quit()

for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in d: continue
        else:
            d[word] = 'x'
print(d)

print('take' in d)

_________________________________________


counts = dict()

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
	print('File doesn\'t exsist:', fname)
	quit()


for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    else:
        words = line.split()
        word = words[2]
        counts[word] = counts.get(word, 0) + 1

print(counts)

_________________________________________

counts = dict()

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
	print('File doesn\'t exsist:', fname)
	quit()


for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    else:
        words = line.split()
        word = words[1]
        counts[word] = counts.get(word, 0) + 1

print(counts)

_________________________________________

counts = dict()

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
	print('File doesn\'t exsist:', fname)
	quit()


for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    else:
        words = line.split()
        word = words[1]
        counts[word] = counts.get(word, 0) + 1

#print(counts)

bigcount = None
bigsender = None

for sender, count in counts.items():
    if bigcount is None or count > bigcount:
        bigsender = sender
        bigcount = count

print(bigsender, bigcount)

_________________________________________


counts = dict()

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
	print('File doesn\'t exsist:', fname)
	quit()


for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    else:
        x = line.split()
        email = x[1]
        y = email.split('@')
        domen = y[1]
        counts[domen] = counts.get(domen, 0) + 1

print(counts)
