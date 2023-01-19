index = -1
fruit = 'apple'
lenght = 0 - len(fruit)
while index >= lenght:
    letter = fruit[index]
    print(letter)
    index = index - 1

_________________________________________

def count(word, letter):
    count = 0
    for x in word:
        if x == letter:
            count = count + 1
    print(count)

word = input('Enter a word ')
letter = input('Enter a letter ')
count(word, letter)

_________________________________________

str = 'X-DSPAM-confidence:0.8475'

pos = str.find(':')
print(pos)
after = float(str[19:])
print(after)
