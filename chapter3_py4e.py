x = input('Enter Hours: ')
hours = float(x)
y = input('Enter Rate: ')
rate = float(y)

if hours > 40:
    pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
else:
    pay = hours * rate
print('Pay: ', pay)

OR

x = input('Enter Hours: ')
hours = float(x)
y = input('Enter Rate: ')
rate = float(y)

if hours > 40:
    extrahours = hours - 40
    extrapay = rate * 1.5
    pay = 40 * rate + extrahours * extrapay
else:
    pay = hours * rate
print('Pay: ', pay)

_________________________________________

x = input('Enter Hours: ')
try:
    hours = float(x)
except:
    print('Error, please enter a numeric input')
    quit()
y = input('Enter Rate: ')
try:
    rate = float(y)
except:
    print('Error, please enter a numeric input')
    quit()


if hours > 40:
    extrahours = hours - 40
    extrapay = rate * 1.5
    pay = 40 * rate + extrahours * extrapay
else:
    pay = hours * rate
print('Pay: ', pay)


_________________________________________

x = input('Enter a score: ')
try:
    score = float(x)
except:
    print('Bad score')
    quit()

if score > 1:
    print('Bad score')
elif score >= 0.9:
    print('A')
elif 0.9 >= score >= 0.8:
    print('B')
elif 0.8 >= score >= 0.7:
    print('C')
elif 0.7 >= score >= 0.6:
    print('D')
elif score < 6:
    print('F')
