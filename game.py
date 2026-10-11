import json
import random



#getting files from json & selecting word
with open('words.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
selected_word = random.choice(data)

def valid_word(guess)-> bool:
    if guess in data:
        return True
    else:
        return False



valid = False

while True:
    guess = input('Enter your guess: ')
    if len(guess) != 5:
        print('Not a 5 letter word')
    elif valid_word(guess):
        break
    else:
        print('That Word doesn''t exist')

while guess != selected_word:

    if guess == selected_word:

        print('Correct!')
        break
    else :
        print('try again')
        guess = input('Enter your guess:')






