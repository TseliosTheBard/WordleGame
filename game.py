import json
import random



#getting files from json & selecting word
with open('words.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
selected_word = random.choice(data)



guess = input('Enter your guess: ')


while guess != selected_word:

    if guess == selected_word:

        print('Correct!')
        break
    else :
        print('try again')
        guess = input('Enter your guess: ')
#idk




def valid_word(guess)-> bool:
    if guess in data:
        return True
    else:
        return False
