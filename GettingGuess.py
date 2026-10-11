from ValidWord import valid_word

def word_guess(data,valid):

    while True:
        temp = input('Enter your guess: ')
        if len(temp) != 5:
            print('Not a 5 letter word')
        elif valid_word(temp, data):
            return temp
            break
        else:
            print('That Word doesn''t exist')