sum = 0
quan = 0
av = 0

while True:
    x = input('Enter a number: ')
    if x == 'done':
        break
    try:
        x = float(x)
    except:
        print('invalid input')
        continue
    sum = sum + x
    quan = quan + 1
    av = sum / quan
print(sum, quan, av)

_________________________________________

smallest = None
biggest = None


while True:
    x = input('Enter a number: ')
    if x == 'done':
        break
    try:
        x = float(x)
    except:
        print('invalid input')
        continue
    if smallest is None or smallest > x:
        smallest = x
    elif biggest is None or biggest < x:
        biggest = x
print('Smallest:', smallest, 'Biggest:', biggest)
