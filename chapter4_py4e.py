import random

for i in range(10):
    x = random.random()
    print(x)

print(random.randint(5, 10))

t = [1, 8, 10, 12]
print(random.choice(t))

_________________________________________

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print('one two')
    print('three four')

repeat_lyrics()

_________________________________________

repeat_lyrics

def print_lyrics():
    print('one two')
    print('three four')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

_________________________________________

def computepay(hours, rate):
    if hours > 40:
        extrahours = hours - 40
        extrapay = rate * 1.5
        pay = 40 * rate + extrahours * extrapay
    else:
        pay = hours * rate
    print('Pay: ', pay)

x = input('Enter Hours: ')
hours = float(x)
y = input('Enter Rate: ')
rate = float(y)

computepay(hours, rate)

_________________________________________

def computegrade(score):
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

x = input('Enter a score: ')
try:
    score = float(x)
except:
    print('Bad score')
    quit()

computegrade(score)
