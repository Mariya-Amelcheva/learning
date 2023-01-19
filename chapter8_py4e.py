def chop(x):
    del x[0]
    del x[-1]

lst = ['a', 'b', 'c']
chop(lst)

print(lst)

def middle(x):
    t = x[1:-1]
    return(t)

lst = ['a', 'b', 'c']
rest = middle(lst)
print(rest)
print(lst)
_________________________________________

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
	print('File doesn\'t exsist:', fname)
	quit()

lst = list()

for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in lst:
            continue
        else: lst.append(word)
lst.sort()

print(lst)

_________________________________________

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
	print('File doesn\'t exsist:', fname)
	quit()

count = 0

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    else:
        line = line.split()
        word = line[1]
        count = count + 1
    print(word)
print('There were', count, 'lines in the file with From as a first word')

_________________________________________

lst = list()

while True:
    x = input('Enter a number: ')
    if x == 'done':
        break
    try:
        x = float(x)
    except:
        print('invalid input')
        continue
    lst.append(x)
    #print(lst)
    smallest = min(lst)
    biggest = max(lst)

print('Maximum:', smallest)
print('Minimum:', biggest)
