import random

word_list = ['blueberry', 'strawberry', 'banana', 'kiwi', 'mango']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please enter a single letter: ")
if len(guess) == 1 and guess.isalpha() == True:
    print('Good guess!')
else: 
    print('Oops! That is not a valid input.')
    
