import json
import random
from getting_guess import word_guess
from checking_function import check_correct


#getting files from json & selecting word
with open('words.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
selected_word = random.choice(data)






valid:bool = False
guess:str = word_guess(data, valid)
print(selected_word)



while True:

    if guess == selected_word:

        print('Correct!')
        break

    else :

        print('try again')
        check_correct(guess,selected_word)
        guess:str = word_guess(data, valid)






