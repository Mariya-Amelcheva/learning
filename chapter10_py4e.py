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

lst = list()
for key, value in list(counts.items()):
    lst.append((value, key))
lst.sort(reverse = True)

for key, value in lst[:1]:
    print(value, key)

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
        time = x[5]
        y = time.split(':')
        hour = y[0]
        counts[hour] = counts.get(hour, 0) + 1

lst = list()
for key, value in list(counts.items()):
    lst.append((key, value))
    lst.sort()

for key, value in lst:
    print(key, value)

_________________________________________


import string

counts = dict()
lst = list()
qwe = list()

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
	print('File doesn\'t exsist:', fname)
	quit()


for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        lst.append(word)

for x in lst:
    word = x
    for x in word:
        qwe.append(x)

for wer in qwe:
    counts[wer] = counts.get(wer, 0) + 1

gh = list()

for key, value in list(counts.items()):
    gh.append((value, key))
    gh.sort(reverse = True)

for value, key in gh:
    print(key, value)
