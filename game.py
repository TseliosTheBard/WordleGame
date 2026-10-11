import json
import random
from GettingGuess import word_guess


#getting files from json & selecting word
with open('words.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
selected_word = random.choice(data)





valid:bool = False
guess:str = word_guess(data,valid)
print(selected_word[0])



while guess != selected_word:

    if guess == selected_word:

        print('Correct!')
        break
    else :
        print('try again')
        guess:str = word_guess(data,valid)






