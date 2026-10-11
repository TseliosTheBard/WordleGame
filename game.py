import json
import random
from getting_guess import word_guess
from checking_function import check_correct
from tkinter import *


window = Tk()
window.title('Word Guess')
window.geometry('500x500')
window.mainloop()

#getting files from json & selecting word
with open('words.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
selected_word = random.choice(data)





#first guess
valid:bool = False
guess:str = word_guess(data, valid)

print(selected_word)


#main loop
while True:

    if guess == selected_word:

        print('Correct!')
        break

    else :

        print('try again')
        check_correct(guess,selected_word)
        guess:str = word_guess(data, valid)




