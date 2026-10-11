from valid_word import check_word

def word_guess(data, valid):

    while True:
        temp = input('Enter your guess: ')
        if len(temp) != 5:
            print('Not a 5 letter word')
        elif check_word(temp, data):
            return temp
            break
        else:
            print('That Word doesn''t exist')